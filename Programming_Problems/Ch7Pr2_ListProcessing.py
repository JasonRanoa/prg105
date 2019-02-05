# Programming Practice 7.2 List Processing
"""
1.  Have a function that creates a list of 20 random integers
    between 1 and 100 (Assign them dynamically, store the list
    in a variable.)
2.  Have a function get a number from the user that is between
    1 and 100 (validate to ensure a number between 1 and 100 was
    entered instead of text or something out of range using a try
    and except statement).
3.  Pass both the list and the user's number to a function and
    have it display all numbers in the list that is greater than
    the user's number. If there are not any, display a message
    that explains there are no numbers in the list greater than the
    entered number.
"""
import random


def make_random_list(list_length):
    num_list = [
        random.randint(1, 100) for i in range(list_length)
    ]
    # List Comprehensions. Reference:
    # https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
    return num_list


def get_user_number():
    # Two checks: Within range and isInt
    user_num = -1
    while not 1 <= user_num <= 100:
        try:
            user_num = int(input("Please enter a number between 1 and 100: "))
            if not 1 <= user_num <= 100:
                print("   Given value is not in the interval. Try again.")
        except ValueError:
            print("   Given value is invalid. Please enter an integer")
    print()
    return user_num


def print_greater_than(num_list, given_num):
    # Prints values in num_list that are greater than given_num
    over_list = [x for x in num_list if x > given_num]
    if len(over_list) < 1:
        print("There are no numbers in the list greater than {}.".format(given_num))
    else:
        print("The following number(s) are greater than {} are the following:".format(given_num))
        print(*over_list, sep=", ")
        # The * before the list calls the list as multiple arguments, instead of as a list
        # Reference: https://stackoverflow.com/questions/5445970/how-to-properly-print-a-list


def main():
    num_list = make_random_list(20)

    print("The program generates a list of 20 numbers in [1,100]")
    print("You'll be asked to enter a number and see which in the list is less than that.")
    print()

    user_num = get_user_number()
    print_greater_than(num_list, user_num)


main()
