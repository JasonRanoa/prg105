"""
    class TriviaBreadHandler
    This class handles the GUI elements for BREAD operations.
        - Browse, Read, Edit, Add, and Delete
    Needs TriviaDataHandler class to handle file stuff.
"""

import tkinter
from bread_application.datahandler_source import TriviaDataHandler


class TriviaBreadHandler:
    def __init__(self, master):
        self.master = master
        self.master.title("Trivia: BREAD Interface")
        self.master.withdraw()  # https://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window

        self.data_handler = TriviaDataHandler()
        if self.data_handler.has_error:
            # CROSS-METHOD VARS
            self.selected_idx = tkinter.IntVar()
            self.main_window = tkinter.Toplevel()
            self.add_window = tkinter.Toplevel()
            self.edit_window = tkinter.Toplevel()
            self.frame_in_canvas = tkinter.Frame()
            self.canvas_scr_width = 0  # canvas scr (scrollable region) dimensions are defined in start_main_frame method
            self.canvas_scr_padx = 0
            # CALL WINDOW
            self.display_error(self.data_handler.error_string)
        else:
            self.start_main_frame()

    """
        def start_main_frame(self)
        This method calls the window that displays the trivia
        and the options for BREAD
    """
    def start_main_frame(self):
        self.main_window = tkinter.Toplevel(self.master)
        self.main_window.title("Trivia List: BREAD Interface")
        self.main_window.geometry("+{x}+{y}".format(x=350, y=150))
        self.main_window.protocol("WM_DELETE_WINDOW", self.master.destroy)  # exits the program once done

        # MAIN PARENT FRAME
        main_frame = tkinter.Frame(self.main_window, padx=10)

        # Header Frame
        header_frame = tkinter.Frame(main_frame, pady=10)
        tkinter.Label(
            header_frame,
            text="Trivia Viewer - BREAD Interface",
            font="Calibri 20 bold", foreground="SpringGreen4"
        ).grid(row=0, column=0, sticky="w")
        tkinter.Label(
            header_frame,
            text="Browse, Read, Edit, Add, and Delete Trivia Items",
            font="Calibri 15 bold", foreground="SpringGreen4"
        ).grid(row=1, column=0, sticky="w")
        header_frame.grid(row=0, column=0, sticky="we", columnspan=2)

        # Side Frame, containing data_list information
        side_frame = tkinter.Frame(main_frame)
        tkinter.Label(
            side_frame,
            text="DATAFILE INFORMATION:",
            font="Calibri 12 bold"
        ).grid(row=0, column=0, sticky="w")
        tkinter.Label(
            side_frame,
            text="Filename: {}  ".format(self.data_handler.get_datafile_location())
        ).grid(row=1, column=0, sticky="w")
        tkinter.Label(
            side_frame,
            text="Trivia Items: {}\n".format(self.data_handler.get_list_length())
        ).grid(row=2, column=0, sticky="w")
        tkinter.Label(
            side_frame,
            text="NOTE:\n To access more info and controls about an item, click on its number.",
            font="Calibri 12 bold", foreground="SpringGreen4",
            wraplength=150
        ).grid(row=3, column=0)
        side_frame.grid(row=1, column=0, sticky="nw")

        # CANVAS FRAME
        self.canvas_scr_width = 800  # TOTAL Frame Width, including padding
        self.canvas_scr_padx = 10
        canvas_frame = tkinter.Frame(main_frame, borderwidth=1, background="Chartreuse4")
        canvas_frame.grid(row=1, column=1, sticky="nw")

        # Reference for Scrolling Canvas:
        # https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
        # https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter
        
        list_canvas = tkinter.Canvas(canvas_frame)
        self.frame_in_canvas = tkinter.Frame(list_canvas)
        scrollbar = tkinter.Scrollbar(
            canvas_frame, orient="vertical", command=list_canvas.yview
        )
        list_canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        list_canvas.pack(side="left")
        list_canvas.create_window((0, 0), window=self.frame_in_canvas, anchor="nw")
        self.frame_in_canvas.bind(
            "<Configure>",
            lambda event: list_canvas.configure(
                scrollregion=list_canvas.bbox("all"),
                width=self.canvas_scr_width - 2 * self.canvas_scr_padx - 15,
                height=500
            )
        )

        # ITEMS INSIDE SCROLLING SECTION RIGHT HERE!
        self.populate_canvas_frame(self.frame_in_canvas, self.canvas_scr_width, self.canvas_scr_padx)

        # Footer Frame
        footer_frame = tkinter.Frame(main_frame, pady=10)
        quit_button = tkinter.Button(
            footer_frame, text="QUIT PROGRAM",
            padx=10, pady=5, font="Calibri 15 bold",
            foreground="firebrick4",
            command=self.master.destroy
        )
        quit_button.pack(side="right")
        add_button = tkinter.Button(
            footer_frame, text="ADD NEW ITEM",
            padx=10, pady=5, font="Calibri 15 bold",
            foreground="SpringGreen4",
            command=self.raise_add_interface
        )
        add_button.pack(side="right")
        footer_frame.grid(row=2, column=1, columnspan=2, sticky="ew")

        # ENDING MAIN FRAME
        main_frame.pack()

    """
        def display_error(self, message)
        Opens another window with the message, colored in red.
        Only allows the user to quit stuff after this method has been called.
    """
    def display_error(self, message):
        ew = tkinter.Toplevel(self.master)  # ew = error_window
        ew.title("Error. Program Terminated.")
        ew.geometry("+{x}+{y}".format(x=650, y=300))
        ew.protocol("WM_DELETE_WINDOW", self.master.destroy)

        ef = tkinter.Frame(ew, padx=25, pady=10)

        errlbl1 = tkinter.Label(
            ef, text="A critical error has happened",
            foreground="firebrick3", font="Calibri 16 bold",
            padx=30
        )
        errlbl1.pack()

        errlbl2 = tkinter.Label(
            ef, text=message + "\n",
            foreground="firebrick3", font="Calibri 12 bold"
        )
        errlbl2.pack(fill="x")

        err_quit_btn = tkinter.Button(
            ef, text="QUIT PROGRAM",
            padx=20, pady=7, font="Calibri 10 bold",
            foreground="firebrick3", command=self.master.destroy
        )
        err_quit_btn.pack()

        ef.pack()

    def populate_canvas_frame(self, canvas_frame, canvas_width, canvas_padding):
        # DESTROY ALL CHILDREN
        for child in canvas_frame.winfo_children():
            child.destroy()

        # POPULATE
        # Because of how I can't bind the value of i to the buttons,
        #   a workaround using tkinter's radios has been added.
        self.selected_idx = tkinter.IntVar()
        self.selected_idx.set(-1)
        for i in range(self.data_handler.get_list_length()):
            tkinter.Label(canvas_frame, text="").grid(row=i, column=0)  # spacing
            tkinter.Radiobutton(
                canvas_frame, text=str(i + 1),
                value=i, variable=self.selected_idx,
                font="Calibri 12 bold", borderwidth=1, padx=7,
                foreground="SpringGreen4", highlightbackground="SpringGreen4",
                indicatoron=0,
                command=self.raise_edit_interface
            ).grid(row=i, column=1, sticky="ew")
            tkinter.Label(
                canvas_frame,
                text=self.data_handler.get_list_member(i),
                wraplength=canvas_width - 2 * canvas_padding - 15 - 10 - 50,  # I don't know why this works. Don't change it.
                justify="left"
            ).grid(row=i, column=2, sticky="nw")

    """
        Creates a new window for the add interface.
        Withdraws the new interface.
    """
    def raise_add_interface(self):
        self.main_window.withdraw()
        self.add_window = tkinter.Toplevel(self.master)
        self.add_window.title("Trivia List: ADD NEW TRIVIA")
        self.add_window.geometry("+{x}+{y}".format(x=600, y=300))
        self.add_window.protocol("WM_DELETE_WINDOW", lambda: (
            self.add_window.withdraw(), self.main_window.deiconify()
        ))

        main_frame = tkinter.Frame(self.add_window, padx=10, pady=7)

        # TITLE
        tkinter.Label(
            main_frame,
            text="Add a new entry for the trivia list:",
            font="Calibri 16 bold", foreground="SpringGreen4"
        ).grid(row=0, column=0, sticky="w")

        tkinter.Label(
            main_frame,
            text="Symbols (other than punctuation) is discouraged."
                 "\nNew line characters are also accepted.",
            justify="left", pady=3
        ).grid(row=1, column=0, sticky="w")

        # ACTUAL ENTRY FORM
        text_entry = tkinter.Text(
            main_frame,
            padx=10, pady=10, width=80, height=7,
            highlightbackground="Chartreuse4",
            relief="flat"
        )
        text_entry.grid(row=2, column=0)

        # Buttons
        buttons_frame = tkinter.Frame(main_frame, pady=7)
        tkinter.Button(
            buttons_frame, text="SUBMIT NEW ENTRY",
            padx=15, pady=7, font="Calibri 12 bold",
            foreground="SpringGreen4",
            command=lambda: (
                self.data_handler.add_new_member(text_entry.get("1.0", "end").strip()),
                self.data_handler.update_datafile(),  # NO ERROR HANDLING, BTW,
                self.populate_canvas_frame(self.frame_in_canvas, self.canvas_scr_width, self.canvas_scr_padx),
                self.add_window.withdraw(),
                self.main_window.deiconify()
            )
        ).grid(row=0, column=1, sticky="e")

        tkinter.Button(
            buttons_frame, text="CANCEL",
            padx=15, pady=7, font="Calibri 12 bold",
            foreground="Yellow4",
            command=lambda: (
                self.add_window.withdraw(),
                self.main_window.deiconify()
            )
        ).grid(row=0, column=0, sticky="e")
        buttons_frame.grid(row=3, column=0, sticky="e")

        main_frame.pack()

    """
        Creates a new window for the edit interface.
        Withdraws the new interface.
    """
    def raise_edit_interface(self):
        self.main_window.withdraw()
        self.edit_window = tkinter.Toplevel(self.master)
        self.edit_window.title("Trivia List: ADD NEW TRIVIA")
        self.edit_window.geometry("+{x}+{y}".format(x=600, y=300))
        self.edit_window.protocol("WM_DELETE_WINDOW", lambda: (
            self.edit_window.withdraw(),
            self.main_window.deiconify(),
            self.selected_idx.set(-1)
        ))

        main_frame = tkinter.Frame(self.edit_window, padx=10, pady=7)

        # TITLE
        tkinter.Label(
            main_frame,
            text="Edit Entry {}:".format(self.selected_idx.get() + 1),
            font="Calibri 16 bold", foreground="SpringGreen4"
        ).grid(row=0, column=0, sticky="w")

        tkinter.Label(
            main_frame,
            text="Symbols (other than punctuation) is discouraged."
                 "\nNew line characters are also accepted.",
            justify="left", pady=3
        ).grid(row=1, column=0, sticky="w")

        # ACTUAL ENTRY FORM
        text_entry = tkinter.Text(
            main_frame,
            padx=10, pady=10, width=80, height=7,
            highlightbackground="Chartreuse4",
            relief="flat"
        )
        text_entry.grid(row=2, column=0)
        text_entry.insert("1.0", self.data_handler.get_list_member(self.selected_idx.get()))

        # Buttons
        buttons_frame = tkinter.Frame(main_frame, pady=7)
        tkinter.Button(
            buttons_frame, text="UPDATE ENTRY",
            padx=15, pady=7, font="Calibri 12 bold",
            foreground="SpringGreen4",
            command=lambda: (
                self.data_handler.set_list_member(
                    self.selected_idx.get(),
                    text_entry.get("1.0", "end").strip()
                ),
                self.data_handler.update_datafile(),  # NO ERROR HANDLING AGAIN, BTW,
                self.populate_canvas_frame(self.frame_in_canvas, self.canvas_scr_width, self.canvas_scr_padx),
                self.edit_window.withdraw(),
                self.selected_idx.set(-1),
                self.main_window.deiconify()
            )
        ).grid(row=0, column=2, sticky="e")

        tkinter.Button(
            buttons_frame, text="DELETE ENTRY",
            padx=15, pady=7, font="Calibri 12 bold",
            foreground="FireBrick4",
            command=lambda: (
                self.data_handler.delete_list_member(self.selected_idx.get()),
                self.data_handler.update_datafile(),  # NO ERROR HANDLING AGAIN, BTW,
                self.populate_canvas_frame(self.frame_in_canvas, self.canvas_scr_width, self.canvas_scr_padx),
                self.edit_window.withdraw(),
                self.selected_idx.set(-1),
                self.main_window.deiconify()
            )
        ).grid(row=0, column=1, sticky="e")

        tkinter.Button(
            buttons_frame, text="CANCEL",
            padx=15, pady=7, font="Calibri 12 bold",
            foreground="Yellow4",
            command=lambda: (
                self.edit_window.withdraw(),
                self.main_window.deiconify(),
                self.selected_idx.set(-1)
            )
        ).grid(row=0, column=0, sticky="e")
        buttons_frame.grid(row=3, column=0, sticky="e")

        main_frame.pack()
