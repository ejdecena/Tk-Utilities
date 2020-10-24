#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk

class View(tk.Toplevel):

    def __init__(self, master, data_in, widget_width, widget_height=None,
        *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        if not widget_height:
            phi           = (1 + 5**0.5)/2
            widget_height = int(widget_width/phi)
        screen_width    = self.winfo_screenwidth()
        screen_height   = self.winfo_screenheight()
        screen_x_center = int((screen_width  - widget_width) / 2)
        screen_y_center = int((screen_height - widget_height) / 2)
        self.geometry("{}x{}+{}+{}".format(widget_width, widget_height,
                                        screen_x_center, screen_y_center))
        self.resizable(False, False)

        self.option_add("*font", "TkDefaultFont 13 normal")

        self.master   = master
        self.data_in  = data_in
        self.data_out = None

        self.create_vars()
        self.create_widgets()
        self.create_binding()
        self.create_packing()

    def create_vars(self):
         raise NotImplementedError

    def create_widgets(self):
         raise NotImplementedError

    def create_binding(self):
        self.bind("<Escape>", self.click_exit)
        self.protocol("WM_DELETE_WINDOW", self.click_exit)

    def create_packing(self):
         raise NotImplementedError

    def show(self):
        self.transient(self.master)
        self.grab_set()
        self.wait_window()
        return self.data_out

    def click_exit(self, event=None):
        self.destroy()
        return "break"


if __name__ == "__main__":
    # Testing ...

    # root     = tk.Tk()
    # view     = View(None, data_in=None, widget_width=400)
    # data_out = view.show()
    pass