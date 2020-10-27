#!/usr/bin/env python3
import os
import resource
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from views.toolbar import ToolBar
from views.statusbar import StatusBar
from views.screen import Screen
from views.config import Config
from views.help import Help
from utils.chronometer import Chronometer
from utils.threadtrace import ThreadTrace

APP_NAME      = "My Application"
WIDGET_WIDTH  = 700
WIDGET_HEIGHT = None

class Main(tk.Tk):

    __IMG_PATH = "views{sep}images{sep}".format(sep=os.sep)

    def __init__(self, app_name, widget_width, widget_height=None):
        super().__init__()
        self.app_name = app_name

        if not widget_height:
            phi           = (1 + 5**0.5)/2
            widget_height = int(widget_width/phi)

        screen_width    = self.winfo_screenwidth()
        screen_height   = self.winfo_screenheight()
        screen_x_center = int((screen_width  - widget_width) / 2)
        screen_y_center = int((screen_height - widget_height) / 2)
        self.title(self.app_name)
        self.geometry("{}x{}+{}+{}".format(widget_width, widget_height,
                                            screen_x_center, screen_y_center))
        self.resizable(True, True)

        appicon = tk.PhotoImage(file=self.__IMG_PATH+"python24x24.png")
        self.iconphoto(False, appicon)
        self.option_add("*font", "TkDefaultFont 13 normal")

        # +------------- YOUR CONFIG HERE -----------+
        self.config = dict(var_op1="< select >", var_op2="5", var_op3="data")
        # +------------------------------------------+

        self.create_vars()
        self.create_widgets()
        self.create_binding()
        self.create_packing()
        self.mainloop()

    def create_vars(self):
         pass

    def create_widgets(self):
        self.toolbar   = ToolBar(self)
        self.screen    = Screen(self)
        self.statusbar = StatusBar(self)
        self.statusbar.text("Ready to Run.")
        self.toolbar.btn_stop.config(state="disabled")
        self.toolbar.btn_save.config(state="disabled")

    def create_binding(self):
        self.bind("<Control-c>", self.click_config)
        self.bind("<Control-C>", self.click_config)
        self.bind("<Control-r>", self.click_run)
        self.bind("<Control-R>", self.click_run)
        self.bind("<F1>",        self.click_help)
        self.bind("<Escape>",    self.click_exit)
        self.protocol("WM_DELETE_WINDOW", self.click_exit)

        self.toolbar.btn_conf.config(command=self.click_config)
        self.toolbar.btn_run.config(command=self.click_run)
        self.toolbar.btn_stop.config(command=self.click_stop)
        self.toolbar.btn_save.config(command=self.click_save)
        self.toolbar.btn_help.config(command=self.click_help)
        self.toolbar.btn_exit.config(command=self.click_exit)

    def create_packing(self):
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        self.screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def click_config(self, event=None):
        config      = Config(self, data_in=self.config, widget_width=280)
        config      = config.show()
        self.config = self.config if not config else config
        return "break"

    def click_run(self, event=None):
        self.toolbar.btn_conf.config(state="disabled")
        self.toolbar.btn_run.config(state="disabled")
        self.toolbar.btn_stop.config(state="normal")
        self.toolbar.btn_save.config(state="disabled")

        self.bind("<Control-s>", self.click_stop)
        self.bind("<Control-S>", self.click_stop)
        self.unbind("<Control-c>")
        self.unbind("<Control-C>")
        self.unbind("<Control-r>")
        self.unbind("<Control-R>")

        self.chrono = Chronometer()
        self.chrono.init()
        self.screen.clear()
        self.__stoped = False

        self.thr_code      = ThreadTrace(target=self.__run_code, daemon=True)
        self.thr_statusbar = ThreadTrace(target=self.__update_statusbar,
                                                                 daemon=True)
        self.thr_code.start()
        self.thr_statusbar.start()

        return "break"

    # USE self.config
    def __run_code(self):
    # +------------- YOUR CODE HERE -------------+
        import code
        code.run(echo=self.screen.print, **self.config)
    # +------------------------------------------+
        self.__post_run_update()

    def __update_statusbar(self):
        while not self.__stoped:
            self.statusbar.text("Running.  Time: {}  Memory: {} KB."\
                .format(self.chrono.time, resource.getpagesize()/1024))

    def __post_run_update(self):
        self.__stoped = True

        self.toolbar.btn_conf.config(state="normal")
        self.toolbar.btn_run.config(state="normal")
        self.toolbar.btn_stop.config(state="disabled")
        self.toolbar.btn_save.config(state="normal")
        self.statusbar.text("End.  Time: {}  Memory: {} KB."\
            .format(self.chrono.time, resource.getpagesize()/1024))

        self.unbind("<Control-s>")
        self.unbind("<Control-S>")
        self.bind("<Control-c>", self.click_config)
        self.bind("<Control-C>", self.click_config)
        self.bind("<Control-r>", self.click_run)
        self.bind("<Control-R>", self.click_run)
        self.bind("<Control-a>", self.click_save)
        self.bind("<Control-A>", self.click_save)

    def click_stop(self, event=None):
        self.__stoped = True
        self.chrono.stop()
        try:
            self.thr_code.kill()
            self.thr_code.join()
        except AttributeError:
            pass

        self.toolbar.btn_conf.config(state="normal")
        self.toolbar.btn_run.config(state="normal")
        self.toolbar.btn_stop.config(state="disabled")
        self.toolbar.btn_save.config(state="normal")
        self.statusbar.text("Stopped.  Time {}  Memory {} KB."\
            .format(self.chrono.time, resource.getpagesize()/1024))

        self.unbind("<Control-s>")
        self.unbind("<Control-S>")
        self.bind("<Control-c>", self.click_config)
        self.bind("<Control-C>", self.click_config)
        self.bind("<Control-r>", self.click_run)
        self.bind("<Control-R>", self.click_run)
        self.bind("<Control-a>", self.click_save)
        self.bind("<Control-A>", self.click_save)

        return "break"

    def click_save(self, event=None):
        file = filedialog.asksaveasfilename(parent=self, title="Save Run.",
                filetypes=[("Run Files", "*.txt")], defaultextension=".txt", 
                initialdir="runs{}".format(os.sep))
        if file:
            open(file, "w").write(self.screen.get_content)
        return "break"

    def click_help(self, event=None):
        Help(self, data_in=None, widget_width=500).show()
        return "break"

    def click_exit(self, event=None):
        self.click_stop()
        self.quit()
        return "break"

if __name__ == "__main__":

    Main(APP_NAME, WIDGET_WIDTH, WIDGET_HEIGHT)