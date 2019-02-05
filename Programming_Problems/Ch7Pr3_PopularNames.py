# Programming Practice 7.3 Popular Names
"""
The following two files contain names of popular Boy's names
and popular Girl's names. Download them and add them to your project file.
Then, write a program that reads the contents of the two files into
two separate lists. The user should be able to enter a boy's name or a
girl's name. The application should check both lists, and then display
messages indicating whether the names were among the most popular if the
name was on one of the lists or that the name was not on the lists of
popular names.
"""

GIRL_NAMES_FILE = "Ch7_Files/GirlNames.txt"
BOY_NAMES_FILE = "Ch7_Files/BoyNames.txt"


def load_names(filename):
    try:
        names_file = open(filename, "r")
        names_list = [name.strip() for name in names_file]
        # The readlines also include \n -- which throws off comparisons
        names_file.close()
        return names_list
    except IOError:
        print("Cannot load file: {}. No names read.".format(filename))
        return []


def ask_user_name():
    return input("Please enter a name: ")


def main():
    boy_names = load_names(BOY_NAMES_FILE)
    girl_names = load_names(GIRL_NAMES_FILE)
    user_name = ask_user_name()

    flag_in_boys = user_name in boy_names
    flag_in_girls = user_name in girl_names

    if flag_in_boys and flag_in_girls:
        # Unlikely but I haven't checked the list for intersections
        print("The name, {}, is a popular boy's and girl's name.".format(user_name))
    elif flag_in_girls:
        print("The name, {}, is a popular girl's name.".format(user_name))
    elif flag_in_boys:
        print("The name, {}, is a popular boy's name.".format(user_name))
    else:
        print("The name, {}, is not popular.".format(user_name))


main()
