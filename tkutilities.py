#!/usr/bin/env python3
"""Tk Utilities."""
import tkinter as tk
import tkinter.ttk as ttk


def center_on_screen(widget, widget_width, widget_height=None):
    """Return the coordinates to center a widget with the geometry method.

    If the widget_height parameter is not provided, it is calculated according to the proportions of the gold number.

    Args:
        widget: widget object.
        widget_width: widget width.
        widget_height: height of the widget.

    Returns:
        widget_width, widget_height, screen_x_center, screen_y_center

    Use:
        widget_width  = 250
        center_widget = center_on_screen(self, widget_width)
        self.geometry("{}x{}+{}+{}".format(*center_widget))
    """
    if not widget_height:
        phi           = (1 + 5**0.5)/2
        widget_height = int(widget_width/phi)
    screen_width    = widget.winfo_screenwidth()
    screen_height   = widget.winfo_screenheight()
    screen_x_center = int((screen_width  - widget_width) / 2)
    screen_y_center = int((screen_height - widget_height) / 2)
    return widget_width, widget_height, screen_x_center, screen_y_center