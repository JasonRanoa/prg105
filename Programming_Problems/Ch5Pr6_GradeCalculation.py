# Programming Practice 5.6 Grade Calculation
"""
Write a program that asks a user to enter five test scores.
You will need to create five variables to hold these scores.

The purpose of this assignment is to get practice passing
information between functions, this is not a good example of the
way programs are really written, but it will help you to understand
how to pass parameters.
"""


def main():
    print("Enter scores for the following tests (0-100)")
    score1 = float(input("   Test 1: "))
    score2 = float(input("   Test 2: "))
    score3 = float(input("   Test 3: "))
    score4 = float(input("   Test 4: "))
    score5 = float(input("   Test 5: "))
    avg_score = calc_average(score1, score2, score3, score4, score5)
    letter_grade = determine_grade(avg_score)
    print(
        "With an average score of {:.1f},\n"
        "the letter grade assigned is {}."
        .format(avg_score, letter_grade)
    )


def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5


def determine_grade(avg_grade):
    if avg_grade >= 90:
        letter_grade = "A"
    elif avg_grade >= 80:
        letter_grade = "B"
    elif avg_grade >= 70:
        letter_grade = "C"
    elif avg_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


main()
