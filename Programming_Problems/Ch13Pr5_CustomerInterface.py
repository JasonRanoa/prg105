# Programming Practice 13.5 Customer Interface
"""
Make up an interface for a business offering 7-10 services or
products with prices. Write a GUI program to allow the user
to click buttons to add services or products and show total
at the bottom. Make sure all necessary labels and instructions
to the user are included in your GUI.
"""

import tkinter
from tkinter import messagebox


class CustomPizzaCreator:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.winfo_toplevel().title("MAKE A CUSTOM PIZZA")
        self.main_frame = tkinter.Frame(
            padx=40, pady=15
        )

        # Title
        self.title_frame = tkinter.Frame(self.main_frame, pady=10)
        self.title_label = tkinter.Label(
            self.title_frame, text="CREATE YOUR OWN PIZZA",
            font=("Calibri", 30), anchor="w"
        )
        self.subtitle_label = tkinter.Label(
            self.title_frame,
            text="Choose your own crust, pizza size, sauce, cheese amount, and toppings".upper(),
            font=("Calibri", 15), anchor="w"
        )
        self.title_label.pack(fill="x")  # uses all space along the x-axis
        self.subtitle_label.pack(fill="x")
        self.title_frame.pack(fill="x")

        # OPTIONS GRID
        self.options_grid = tkinter.Frame(self.main_frame)
        # there are six columns and lots of rows
        group_label_size = 10
        option_label_size = 25
        add_price_label_size = 5
        curr_row = 1

        # Size Options, r = 2
        self.size_label = tkinter.Label(
            self.options_grid, text="Pizza Size: ",
            width=group_label_size, anchor="w"
        ).grid(row=curr_row, column=1, sticky="w")
        self.size_choices = [
            ("Medium", 0.00), ("Large", 2.00)
        ]
        self.size_chosen_index = tkinter.IntVar()
        for num, item in enumerate(self.size_choices):
            tkinter.Radiobutton(
                self.options_grid, text=item[0], width=option_label_size,
                variable=self.size_chosen_index, value=num,
                command=self.calculate_price
            ).grid(row=curr_row+num, column=2, sticky="w")
            extra_lbl = ""
            if item[1] != 0:
                extra_lbl = "+${:.2f}".format(item[1])
            tkinter.Label(
                self.options_grid, text=extra_lbl, width=add_price_label_size,
                foreground="firebrick2"
            ).grid(row=curr_row+num, column=3, sticky="e")
        tkinter.Label(
            self.options_grid, text=""
        ).grid(row=curr_row+len(self.size_choices), column=1)  # empty
        curr_row += len(self.size_choices) + 1

        # Crust Options, r = 5
        self.crust_label = tkinter.Label(
            self.options_grid, text="Crust Type: ",
            width=group_label_size, anchor="w"
        ).grid(row=curr_row, column=1, sticky="w")
        self.crust_choices = [
            ("Hand-Tossed Pizza", 0.00),
            ("Original Pan Pizza", 1.00),
            ("Thin & Crispy", 0.00),
            ("Original Stuffed Crust", 2.50),
            ("Ultimate Cheesy Crust", 0.00)
        ]
        self.crust_chosen_index = tkinter.IntVar()
        for num, item in enumerate(self.crust_choices):
            tkinter.Radiobutton(
                self.options_grid, text=item[0], width=option_label_size,
                variable=self.crust_chosen_index, value=num,
                command=self.calculate_price
            ).grid(row=curr_row+num, column=2, sticky="w")
            extra_lbl = ""
            if item[1] != 0:
                extra_lbl = "+${:.2f}".format(item[1])
            tkinter.Label(
                self.options_grid, text=extra_lbl, width=add_price_label_size,
                foreground="firebrick2"
            ).grid(row=curr_row+num, column=3, sticky="e")
        tkinter.Label(
            self.options_grid, text=""
        ).grid(row=curr_row+len(self.crust_choices), column=1)  # empty
        curr_row += len(self.crust_choices) + 1

        # Sauce Options, r = 4
        self.sauce_label = tkinter.Label(
            self.options_grid, text="Sauce Type: ",
            width=group_label_size, anchor="w"
        ).grid(row=curr_row, column=1, sticky="w")
        self.sauce_choices = [
            ("Classic Marinara", 0.00),
            ("Creamy Garlic Parmesan", 0.00),
            ("Barbeque", 0.00),
            ("Buffalo", 0.00)
        ]
        self.sauce_chosen_index = tkinter.IntVar()
        for num, item in enumerate(self.sauce_choices):
            tkinter.Radiobutton(
                self.options_grid, text=item[0], width=option_label_size,
                variable=self.sauce_chosen_index, value=num,
                command=self.calculate_price
            ).grid(row=curr_row+num, column=2, sticky="w")
            extra_lbl = ""
            if item[1] != 0:
                extra_lbl = "+${:.2f}".format(item[1])
            tkinter.Label(
                self.options_grid, text=extra_lbl, width=add_price_label_size,
                foreground="firebrick2"
            ).grid(row=curr_row+num, column=3, sticky="e")
        tkinter.Label(
            self.options_grid, text=""
        ).grid(row=curr_row+len(self.sauce_choices), column=1)  # empty
        curr_row += len(self.sauce_choices) + 1

        # Cheese
        self.cheese_label = tkinter.Label(
            self.options_grid, text="Cheese: ",
            width=group_label_size, anchor="w"
        ).grid(row=curr_row, column=1, sticky="w")
        self.cheese_choices = [
            ("Regular", 0.00),
            ("EXTRA", 2.00),
            ("Light", 0.00),
            ("None", 0.00)
        ]
        self.cheese_chosen_index = tkinter.IntVar()
        for num, item in enumerate(self.cheese_choices):
            tkinter.Radiobutton(
                self.options_grid, text=item[0], width=option_label_size,
                variable=self.cheese_chosen_index, value=num,
                command=self.calculate_price
            ).grid(row=curr_row+num, column=2, sticky="w")
            extra_lbl = ""
            if item[1] != 0:
                extra_lbl = "+${:.2f}".format(item[1])
            tkinter.Label(
                self.options_grid, text=extra_lbl, width=add_price_label_size,
                foreground="firebrick2"
            ).grid(row=curr_row+num, column=3, sticky="e")

        # Empty Column
        tkinter.Label(
            self.options_grid, text="", width=5
        ).grid(row=1, column=4)  # empty

        # Toppings
        curr_row = 1
        self.toppings_label = tkinter.Label(
            self.options_grid, text="Toppings: ",
            width=group_label_size, anchor="w"
        ).grid(row=curr_row, column=5, sticky="w")
        self.toppings_choices = [
            ("Pepperoni", 2.00),
            ("Italian Sausage", 2.00),
            ("Meatball", 2.00),
            ("Ham", 2.00),
            ("Bacon", 2.00),
            ("Grilled Chicken", 2.00),
            ("Beef", 2.00),
            ("Pork", 2.00),
            ("Pineapple", 1.75),
            ("Mushrooms", 1.75),
            ("Roasted Spinach", 1.75),
            ("Mediterranean Black Olives", 1.75),
            ("Green Bell Peppers", 1.75),
            ("Banana Peppers", 1.75),
            ("Jalapeno Peppers", 1.75),
            ("Roma Tomatoes", 1.75)
        ]
        self.toppings_chosen_indices = [
            tkinter.IntVar() for _ in range(len(self.toppings_choices))
        ]
        for num, item in enumerate(self.toppings_choices):
            tkinter.Checkbutton(
                self.options_grid, text=item[0], width=option_label_size,
                variable=self.toppings_chosen_indices[num],
                command=self.calculate_price
            ).grid(row=curr_row+num, column=6, sticky="w")
            extra_lbl = ""
            if item[1] != 0:
                extra_lbl = "+${:.2f}".format(item[1])
            tkinter.Label(
                self.options_grid, text=extra_lbl, width=add_price_label_size,
                foreground="springgreen4"
            ).grid(row=curr_row+num, column=7, sticky="e")

        self.options_grid.pack(fill="x")

        # Price Frame
        self.price_frame = tkinter.Frame(self.main_frame)

        self.price_title = tkinter.Label(
            self.price_frame, text="TOTAL PRICE: ",
            font=("Calibri", 25)
        )
        self.price_label_var = tkinter.StringVar()
        self.price_label = tkinter.Label(
            self.price_frame, textvariable=self.price_label_var,
            font=("Calibri", 35),
            foreground="springgreen4"
        )
        self.calculate_price()
        self.price_label.pack(side="right")
        self.price_title.pack(side="right")
        self.price_frame.pack(fill="x")

        # Button for next
        self.next_frame = tkinter.Frame(
            self.main_frame, pady=10
        )
        self.next_button = tkinter.Button(
            self.next_frame, text="NEXT >",
            padx=10, pady=5, font=("Calibri", 20),
            command=self.do_next_thing
        )
        self.next_button.pack(side="right")
        self.next_frame.pack(fill="x")

        self.main_frame.pack()
        self.main_window.mainloop()

    def calculate_price(self):
        base_price = 10.99
        price = base_price \
            + self.size_choices[self.size_chosen_index.get()][1] \
            + self.crust_choices[self.crust_chosen_index.get()][1] \
            + self.sauce_choices[self.size_chosen_index.get()][1] \
            + self.cheese_choices[self.cheese_chosen_index.get()][1]
        for num, topic_choice in enumerate(self.toppings_chosen_indices):
            if topic_choice.get():  # if true
                price += self.toppings_choices[num][1]
        # add additional costs depending on topics
        self.price_label_var.set("${:.2f}".format(price))

    def do_next_thing(self):
        tkinter.messagebox.showinfo(
            "This goes somewhere, I promise.",
            "Usually, there would be a function here that would "
            "proceed to submit this order to a server or something...\n\n"
            "... but that's outside the scope of the homework problem.\n\n"
            "In any case, the total's " + self.price_label_var.get() + "."
        )


_ = CustomPizzaCreator()
