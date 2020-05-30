#!/usr/bin/env python3
"""Tk Utilities."""
import tkinter as tk
import tkinter.ttk as ttk


class BaseView(tk.Toplevel):
    """It is a base class from which they will inherit all other windows of an application.
    
    Args:
        master: parent object.
        data_in: view input data.
        widget_width: width of the window.
        widget_height: height of the window. If it is not provided, it is calculated according to the golden number (Phi).

    Attributes:
        master: parent object.
        data_in: view input data.
        data_out: view output data and returned in the render() method.

    Use:
        class MyView(BaseView):

            def  def __init__(self, master, data_in):
                widget_width  = 300
                widget_height = None
                super().__init__(master, data_in, widget_width, widget_height)

                self.create_vars()
                self.create_widgets()
                self.create_binding()
                self.create_packing()

        view     = MyView(self, data_in=None)
        data_out = view.render()
    """

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

        self.master   = master
        self.data_in  = data_in
        self.data_out = None

    def render(self):
        """Method that renders the window and waits for the window to close to return the data_out attribute.
        """
        self.transient(self.master)
        self.grab_set()
        self.wait_window()
        return self.data_out


if __name__ == "__main__":
    # Testing ...

    # view     = BaseView(None, data_in=None, widget_width=400)
    # data_out = view.render()