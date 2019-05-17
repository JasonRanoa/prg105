"""
    PRG 105 Programming Logic
    Final Project - Part 1 BREAD Interface

    This program acts as the "main" program calling in
    the necessary modules for running the BREAD interface.
"""

import tkinter
from final_exam.modules.breadui_source import BreadUIHandler


def main():
    root = tkinter.Tk()
    _ = BreadUIHandler(root)
    root.mainloop()


main()
