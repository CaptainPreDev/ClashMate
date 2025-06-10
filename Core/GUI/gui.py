# gui_window.py
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def launch_gui():
    app = ttk.Window(
        title="ClashMate - An Open Source COC Bot", 
        themename="darkly", 
        size=(500, 750)
    )
    app.resizable(False, False)

    label = ttk.Label(app, text="Welcome to ClashMate!", font=("Segoe UI", 16))
    label.pack(pady=20)

    app.mainloop()