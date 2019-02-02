"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 4.2 A condition controlled loop
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0: while num > 0
num = 10
# write your code here, the variable needs to exist before you start the loop
while num > 0:
    num = num - 1
    print(num, end=" ")
print()
print()

# TODO 4.3 the For Loop
print("=" * 10, "Section 4.3 for loop", "=" * 10)
# Use a for loop with a list of the days of the week,
# print each day of the week
for day in ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]:
    print(day, end=" ")
print()
print()

# TODO 4.3 the for loop - range function
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
# use the range function to print the numbers from 1 to 10
for num in range(10):
    print(num + 1, end=" ")
print()
print()

# TODO 4.4 a running total
print("=" * 10, "Section 4.4 running total", "=" * 10)
# Use a loop to have the user enter 5 numbers, provide a total at the end
# You will need to initialize your accumulator before entering the loop
# You can assume valid integers are entered
total = 0
for i in range(5):
    user_num = int(input("Enter number: "))
    total = total + user_num
print("Total = {}".format(total))
print()

# TODO 4.5 Sentinel Value
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Use a loop to have the user enter test scores until a
# sentinel value of -1 is entered.
# After the loop, display the total, the count and the average (total / count)
print("Enter test scores. If done, enter -1.")
num_scores = 0
total_score = 0
test_score = int(input(
    "  Enter test score ({}): ".format(num_scores + 1)
))
while test_score != -1:
    num_scores = num_scores + 1
    total_score = total_score + test_score
    test_score = int(input(
        "  Enter test score ({}): ".format(num_scores + 1)
    ))
if num_scores == 0:
    num_scores = 1  # Prevents division by zero.
print("The total is {} and the average is {:.2f}".format(total_score, total_score / num_scores))
print()

# TODO 4.6 validating data
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data
number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:
    number = int(input("Number not in valid range. Try again: "))
