# Programming Practice 6.2 Average of Numbers
"""
Write a program that uses the numbers.txt file,
which contains a series of integers. Your program will
calculate the average of all of the numbers stored in the
file and display the total on the screen. Format to show a
maximum of two numbers to the right of the decimal point.
"""

num_file = open("Ch6_Files/numbers.txt", "r")
total = 0
count = 0

for num in num_file:
    total = total + int(num)
    count = count + 1

average = total / count
print(
    "Numbers Read: {}\n"
    "Total: {:,.0f}\n"
    "Average: {:,.2f}"
    .format(count, total, average)
)

num_file.close()
