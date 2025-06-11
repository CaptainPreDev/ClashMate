from Profiles import globals
from datetime import datetime

def _format_msg(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    return f"[{timestamp}] {msg}"

def log_success(msg):
    globals.log_queue.put(("success", _format_msg(msg)))

def log_failure(msg):
    globals.log_queue.put(("failure", _format_msg(msg)))

def log_normal(msg):
    globals.log_queue.put(("normal", _format_msg(msg)))
