# Programming Practice 9.1 Name and Email Address
"""
Write a program that keeps names and email addresses in a
dictionary as key-value pairs. The program should display a
menu that lets the user look up a person's email address,
add a new name and email address, change an existing email
address, and delete an existing name and email address.
The program should pickle the dictionary and save it to a
file when the user exits the program. Each time the program
starts, it should retrieve the dictionary from the file and unpickle it.
"""

import pickle

DATA_FILENAME = "Ch9_Files/Names_and_Addresses.bin"


def main():
    user_dict = get_dictionary_from_file()
    user_response = -1
    # Reference: https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement
    # Python treats functions as objects too
    ui_branches = {
        1: ui_lookup,
        2: ui_add_entry,
        3: ui_update_entry,
        4: ui_delete_entry
    }
    while user_response != 5:
        user_response = get_user_init_response()
        if user_response != 5:
            ui_branches[user_response](user_dict)

    print("--- END ---")


def get_dictionary_from_file():
    # Unpickle data file. If non-existent, make a new one.
    temp_dict = {}
    try:
        data_file = open(DATA_FILENAME, "rb")
        # Assuming pickle file is not corrupted.
        # Not dealing with that mess at the moment
        temp_dict = pickle.load(data_file)
        data_file.close()
    except IOError:
        data_file = open(DATA_FILENAME, "wb")
        pickle.dump(temp_dict, data_file)
        data_file.close()
    return temp_dict


def update_file(directory):
    # Pickle dictionary to file, complete overwrite
    save_file = open(DATA_FILENAME, "wb")
    pickle.dump(directory, save_file)
    save_file.close()


def get_user_init_response():
    # Print options
    print(
        "Name and Email Address Directory.",
        "Select an action from the ff. by entering number of choice:",
        "   (1) Look up a person's email address",
        "   (2) Add a new entry",
        "   (3) Change an existing email address",
        "   (4) Delete an entry",
        "   (5) Exit the program.",
        sep="\n"
    )
    print()
    # Get user response. Loop until valid response is received
    response = -1
    while response not in range(1, 6):
        raw_response = input("Response? ")
        if raw_response.isdigit():
            response = int(raw_response)
        if response not in range(1, 6):
            response = -1
            print("Please enter a number between 1 and 5.")
    print()
    return response


def ui_lookup(directory):
    print("---LOOK UP/FIND")
    name = input("   Enter name saved in record: ")
    print()

    if name in directory:
        email = directory[name]
        print(
            "   Record found.",
            "   Name  : {}".format(name),
            "   Email : {}".format(email),
            sep="\n"
        )
    else:
        print("   Name not in file. ")
    print()


def ui_add_entry(directory):
    # Adds new entry. Does not check for overwrites and duplicates
    print("---ADD NEW ENTRY")
    print("   Please enter the ff. details.")
    name = input("   Name  : ")
    email = input("   Email : ")
    print()

    directory[name] = email
    update_file(directory)
    print("Name and email address added to file.")
    print()


def ui_update_entry(directory):
    print("---UPDATE RECORD")
    name = input("   Enter name saved in record: ")
    print()

    if name in directory:
        email = directory[name]
        print(
            "   Record found.",
            "   Name  : {}".format(name),
            "   Email : {}".format(email),
            sep="\n"
        )
        print()

        new_email = input("   Enter new email address: ")
        directory[name] = new_email
        update_file(directory)

        print("   Record updated.")
        print()
    else:
        print("   Record not found. ")
    print()


def ui_delete_entry(directory):
    print("---DELETE RECORD")
    name = input("   Enter name saved in record: ")
    print()

    if name in directory:
        email = directory[name]
        print(
            "   Record found.",
            "   Name  : {}".format(name),
            "   Email : {}".format(email),
            sep="\n"
        )
        print()

        # Reference: https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary
        # Not sure but does Python only pass dictionaries by reference?
        del directory[name]
        update_file(directory)

        print("   Record deleted.")
        print()
    else:
        print("   Record not found. ")
    print()


main()
