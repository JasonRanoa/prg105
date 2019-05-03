"""
    class TriviaDataHandler
    Handles all methods that involve reading and writing into files.
"""


class TriviaDataHandler:
    data_path = "trivia_datafile.txt"
    trivia_array = []

    # Error Stuff
    has_error = False
    error_string = ""

    """
        def __init__(self)
        Opens datafile for trivia game.
        If file cannot be opened, tries to create new file.
        If anything fails, hasError flag is turned to true.
            Error message is saved.
    """
    def __init__(self):
        try:
            self.datafile = open(self.data_path, "r")
            self.load_trivia_into_array()
            self.datafile.close()
        except IOError:
            # Attempts to create file if file not found.
            try:
                self.datafile = open(self.data_path, "w")
                print("New file created: ", self.data_path)
                self.trivia_array = []
                self.datafile.close()
            except IOError:
                print("File cannot be opened or created")
                self.has_error = True
                self.error_string = "File cannot be opened or created"

    """
        def load_trivia_into_array(self)
        Assumes file is already opened and loads trivia stuff into the array.
        This method should only be called after opening the file with self.datafile
    """
    def load_trivia_into_array(self):
        self.trivia_array = []  # resets array so no weird indexing happens
        counter = 0
        prev_counter = -1  # deals with entries with multiple lines.
        for raw_line in self.datafile:
            line = raw_line.strip()
            if len(line) == 0:
                continue  # ignores blank lines

            if line[0] == "-":  # reaches delimiter
                prev_counter = counter
                counter += 1
            elif prev_counter != counter:  # new item
                self.trivia_array.append(line)
                prev_counter = counter
            else:
                self.trivia_array[counter] += "\n" + line

    """
        def update_datafile(self)
        Re-writes the new file with the current data on trivia_array.
        
        Datafile is also supposed to be ready, judging from initial conditions.
        This is supposed to work in conjuction to the load_trivia_into_array method.
    """
    def update_datafile(self):
        try:
            self.datafile = open(self.data_path, "w")
            for item in self.trivia_array:
                self.datafile.write(item + "\n")
                self.datafile.write("- \n")  # item delimiter
            self.datafile.close()
        except IOError:
            print("File cannot be updated with new data.")  # kind of vague but we're doing this in bulk.
            self.has_error = True
            self.error_string = "File cannot be updated with new data."

    """
        Standard getter and setter stuff.
        Only the error-related members are treated as public members.
        All other members are supposed to go through a getter/setter method
            for ease of refactoring next time.
    """
    def get_datafile_location(self):
        return self.data_path

    def get_list_length(self):
        return len(self.trivia_array)

    def get_list_member(self, idx):
        try:
            return self.trivia_array[idx]
        except IndexError:  # error out of bounds or invalid index
            return ""  # Empty string

    def set_list_member(self, idx, new_data):
        try:
            self.trivia_array[idx] = new_data
        except IndexError:
            print("Cannot update data on index {}.".format(idx))
            self.has_error = True
            self.error_string = "Data cannot be updated on index {}".format(idx)

    def add_new_member(self, new_data):
        self.trivia_array.append(new_data)

    def delete_list_member(self, idx):
        try:
            del self.trivia_array[idx]
        except IndexError:  # error out of bounds or invalid index
            return ""
