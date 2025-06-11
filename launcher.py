import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext
from Profiles import globals
import threading
import queue
from Core.main_loop import bot_logic

def launch_gui():
    global app, log_area, start_button, stop_button

    app = ttk.Window(
        title="ClashMate - An Open Source COC Bot",
        themename="darkly",
        size=(500, 750)
    )
    app.resizable(False, False)

    label = ttk.Label(app, text="Welcome to ClashMate!", font=("Segoe UI", 16))
    label.pack(pady=20)

    # Scrollable text area
    log_area = scrolledtext.ScrolledText(app, wrap='word', height=30, font=("Consolas", 10))
    log_area.pack(fill='both', padx=15, pady=10, expand=True)
    log_area.config(state='disabled')

    # Tag configs
    log_area.tag_configure("success", foreground="lime")
    log_area.tag_configure("normal", foreground="white")
    log_area.tag_configure("failure", foreground="red")

    # Buttons
    btn_frame = ttk.Frame(app)
    btn_frame.pack(pady=20)

    start_button = ttk.Button(btn_frame, text="Start", bootstyle="success",command=on_start)
    start_button.pack(side="left", padx=10)

    stop_button = ttk.Button(btn_frame, text="Stop", bootstyle="danger",command=on_stop)
    stop_button.pack(side="left", padx=10)

    app.after(100, process_log_queue)
    app.mainloop()

def on_start():
    if globals.bot_thread and globals.bot_thread.is_alive():
        return
    globals.stop_game_loop.clear()
    globals.bot_thread = threading.Thread(target=bot_logic, daemon=True)
    globals.bot_thread.start()

def on_stop():
        globals.stop_game_loop.set()

def process_log_queue():
    try:
        while True:
            tag, msg = globals.log_queue.get_nowait()

            autoscroll = log_area.yview()[1] >= 0.95

            log_area.config(state='normal')
            log_area.insert('end', f"{msg}\n", tag)
            if autoscroll:
                log_area.see('end')  # only scroll if you were already at the bottom
            log_area.config(state='disabled')
    except queue.Empty:
        pass
    app.after(100, process_log_queue)

launch_gui()