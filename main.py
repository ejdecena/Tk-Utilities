#!/usr/bin/env python3
"""Tk Utilities."""
from appview import AppView
from loginview import LoginView
import tkinter.messagebox as mb


def main():
    """This script combines the LoginView and AppView windows to create an application login. It starts the AppView to the user providing a username = 1 and password = 1.
    """
    while True:
        login = LoginView(widget_width=252)
        if (login.username == "1") and (login.password == "1"):
            break
        else:
            mb.showerror("Incorrect Login.",
                         "You have entered an incorrect login.")
            login.destroy()

    login.destroy()
    AppView("My Application", widget_width=400)


if __name__ == "__main__":

    main()