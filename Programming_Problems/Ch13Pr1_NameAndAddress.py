# Programming Practice 13.1 Name and Address
"""
Write a GUI program that displays your name and address when a
button is clicked (you can use the address of the school).
The program’s window should resemble the sketch on the far left
side of figure 13-26 when it runs. When the user clicks the Show
Info button, the program should display your name and address as
shown in the sketch on the right of the figure.
"""

import tkinter


class NameAddressGUI:
    def __init__(self):
        self.is_info_displayed = False
        self.main_window = tkinter.Tk()

        # Label text values, blank at the beginning
        self.name_lbl_val = tkinter.StringVar()
        self.addr_lbl_val1 = tkinter.StringVar()
        self.addr_lbl_val2 = tkinter.StringVar()

        # Top frame shows name and address
        self.top_frame = tkinter.Frame()
        self.name_lbl = tkinter.Label(
            self.top_frame, textvariable=self.name_lbl_val,
            width="25"
        )
        self.address_lbl_1 = tkinter.Label(
            self.top_frame, textvariable=self.addr_lbl_val1,
            width="25"
        )
        self.address_lbl_2 = tkinter.Label(
            self.top_frame, textvariable=self.addr_lbl_val2,
            width="25"
        )
        self.name_lbl.pack(side="top")
        self.address_lbl_1.pack(side="top")
        self.address_lbl_2.pack(side="top")

        # Bottom frame shows controls
        self.bottom_frame = tkinter.Frame()
        self.display_toggle_btn = tkinter.Button(
            self.bottom_frame, text="Show Info", command=self.toggle_display
        )
        self.quit_btn = tkinter.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy
        )
        self.display_toggle_btn.pack(side="left")
        self.quit_btn.pack(side="right")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def toggle_display(self):
        if self.is_info_displayed:
            self.name_lbl_val.set("")
            self.addr_lbl_val1.set("")
            self.addr_lbl_val2.set("")
            self.is_info_displayed = False
        else:
            self.name_lbl_val.set("Julius Ranoa")
            self.addr_lbl_val1.set("8900 US-14, Crystal Lake")
            self.addr_lbl_val2.set("Illinois 60051")
            self.is_info_displayed = True


def main():
    NameAddressGUI()


main()
