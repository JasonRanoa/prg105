"""
    Class DirectoryHandler
    This class handles the files that contain the question lists for this game.
    All data is saved under quiz_data/__metadata.json (two underscores)

    Only files that are listed in this file are loaded as "categories".
    File parameters:
        filename        : the data file it's saved as
        category_name   : the category name that gets shown to the players
        description     : category description
        hidden          : (bool) if true, this category is hidden to players
        qn_num          : (int) number of questions recorded
"""

import json
import os


class DirectoryHandler:
    QUIZ_PARENT_DIR = "quiz_data"  # folder where the metadata and quiz data are saved.
    METADATA_FILENAME = "__metadata.json"
    file_metadata_list = []  # array where file metadata is loaded
    # the file names as they are saved in the directory
    # this gets updated every time the metadata file is updated
    loaded_file_names = []

    def __init__(self):
        self.load_metadata_from_file()

    """
        def load_metadata_from_file(self)
        Loads the metadata information from metadata.json and compares that
        to the files found in QUIZ_PARENT_DIR. Files in that folder that are not
        in the metadata file are not loaded.
    """
    def load_metadata_from_file(self):
        self.file_metadata_list = []  # Resets list.
        try:
            metadata_file = open(self.QUIZ_PARENT_DIR + "/" + self.METADATA_FILENAME, "r")

            if os.stat(self.QUIZ_PARENT_DIR + "/" + self.METADATA_FILENAME).st_size != 0:
                temp_metadata = json.load(metadata_file)  # loads json file
            else:
                temp_metadata = []  # just create an empty list if item cannot be loaded.
            raw_file_list = os.listdir(self.QUIZ_PARENT_DIR)

            # If temp_metadata is not an iterable, then the next code block
            # will fail. This also means that the metadata file is corrupted.
            # Reference: https://stackoverflow.com/questions/16807011/python-how-to-identify-if-a-variable-is-an-array-or-a-scalar
            if not isinstance(temp_metadata, list):
                print("DIR/FILE ERROR: Metadata file is corrupted.")
                quit()

            for entry in temp_metadata:
                if type(entry) is dict and "filename" in entry.keys():
                    # skip if entry is not a dictionary OR has no "filename" key
                    # this means that the file is not formatted correctly
                    #       or has been edited manually (and the person messed up)
                    if entry["filename"] in raw_file_list:
                        self.file_metadata_list.append(entry.copy())
                    else:  # create empty file and reset file stats.
                        self.create_blank_file(entry["filename"])
                        self.file_metadata_list.append({
                            "filename": entry["filename"],
                            "category_name": entry["category_name"] if "category_name" in entry.keys() else "-UNKNOWN-",
                            "description": "",
                            "hidden": True,
                            "qn_num": 0,
                        })
            metadata_file.close()

            # Save changes to metadata file
            self.update_metadata_file()
            # Update loaded file names array
            self.loaded_file_names = []  # Reset list.
            for entry in self.file_metadata_list:
                self.loaded_file_names.append(entry["filename"])

        except (IOError, OSError):
            print("DIR/FILE ERROR: Category data cannot be loaded.")
            quit()


    """
        def update_metadata_file
        Updates metadata file with the new list. Overwrites previous data.
    """
    def update_metadata_file(self):
        try:
            for idx, original_filename in enumerate(self.loaded_file_names):
                if not original_filename:  # if string is empty and therefore no original file
                    pass
                elif original_filename != self.file_metadata_list[idx]["filename"]:
                    os.rename(
                        self.QUIZ_PARENT_DIR + "/" + original_filename,
                        self.QUIZ_PARENT_DIR + "/" + self.file_metadata_list[idx]["filename"]
                    )
                else:
                    pass  # do nothing

            metadata_file = open(self.QUIZ_PARENT_DIR + "/" + self.METADATA_FILENAME, "w")
            metadata_file.write(
                json.dumps(self.file_metadata_list, indent=4)
            )
            metadata_file.close()
        except (IOError, OSError):
            print("DIR/FILE ERROR: Metadata file cannot be saved/overwritten.")
            quit()

    """
        def create_blank_file
        Creates a blank file on the metadata folder.
        This method is called when a file cannot be found given a valid filename
    """
    def create_blank_file(self, filename):
        try:
            new_file = open(self.QUIZ_PARENT_DIR + "/" + filename, "w")
            # basically, do nothing with the file.
            new_file.close()
        except IOError:
            print("DIR/FILE ERROR: Blank file cannot be created under filename: {}".format(filename))
            quit()

    """
        def append_new_entry(self, filename, category_name, hidden, qn_num)
        Adds new entry to metadata list and saves file.
    """
    def append_new_entry(self, filename, category_name, description, hidden, qn_number):
        if not filename or not category_name:
            print("DIR/FILE ERROR. A file cannot be created without a filename or a category name. ")
            quit()

        self.file_metadata_list.append({
            "filename": filename,
            "category_name": category_name,
            "description": description,
            "hidden": bool(hidden),
            "qn_num": qn_number
        })
        self.loaded_file_names.append("")
        self.create_blank_file(filename)
        self.update_metadata_file()

    """
    
    """
    def edit_entry_by_idx(self, idx, filename, category_name, description, hidden, qn_number):
        if not filename or not category_name:
            print("DIR/FILE ERROR. A file cannot be created without a filename or a category name. ")
            quit()
        try:
            self.file_metadata_list[idx]["filename"] = filename
            self.file_metadata_list[idx]["category_name"] = category_name
            self.file_metadata_list[idx]["description"] = description
            self.file_metadata_list[idx]["hidden"] = hidden
            self.file_metadata_list[idx]["qn_num"] = qn_number

            self.update_metadata_file()
            self.loaded_file_names[idx] = filename
        except IndexError:
            print("DIR/FILE ERROR. Index passed for edit is out of bounds. ")
            quit()

    """
    """
    def update_file_question_count(self, idx, qn_number):
        try:
            self.file_metadata_list[idx]["qn_num"] = qn_number
            self.update_metadata_file()
        except IndexError:
            print("DIR/FILE ERROR. Index passed for edit is out of bounds. ")
            quit()

    """
        def delete_entry_by_idx(self, idx)
        Deletes entry by their index in self.file_metadata_list
        This method fails silently if index provided is not in array
    """
    def delete_entry_by_idx(self, idx):
        try:
            os.remove(self.QUIZ_PARENT_DIR + "/" + self.file_metadata_list[idx]["filename"])
            del self.loaded_file_names[idx]
            del self.file_metadata_list[idx]
            self.update_metadata_file()
        except (IndexError, OSError):
            pass

    """
        STANDARD GETTERS AND SETTERS
    """
    def get_list_length(self):
        return len(self.file_metadata_list)

    # VALIDATES AN INDEX
    def is_valid_index(self, index):
        try:
            _ = self.file_metadata_list[index]
            return True
        except (IndexError, TypeError):
            return False
