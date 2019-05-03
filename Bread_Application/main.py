"""
    PRG 105 Programming Logic / Spring 2019
    CRUD GUI
"""

import tkinter
from bread_application.breadhandler_source import TriviaBreadHandler


def main():
    root = tkinter.Tk()
    _ = TriviaBreadHandler(root)
    root.mainloop()


main()
