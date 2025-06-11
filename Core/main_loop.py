from Profiles import globals
import time
from Profiles import globals
from Core.Functions.logging import *

def bot_logic():
    while not globals.stop_game_loop.is_set():
            log_success("Bot HOORAY!")
            log_normal("Bot HOORAY!")
            log_failure("Bot HOORAY!")
            time.sleep(0.2)
    globals.bot_thread = None