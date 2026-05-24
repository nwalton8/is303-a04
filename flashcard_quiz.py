'''
Noah Walton
IS303-A04

Flashcard Quiz
Quizzes the user on flashcards with randomized order and score tracking
Create card deck, shuffle (random library), ask question, track score, show results

Input:
- Number of flashcards
- Question and answer for each flashcard
- User's answer to each question

Processes:
- list_shuffle(the_dictionary) (Shuffle flashcards)
- ask_questions(the_dictionary) (Ask questions and receive user input)

Outputs:
- Number of correct answers
- current score after each question
- Final score and percentage at the end of the quiz
'''
import random
questions_answers = {}
def list_shuffle(questions_answers):
    items = list(questions_answers.items())
    random.shuffle(items)
    print("Flashcards shuffled!\n")
    return dict(items)
def ask_questions(questions_answers):
    score = 0
    total_questions = len(questions_answers)
    for question, answer in questions_answers.items():
        user_answer = input(f"{question} : ")
        if user_answer.strip().lower() == answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {answer}")
        print(f"Current Score: {score}/{total_questions}\n")
    return score, total_questions
def main():
    num_flashcards = int(input("Enter the number of flashcards: "))
    for _ in range(num_flashcards):
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        questions_answers[question] = answer
    print("\n" * 50)  # Clear the screen
    shuffled_flashcards = list_shuffle(questions_answers)
    score, total_questions = ask_questions(shuffled_flashcards)
    percentage = (score / total_questions) * 100
    print(f"Final Score: {score}/{total_questions} ({percentage:.2f}%)")
main()