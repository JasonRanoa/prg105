"""
    class BreadUIHandler
    Contains all code related to creating graphic UI elements.
"""

import tkinter
from .dirhandler_source import DirectoryHandler
from .listhandler_source import ListHandler


class BreadUIHandler:
    # GLOBAL SETTINGS AND HANDLERS
    DIR_HANDLER = DirectoryHandler()
    LIST_HANDLER = None  # ListHandler object, loaded when a file is chosen.
    DEFAULT_FONT = "Calibri"

    # TOP-LEVEL WINDOWS, all redefined in their respective methods
    select_file_window = None
    add_file_window = None
    main_bread_window = None
    edit_file_metadata_window = None
    delete_file_confirmation_window = None
    add_new_question_window = None
    edit_question_window = None
    delete_question_confirmation_window = None

    # Frames and Items Placeholders
    # Rel. to -- File Selection
    file_list_frame = None
    selected_file_idx = None
    # Rel. to -- BREAD
    bread_frame = None
    selected_question_idx = None

    """
        Initialization method.
        Accepts a tkinter loop as an argument. This allows the main program
        to control when the program runs.
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Trivia Quiz Game: BREAD Interface")
        self.master.withdraw()

        self.display_file_selection_window()

    """
        def display_file_selection_window()
        Displays a window listing all the files available to edit
        This list comes from the DIR_HANDLER
    """
    def display_file_selection_window(self):
        # WINDOW SETTINGS
        self.select_file_window = tkinter.Toplevel(self.master)
        self.select_file_window.title("Trivia Quiz Game: File Selection")
        self.select_file_window.geometry("+{x}+{y}".format(x=570, y=100))
        self.select_file_window.protocol(
            "WM_DELETE_WINDOW", self.master.destroy
        )

        # PARENT FRAME
        self.file_list_frame = tkinter.Frame(self.select_file_window, padx=15, pady=10)
        self.reset_file_selection_frame()
        self.file_list_frame.pack()

    """
        def reset_file_selection_frame(self)        
        This function fills the main_frame with UI elements needed for 
        the file selection UI.
        This method is made separate since the method will be called again
    """
    def reset_file_selection_frame(self):
        # Reset frame contents, if the frame has been defined before.
        if isinstance(self.file_list_frame, tkinter.Frame):
            for child in self.file_list_frame.winfo_children():
                child.destroy()
        else:  # initialize if frame hasn't been used before
            self.file_list_frame = tkinter.Frame()

        # HEADER
        header_frame = tkinter.Frame(self.file_list_frame)
        tkinter.Label(
            header_frame, text="TRIVIA QUIZ GAME: BREAD Interface",
            font=(self.DEFAULT_FONT, 18, "bold"), anchor="w", width=30
        ).pack(fill="x")

        if self.DIR_HANDLER.get_list_length() == 0:
            # If no valid files are found.
            tkinter.Label(
                header_frame,
                font=(self.DEFAULT_FONT, 14, "bold"), anchor="nw", justify="left",
                text="There are no quiz files found. "
                     "To start, please create a new file.",
                foreground="Slate Gray"
            ).pack(fill="x")
        else:
            tkinter.Label(
                header_frame,
                font=(self.DEFAULT_FONT, 14, "bold"), anchor="nw", justify="left",
                text="To start, choose a file to work with. "
                     "Click on the file index to open the file."
            ).pack(fill="x")

        header_frame.grid(row=0, column=0, sticky="w")

        # ITEMS. If no items, this gets ignored.
        # Initialize variables
        items_frame = tkinter.Frame(self.file_list_frame, pady=5)
        self.selected_file_idx = tkinter.IntVar()
        self.selected_file_idx.set(-1)  # No default (selected) value for radio list

        # Drawing UI elements
        for idx, file in enumerate(self.DIR_HANDLER.file_metadata_list):
            # Radio buttons
            tkinter.Radiobutton(
                items_frame, text=str(idx + 1), value=idx, variable=self.selected_file_idx,
                font=(self.DEFAULT_FONT, 10, "bold"), borderwidth=1, padx=7,
                foreground="SpringGreen4", highlightbackground="SpringGreen4",
                indicatoron=0,
                command=lambda: (
                    self.select_file_window.withdraw(),
                    self.display_main_bread_window()
                )
            ).grid(row=(idx * 3), rowspan=3, column=1, sticky="new", padx=10, pady=5)

            # Entry Information
            tkinter.Label(
                items_frame,
                text=file["category_name"] if file["category_name"] else "-",
                font=(self.DEFAULT_FONT, 16, "bold"), width=40, anchor="w"
            ).grid(row=(idx * 3), column=2, sticky="w")
            tkinter.Label(
                items_frame,
                text=(
                    "This category is hidden from players." if file["hidden"]
                    else "This category is marked ready-to-play."
                ),
                font=(self.DEFAULT_FONT, 12, "bold"),
                foreground="FireBrick4" if file["hidden"] else "Dark Green",
                anchor="nw"
            ).grid(row=(idx * 3 + 1), column=2, sticky="w")
            tkinter.Label(
                items_frame,
                text=file["description"] if file["description"] else "No description added.",
                font=(self.DEFAULT_FONT, 12),
                foreground="gray20" if file["description"] else "gray25",
                anchor="nw", wraplength=455, justify="left"
            ).grid(row=(idx * 3 + 2), column=2, sticky="w")

        items_frame.grid(row=1, column=0, sticky="w")

        # Add button
        add_btn_frame = tkinter.Frame(self.file_list_frame, pady=3)
        tkinter.Button(
            add_btn_frame, text="ADD NEW CATEGORY",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 12, "bold"),
            foreground="SpringGreen4",
            command=lambda: (
                self.select_file_window.withdraw(),
                self.display_add_file_window()
            )
        ).pack(side="left")
        add_btn_frame.grid(row=2, column=0, sticky="w")

    """
        def display_add_file_window
        This displays a form for adding new files.
        If file cannot be created, the program will simply quit.
            -- I don't know how to pass exceptions from another file. Throwing it didn't work. :(
        
        Exiting this window (by the exit button or the cancel button) withdraws the add_file_window
        and calls the select_file_window back.
    """
    def display_add_file_window(self):
        # WINDOW SETTINGS
        self.add_file_window = tkinter.Toplevel(self.master)
        self.add_file_window.title("Trivia Quiz Game: Add New File")
        self.add_file_window.geometry("+{x}+{y}".format(x=550, y=75))
        self.add_file_window.protocol(
            "WM_DELETE_WINDOW", lambda: (
                self.add_file_window.withdraw(),
                self.select_file_window.deiconify()
            )
        )

        # PARENT FRAME
        main_frame = tkinter.Frame(self.add_file_window, padx=15, pady=10)

        # Title
        header_frame = tkinter.Frame(main_frame)
        tkinter.Label(
            header_frame, text="TRIVIA QUIZ GAME: Add New Category",
            font=(self.DEFAULT_FONT, 16, "bold"), anchor="w", width=30
        ).pack(fill="x")
        tkinter.Label(
            header_frame,
            text="This will create a new file on this folder: {}".format(self.DIR_HANDLER.QUIZ_PARENT_DIR),
            font=(self.DEFAULT_FONT, 12, "bold"), anchor="nw", width=30,
            foreground="gray25"
        ).pack(fill="x")
        header_frame.grid(row=0, sticky="w")

        # Form Frame
        form_frame = tkinter.Frame(main_frame, pady=10)

        # Form Titles
        titles = [
            (
                "Filename:",
                "The new file will be saved under this filename. "
                "The filename is also hidden from the players. "
                "THIS ENTRY DOES NOT INCLUDE THE FILE EXTENSION. PLEASE INCLUDE .json AT THE END"
            ),
            (
                "Category Name:",
                "A short descriptive title for the question list. "
                "This is the title shown to the players"
            ),
            (
                "Description:",
                "Write a description for the quiz list."
            ),
            (
                "Hidden?",
                "If the file is hidden, it will not be shown to the player. "
                "This is good when the file is still being edited."
            )
        ]
        for idx, title_set in enumerate(titles):
            tkinter.Label(
                form_frame, text=title_set[0],
                font=(self.DEFAULT_FONT, 14, "bold"),
                foreground="gray15",
                pady=(7 if idx != 3 else 0)  # for the last checkbox
            ).grid(row=(idx * 2), column=0, rowspan=2, sticky="ne", padx=3)
            tkinter.Label(
                form_frame, text=title_set[1],
                font=(self.DEFAULT_FONT, 11), justify="left",
                wraplength=380,
                pady=5,
                foreground="gray25"
            ).grid(row=(idx * 2 + 1), column=1, sticky="w")

        # Form Entries
        new_entry = {
            "filename": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                padx=10, pady=10, width=40, height=1,
                highlightthickness=1, highlightbackground="gray64",
            ),
            "category_name": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                padx=10, pady=10, width=40, height=1,
                highlightthickness=1, highlightbackground="gray64"
            ),
            "description": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                wrap="word", padx=10, pady=10, width=40, height=4,
                highlightthickness=1, highlightbackground="gray64"
            ),
            "hidden": tkinter.IntVar()
            # qn_num is, by default, 0
        }
        new_entry["filename"].grid(row=0, column=1, sticky="w", padx=5)
        new_entry["category_name"].grid(row=2, column=1, sticky="w", padx=5)
        new_entry["description"].grid(row=4, column=1, sticky="w", padx=5)
        tkinter.Checkbutton(
            form_frame, variable=new_entry["hidden"],
            text="Is the file hidden to the players?",
            font=(self.DEFAULT_FONT, 14),
            padx=10, onvalue=True, offvalue=False
        ).grid(row=6, column=1, sticky="w", padx=3)
        new_entry["hidden"].set(True)

        form_frame.grid(row=1)

        # Buttons Frame
        buttons_frame = tkinter.Frame(main_frame, padx=5)
        tkinter.Button(
            buttons_frame, text="CANCEL",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 13, "bold"),
            foreground="goldenrod4", relief="flat",
            command=lambda: (
                self.add_file_window.withdraw(),
                self.select_file_window.deiconify()
            )
        ).pack(side="left")
        tkinter.Button(
            buttons_frame, text="CREATE NEW FILE",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 13, "bold"),
            foreground="springgreen4",
            command=lambda: (
                self.DIR_HANDLER.append_new_entry(
                    new_entry["filename"].get("1.0", "end").strip(),
                    new_entry["category_name"].get("1.0", "end").strip(),
                    new_entry["description"].get("1.0", "end").strip(),
                    bool(new_entry["hidden"].get()),
                    0
                ),
                self.display_modal(
                    self.add_file_window,
                    "NEW CATEGORY ADDED",
                    "The entry has been added to the metadata file. "
                    "A new file, {}, has been created".format(new_entry["filename"].get("1.0", "end").strip()),
                    self.select_file_window
                ),
                self.reset_file_selection_frame(),
            )
        ).pack(side="left")
        buttons_frame.grid(row=2, sticky="e")

        # END PARENT FRAME
        main_frame.pack()

    """
        def display_main_bread_window
        This loads and displays the questions and metadata about the category.
        -- uses the reset_bread_frame method to populate UI elements
    """
    def display_main_bread_window(self):
        # WINDOW SETTINGS
        self.main_bread_window = tkinter.Toplevel(self.master)
        self.main_bread_window.title("Trivia Quiz Game: Quiz List BREAD")
        self.main_bread_window.geometry("+{x}+{y}".format(x=330, y=150))
        self.main_bread_window.protocol(
            "WM_DELETE_WINDOW", lambda: (
                self.main_bread_window.withdraw(),
                self.select_file_window.deiconify(),
                self.selected_file_idx.set(-1)
            )
        )

        # MAIN CONTAINER
        self.bread_frame = tkinter.Frame(self.main_bread_window, padx=15, pady=7)
        self.reset_bread_frame()
        # MAIN CONTAINER END
        self.bread_frame.pack()

    """
        def reset_bread_frame(self)
        Load a file handler and populate the bread_frame with UI elements
    """
    def reset_bread_frame(self):
        # If selected_file_index is not a valid index
        #   -- This shouldn't be a problem but just in case.
        if not self.DIR_HANDLER.is_valid_index(self.selected_file_idx.get()):
            print("DIR/INDEX ERROR. Saved file index is not valid")
            quit()

        # Load a ListHandler
        self.LIST_HANDLER = ListHandler(
            self.DIR_HANDLER.file_metadata_list[self.selected_file_idx.get()]
        )

        # Reset Frame
        for child in self.bread_frame.winfo_children():
            child.destroy()

        # Header Frame
        header_frame = tkinter.Frame(self.bread_frame, pady=2)
        tkinter.Label(
            header_frame,
            text="Trivia Viewer - BREAD Interface",
            font="Calibri 20 bold", anchor="sw"
        ).grid(row=0, column=0, sticky="w")
        tkinter.Label(
            header_frame,
            text="Browse, Read, Edit, Add, and Delete Trivia Quiz Items",
            font="Calibri 12 bold", foreground="Gray25", anchor="nw"
        ).grid(row=1, column=0, sticky="w")
        header_frame.grid(row=0, column=0, sticky="we", columnspan=2)

        """
            SIDE FRAME THINGS BELOW
        """
        side_frame = tkinter.Frame(self.bread_frame)

        tkinter.Label(
            side_frame, text="DATAFILE INFORMATION: ",
            font=(self.DEFAULT_FONT, 12, "bold"), foreground="gray30",
            anchor="w"
        ).grid(row=0, column=0, columnspan=2, sticky="w")

        # Labels
        labels = [
            "Filename: ", "Category: ", "Description: ",
            "Status: ", "Num. Items: "
        ]
        for idx, label in enumerate(labels):
            tkinter.Label(
                side_frame, text=label,
                font=(self.DEFAULT_FONT, 12),
            ).grid(row=1 + idx, column=0, sticky="nw")
        keys = [
            "filename", "category_name", "description",
            "hidden", "qn_num"
        ]
        dir_data = self.DIR_HANDLER.file_metadata_list[self.selected_file_idx.get()].copy()
        for idx, key in enumerate(keys):
            tkinter.Label(
                side_frame, text=dir_data[key], wraplength=200,
                font=(self.DEFAULT_FONT, 12, "bold"), justify="left"
            ).grid(row=1 + idx, column=1, sticky="nw")
        # Override "hidden" label
        tkinter.Label(
            side_frame,
            text="HIDDEN FROM PLAYERS" if dir_data["hidden"] else "READY-FOR-PLAY",
            foreground="FireBrick4" if dir_data["hidden"] else "SpringGreen4",
            wraplength=200, font=(self.DEFAULT_FONT, 12, "bold"), justify="left"
        ).grid(row=4, column=1, sticky="nw")

        # Space
        tkinter.Label(side_frame, text=" ", font=(self.DEFAULT_FONT, 4)).grid(row=6)

        # Actions
        tkinter.Label(
            side_frame, text="AVAILABLE ACTIONS: ",
            font=(self.DEFAULT_FONT, 12, "bold"), foreground="gray30",
            anchor="w"
        ).grid(row=7, column=0, columnspan=2, sticky="w")

        actions = [
            (
                "Edit File Metadata",
                lambda: (self.display_edit_file_metadata_window(), self.main_bread_window.withdraw()),
                "goldenrod4"
            ),
            (
                "Delete File",
                lambda: (self.display_delete_file_confirmation_window(), self.main_bread_window.withdraw()),
                "firebrick4"
            ),
            (
                "Add New Question",
                lambda: (self.display_add_new_question_window(), self.main_bread_window.withdraw()),
                "springgreen4"
            )
        ]
        for idx, action in enumerate(actions):
            frame = tkinter.Frame(side_frame, pady=1, padx=4)
            tkinter.Button(
                frame, text=action[0],
                font=(self.DEFAULT_FONT, 12, "bold"), padx=15, pady=7,
                foreground=action[2], command=action[1]
            ).pack()
            frame.grid(row=8 + idx, column=0, columnspan=2, sticky="w")

        # Last Note
        label_frame = tkinter.Frame(side_frame)
        tkinter.Label(
            label_frame,
            text="\nNote: ",
            font=(self.DEFAULT_FONT, 12), foreground="gray30",
            anchor="w"
        ).grid(row=0, column=0, sticky="nw")
        tkinter.Label(
            label_frame,
            text="\nTo access more controls for a specific item, click on the item's number",
            font=(self.DEFAULT_FONT, 12), foreground="gray30",
            anchor="w", wraplength=250, justify="left"
        ).grid(row=0, column=1, sticky="nw")
        label_frame.grid(row=11, column=0, columnspan=2, sticky="w")

        # END SIDE FRAME
        side_frame.grid(row=1, column=0, sticky="new")

        """
            CANVAS THINGS BELOW
        """
        canvas_scr_width = 800  # TOTAL Frame Width, including padding
        canvas_scr_padx = 10
        canvas_frame = tkinter.Frame(self.bread_frame, borderwidth=1, background="Gray76")
        canvas_frame.grid(row=1, column=1, sticky="nw", padx=10, pady=7)

        # Reference for Scrolling Canvas:
        # https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
        # https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter

        list_canvas = tkinter.Canvas(canvas_frame)
        frame_in_canvas = tkinter.Frame(list_canvas, padx=3, pady=3)
        scrollbar = tkinter.Scrollbar(
            canvas_frame, orient="vertical", command=list_canvas.yview
        )
        list_canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        list_canvas.pack(side="left")
        list_canvas.create_window((0, 0), window=frame_in_canvas, anchor="nw")
        frame_in_canvas.bind(
            "<Configure>",
            lambda event: list_canvas.configure(
                scrollregion=list_canvas.bbox("all"),
                width=canvas_scr_width - 2 * canvas_scr_padx - 15,
                height=500
            )
        )

        """
            QUESTION THINGS BELOW
        """
        self.selected_question_idx = tkinter.IntVar()
        self.selected_question_idx.set(-1)
        # If there are no questions, add a label that says NO QUESTIONS FOUND.
        if self.LIST_HANDLER.get_num_questions() == 0:
            tkinter.Label(
                frame_in_canvas, text="THERE ARE NO QUESTIONS FOUND.",
                font=(self.DEFAULT_FONT, 16, "bold"), foreground="gray64"
            ).grid(row=0, column=0)
            frame_in_canvas.config(padx=8, pady=8)
        for idx, question in enumerate(self.LIST_HANDLER.questions_list):
            tkinter.Label(
                frame_in_canvas, text="QUESTION NO. {}".format(idx + 1),
                font=(self.DEFAULT_FONT, 9, "bold")
            ).grid(row=idx * 5, column=0, sticky="ne", padx=3, pady=1)
            for label_idx, label in enumerate(["Correct Answer:", "Status:", "Actions:"]):
                tkinter.Label(
                    frame_in_canvas, text=label.upper(),
                    font=(self.DEFAULT_FONT, 9, "bold")
                ).grid(row=idx * 5 + label_idx + 1, column=0, sticky="ne", padx=3, pady=1)

            tkinter.Label(
                frame_in_canvas,
                text=question.question if question.question else "Question is blank.",
                foreground="black" if question.question else "Gray64",
                font=(self.DEFAULT_FONT, 12, "bold"), justify="left",
                wraplength=canvas_scr_width - 2 * canvas_scr_padx - 150
            ).grid(row=idx * 5, column=1, sticky="nw")

            tkinter.Label(
                frame_in_canvas,
                text=(
                    question.get_correct_answer()
                    if question.get_correct_answer() else "No correct answer identified."
                ),
                foreground="black" if question.get_correct_answer() else "Gray64",
                font=(self.DEFAULT_FONT, 12, "bold"), justify="left",
                wraplength=canvas_scr_width - 2 * canvas_scr_padx - 200
            ).grid(row=idx * 5 + 1, column=1, sticky="nw")

            tkinter.Label(
                frame_in_canvas,
                text="HIDDEN FROM PLAYERS" if question.hidden else "READY-FOR-PLAY",
                foreground="firebrick4" if question.hidden else "springgreen4",
                font=(self.DEFAULT_FONT, 10, "bold"), justify="left",
                wraplength=canvas_scr_width - 2 * canvas_scr_padx - 200
            ).grid(row=idx * 5 + 2, column=1, sticky="nw")

            # ACTION BUTTONS
            item_buttons_frame = tkinter.Frame(frame_in_canvas, pady=1)
            tkinter.Radiobutton(
                item_buttons_frame, text="EDIT",
                value=idx, variable=self.selected_question_idx,
                font=(self.DEFAULT_FONT, 10, "bold"), borderwidth=1, padx=9,
                foreground="goldenrod4", highlightbackground="goldenrod4",
                indicatoron=0,
                command=lambda: (
                    self.main_bread_window.withdraw(),
                    self.display_edit_question_window()
                )
            ).grid(row=0, column=0, sticky="nw", padx=2)
            tkinter.Radiobutton(
                item_buttons_frame, text="DELETE",
                value=idx, variable=self.selected_question_idx,
                font=(self.DEFAULT_FONT, 10, "bold"), borderwidth=1, padx=9,
                foreground="firebrick4", highlightbackground="firebrick4",
                indicatoron=0,
                command=lambda: (
                    self.main_bread_window.withdraw(),
                    self.display_delete_question_confirmation_window()
                )
            ).grid(row=0, column=1, sticky="nw", padx=2)

            item_buttons_frame.grid(row=idx * 5 + 3, column=1, sticky="nw")

            # SPACING
            tkinter.Label(
                frame_in_canvas,
                text="-" * 40,
                foreground="gray64", font=(self.DEFAULT_FONT, 5),
                justify="left"
            ).grid(row=idx * 5 + 4, column=1, sticky="nw")

    """
        def display_modal(self, from_window, text, to_window)
        THIS IS THE ONLY METHOD THAT CREATES A TOPLEVEL AND DESTROYS IT AFTERWARDS
        Everything else, another method is called to withdraw its own window.
    """
    def display_modal(self, from_window, title, message, to_window):
        # Hide from window
        from_window.withdraw()

        window = tkinter.Toplevel(self.master)
        window.title("Trivia Quiz Game: Message")
        window.geometry("+{x}+{y}".format(x=620, y=200))
        window.protocol(
            "WM_DELETE_WINDOW", lambda: (
                window.withdraw(),
                to_window.deiconify()
            )
        )

        wrap_ln = 400
        main_frame = tkinter.Frame(window, padx=20, pady=7)
        tkinter.Label(
            main_frame, text=title,
            font=(self.DEFAULT_FONT, 18, "bold"),
            wraplength=wrap_ln, anchor="s"
        ).grid(row=0)
        tkinter.Label(
            main_frame, text=message,
            font=(self.DEFAULT_FONT, 13),
            wraplength=wrap_ln, pady=3,
        ).grid(row=1)
        tkinter.Button(
            main_frame, text="OKAY",
            font=(self.DEFAULT_FONT, 10, "bold"), padx=20, pady=7,
            foreground="gray46",
            command=lambda: (
                window.withdraw(),
                to_window.deiconify()
            )
        ).grid(row=2, pady=3)
        main_frame.pack()

    """
        def display_edit_file_metadata_window(self)
        Lets the user edit one file's metadata information.
        All the renaming and metadata updating is done by the DIR_HANDLER
    """
    def display_edit_file_metadata_window(self):
        # WINDOW SETTINGS
        self.edit_file_metadata_window = tkinter.Toplevel(self.master)
        self.edit_file_metadata_window.title("Trivia Quiz Game: Edit File Metadata")
        self.edit_file_metadata_window.geometry("+{x}+{y}".format(x=550, y=75))
        self.edit_file_metadata_window.protocol(
            "WM_DELETE_WINDOW", lambda: (
                self.edit_file_metadata_window.withdraw(),
                self.main_bread_window.deiconify()
            )
        )

        # PARENT FRAME
        main_frame = tkinter.Frame(self.edit_file_metadata_window, padx=15, pady=10)

        # ENTRY_DATA
        current_entry = self.DIR_HANDLER.file_metadata_list[self.selected_file_idx.get()]

        # Title
        header_frame = tkinter.Frame(main_frame)
        tkinter.Label(
            header_frame, text="TRIVIA QUIZ GAME: Edit Category -- {}".format(current_entry["category_name"]),
            font=(self.DEFAULT_FONT, 16, "bold"), anchor="w"
        ).pack(fill="x")
        tkinter.Label(
            header_frame,
            text="The file's current filename is: ".format(current_entry["filename"]),
            font=(self.DEFAULT_FONT, 12, "bold"), anchor="nw",
            foreground="gray25"
        ).pack(fill="x")
        header_frame.grid(row=0, sticky="w")

        # Form Frame
        form_frame = tkinter.Frame(main_frame, pady=10)

        # Form Titles
        titles = [
            (
                "Filename:",
                "The new file will be saved under this filename. "
                "The filename is also hidden from the players. "
                "THIS ENTRY DOES NOT INCLUDE THE FILE EXTENSION. PLEASE INCLUDE .json AT THE END"
            ),
            (
                "Category Name:",
                "A short descriptive title for the question list. "
                "This is the title shown to the players"
            ),
            (
                "Description:",
                "Write a description for the quiz list."
            ),
            (
                "Hidden?",
                "If the file is hidden, it will not be shown to the player. "
                "This is good when the file is still being edited."
            )
        ]
        for idx, title_set in enumerate(titles):
            tkinter.Label(
                form_frame, text=title_set[0],
                font=(self.DEFAULT_FONT, 14, "bold"),
                foreground="gray15",
                pady=(7 if idx != 3 else 0)  # for the last checkbox
            ).grid(row=(idx * 2), column=0, rowspan=2, sticky="ne", padx=3)
            tkinter.Label(
                form_frame, text=title_set[1],
                font=(self.DEFAULT_FONT, 11), justify="left",
                wraplength=380,
                pady=5,
                foreground="gray25"
            ).grid(row=(idx * 2 + 1), column=1, sticky="w")

        # Form Entries
        new_entry = {
            "filename": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                padx=10, pady=10, width=40, height=1,
                highlightthickness=1, highlightbackground="gray64",
            ),
            "category_name": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                padx=10, pady=10, width=40, height=1,
                highlightthickness=1, highlightbackground="gray64"
            ),
            "description": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                wrap="word", padx=10, pady=10, width=40, height=4,
                highlightthickness=1, highlightbackground="gray64"
            ),
            "hidden": tkinter.IntVar()
            # qn_num is, by default, 0
        }
        new_entry["filename"].grid(row=0, column=1, sticky="w", padx=5)
        new_entry["category_name"].grid(row=2, column=1, sticky="w", padx=5)
        new_entry["description"].grid(row=4, column=1, sticky="w", padx=5)
        tkinter.Checkbutton(
            form_frame, variable=new_entry["hidden"],
            text="Is the file hidden to the players?",
            font=(self.DEFAULT_FONT, 14),
            padx=10, onvalue=True, offvalue=False
        ).grid(row=6, column=1, sticky="w", padx=3)
        new_entry["hidden"].set(True)

        # ADD CURRENT INFORMATION
        entry_metadata = self.DIR_HANDLER.file_metadata_list[self.selected_file_idx.get()]
        new_entry["filename"].insert("end", entry_metadata["filename"])
        new_entry["category_name"].insert("end", entry_metadata["category_name"])
        new_entry["description"].insert("end", entry_metadata["description"])
        new_entry["hidden"].set(entry_metadata["hidden"])

        form_frame.grid(row=1)

        # Buttons Frame
        buttons_frame = tkinter.Frame(main_frame, padx=5)
        tkinter.Button(
            buttons_frame, text="CANCEL",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 13, "bold"),
            foreground="goldenrod4", relief="flat",
            command=lambda: (
                self.edit_file_metadata_window.withdraw(),
                self.main_bread_window.deiconify()
            )
        ).pack(side="left")

        tkinter.Button(
            buttons_frame, text="SUBMIT CHANGES",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 13, "bold"),
            foreground="springgreen4",
            command=lambda: (
                self.DIR_HANDLER.edit_entry_by_idx(
                    self.selected_file_idx.get(),
                    new_entry["filename"].get("1.0", "end").strip(),
                    new_entry["category_name"].get("1.0", "end").strip(),
                    new_entry["description"].get("1.0", "end").strip(),
                    bool(new_entry["hidden"].get()),
                    len(self.LIST_HANDLER.questions_list)
                ),
                self.reset_bread_frame(),
                self.reset_file_selection_frame(),
                self.display_modal(
                    self.edit_file_metadata_window,
                    "CHANGES SUBMITTED",
                    "The metadata to this category: {} has been updated"
                        .format(new_entry["filename"].get("1.0", "end").strip()),
                    self.main_bread_window
                )
            )
        ).pack(side="left")
        buttons_frame.grid(row=2, sticky="e")

        # END PARENT FRAME
        main_frame.pack()

    """
        def display_delete_file_confirmation_window(self)
        Asks if the user wants to delete the file and confirms since 
        this operation cannot be undone. All information would be lost.
    """
    def display_delete_file_confirmation_window(self):
        # WINDOW SETTINGS
        self.delete_file_confirmation_window = tkinter.Toplevel(self.master)
        self.delete_file_confirmation_window.title("Trivia Quiz Game: Confirm Delete Operation")
        self.delete_file_confirmation_window.geometry("+{x}+{y}".format(x=650, y=300))
        self.delete_file_confirmation_window.protocol(
            "WM_DELETE_WINDOW", lambda: (
                self.delete_file_confirmation_window.withdraw(),
                self.main_bread_window.deiconify()
            )
        )

        wrap_ln = 600
        main_frame = tkinter.Frame(self.delete_file_confirmation_window, padx=20, pady=20)
        tkinter.Label(
            main_frame, text="ARE YOU SURE YOU WANT TO DELETE...",
            font=(self.DEFAULT_FONT, 14, "bold"), foreground="firebrick4",
            wraplength=wrap_ln
        ).grid(row=0)
        tkinter.Label(
            main_frame,
            text="The " + self.DIR_HANDLER.file_metadata_list[self.selected_file_idx.get()]["category_name"]
                 + " Category?",
            font=(self.DEFAULT_FONT, 20, "bold"),
            wraplength=wrap_ln
        ).grid(row=1)
        tkinter.Label(
            main_frame, text="WARNING! THIS ACTION CANNOT BE UNDONE!",
            font=(self.DEFAULT_FONT, 11, "bold"), anchor="s",
            wraplength=wrap_ln, pady=3, foreground="firebrick4",
        ).grid(row=2)
        tkinter.Label(
            main_frame, text="ALL CATEGORY METADATA AND QUESTION DATA WILL BE GONE.",
            font=(self.DEFAULT_FONT, 11, "bold"), anchor="n",
            wraplength=wrap_ln, pady=3, foreground="firebrick4",
        ).grid(row=3)

        buttons_frame = tkinter.Frame(main_frame, pady=3)
        # Cancel Button
        tkinter.Button(
            buttons_frame, text="CANCEL",
            font=(self.DEFAULT_FONT, 10, "bold"), padx=20, pady=7,
            foreground="gray46",
            command=lambda: (
                self.delete_file_confirmation_window.withdraw(),
                self.main_bread_window.deiconify()
            )
        ).grid(row=0, column=0, padx=1)
        # DELETE BUTTON

        temp_category_name = self.DIR_HANDLER.file_metadata_list[self.selected_file_idx.get()]["category_name"]
        tkinter.Button(
            buttons_frame, text="DELETE FILE",
            font=(self.DEFAULT_FONT, 12, "bold"), padx=20, pady=7,
            foreground="firebrick4",
            command=lambda: (
                self.DIR_HANDLER.delete_entry_by_idx(self.selected_file_idx.get()),
                self.reset_file_selection_frame(),
                self.display_modal(
                    self.delete_file_confirmation_window,
                    "FILE DELETED",
                    "All question data for the {} category has been deleted and is now lost."
                        .format(temp_category_name),
                    self.select_file_window
                )
            )
        ).grid(row=0, column=1, padx=1)
        buttons_frame.grid(row=4)

        main_frame.pack()

    def display_add_new_question_window(self):
        # WINDOW SETTINGS
        self.add_new_question_window = tkinter.Toplevel(self.master)
        self.add_new_question_window.title("Trivia Quiz Game: Add New Question")
        self.add_new_question_window.geometry("+{x}+{y}".format(x=550, y=75))
        self.add_new_question_window.protocol(
            "WM_DELETE_WINDOW", lambda: (
                self.add_new_question_window.withdraw(),
                self.main_bread_window.deiconify()
            )
        )

        # PARENT FRAME
        main_frame = tkinter.Frame(self.add_new_question_window, padx=15, pady=10)

        # Title
        header_frame = tkinter.Frame(main_frame)
        tkinter.Label(
            header_frame, text="TRIVIA QUIZ GAME: Add New Question",
            font=(self.DEFAULT_FONT, 16, "bold"), anchor="w", width=30
        ).pack(fill="x")
        tkinter.Label(
            header_frame,
            text="This question will be added to this category: {}".
            format(self.LIST_HANDLER.list_metadata["category_name"]),
            font=(self.DEFAULT_FONT, 12, "bold"), anchor="nw",
            foreground="gray25"
        ).pack(fill="x")
        header_frame.grid(row=0, sticky="w")

        """
            FORM THINGS BELOW
        """
        form_frame = tkinter.Frame(main_frame)

        titles = [
            (
                "Question:",
                "This question is displayed in the game. "
            ),
            (
                "Choices:",
                "Four choices is required. "
            ),
            (
                "Correct Answer:",
                "Select the letter of the correct choice (on the left of the choice). "
            ),
            (
                "Feedback Text:",
                "This text appears once the question is answered (regardless of correctness). "
            ),
            (
                "Hidden?",
                "If the question is hidden, it will not be shown to the player. "
                "This is good when the question is still being edited."
            )
        ]
        for idx, title_set in enumerate(titles):
            tkinter.Label(
                form_frame, text=title_set[0],
                font=(self.DEFAULT_FONT, 14, "bold"),
                foreground="gray15",
                pady=(7 if idx != 4 else 0)  # for the last checkbox
            ).grid(row=(idx * 2), column=0, rowspan=2, sticky="ne", padx=3)
            tkinter.Label(
                form_frame, text=title_set[1],
                font=(self.DEFAULT_FONT, 11), justify="left",
                wraplength=380,
                pady=5,
                foreground="gray25"
            ).grid(row=(idx * 2 + 1), column=1, sticky="w")

        # Form Entries
        new_entry = {
            "question": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                wrap="word", padx=10, pady=10, width=50, height=2,
                highlightthickness=1, highlightbackground="gray64",
            ),
            "choices": tkinter.Frame(form_frame),  # placeholder frame
            "correct_answer": tkinter.Frame(form_frame),  # placeholder frame
            "feedback_text": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                wrap="word", padx=10, pady=10, width=50, height=2,
                highlightthickness=1, highlightbackground="gray64"
            ),
            "hidden": tkinter.IntVar()
            # qn_num is, by default, 0
        }
        new_entry["question"].grid(row=0, column=1, sticky="w", padx=5)
        new_entry["choices"].grid(row=2, column=1, sticky="w", padx=5)
        new_entry["correct_answer"].grid(row=4, column=1, sticky="w", padx=5)
        new_entry["feedback_text"].grid(row=6, column=1, sticky="w", padx=5)
        tkinter.Checkbutton(
            form_frame, variable=new_entry["hidden"],
            text="Is this question hidden to the players?",
            font=(self.DEFAULT_FONT, 14),
            padx=10, onvalue=True, offvalue=False
        ).grid(row=8, column=1, sticky="w", padx=3)
        new_entry["hidden"].set(True)

        """
            CHOICE ELEMENTS BELOW
        """
        choices_frame = tkinter.Frame(new_entry["choices"])

        temp_choices_textvar = []

        # CORRECT CHOICE INITIALIZATION
        num_choices = 4
        correct_choice_idx = tkinter.IntVar()
        correct_choice_idx.set(0)  # first option is correct by default
        correct_choice_textvar = tkinter.Text(
            new_entry["correct_answer"], font=(self.DEFAULT_FONT, 13, "bold"),
            wrap="word", padx=10, pady=10, width=44, height=1,
            highlightthickness=1, highlightbackground="gray64",
            background="gray89", foreground="dark olive green"
        )
        correct_choice_textvar.insert(
            "end", "Option {}".format(chr(correct_choice_idx.get() + ord('A')))
        )
        correct_choice_textvar.config(state="disabled")

        # SETTING UP CHOICE TEXT INPUTS
        for i in range(num_choices):
            tkinter.Radiobutton(
                choices_frame, text=chr(i + ord('A')), value=i, variable=correct_choice_idx,
                font=(self.DEFAULT_FONT, 10, "bold"), borderwidth=1, padx=7, pady=2,
                foreground="Gray45", highlightbackground="Gray45",
                indicatoron=0,
                command=lambda: (
                    correct_choice_textvar.config(state="normal"),
                    correct_choice_textvar.delete("1.0", "end"),
                    correct_choice_textvar.insert(
                        "end",
                        "Option {}".format(
                            chr(correct_choice_idx.get() + ord('A'))
                        )
                    ),
                    correct_choice_textvar.config(state="disabled")
                )
            ).grid(row=i, column=0, sticky="ew", padx=5)

            temp_choices_textvar.append(tkinter.Text(
                choices_frame, font=(self.DEFAULT_FONT, 14),
                wrap="word", padx=10, pady=10, width=44, height=1,
                highlightthickness=1, highlightbackground="gray64"
            ))
            temp_choices_textvar[i].grid(row=i, column=1, pady=2)

        choices_frame.grid(sticky="ew")

        correct_choice_textvar.grid()
        form_frame.grid(row=1)

        # Buttons Frame
        temp_file_selected_idx = self.selected_file_idx.get()
        buttons_frame = tkinter.Frame(main_frame, padx=5)
        tkinter.Button(
            buttons_frame, text="CANCEL",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 13, "bold"),
            foreground="goldenrod4", relief="flat",
            command=lambda: (
                self.add_new_question_window.withdraw(),
                self.main_bread_window.deiconify()
            )
        ).pack(side="left")
        tkinter.Button(
            buttons_frame, text="ADD NEW QUESTION",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 13, "bold"),
            foreground="springgreen4",
            command=lambda: (
                self.LIST_HANDLER.add_new_question({
                    "question": new_entry["question"].get("1.0", "end").strip(),
                    "options": [
                        temp_choices_textvar[j].get("1.0", "end").strip() for j in range(num_choices)
                    ],
                    "answer_idx": correct_choice_idx.get(),
                    "feedback_txt": new_entry["feedback_text"].get("1.0", "end").strip(),
                    "hidden": new_entry["hidden"]
                }),
                self.DIR_HANDLER.update_file_question_count(
                    self.selected_file_idx.get(), self.LIST_HANDLER.get_num_questions()
                ),
                self.LIST_HANDLER.update_file(),
                self.reset_bread_frame(),
                self.reset_file_selection_frame(),
                self.selected_file_idx.set(temp_file_selected_idx),
                self.display_modal(
                    self.add_new_question_window,
                    "NEW QUESTION ADDED",
                    "This question has been added to this category: {}."
                        .format(self.LIST_HANDLER.list_metadata["filename"]),
                    self.main_bread_window
                )
            )
        ).pack(side="left")
        buttons_frame.grid(row=2, sticky="e")

        # PARENT FRAME -- END
        main_frame.pack()

    def display_edit_question_window(self):
        # WINDOW SETTINGS
        self.edit_question_window = tkinter.Toplevel(self.master)
        self.edit_question_window.title("Trivia Quiz Game: Edit Question")
        self.edit_question_window.geometry("+{x}+{y}".format(x=550, y=75))
        self.edit_question_window.protocol(
            "WM_DELETE_WINDOW", lambda: (
                self.edit_question_window.withdraw(),
                self.main_bread_window.deiconify(),
                self.selected_question_idx.set(-1)
            )
        )

        # PARENT FRAME
        main_frame = tkinter.Frame(self.edit_question_window, padx=15, pady=10)

        # Title
        header_frame = tkinter.Frame(main_frame)
        tkinter.Label(
            header_frame, text="TRIVIA QUIZ GAME: Edit New Question",
            font=(self.DEFAULT_FONT, 16, "bold"), anchor="w", width=30
        ).pack(fill="x")
        tkinter.Label(
            header_frame,
            text="Question {} is of the category: {}".format(
                self.selected_question_idx.get() + 1,
                self.LIST_HANDLER.list_metadata["category_name"]
            ),
            font=(self.DEFAULT_FONT, 12, "bold"), anchor="nw",
            foreground="gray25"
        ).pack(fill="x")
        header_frame.grid(row=0, sticky="w")

        """
            FORM THINGS BELOW
        """
        form_frame = tkinter.Frame(main_frame)

        titles = [
            (
                "Question:",
                "This question is displayed in the game. "
            ),
            (
                "Choices:",
                "Four choices is required. "
            ),
            (
                "Correct Answer:",
                "Select the letter of the correct choice (on the left of the choice). "
            ),
            (
                "Feedback Text:",
                "This text appears once the question is answered (regardless of correctness). "
            ),
            (
                "Hidden?",
                "If the question is hidden, it will not be shown to the player. "
                "This is good when the question is still being edited."
            )
        ]
        for idx, title_set in enumerate(titles):
            tkinter.Label(
                form_frame, text=title_set[0],
                font=(self.DEFAULT_FONT, 14, "bold"),
                foreground="gray15",
                pady=(7 if idx != 4 else 0)  # for the last checkbox
            ).grid(row=(idx * 2), column=0, rowspan=2, sticky="ne", padx=3)
            tkinter.Label(
                form_frame, text=title_set[1],
                font=(self.DEFAULT_FONT, 11), justify="left",
                wraplength=380,
                pady=5,
                foreground="gray25"
            ).grid(row=(idx * 2 + 1), column=1, sticky="w")

        # Form Entries
        new_entry = {
            "question": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                wrap="word", padx=10, pady=10, width=50, height=2,
                highlightthickness=1, highlightbackground="gray64",
            ),
            "choices": tkinter.Frame(form_frame),  # placeholder frame
            "correct_answer": tkinter.Frame(form_frame),  # placeholder frame
            "feedback_text": tkinter.Text(
                form_frame, font=(self.DEFAULT_FONT, 14),
                wrap="word", padx=10, pady=10, width=50, height=2,
                highlightthickness=1, highlightbackground="gray64"
            ),
            "hidden": tkinter.IntVar()
            # qn_num is, by default, 0
        }
        new_entry["question"].grid(row=0, column=1, sticky="w", padx=5)
        new_entry["choices"].grid(row=2, column=1, sticky="w", padx=5)
        new_entry["correct_answer"].grid(row=4, column=1, sticky="w", padx=5)
        new_entry["feedback_text"].grid(row=6, column=1, sticky="w", padx=5)
        tkinter.Checkbutton(
            form_frame, variable=new_entry["hidden"],
            text="Is this question hidden to the players?",
            font=(self.DEFAULT_FONT, 14),
            padx=10, onvalue=True, offvalue=False
        ).grid(row=8, column=1, sticky="w", padx=3)
        new_entry["hidden"].set(True)

        """
            CHOICE ELEMENTS BELOW
        """
        choices_frame = tkinter.Frame(new_entry["choices"])

        temp_choices_textvar = []

        # CORRECT CHOICE INITIALIZATION
        num_choices = 4
        correct_choice_idx = tkinter.IntVar()
        correct_choice_idx.set(0)  # first option is correct by default
        correct_choice_textvar = tkinter.Text(
            new_entry["correct_answer"], font=(self.DEFAULT_FONT, 13, "bold"),
            wrap="word", padx=10, pady=10, width=44, height=1,
            highlightthickness=1, highlightbackground="gray64",
            background="gray89", foreground="dark olive green"
        )
        correct_choice_textvar.insert(
            "end", "Option {}".format(chr(correct_choice_idx.get() + ord('A')))
        )
        correct_choice_textvar.config(state="disabled")

        # SETTING UP CHOICE TEXT INPUTS
        for i in range(num_choices):
            tkinter.Radiobutton(
                choices_frame, text=chr(i + ord('A')), value=i, variable=correct_choice_idx,
                font=(self.DEFAULT_FONT, 10, "bold"), borderwidth=1, padx=7, pady=2,
                foreground="Gray45", highlightbackground="Gray45",
                indicatoron=0,
                command=lambda: (
                    correct_choice_textvar.config(state="normal"),
                    correct_choice_textvar.delete("1.0", "end"),
                    correct_choice_textvar.insert(
                        "end",
                        "Option {}".format(
                            chr(correct_choice_idx.get() + ord('A'))
                        )
                    ),
                    correct_choice_textvar.config(state="disabled")
                )
            ).grid(row=i, column=0, sticky="ew", padx=5)

            temp_choices_textvar.append(tkinter.Text(
                choices_frame, font=(self.DEFAULT_FONT, 14),
                wrap="word", padx=10, pady=10, width=44, height=1,
                highlightthickness=1, highlightbackground="gray64"
            ))
            temp_choices_textvar[i].grid(row=i, column=1, pady=2)

        choices_frame.grid(sticky="ew")

        correct_choice_textvar.grid()
        form_frame.grid(row=1)

        """
            UPDATING FORM ELEMENTS TO DEFAULT STATE BELOW
        """
        temp_question = self.LIST_HANDLER.questions_list[self.selected_question_idx.get()]
        new_entry["question"].insert("end", temp_question.question)
        new_entry["feedback_text"].insert("end", temp_question.feedback_txt)
        for idx, textvar in enumerate(temp_choices_textvar):
            try:
                textvar.insert("end", temp_question.options[idx])
            except IndexError:
                pass  # just ignore if option doesn't exist.
        correct_choice_idx.set(temp_question.answer_idx)
        correct_choice_textvar.config(state="normal")
        correct_choice_textvar.delete("1.0", "end")
        correct_choice_textvar.insert(
            "end", "Option {}".format(chr(correct_choice_idx.get() + ord('A')))
        )
        correct_choice_textvar.config(state="disabled")
        new_entry["hidden"].set(temp_question.hidden)

        # Buttons Frame
        buttons_frame = tkinter.Frame(main_frame, padx=5)
        tkinter.Button(
            buttons_frame, text="CANCEL",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 13, "bold"),
            foreground="goldenrod4", relief="flat",
            command=lambda: (
                self.edit_question_window.withdraw(),
                self.main_bread_window.deiconify(),
                self.selected_question_idx.set(-1)
            )
        ).pack(side="left")
        temp_file_selected_idx = self.selected_file_idx.get()
        tkinter.Button(
            buttons_frame, text="SAVE CHANGES",
            padx=15, pady=5, font=(self.DEFAULT_FONT, 13, "bold"),
            foreground="springgreen4",
            command=lambda: (
                self.LIST_HANDLER.edit_question(
                    self.selected_question_idx.get(),
                    {
                        "question": new_entry["question"].get("1.0", "end").strip(),
                        "options": [
                            temp_choices_textvar[j].get("1.0", "end").strip() for j in range(num_choices)
                        ],
                        "answer_idx": correct_choice_idx.get(),
                        "feedback_txt": new_entry["feedback_text"].get("1.0", "end").strip(),
                        "hidden": new_entry["hidden"].get()
                    }
                ),
                self.LIST_HANDLER.update_file(),
                self.display_modal(
                    self.edit_question_window,
                    "CHANGES SAVED",
                    "Changes to Question {} of Category {} has been saved.".format(
                        self.selected_question_idx.get() + 1,
                        self.LIST_HANDLER.list_metadata["filename"]
                    ),
                    self.main_bread_window
                ),
                self.reset_bread_frame(),
                self.reset_file_selection_frame(),
                self.selected_file_idx.set(temp_file_selected_idx),
            )
        ).pack(side="left")
        buttons_frame.grid(row=2, sticky="e")

        # PARENT FRAME -- END
        main_frame.pack()

    def display_delete_question_confirmation_window(self):
        # WINDOW SETTINGS
        self.delete_question_confirmation_window = tkinter.Toplevel(self.master)
        self.delete_question_confirmation_window.title("Trivia Quiz Game: Confirm Question Deletion")
        self.delete_question_confirmation_window.geometry("+{x}+{y}".format(x=550, y=75))
        self.delete_question_confirmation_window.protocol(
            "WM_DELETE_WINDOW", lambda: (
                self.delete_question_confirmation_window.withdraw(),
                self.main_bread_window.deiconify(),
                self.selected_question_idx.set(-1)
            )
        )

        wrap_ln = 600
        main_frame = tkinter.Frame(self.delete_question_confirmation_window, padx=20, pady=20)
        tkinter.Label(
            main_frame, text="ARE YOU SURE YOU WANT TO DELETE...",
            font=(self.DEFAULT_FONT, 14, "bold"), foreground="firebrick4",
            wraplength=wrap_ln
        ).grid(row=0)
        tkinter.Label(
            main_frame,
            text=(
                "Question {} in the {} Category?".format(
                    self.selected_question_idx.get() + 1,
                    self.DIR_HANDLER.file_metadata_list[self.selected_file_idx.get()]["category_name"]
                )
            ),
            font=(self.DEFAULT_FONT, 16, "bold"),
            wraplength=wrap_ln
        ).grid(row=1)
        tkinter.Label(
            main_frame, text="WARNING! THIS ACTION CANNOT BE UNDONE!",
            font=(self.DEFAULT_FONT, 11, "bold"), anchor="s",
            wraplength=wrap_ln, pady=3, foreground="firebrick4",
        ).grid(row=2)
        tkinter.Label(
            main_frame, text="QUESTION DATA WILL BE PERMANENTLY LOST.",
            font=(self.DEFAULT_FONT, 11, "bold"), anchor="n",
            wraplength=wrap_ln, pady=3, foreground="firebrick4",
        ).grid(row=3)

        buttons_frame = tkinter.Frame(main_frame, pady=3)
        # Cancel Button
        tkinter.Button(
            buttons_frame, text="CANCEL",
            font=(self.DEFAULT_FONT, 10, "bold"), padx=20, pady=7,
            foreground="gray46",
            command=lambda: (
                self.delete_question_confirmation_window.withdraw(),
                self.main_bread_window.deiconify()
            )
        ).grid(row=0, column=0, padx=1)

        # DELETE BUTTON
        temp_selected_file_idx = self.selected_file_idx.get()
        temp_selected_question_idx = self.selected_question_idx.get()
        tkinter.Button(
            buttons_frame, text="DELETE QUESTION",
            font=(self.DEFAULT_FONT, 12, "bold"), padx=20, pady=7,
            foreground="firebrick4",
            command=lambda: (
                self.LIST_HANDLER.delete_question_by_idx(self.selected_question_idx.get()),
                self.DIR_HANDLER.update_file_question_count(
                    self.selected_file_idx.get(), self.LIST_HANDLER.get_num_questions()
                ),
                self.reset_bread_frame(),
                self.reset_file_selection_frame(),
                self.selected_file_idx.set(temp_selected_file_idx),
                self.display_modal(
                    self.delete_question_confirmation_window,
                    "QUESTION DELETED",
                    "Question {} of the {} Category has been deleted".format(
                        temp_selected_question_idx + 1,
                        self.LIST_HANDLER.list_metadata["category_name"]
                    ),
                    self.main_bread_window
                )
            )
        ).grid(row=0, column=1, padx=1)
        buttons_frame.grid(row=4)

        main_frame.pack()



