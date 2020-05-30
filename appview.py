#!/usr/bin/env python3
"""Tk Utilities."""
import tkinter as tk
import tkinter.ttk as ttk


class AppView(tk.Tk):
    """It implements the main window of a user interface with established specifications of form, location and fonts.
    
    Args:
        app_name: name of the application.
        widget_width: width of the window.
        widget_height: height of the window. If it is not provided, it is calculated according to the golden number (Phi).

    Attributes:
        app_name: application name.

    Use:
        AppView("My Application", widget_width=400)
    """

    def __init__(self, app_name, widget_width, widget_height=None):
        super().__init__()
        if not widget_height:
            phi           = (1 + 5**0.5)/2
            widget_height = int(widget_width/phi)
        screen_width    = self.winfo_screenwidth()
        screen_height   = self.winfo_screenheight()
        screen_x_center = int((screen_width  - widget_width) / 2)
        screen_y_center = int((screen_height - widget_height) / 2)
        self.title(app_name)
        self.geometry("{}x{}+{}+{}".format(widget_width, widget_height,
                                            screen_x_center, screen_y_center))
        self.resizable(False, False)

        self.option_add("*font", "TkDefaultFont 12 normal")
        ttk.Style().configure("TButton", font="TkDefaultFont 12 normal")
        ttk.Style().map("TCombobox", fieldbackground=[("readonly","white")])
        ttk.Style().map("TCombobox", selectbackground=[("readonly", "white")])
        ttk.Style().map("TCombobox", selectforeground=[("readonly", "black")])

        self.create_vars()
        self.create_widgets()
        self.create_binding()
        self.create_packing()

        self.app_name = app_name
        self.mainloop()

    def create_vars(self):
        pass

    def create_widgets(self):
        pass

    def create_binding(self):
        self.bind("<Escape>", self.on_quit_btn_clicked)
        self.protocol("WM_DELETE_WINDOW", self.on_quit_btn_clicked)

    def create_packing(self):
        ttk.Label(self, text="Application's interface!").pack(pady=10)
        ttk.Button(self, text="Quit", command=self.on_quit_btn_clicked).pack()

    def on_quit_btn_clicked(self, event=None):
        self.quit()
        return "break"


if __name__ == "__main__":
    # Testing...

    AppView("My Application", widget_width=400)