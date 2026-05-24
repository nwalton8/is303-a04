'''
Noah Walton
IS303-A04
 
Dice Game - Panda Royale
a competitive dice game where players roll various dice to accumulate points, trade dice, and strategize to win.

Input:
- Number of players
- Player names
- Player choices for trading and selecting new dice 

Processes:
- welcome_message() (Introduce the game and rules)
- get_num_players() (Get and validate number of players)
- get_player_names(num_players) (Collect player names and initialize their data)
- display_scoreboard(players) (Show current scores and dice inventory)
- roll_die(player) (Simulate rolling all dice for a player and calculate scores)
- turn_order(players) (Determine turn order based on yellow die rolls)
- trade_dice(player, players) (Allow players to trade clear dice for other dice)
- choose_new_die(players, main_bag) (Players choose new dice from a shared pool)
- determine_pity_die(players) (Assign pink pity dice to lowest scorers)
- play_round(players, main_bag, is_final_round) (Execute all steps for a round of play)

Outputs:
- Updated scores and dice inventory after each round
- Final scores and winner(s) at the end of the game
'''
import random

players = []
main_bag = {
    "yellow(6 sided)": 0,
    "yellow(8 sided)": 7,
    "green(20 sided)": 10,
    "blue(6 sided)": 10,
    "blue(8 sided)": 9,
    "blue(12 sided)": 9,
    "blue glitter(6 sided)": 7,
    "purple(8 sided)": 7,
    "purple(12 sided)": 7,
    "red(6 sided)": 10,
    "red(8 sided)": 9,
    "clear(6 sided)": 7,
    "pink(12 sided)": 0
}

def welcome_message():
    print("Welcome to Panda Royale!")
    print("In this game, you will compete against other players by rolling dice and accumulating points.")
    print("Each player starts with one yellow 6-sided die, and can earn more dice throughout the game.")
    print("The player with the highest total score after 10 rounds wins!")
    print("Let's get started!")

def get_num_players():
    while True:
        try:
            num_players = int(input("Enter the number of players (2-10): "))
            if 2 <= num_players <= 10:
                return num_players
            else:
                print("Please enter a number between 2 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 10.")

def get_player_names(num_players):
    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ")
        players.append({
            "name": name,
            "turn_order": 0,
            "round_score": 0,
            "total_score": 0,
            "yellow_score_for_round": 0,
            "dice": {
                "yellow(6 sided)": 1, "yellow(8 sided)": 0,
                "green(20 sided)": 0, "blue(6 sided)": 0,
                "blue(8 sided)": 0, "blue(12 sided)": 0,
                "blue glitter(6 sided)": 0, "purple(8 sided)": 0,
                "purple(12 sided)": 0, "red(6 sided)": 0,
                "red(8 sided)": 0, "clear(6 sided)": 0,
                "pink(12 sided)": 0
            }
        })
    return players

def display_scoreboard(players):
    print("\nScoreboard:")
    print("-" * 60)
    for player in players:
        print(f"{player['name']:<10}  Yellow Score: {player['yellow_score_for_round']:>3}  "
              f"Round Score: {player['round_score']:>6}  Total Score: {player['total_score']:>6}")
    print("-" * 60)

# FIX 1: Yellow dice roll once — same value used for both round_score and yellow_score_for_round
# FIX 2: Blue dice totaled first, THEN doubled once if any glitter die is present
def roll_die(player):
    player["round_score"] = 0
    player["yellow_score_for_round"] = 0
    temp_blue_total = 0
    has_glitter = player["dice"]["blue glitter(6 sided)"] > 0
    num_red_dice = 0
    red_score = 0

    for die, quantity in player["dice"].items():
        for _ in range(quantity):
            if die == "yellow(6 sided)":
                # FIX 1: roll once, use for both totals
                roll = random.randint(1, 6)
                player["yellow_score_for_round"] += roll
                player["round_score"] += roll

            elif die == "yellow(8 sided)":
                roll = random.randint(1, 8)
                player["yellow_score_for_round"] += roll
                player["round_score"] += roll

            elif die == "green(20 sided)":
                player["round_score"] += random.randint(1, 20)

            # FIX 2: accumulate blue total, apply doubling after the loop
            elif die == "blue(6 sided)":
                temp_blue_total += random.randint(1, 6)
            elif die == "blue(8 sided)":
                temp_blue_total += random.randint(1, 8)
            elif die == "blue(12 sided)":
                temp_blue_total += random.randint(1, 12)
            elif die == "blue glitter(6 sided)":
                temp_blue_total += random.randint(1, 6)  # glitter is also a blue die

            elif die == "purple(8 sided)":
                player["round_score"] += random.randint(1, 8) * 2
            elif die == "purple(12 sided)":
                player["round_score"] += random.randint(1, 12) * 2

            elif die == "red(6 sided)":
                num_red_dice += 1
                red_value = random.randint(1, 6)
                red_score += red_value if red_value >= 4 else -red_value
            elif die == "red(8 sided)":
                num_red_dice += 1
                red_value = random.randint(1, 8)
                red_score += red_value if red_value >= 5 else -red_value

            elif die == "clear(6 sided)":
                player["round_score"] += random.randint(1, 6)
            elif die == "pink(12 sided)":
                player["round_score"] += random.randint(1, 12)

    # FIX 2: apply glitter doubling to the whole blue total at once
    if has_glitter:
        temp_blue_total *= 2
    player["round_score"] += temp_blue_total

    # Red scoring: sum * number of red dice
    if num_red_dice > 0:
        player["round_score"] += red_score * num_red_dice

    player["total_score"] += player["round_score"]
    player["dice"]["pink(12 sided)"] = 0  # reset pink after rolling
    return player

def display_dice_inventory(player):
    print(f"\n{player['name']}'s Dice Inventory:")
    for die, quantity in player["dice"].items():
        if quantity > 0:
            print(f"  {die}: {quantity}")
    print("-" * 40)

def turn_order(players):
    players.sort(key=lambda x: x["yellow_score_for_round"], reverse=True)
    for i, player in enumerate(players):
        player["turn_order"] = i + 1
    return players

def trade_dice(player, players):
    if player["dice"]["clear(6 sided)"] > 0:
        print(f"\n{player['name']}, you have {player['dice']['clear(6 sided)']} clear die/dice for trading.")
        trade_choice = input("Do you want to trade a clear die? (yes/no): ").lower()
        while trade_choice == "yes" and player["dice"]["clear(6 sided)"] > 0:
            target_player_name = input("Enter the name of the player you want to trade with: ")
            target_player = next((p for p in players if p["name"] == target_player_name), None)
            if not target_player or target_player == player:
                print("Invalid player name. Please try again.")
                continue
            display_dice_inventory(target_player)
            die_to_take = input("Enter the type of die you want to take (not pink): ")
            if (die_to_take in target_player["dice"]
                    and target_player["dice"][die_to_take] > 0
                    and die_to_take != "pink(12 sided)"):
                player["dice"]["clear(6 sided)"] -= 1
                player["dice"][die_to_take] += 1
                target_player["dice"][die_to_take] -= 1
                target_player["dice"]["clear(6 sided)"] += 1
                print(f"Trade successful! You traded a clear die for a {die_to_take}.")
                if player["dice"]["clear(6 sided)"] > 0:
                    trade_choice = input("Trade another clear die? (yes/no): ").lower()
                else:
                    break
            else:
                print("Invalid die choice (empty, doesn't exist, or is a pink die). Try again.")
    else:
        print(f"{player['name']} has no clear dice to trade.")
    return players

# FIX 3 & 4: each player in sorted turn order picks their own die from the shared pool
def choose_new_die(players, main_bag):
    num_players = len(players)

    # Build pool from bag
    available = [die for die, qty in main_bag.items() for _ in range(qty)]
    random.shuffle(available)
    pool = available[:num_players + 1]  # one more die than players

    # Remove drawn dice from bag
    for die in pool:
        main_bag[die] -= 1

    print(f"\nNew dice pool: {', '.join(pool)}")

    # Turn order by yellow score (highest first)
    sorted_players = sorted(players, key=lambda x: x["yellow_score_for_round"], reverse=True)

    for p in sorted_players:
        print(f"\nRemaining pool: {', '.join(pool)}")
        while True:
            chosen_die = input(f"{p['name']} (yellow score {p['yellow_score_for_round']}), choose a die: ")
            if chosen_die in pool:
                p["dice"][chosen_die] += 1
                pool.remove(chosen_die)
                print(f"{p['name']} added a {chosen_die} to their hand.")
                break
            else:
                print("That die is not in the pool. Please choose from the available dice.")

    # Leftover die goes back in the bag
    if pool:
        leftover = pool[0]
        main_bag[leftover] += 1
        print(f"\nThe leftover {leftover} goes back in the bag.")

    return players

def determine_pity_die(players):
    # Reset all pink dice first
    for player in players:
        player["dice"]["pink(12 sided)"] = 0

    num_pity_dice = 1 if len(players) <= 3 else 2 if len(players) <= 6 else 3 if len(players) <= 9 else 4
 
    players_by_score = sorted(players, key=lambda x: x["round_score"])
    for i in range(num_pity_dice):
        players_by_score[i]["dice"]["pink(12 sided)"] += 1
        print(f"{players_by_score[i]['name']} receives a pink pity die.")
    return players

def play_round(players, main_bag, is_final_round=False):
    # Step 1: Roll dice
    for i, player in enumerate(players):
        players[i] = roll_die(player)
 
    display_scoreboard(players)
 
    if not is_final_round:
        # Step 2: Pity dice
        players = determine_pity_die(players)
 
        # Step 3: Trade dice (panda token holder goes last; here we use turn order)
        players = turn_order(players)
        for player in players:
            players = trade_dice(player, players)
 
        # Step 4: Choose new die
        players = choose_new_die(players, main_bag)
 
    return players

# --- Main ---
print("\n" * 50)
welcome_message()
num_players = get_num_players()
players = get_player_names(num_players)

for round_num in range(1, 11):
    print(f"\n{'='*20} Round {round_num} {'='*20}")
    is_final = (round_num == 10)
    players = play_round(players, main_bag, is_final_round=is_final)

print("\nGame Over! Final Scores:")
display_scoreboard(players)
winner_score = max(p["total_score"] for p in players)
winners = [p["name"] for p in players if p["total_score"] == winner_score]
if len(winners) == 1:
    print(f"\n {winners[0]} wins Panda Royale!")
else:
    print(f"\n It's a tie! Winners: {', '.join(winners)}")
