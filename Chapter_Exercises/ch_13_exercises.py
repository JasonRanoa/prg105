"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
from tkinter import messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text="Julius Ranoa")
        self.label.pack()
        tkinter.mainloop()


# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

my_gui = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Top Frame Stuff
        self.label_name = tkinter.Label(self.top_frame, text="Julius Ranoa")
        self.label_major = tkinter.Label(self.top_frame, text="Computer Science")
        self.label_name.pack()
        self.label_major.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        # Bottom Frame Stuff
        self.label_classes = [
            tkinter.Label(self.bottom_frame, text="MAT 260 Differential Equations"),
            tkinter.Label(self.bottom_frame, text="ART 151 Art Appreciation"),
            tkinter.Label(self.bottom_frame, text="ENG 152 Composition II"),
            tkinter.Label(self.bottom_frame, text="PRG 105 Programming Logic")
        ]
        for lbl in self.label_classes:
            lbl.pack()

        tkinter.mainloop()


my_gui3 = MyGUI3()


# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class JokeGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.joke = tkinter.Label(
            self.main_window,
            text="There are 10 kinds of people in the world\n"
            "-- those who understand binary, \n"
            "-- those who don't."
        )
        self.joke.pack()

        self.punchline = "-- those who don't expect this joke to be in base-3!"
        self.btn = tkinter.Button(
            self.main_window, text="... and ...",
            command=self.show_punchline
        )
        self.btn.pack()

        tkinter.mainloop()

    def show_punchline(self):
        tkinter.messagebox.showinfo("...", self.punchline)


jk = JokeGUI()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class ConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(
            self.top_frame, text="Enter measurement in inches: "
        )
        self.inch_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.inch_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame, text="Converted to centimeters: ")
        self.value = tkinter.StringVar()
        self.cm_label = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.descr_label.pack(side='left')
        self.cm_label.pack(side='left')

        self.calc_button = tkinter.Button(
            self.bottom_frame, text="Convert", command=self.convert
        )
        self.quit_button = tkinter.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy
        )
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        inch = float(self.inch_entry.get())
        cm = inch * 2.54
        self.value.set(round(cm, 2))


cv = ConverterGUI()
