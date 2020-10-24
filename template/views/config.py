#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
from view import View

class Config(View):

    def __init__(self, master, data_in, widget_width, widget_height=None,
        *args, **kwargs):
        super().__init__(master, data_in, widget_width, widget_height,
                                                        *args, **kwargs)
        self.title("Configuration.")
        self.resizable(True, True)

    def create_vars(self):
         self.var_op1 = tk.StringVar()
         self.var_op2 = tk.StringVar()
         self.var_op3 = tk.StringVar()

         self.var_op1.set(self.data_in["var_op1"])
         self.var_op2.set(self.data_in["var_op2"])
         self.var_op3.set(self.data_in["var_op3"])

    def create_widgets(self):
         self.lbl_op1 = tk.Label(self, text="O 1:")
         self.lbl_op2 = tk.Label(self, text="Opt 2:")
         self.lbl_op3 = tk.Label(self, text="Option 3:")

         cmb_list = ("January", "February", "March")
         self.cmb_opt1 = ttk.Combobox(self, width=12, state="readonly",
                                values=cmb_list, textvariable=self.var_op1)

         self.spb_opt2 = tk.Spinbox(self, from_=0, to=10, width=12,
                                state="readonly", textvariable=self.var_op2)
         self.ent_opt3 = tk.Entry(self, width=13, textvariable=self.var_op3)
         self.btn_save = tk.Button(self, text="Save", underline=0)

    def create_binding(self):
        super().create_binding()
        self.bind("<Return>", self.click_btn_save)
        self.bind("<Alt-s>", self.click_btn_save)
        self.bind("<Alt-S>", self.click_btn_save)
        self.btn_save.config(command=self.click_btn_save)
        self.var_op3.trace("w", lambda *args: self.validate_ent_opt3())

    def create_packing(self):
        opts_lbl = dict(padx=3, pady=4, sticky=tk.E)
        self.lbl_op1.grid(row=0, column=0, **opts_lbl)
        self.lbl_op2.grid(row=1, column=0, **opts_lbl)
        self.lbl_op3.grid(row=2, column=0, **opts_lbl)

        opts_obj = dict(padx=3, pady=4, sticky=tk.W)
        self.cmb_opt1.grid(row=0, column=1, **opts_obj)
        self.spb_opt2.grid(row=1, column=1, **opts_obj)
        self.ent_opt3.grid(row=2, column=1, **opts_obj)

        self.btn_save.grid(row=3, column=0, columnspan=2, pady=(30,),
                                                        sticky=tk.SE)

        self.cmb_opt1.focus_set()

    def validate_ent_opt3(self, event=None):
        if len(self.var_op3.get()) > 10:
            self.var_op3.set(self.var_op3.get()[:-1])

    def click_btn_save(self, event=None):
        self.data_out = dict(var_op1=self.var_op1.get(),
                            var_op2=self.var_op2.get(),
                            var_op3=self.var_op3.get())
        self.destroy()
        return "break"


if __name__ == "__main__":
    # Testing...

    root = tk.Tk()
    conf = Config(master=root, data_in=None, widget_width=260)
    conf.show()
    root.mainloop()