# Programming Challenge 10.2 Trivia Game
"""
In this programming exercise, you will create a simple trivia game
for two players. The program will work like this:

Starting with player 1, each player gets a turn at answering 5
trivia questions. (There should be a total of 10 questions.)
When a question is displayed, 4 possible answers are also displayed.
Only one of the answers is correct, and if the player selects the
correct answer, he or she earns a point.
After answers have been selected for all the questions,
the program displays the number of points earned by each player
and declares the player with the highest number of points the winner.
To create this program, write a Question class to hold the data
for the trivia question. The question class should have attributes
for the following data:

A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)

The Question class should also have an appropriate __init__ method,
accessors, and mutators.

The program should have a list or a dictionary containing 10 Question
Objects, one for each trivia question. Make up your own trivia question
on the subject or subjects of your choice for the objects.
"""

import math
import random


"""
class Question has three attributes:
(1) Question Text
(2) Correct Answer, containing the index to the right answer in dictionary
(3) Possible Answers, a dictionary
"""


class Question:
    def __init__(self):
        self.question_text = ""
        self.correct_answer = 0
        self.possible_answers = {}

    def set_question_text(self, text):
        self.question_text = text

    def set_correct_answer(self, choice_number):
        self.correct_answer = choice_number

    def set_possible_answers(self, answer_dict):
        self.possible_answers = answer_dict.copy()

    def get_question_text(self):
        return self.question_text

    def get_correct_answer(self):
        return self.correct_answer

    def get_possible_answers(self):
        return self.possible_answers


"""
This method loads questions from a file and compiles them into a list.
Note that this code is very much dependent on the fact that the file it's
reading is tailored to work with it. No exception handling here.
"""


def load_questions_from_file():
    questions = []
    try:
        # The file contains 10 questions about BNHA
        qn_file = open("Ch10_Files/trivia_questions.txt")
        for i in range(10):
            qn = Question()
            qn.set_question_text(qn_file.readline()[:-1])

            possible_choices = {
                1: qn_file.readline()[2:-1],
                2: qn_file.readline()[2:-1],
                3: qn_file.readline()[2:-1],
                4: qn_file.readline()[2:-1]
            }
            qn.set_possible_answers(possible_choices)
            qn.set_correct_answer(
                int(qn_file.readline()[3])
            )
            qn_file.readline()  # Reads blank line
            questions.append(qn)

        qn_file.close()
    except IOError:
        print("Error Loading File.")

    return questions


"""
class Player. Contains name and points.
"""


class Player:
    def __init__(self):
        self.name = ""
        self.points = 0

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def set_name(self, new_name):
        self.name = new_name

    def set_points(self, new_points):
        self.points = new_points

    def add_one_point(self):
        self.points += 1


"""
Method: Player Loop. Accepts player, qn_list, and qn_per_person
Since lists are mutable data-types, these should function as if 
they're passed by reference.
"""


def player_loop(player, qn_list, qn_per_person):
    print("Player {} -- GAME START.".format(player.get_name()))
    for i in range(qn_per_person):
        # Retrieves qn and removes it from the pool
        curr_qn = qn_list.pop(
            random.randint(0, len(qn_list) - 1)
        )

        # Prints question information
        print("Qn. {}: {}".format(i + 1, curr_qn.get_question_text()))
        print("       Choose an answer from the ff.: ")
        for idx, ans in curr_qn.get_possible_answers().items():
            print("         ({}) {}".format(idx, ans))

        user_response = get_valid_user_int_response(
            "       Your Answer (Enter Index): ",
            "       Please enter a number from 1 to 4.\n",
            1, len(curr_qn.get_possible_answers()) + 1
        )
        print()

        # Checks user response from correct one
        if user_response == curr_qn.get_correct_answer():
            player.add_one_point()
            print("       CORRECT! Points so far: {}.".format(player.get_points()))
        else:
            print(
                "       WRONG! The correct answer is ({}) {}"
                .format(curr_qn.get_correct_answer(), curr_qn.get_possible_answers()[curr_qn.get_correct_answer()])
            )
        print()

    print("--- GAME END.")
    print("    Player: {}. Total Point(s): {}".format(player.get_name(), player.get_points()))
    input("    Press [ENTER] to continue.")
    print()


"""
The ff. method tries to get a valid answer from the user by looping as necessary.
Two flags can happen -- entry is not a number, and number is not in range.
By default, response = -1. When the entry is not a number, this remains the same.
If not, response is changed to a number.
In both cases, if the number is out of range, response is deemed invalid.
"""


def get_valid_user_int_response(prompt, err_prompt, min_range, max_range_exclusive):
    response = -1
    while response not in range(min_range, max_range_exclusive):
        raw_response = input(prompt)
        if raw_response.isdigit():
            response = int(raw_response)
        if response not in range(min_range, max_range_exclusive):
            response = -1
            print(err_prompt)
    return response


"""
Main Loop. 
"""


def main():
    questions = load_questions_from_file()

    # Setting up player information
    print("TRIVIA GAME.")
    players = [Player() for _ in range(2)]
    for i in range(len(players)):
        players[i].set_name(
            input("  Enter Player {} Name: ".format(i+1))
        )
    print()

    # Introduction
    print("Each player will answer the same number of questions.")
    print("Questions will be about Horikoshi's My Hero Academia series.")
    print()

    # Setting up question distribution.
    # Questions are removed from list once asked
    qn_per_person = math.floor(len(questions)/len(players))

    # Player loops.
    for player in players:
        player_loop(player, questions, qn_per_person)

    # Tallying up things
    max_score = max([pl.get_points() for pl in players])
    top_players_name = [
        p.get_name() for p in players if p.get_points() == max_score
    ]

    # Printing the results
    print("Here are the results for the game!")
    for player in players:
        print(
            "  Player {:<10} : {} Point(s)"
            .format(player.get_name(), player.get_points())
        )
    print()

    if len(top_players_name) == 1:
        print("The winner is Player {}!".format(top_players_name[0]))
    else:
        print("The winners are: ", end="")
        print(*top_players_name, sep=", ", end="!\n")
    print("Congratulations!")


main()
