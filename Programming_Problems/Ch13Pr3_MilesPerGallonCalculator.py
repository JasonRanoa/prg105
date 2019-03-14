# Programming Practice 13.3 Miles per Gallon Calculator
"""
Write a GUI program that calculates a car’s gas mileage.
The program’s window should have Entry widgets that let the user
enter the number of gallons of gas the car holds, and the number of
miles it can be driven on a full tank.
When a Calculate MPG button is clicked, the program should display
the number of miles that the car may be driven per gallon of gas.

Use the following formula to calculate miles per gallon:
MPG = miles / gallons
"""

import tkinter


class MPGCalculator:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # MAIN FRAME
        self.main_frame = tkinter.Frame(
            padx=20, pady=15
        )

        # Title Frame
        self.title_frame = tkinter.Frame(self.main_frame)
        self.title_label = tkinter.Label(
            self.title_frame, text="MPG Calculator",
            borderwidth=2, font=("Calibri", 18)
        )
        self.title_label.pack()
        self.title_frame.pack()

        # Gallon Entry
        self.gallon_frame = tkinter.Frame(self.main_frame)
        self.gallon_label = tkinter.Label(
            self.gallon_frame, wraplength=200, width=25,
            text="Enter how many gallons the car holds on a full tank",
        )
        self.gallon_colon = tkinter.Label(
            self.gallon_frame, text=":", width=1
        )
        self.gallon_entry_val = tkinter.StringVar()
        self.gallon_entry = tkinter.Entry(
            self.gallon_frame, width=10,
            textvariable=self.gallon_entry_val
        )
        self.gallon_label2 = tkinter.Label(
            self.gallon_frame, text="gallon(s)", width=7, justify="left"
        )
        self.gallon_label.pack(side="left")
        self.gallon_colon.pack(side="left")
        self.gallon_entry.pack(side="left")
        self.gallon_label2.pack(side="left")
        self.gallon_frame.pack()

        # Miles Entry
        self.miles_frame = tkinter.Frame(self.main_frame)
        self.miles_label = tkinter.Label(
            self.miles_frame, wraplength=200, width=25,
            text="Enter how many miles the car can be driven on a full tank",
        )
        self.miles_colon = tkinter.Label(
            self.miles_frame, text=":", width=1
        )
        self.miles_entry_val = tkinter.StringVar()
        self.miles_entry = tkinter.Entry(
            self.miles_frame, width=10,
            textvariable=self.miles_entry_val
        )
        self.miles_label2 = tkinter.Label(
            self.miles_frame, text="mile(s)", width=7, justify="left"
        )
        self.miles_label.pack(side="left")
        self.miles_colon.pack(side="left")
        self.miles_entry.pack(side="left")
        self.miles_label2.pack(side="left")
        self.miles_frame.pack()

        # Button
        self.button_frame = tkinter.Frame(
            self.main_frame, pady=5
        )
        self.calculate_button = tkinter.Button(
            self.button_frame, text="Calculate Mileage",
            padx=10, pady=5,
            command=self.calculate_mileage
        )
        self.calculate_button.pack()
        self.button_frame.pack()

        # Results
        self.results_frame = tkinter.Frame(self.main_frame)
        self.results_label_val = tkinter.StringVar()
        self.results_label_val.set(
            "Please press the \"Calculate Mileage\" button."
        )
        self.results_label = tkinter.Label(
            self.results_frame, textvariable=self.results_label_val,
            font=("Calibri", 17)
        )
        self.results_label.pack()
        self.results_frame.pack()

        self.main_frame.pack()

        tkinter.mainloop()

    def calculate_mileage(self):
        try:
            miles = float(self.miles_entry_val.get())
            gallons = float(self.gallon_entry_val.get())
            mileage = miles / gallons
            self.results_label_val.set(
                "Calculated Mileage: {:.2f} MPG".format(mileage)
            )
        except ValueError:
            self.results_label_val.set(
                "Values entered are invalid. Try again."
            )


_ = MPGCalculator()
