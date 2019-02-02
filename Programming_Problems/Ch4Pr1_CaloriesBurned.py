# Programming Practice 4.1 Calories Burned
"""
Running on a treadmill you burn 4.2 calories per minute.
Write a program that uses a loop to display the number of calories
burned after 10, 15, 20, 25 and 30 minutes.
"""

CALORIES_PER_MINUTE = 4.2
for i in range(5):
    minutes = 10 + i * 5
    print(
        "You burned {:.1f} calories in {} minutes"
        .format(CALORIES_PER_MINUTE * minutes, minutes)
    )
