# Programming Practice 4.3 Average Rainfall
"""
Write a program that uses nested loops to collect data and
calculate the average rainfall over a period of years. The
program should first ask for the number of years. The outer
loop will iterate once for each year. The inner loop will iterate
12 times, once for each month. Each iteration of the inner loop
will ask the user for the inches of rainfall for that month. After
all iterations, the program should display the number of months,
the total inches of rainfall, and the average rainfall per month
for the entire period.
"""

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

print(
    "This program calculates the total rainfall and average \n"
    "monthly rainfall over a certain number of years. "
)
num_years = int(input("How many years to collect data for? "))
print()

total_rainfall = 0
total_months = num_years * 12
monthly_rainfall = 0
for year in range(num_years):
    print("Enter data (monthly) for Year {}: ".format(year + 1))
    for month in months:
        monthly_rainfall = float(input(
            "   Rainfall Data for {:<12}  ".format(month + "?")
        ))
        total_rainfall = total_rainfall + monthly_rainfall
    print()

average_rainfall = total_rainfall / total_months
print(
    "The total amount of rainfall over {} months was {:,.2f} inches \n"
    "The average monthly rainfall was {:,.2f} inches"
    .format(total_months, total_rainfall, average_rainfall)
)
