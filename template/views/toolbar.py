#!/usr/bin/env python3
import os
import tkinter as tk
from tooltip import CreateToolTip

class ToolBar(tk.Frame):

    __IMG_PATH = "views{sep}images{sep}".format(sep=os.sep)

    def __init__(self, parent):
        super().__init__(parent, relief=tk.RAISED, bd=2, bg="#E5E5E5")

        self.create_vars()
        self.create_widgets()
        self.create_binding()
        self.create_packing()

    def create_vars(self):
        pass

    def create_widgets(self):
        self.icon_conf = tk.PhotoImage(file=self.__IMG_PATH+"options24x24.png")
        self.icon_run  = tk.PhotoImage(file=self.__IMG_PATH+"run24x24.png")
        self.icon_stop = tk.PhotoImage(file=self.__IMG_PATH+"stop24x24.png")
        self.icon_help = tk.PhotoImage(file=self.__IMG_PATH+"help24x24.png")
        self.icon_exit = tk.PhotoImage(file=self.__IMG_PATH+"quit24x24.png")

        self.btn_conf  = tk.Button(self, image=self.icon_conf)
        self.btn_run   = tk.Button(self, image=self.icon_run)
        self.btn_stop  = tk.Button(self, image=self.icon_stop,
                                                            state=tk.DISABLED)
        self.btn_help  = tk.Button(self, image=self.icon_help)
        self.btn_exit  = tk.Button(self, image=self.icon_exit)

        CreateToolTip(self.btn_conf, "Configuration.\nCtrl + C")
        CreateToolTip(self.btn_run,  "Run Code.\nCtrl + R")
        CreateToolTip(self.btn_stop, "Stop Running.\nCtrl + S")
        CreateToolTip(self.btn_help, "Show Help.\nF1")
        CreateToolTip(self.btn_exit, "Stop and Exit.\nEsc")

    def create_binding(self):
        pass

    def create_packing(self):
        self.btn_conf.pack(side=tk.LEFT, padx=(7, 3), pady=1)
        self.btn_run.pack(side=tk.LEFT, padx=3, pady=1)
        self.btn_stop.pack(side=tk.LEFT, padx=3, pady=1)
        self.btn_help.pack(side=tk.LEFT, padx=3, pady=1)
        self.btn_exit.pack(side=tk.LEFT, padx=3, pady=1)


if __name__ == "__main__":
    # Testing ...

    root = tk.Tk()
    tb   = ToolBar(parent=root)

    tb.pack(side=tk.TOP, fill=tk.X)
    root.mainloop()