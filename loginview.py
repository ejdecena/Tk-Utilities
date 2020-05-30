#!/usr/bin/env python3
"""Tk Utilities."""
import tkinter as tk
import tkinter.ttk as ttk


class LoginView(tk.Tk):
    """It is a class that implements a login type form.

    Args:
        widget_width: width of the form.
        widget_height: height of the form. If it is not provided, it is calculated according to the golden number (Phi).

    Attributes:
        username: user name entered by the user.
        password: password entered by the user.

    Class Attributes:
        LEN_USERNAME: length of characters in the username field.
        LEN_PASSWORD: length of characters in the password field.

    Use:
        login = LoginView(widget_width=252)
        print("Username:", login.username)
        print("Password:", login.password)
    """

    LEN_USERNAME = 14
    LEN_PASSWORD = 14

    def __init__(self, widget_width, widget_height=None):
        super().__init__()
        if not widget_height:
            phi           = (1 + 5**0.5)/2
            widget_height = int(widget_width/phi)
        screen_width    = self.winfo_screenwidth()
        screen_height   = self.winfo_screenheight()
        screen_x_center = int((screen_width  - widget_width) / 2)
        screen_y_center = int((screen_height - widget_height) / 2)
        self.title("Login.")
        self.geometry("{}x{}+{}+{}".format(widget_width, widget_height,
                                            screen_x_center, screen_y_center))
        self.resizable(False, False)
        self.option_add("*font", "TkDefaultFont 12 normal")
        ttk.Style().configure("TButton", font="TkDefaultFont 12 normal")

        self.create_vars()
        self.create_widgets()
        self.create_binding()
        self.create_packing()

        self.bell()
        self.ent_username.focus_set()
        self.mainloop()

    def create_vars(self):
        self.var_username = tk.StringVar()
        self.var_password = tk.StringVar()

    def create_widgets(self):
        self.frame = ttk.Frame(self)

        vcmd   = (self.register(self.validate_entries), "%W", "%P")
        invcmd = (self.register(self.invalid_entries), "%W", "%P")
        self.ent_username = ttk.Entry(self.frame, width=19, validate="key",
                                      validatecommand=vcmd, name="username",
                                      invalidcommand=invcmd,
                                      textvariable=self.var_username)
        self.ent_password = ttk.Entry(self.frame, show="*", validate="key",
                                      width=19, validatecommand=vcmd,
                                      name="password", invalidcommand=invcmd,
                                      textvariable=self.var_password)

        self.btn_cancel   = ttk.Button(self, text="Cancel", underline=0,
                                        command=self.on_wm_delete_window)
        self.btn_login    = ttk.Button(self, text="Login", underline=0,
                                        command=self.on_login_clicked,
                                        state=tk.DISABLED)
    def create_binding(self):
        self.protocol("WM_DELETE_WINDOW", self.on_wm_delete_window)
        self.bind("<Alt-u>", lambda event: self.ent_username.focus_set())
        self.bind("<Alt-p>", lambda event: self.ent_password.focus_set())
        self.bind("<Alt-c>", lambda event: self.btn_cancel.focus_set())
        self.bind("<Alt-l>", lambda event: self.btn_login.focus_set())
        self.bind("<Return>", self.on_login_clicked)
        self.bind("<Escape>", self.on_wm_delete_window)
        self.var_username.trace("w", lambda *args: self.on_entry_change())
        self.var_password.trace("w", lambda *args: self.on_entry_change())

    def create_packing(self):
        lbl_opts = dict(sticky=tk.NE, padx=5, pady=2)
        ent_opts = dict(sticky=tk.NW, pady=2)
        self.frame.pack(padx=5, pady=5)
        ttk.Label(self.frame, text="Username:",underline=0)\
                 .grid(row=0, column=0, **lbl_opts)
        ttk.Label(self.frame, text="Password:",underline=0)\
                 .grid(row=1, column=0, **lbl_opts)
        self.ent_username.grid(row=0, column=1, **ent_opts)
        self.ent_password.grid(row=1, column=1, **ent_opts)
        self.btn_cancel.pack(side=tk.LEFT, padx=10)
        self.btn_login.pack(side=tk.RIGHT, padx=10)

    def validate_entries(self, W, P):
        widget = W.split(".")[-1]
        if widget == "username":
            len_entry = LoginView.LEN_USERNAME
        elif widget == "password":
            len_entry = LoginView.LEN_PASSWORD
        else:
            raise ValueError("Invalid widget name.")
        return len(P) <= len_entry

    def invalid_entries(self, W, P):
        widget = W.split(".")[-1]
        if widget == "username":
            self.var_username.set(P[:-1])
        elif widget == "password":
            self.var_password.set(P[:-1])
        else:
            raise ValueError("Invalid widget name.")

    def on_entry_change(self, event=None):
        username = self.var_username.get()
        password = self.var_password.get()
        if username.strip() and password.strip():
            self.btn_login["state"] = tk.NORMAL
        else:
            self.btn_login["state"] = tk.DISABLED
        return "break"

    def on_login_clicked(self, event=None):
        if str(self.btn_login["state"]) == tk.NORMAL:
            self.quit()
        return "break"

    def on_wm_delete_window(self, event=None):
        exit()

    @property
    def username(self):
        return self.var_username.get()

    @property
    def password(self):
        return self.var_password.get()


if __name__ == "__main__":
    # Testing ...

    login = LoginView(widget_width=252)
    print("Username:", login.username)
    print("Password:", login.password)