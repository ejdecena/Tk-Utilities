#!/usr/bin/env python3
import tkinter as tk
import tkinter.scrolledtext as st

class Screen(tk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, borderwidth=1, relief=tk.SUNKEN, **kwargs)
        self.parent = parent

        self.__text = st.ScrolledText(self, borderwidth=0, wrap=tk.WORD,
                               highlightthickness=0, height=0,
                               state="disabled")
        self.__text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def clear(self):
        self.__text.config(state="normal")
        self.__text.delete(1.0, tk.END)
        self.__text.config(state="disabled")

    def print(self, text, end="\n"):
        self.__text.config(state="normal")
        self.__text.insert(tk.END, " "+text+end)
        self.__text.config(state="disabled")
        self.__text.see(tk.END)


if __name__ == "__main__":
    # Testing ...

    root = tk.Tk()
    sb   = Screen(parent=root)
    sb.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    sb.print("Testing test...")
    root.mainloop()