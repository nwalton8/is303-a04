
#before debugging

'''
Noah Walton
IS303-A04

Dice Game
A simple dice game where the player rolls against the computer
Roll dice (random library), determine winner, play round, show scoreboard
recreate panda royale game by nate and jake jenne

Inputs:
- Player's name (string)
- number of additional players, besides self (1 to 9) (int)
- Player's choice of dice (int, optioned as 1, 2, 3, ...) (dependant on players but will have one more than 
the number of players available for each round)

Processes:
- dice_rolling (random library)
- dice_scoring (determine winner of each round)
- round_play (play a round of the game, including rolling and scoring)
- scoreboard (keep track of scores and display them after each round)
- dice_inventory (keep track of available dice for each player, and update after each round)
- dice_in_main_bag (keep track of dice available in the main bag, and update after each round)
- computer_logic (determine computer's choice of dice based on available options and strategy)
- determine_pity_die (determine which players earn a pity die based on their scores and the rules of the game)
- trade_dice (allow players to trade dice with each other based on the rules of the game)
- choose_new_die (allow players to choose a new die to add to their hand based on the rules of the game)
- Welcome_message (display a welcome message and instructions for the game)
- Determine winner of each round
- Keep track of scores

Outputs: 
- Display player and computer scores
- display each player's current dice inventory
- Show winner of each round
- Show final winner at the end of the game
- Display final scoreboard

Game overview:
Each year, as the mid-summer festival begins, the seven panda clans gather to celebrate their many years of peace 
and prosperity. After all the feasts, stories, and games, the Elders host the annual competition wherein the 
bravest of all pandas gather together to battle for honor and glory. The panda clans each have their own 
powers and abilities, and the Elders consider those strengths carefully as they assemble their teams from 
members of each of them.

You will play as one of the panda Elders and will choose pandas to join your team from among the seven cans 
(represented by seven colors of dice). Each panda clan will offer unique abilities to your team, so choose 
wisely in order to accumulate the highest score over 10 rounds.


Dice contents:
- 10 yellow 6-sided dice (one per player, rest are not for use)
- 7 yellow 8-sided dice
- 10 green 20-sided dice
- 10 blue 6-sided dice
- 9 blue 8-sided dice
- 9 blue 12-sided dice
- 7 blue glitter 6-sided dice
- 7 purple 8-sided dice
- 7 purple 12-sided dice
- 10 red 6-sided dice
- 9 red 8-sided dice
- 7 clear 6-sided dice
- 4 pink 12-sided dice (pity dice, given to lowest scoring players each round, dependant on num of players)

Rules: (for personal refference for building the code)
- each player starts with one yellow 6-sided die
- for total players, 2-3 players = 1 pink dice, 4-6 players = 2 pink dice, 7-9 players = 3 pink dice, 
10 players = 4 pink dice.
- 10 round game
- steps for each round: 1. role dice and calculate scores, 2. determine which players earn pity die, 
3. trade dice, 4. choose a new die to add to your hand
- note: only step one in final round 

1. ROLL DICE AND CALCULATE SCORES
Simultaneously, all players roll all of their dice. Next, everyone sums the face value of their yellow dice. 
Whoever has the highest total yellow value earns the Panda token. In the case of a tie for the highest yellow 
value, all players re-roll all of their yellow dice until the tie is broken. Players then tally their scores for 
the round, counting only their own dice. Each color of dice has its own method of scoring:

- Yellow dice: Sum the face value of all your yellow dice.
- Purple dice: Add the face value of all your purple dice and then double it.
- Blue dice: Add the face value of all your blue dice. If at least one of your blue dice is a special 
  die (glitter), then double the total value of your blue dice. If you have multiple special glittery dice, 
  your blue total is only doubled once.
- Red dice: Add the face value of all red dice, counting all white numbers as positive and black numbers as 
negative. Then multiply the sum by the total number of red dice you own. 
For a red 6-sided die (1-3 is black, 4-6 is white), and a red 8-sided die (1-4 is black, 5-8 is white)
- Green dice: Add the face value of all green dice.
- Clear dice: Add the face value of all clear (white) dice. The special properties of these discussed later.
- Pink dice: Record the value of your pink die if you have one. These dice are special and are distributed to 
the lowest-scoring players each round. Detailed more later.

Each player should tally their points for the round and write the total in the right-most column on their score 
sheet. Note that due to the red dice, your total score for the round could be negative.

2. Claim The Pity Dice
After calculating the total for the round, the pink pit dice are all redistributed. The lowest-scoring player 
for the round takes one pink pity die. Then, the next lowest player takes one, and so on until all pink dice are 
distributed. If at any time during this process there is a tie for the lowest score and not enough pink dice for 
each of the tied players, start with the player to the right of the Panda token and work counter-clockwise around 
the table, giving each of the tied players a pink die until they are all taken. All pink dice are redistributed 
each round so that no player should ever have more than one pink die at a time.

3. Trade Dice
Beginning with the player to the left of the Panda token, each player who has at least one clear(white) die may 
choose to trade it with any other player. To trade, simply give the clear die to another player and take any one 
of their dice. Note that you cannot take a pink die, but all other dice are available for the taking, even dice 
that were just acquired via trade. You do not have to trade dice if you do not wish to do so, and if you have 
multiple clear dice, you may trade any number of them. Note that once a clear die has been traded, it cannot be 
used to trade again until the next round. Moving clockwise around the table, take turns trading dice so that the 
player with the Panda token has the final opportunity to trade.

4. Choose New Dice
Finally, draw random dice out of the bag until you have one more die than the number of players. Place these new 
dice in the center of the table as the pool of dice from which players will choose. Take turns choosing one die 
from the pool to add to your hand. Turn order is determined by each player's yellow score for the round that was 
just completed. Begin with the player who has the highest yellow score and end with the player who has the lowest 
yellow score. Any tied players should take turns in clockwise order, starting from the Panda token. Once all 
players have chosen a new die to add to their hand, place the remaining die back in the bag and begin the next 
round.

END OF GAME
The game ends after the tenth round, and final scores are tallied. There is no need to break ties for yellow 
rolls, assign pity dice, or choose new dice after the final roll. Instead, calculate your total score by summing 
your scores for each of the ten rounds. The player with the highest total wins Panda Royale. In the case of a 
tie, the win is shared.

'''
import random

players = [
]


main_bag = {"yellow(6 sided)": 0, "yellow(8 sided)": 7, "green(20 sided)": 10, "blue(6 sided)": 10, "blue(8 sided)": 9, "blue(12 sided)": 9, "blue glitter(6 sided)": 7, "purple(8 sided)": 7, "purple(12 sided)": 7, "red(6 sided)": 10, "red(8 sided)": 9, "clear(6 sided)": 7, "pink(12 sided)": 0}

# Functions:
def welcome_message():
    print("Welcome to Panda Royale!")
    print("In this game, you will compete against other players by rolling dice and accumulating points.")
    print("Each player starts with one yellow 6-sided die, and can earn more dice throughout the game.")
    print("The player with the highest total score after 10 rounds wins!")
    print("Let's get started!")
    return

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
        players.append({"name": name, "turn_order": 0, "round_score": 0, "total_score": 0, "yellow_score_for_round": 0, "dice": {"yellow(6 sided)": 1, "yellow(8 sided)": 0, "green(20 sided)": 0, "blue(6 sided)": 0, "blue(8 sided)": 0, "blue(12 sided)": 0, "blue glitter(6 sided)": 0, "purple(8 sided)": 0, "purple(12 sided)": 0, "red(6 sided)": 0, "red(8 sided)": 0, "clear(6 sided)": 0, "pink(12 sided)": 0}})
    return players

def display_scoreboard(players):
    print("\nScoreboard:")
    print("-" * 40)
    for player in players:
        print(f"{player['name']:<10}, Yellow Score: {player['yellow_score_for_round']:>2}, Round Score: {player['round_score']:>6}, Total Score: {player['total_score']:>6}")
    print("-" * 40)

def roll_die(player):
    player["round_score"] = 0
    player["yellow_score_for_round"] = 0
    temp_blue = 0
    num_red_dice = 0
    red_score = 0
    for die, quantity in player["dice"].items():
        for _ in range(quantity):
            if die == "yellow(6 sided)":
                player["round_score"] += random.randint(1, 6)
                player["yellow_score_for_round"] += random.randint(1, 6)
            elif die == "yellow(8 sided)":
                player["round_score"] += random.randint(1, 8)
                player["yellow_score_for_round"] += random.randint(1, 8)
            elif die == "green(20 sided)":
                player["round_score"] += random.randint(1, 20)
            elif die == "blue(6 sided)":
                temp_blue = random.randint(1, 6)
                if player["dice"]["blue glitter(6 sided)"] > 0:
                    temp_blue *= 2
                player["round_score"] += temp_blue
                temp_blue = 0
            elif die == "blue(8 sided)":
                temp_blue = random.randint(1, 8)
                if player["dice"]["blue glitter(6 sided)"] > 0:
                    temp_blue *= 2
                player["round_score"] += temp_blue
                temp_blue = 0
            elif die == "blue(12 sided)":
                temp_blue = random.randint(1, 12)
                if player["dice"]["blue glitter(6 sided)"] > 0:
                    temp_blue *= 2
                player["round_score"] += temp_blue
                temp_blue = 0
            elif die == "blue glitter(6 sided)":
                player["round_score"] += random.randint(1, 6) * 2
            elif die == "purple(8 sided)":
                player["round_score"] += random.randint(1, 8) * 2
            elif die == "purple(12 sided)":
                player["round_score"] += random.randint(1, 12) * 2
            elif die == "red(6 sided)":
                num_red_dice += 1
                red_value = random.randint(1, 6)
                if red_value <= 3:
                    red_score -= red_value
                else:
                    red_score += red_value
            elif die == "red(8 sided)":
                num_red_dice += 1
                red_value = random.randint(1, 8)
                if red_value <= 4:
                    red_score -= red_value
                else:
                    red_score += red_value
            elif die == "clear(6 sided)":
                player["round_score"] += random.randint(1, 6)
            elif die == "pink(12 sided)":
                player["round_score"] += random.randint(1, 12)
    player["round_score"] += red_score * num_red_dice
    player["total_score"] += player["round_score"]
    player["dice"]["pink(12 sided)"] = 0  # Reset pink dice after rolling
    return player
     
def display_dice_inventory(player):
    print(f"{player['name']}'s Dice Inventory:")
    for die, quantity in player["dice"].items():
        print(f"{die}: {quantity}")
    print("-" * 40)
    
def turn_order(players):
    players.sort(key=lambda x: x["yellow_score_for_round"], reverse=True)
    for i, player in enumerate(players):
        player["turn_order"] = i + 1
    return players
        
def trade_dice(player, players):
    if player["dice"]["clear(6 sided)"] > 0:
        print(f"{player['name']}, you have {player['dice']['clear(6 sided)']} clear dice available for trading.")
        trade_choice = input("Do you want to trade a clear die? (yes/no): ").lower()
        if trade_choice == "yes":
            while True:
                target_player_name = input("Enter the name of the player you want to trade with: ")
                target_player = next((p for p in players if p["name"] == target_player_name), None)
                if target_player and target_player != player:
                    print(f"{target_player['name']}'s Dice Inventory:")
                    for die, quantity in target_player["dice"].items():
                        print(f"{die}: {quantity}")
                    die_to_take = input("Enter the type of die you want to take from the target player: ")
                    if die_to_take in target_player["dice"] and target_player["dice"][die_to_take] > 0 and die_to_take != "pink(12 sided)":
                        # Perform the trade
                        player["dice"]["clear(6 sided)"] -= 1
                        player["dice"][die_to_take] += 1
                        target_player["dice"][die_to_take] -= 1
                        target_player["dice"]["clear(6 sided)"] += 1
                        print(f"Trade successful! You traded a clear die for a {die_to_take}.")
                        break
                    else:
                        print("Invalid die choice. Please try again.")
                else:
                    print("Invalid player name. Please try again.")
    else:
        print(f"{player['name']}, you do not have any clear dice available for trading.")
    return players
        
def choose_new_die(player, players, main_bag):
    num_players = len(players)
    new_dice_pool = []
    for die, quantity in main_bag.items():
        new_dice_pool.extend([die] * quantity)
    random.shuffle(new_dice_pool)
    new_dice_pool = new_dice_pool[:num_players + 1]
    print(f"New dice available for choosing: {', '.join(new_dice_pool)}")
    for p in players:
        print(f"{p['name']} - Yellow Score: {p['yellow_score_for_round']}")
        while True:
            chosen_die = input(f" {player['name']}, enter the type of die you want to add to your hand: ")
            if chosen_die in new_dice_pool:
                player["dice"][chosen_die] += 1
                main_bag[chosen_die] -= 1
                print(f"You added a {chosen_die} to your hand.")
                break
            else:
                print("Invalid die choice. Please try again.")
    return players
                
def determine_pity_die(players):
    players.sort(key=lambda x: x["round_score"])
    for player in players:
        if player['dice']['pink(12 sided)'] > 0:
            player['dice']['pink(12 sided)'] = 0
    num_pity_dice = 0
    if len(players) <= 3:
        num_pity_dice = 1
    elif len(players) <= 6:
        num_pity_dice = 2
    elif len(players) <= 9:
        num_pity_dice = 3
    else:
        num_pity_dice = 4
    for i in range(num_pity_dice):
        players[i]["dice"]["pink(12 sided)"] += 1
    return players
                   
def play_round(players, main_bag):
    for player in players:
        players[players.index(player)] = roll_die(player)
    display_scoreboard(players)
    players = determine_pity_die(players)
    players = turn_order(players)
    for player in players:
        players = trade_dice(player, players)
    players = choose_new_die(player, players, main_bag)
    return players
        
print("\n" * 50)  # Clear the screen
welcome_message()
num_players = get_num_players()
players = get_player_names(num_players)
for round in range(1, 11):
    print(f"\n--- Round {round} ---")
    players = play_round(players, main_bag)
print("\nGame Over! Final Scores:")
display_scoreboard(players)
