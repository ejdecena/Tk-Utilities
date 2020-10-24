#!/usr/bin/env python3
import tkinter as tk

class ToolTip:

    def __init__(self, widget):
        self.widget    = widget
        self.tipwindow = None
        self.id        = None
        self.x         = self.y = 0

    def showtip(self, text):
        """Display text in tooltip window."""
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 37 # 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "12", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)


if __name__ == "__main__":
    # Testing...

    root = tk.Tk()
    btn  = tk.Button(root, text="My Button")
    CreateToolTip(btn, "This is a Tooltip.")
    btn.pack()
    root.mainloop()