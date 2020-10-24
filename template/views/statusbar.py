#!/usr/bin/env python3
import tkinter as tk

class StatusBar(tk.Frame):

    def __init__(self, parent):
        self.statusbar = tk.StringVar()
        super().__init__(parent, bd=2, bg="#E5E5E5")

        self.lbl_text = tk.Label(self,  bd=1, textvariable=self.statusbar,
                                 relief=tk.SUNKEN, anchor=tk.W)
        self.lbl_text.pack(fill=tk.X)

    def text(self, text):
        self.statusbar.set(" " + text)


if __name__ == "__main__":
    # Testing ...

    root = tk.Tk()
    sb   = StatusBar(parent=root)

    sb.pack(side=tk.TOP, fill=tk.X)
    sb.text("Testing test...")
    root.mainloop()