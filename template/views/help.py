#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as st
from view import View

class Help(View):

    def __init__(self, master, data_in, widget_width, widget_height=None,
        *args, **kwargs):
        super().__init__(master, data_in, widget_width, widget_height, *args, **kwargs)
        self.title("Help.")

    def create_vars(self):
        pass

    def create_widgets(self):
        text = """sdfsdf sdfsdf sdfsdf sdfsdf sdfdsfds sdfdsf sdfsdf sdfsdf
sdfsdf sdfsdf sdfsdf sdfdsfds sdfdsf sdfsdf sdfsdf sdfsdf sdfsdf sdfsdf
sdfdsfds sdfdsf sdfsdf sdfsdf sdfsdf sdfsdf sdfsdf sdfdsfds sdfdsf sdfsdf
sdfsdf sdfsdf sdfsdf sdfsdf sdfdsfds sdfdsf sdfsdf sdfsdf sdfsdf sdfsdf sdfsdf
sdfdsfds sdfdsf sdfsdf.
        """
        self.text = st.ScrolledText(self, borderwidth=0, wrap=tk.WORD,
                                                                height=13)
        self.btn_ok  = tk.Button(self, text="OK", width=8, underline=0)
        self.text.insert(tk.INSERT, text)
        self.text.config(state="disabled")

    def create_binding(self):
        super().create_binding()
        self.bind("<Alt-o>", lambda e: self.destroy())
        self.bind("<Alt-O>", lambda e: self.destroy())
        self.btn_ok.config(command=self.destroy)

    def create_packing(self):
        self.text.pack(side=tk.TOP, anchor=tk.N)
        self.btn_ok.pack(side=tk.BOTTOM, pady=6, anchor=tk.S)

if __name__ == "__main__":
    # Testing ...

    root = tk.Tk()
    hlp  = Help(master=root, data_in=None, widget_width=400)
    hlp.show()
    root.mainloop()