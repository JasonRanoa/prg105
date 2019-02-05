# Programming Practice 7.1 Rainfall Statistics
"""
Copy program 4.3 into the chapter 7 folder and rename it as
"7-1-Rainfall-Statistics"
Modify the program so that the rainfall for each month is stored
into a list. Eliminate the user's ability to select the number of
years, you will just work with one year's data.
The program should calculate and display the total rainfall for the
year, the average monthly rainfall the year, and the months with the
highest and lowest amounts of rain for the year.
Hint: convert months to a list so you can use the index value to
print the max and min months.
"""

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
rainfall_data = [0.0] * len(months)
total_rainfall = 0

# Initial Prompt
print(
    "This program calculates the total rainfall and average \n"
    "monthly rainfall over a period of one year. "
)
print()

# Data Collection
print("Enter monthly rainfall data for the ff. months in inches.")
for i in range(len(months)):
    rainfall_data[i] = float(input(
        "   Rainfall Data for {:<12}  ".format(months[i] + "?")
    ))
    total_rainfall = total_rainfall + rainfall_data[i]
print()

average_rainfall = total_rainfall / len(months)
max_rainfall_idx = rainfall_data.index(max(rainfall_data))
min_rainfall_idx = rainfall_data.index(min(rainfall_data))

# Displaying Results
print(
    "The statistics for this year are the following: \n"
    "   Total Rainfall      : {total:.1f} inch(es)\n"
    "   Average Rainfall    : {avg:.2f} inch(es)\n"
    "   Highest Amt of Rain : {max_mth}, {max_data:.1f} inches\n"
    "   Lowest Amt of Rain  : {min_mth}, {min_data:.1f} inches\n"
    .format(
        total=total_rainfall, avg=average_rainfall,
        max_mth=months[max_rainfall_idx], max_data=rainfall_data[max_rainfall_idx],
        min_mth=months[min_rainfall_idx], min_data=rainfall_data[min_rainfall_idx]
    )
)
