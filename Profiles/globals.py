import threading, queue

stop_game_loop  = threading.Event()  # tell the worker to exit
log_queue   = queue.Queue()      # messages → GUI
bot_thread  = None               # handle to the worker thread
log_queue = queue.Queue()
