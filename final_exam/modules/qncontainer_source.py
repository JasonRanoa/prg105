"""
    class Question
    This class is a container class for the question file.

    This class should only be directly used by the ListHandler class.
    Each Question object has the following members:
        question        : the question as it's displayed on the player screen
        options         : an array of strings listing the options for this question
        answer_idx      : the index of the correct answer among the choices.
                          If answer_idx is not in the options' indices, this question
                            considered invalid.
        feedback_txt    : Text shown after player attempts an answer [optional]
        hidden          : If true, this question is NOT shown to the player
                          Useful for questions that aren't ready for play yet.

"""


class Question:
    question = ""
    options = []
    answer_idx = None
    feedback_txt = ""
    hidden = True

    """
        def __init__(self, entry_dict)
        Arguments:  entry_dict -- contains initial values for the question.
                                  This is applied using the edit method.
    """
    def __init__(self, entry_dict):
        self.edit(entry_dict)

    """
        def edit(self, new_dict)
        Arguments:  new_dict -- a dictionary loaded directly from the json file
                                that is supposed to come from the ListHandler
        This method also validates the information passed.
        If any of these information fail, then the question is by default HIDDEN.
    """
    def edit(self, new_dict):
        if not isinstance(new_dict, dict):
            print("QUESTION ERROR. Initial argument is not a dictionary.")
            quit()

        # Assume that the question is player-ready then do validations.
        self.hidden = new_dict["hidden"] if "hidden" in new_dict.keys() else True

        # Question
        if "question" in new_dict.keys() and isinstance(new_dict["question"], str):
            self.question = new_dict["question"]
        else:
            self.hidden = True

        # Options and Answer_Index
        if "options" in new_dict.keys() and isinstance(new_dict["options"], list):
            # if options is not an array, then don't add it
            self.options = new_dict["options"].copy()

            # an answer_idx only makes sense if there are options
            # check if index is valid first then add it if it is.
            if "answer_idx" in new_dict.keys():
                try:
                    _ = new_dict["options"][new_dict["answer_idx"]]
                    self.answer_idx = new_dict["answer_idx"]
                except IndexError:  # if index is not valid
                    self.hidden = True
            else:  # if no index is saved.
                self.hidden = True

        else:  # if options is not a list, the question must be hidden
            self.hidden = True

        # Feedback string. This is optional.
        if "feedback_txt" in new_dict.keys() and isinstance("feedback_txt", str):
            self.feedback_txt = new_dict["feedback_txt"]

        # All data is loaded. Method END.

    def get_dictionary_version(self):
        return {
            "question": self.question,
            "options": self.options.copy(),
            "answer_idx": self.answer_idx,
            "feedback_txt": self.feedback_txt,
            "hidden": bool(self.hidden)
        }

    def get_correct_answer(self):
        try:
            return self.options[self.answer_idx]
        except IndexError:
            return("")
