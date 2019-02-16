# Programming Practice 8.2 Alphabetic Telephone Number Translator
"""
Many companies use telephone numbers like 555-GET-FOOD so
the number is easier for their customers to remember.
On a standard telephone the alphabetic letters are mapped to
numbers in the following fashion:

A, B, C = 2
D, E, F = 3
G, H, I = 4
J, K, L = 5
M, N, O = 6
P, Q, R, S = 7
T, U, V, = 8
W, X, Y, Z = 9

Write a program that asks the user to enter a 10-character telephone
number in the format XXX-XXX-XXXX. The application should display
the telephone number with any alphabetic characters that appeared
in the original translated to their numeric equivalent.
"""

# Translation Code, Parallel Arrays
alphas = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
digits = [2, 3, 4, 5, 6, 7, 8, 9]


def alpha_to_num(letter):
    if letter.isalpha():
        letter = letter.upper()  # Makes things easier
        for i in range(len(alphas)):
            if letter in alphas[i]:
                letter = str(digits[i])  # changes letter to a digit char
                break  # breaks checking loop once found
    return letter


print("This program converts spelled numbers to actual numbers.")
tel_num = input("Enter a spelled phone number: ")
translated_num = ""
for char in tel_num:
    translated_num += alpha_to_num(char)
print()

print("This number, {}, converts to {}.".format(tel_num, translated_num))
