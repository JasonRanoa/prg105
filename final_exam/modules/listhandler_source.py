"""
    class ListHandler
    This class handles the list of questions and is the middle-class
    between the question data and the GUI.
"""

import os
import json
from .qncontainer_source import Question


class ListHandler:
    QUIZ_PARENT_DIR = "quiz_data"  # folder where the question lists and metadata saved

    # Class Members
    # Directory-related members
    list_metadata = {}  # THIS COPY HAS NO CONTROL OVER THE ACTUAL FILES. ONLY FOR REFERENCE
    # Question-related members
    questions_list = []  # contains Question objects

    """
        def __init__(self, file_index)
        Args:   file_index -- The file index as the item appears in the dir handler.
                              This class is supposed to work with a dir handler.
    """
    def __init__(self, list_metadata):
        self.list_metadata = list_metadata.copy()
        self.load_questions_from_file()

    """
        def load_questions_from_file(self)
        If there's something wrong with the file, the program is ended.
            A print statement is made about the error.
            However, if the files are correctly formatted, there should be no problem with this.
        Question objects are appended to the questions_list
    """
    def load_questions_from_file(self):
        # Reset questions list
        self.questions_list = []
        try:
            file_path = self.QUIZ_PARENT_DIR + "/" + self.list_metadata["filename"]
            # first check if file is empty
            if os.stat(file_path).st_size != 0:
                list_file = open(file_path, "r")
                raw_list = json.loads(list_file.read())

                # if the json loaded is not an iterable, quit program.
                if not isinstance(raw_list, list):
                    print("LIST/FILE ERROR. Question file is corrupted.")
                    quit()

                # Create a Question item from each item
                for item in raw_list:
                    self.questions_list.append(Question(item))

                list_file.close()
            else:  # do nothing if file is empty
                pass

        except (IOError, OSError, KeyError):  # KeyError is for the metadata dictionary
            print("LIST/FILE ERROR. Questions cannot be loaded from file.")
            quit()

    """
    """
    def update_file(self):
        try:
            temp_json_list = []
            for question in self.questions_list:
                temp_json_list.append(question.get_dictionary_version())

            file_path = self.QUIZ_PARENT_DIR + "/" + self.list_metadata["filename"]
            list_file = open(file_path, "w")
            list_file.write(json.dumps(temp_json_list, indent=4))
            list_file.close()
        except IOError:
            print("LIST/FILE ERROR. Questions cannot be saved into file. ")
            quit()

    """
        def edit_question(self, index, new_dict)
        Args:   index -- contains the index of question as it appears on the question_list
                new_dict -- a dictionary that contains the updated information
                            NOTE: Not just new, all unchanged information is also duplicated.    
    """
    def edit_question(self, index, new_dict):
        try:
            self.questions_list[index].edit(new_dict)
        except IndexError:
            print("LIST/QUESTION ERROR. Invalid index given.")

    """
        def update_list_metadata(self, new_metadata)
    """
    def update_list_metadata(self, new_metadata):
        self.list_metadata = new_metadata.copy()

    """
        def add_new_question(self, new_dict)
        This method functions similar with the edit_question method
            just without the index argument.
    """
    def add_new_question(self, new_dict):
        self.questions_list.append(Question(new_dict))

    """
    """
    def get_num_questions(self):
        return len(self.questions_list)

    def delete_question_by_idx(self, idx):
        try:
            del self.questions_list[idx]
            self.update_file()
        except IndexError:
            pass
