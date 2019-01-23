# Programming Practice 2.3 Ingredient Adjuster
"""
A cookie recipe calls for the following ingredients:
      1.5 cups of sugar
      1 cup of butter
      2.75 cups of flour
The recipe produces 48 cookies with this amount of ingredients.
Write a program that asks the user how many cookies they want to make,
and then displays the number of cups (to two decimal places) of each
ingredient needed for the specified number of cookies.
"""
# Program written by Julius Ranoa

# Constants, Cookie Recipe. Amount in cups
COOKIE_COUNT = 48
SUGAR_AMT = 1.5;
BUTTER_AMT = 1;
FLOUR_AMT = 2.75;

# Prompts and inputs
print("This program calculates the amount of ingredients needed for a cookie recipe.")
desired_amt_cookie = int( input("Enter desired number of cookies: ") );
print();

# Calculations
needed_sugar = SUGAR_AMT / COOKIE_COUNT * desired_amt_cookie;
needed_butter = BUTTER_AMT / COOKIE_COUNT * desired_amt_cookie;
needed_flour = FLOUR_AMT / COOKIE_COUNT * desired_amt_cookie;

# Results
# Note. A semicolon is needed before any format specs
print("You wanted {} cookie(s).".format(desired_amt_cookie));
print("For that, you need the following:\n"
      "\t{:.2f} cup(s) of sugar\n".format(needed_sugar),
      "\t{:.2f} cup(s) of butter\n".format(needed_butter),
      "\t{:.2f} cup(s) of flour".format(needed_flour)
);



