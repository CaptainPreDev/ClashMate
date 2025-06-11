import subprocess, time, numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

DEVICE_ID   = "emulator-5554"
TARGET_FPS  = 60
FRAME_TIME  = 1.0 / TARGET_FPS

def adb_screencap(device_id: str) -> np.ndarray | None:
    result = subprocess.run(
        ["adb", "-s", device_id, "exec-out", "screencap", "-p"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode:
        print("ADB error:", result.stderr.decode().strip())
        return None
    try:
        img = Image.open(BytesIO(result.stdout))
        return np.asarray(img)
    except Exception as e:
        print("Decode error:", e)
        return None

def main():
    print(f"Streaming from {DEVICE_ID} at ~15 FPS. Close the window to stop.")
    plt.ion()
    fig, ax = plt.subplots()
    im = ax.imshow(np.zeros((100,100,3), dtype=np.uint8))  # placeholder
    fig.canvas.manager.set_window_title('Live Feed')
    
    while True:
        t0 = time.time()
        frame = adb_screencap(DEVICE_ID)
        if frame is not None:
            im.set_data(frame)
            plt.draw()
            plt.pause(0.001)  # allow GUI to update

        if not plt.fignum_exists(fig.number):
            break  # Exit if window is closed

        elapsed = time.time() - t0
        if elapsed < FRAME_TIME:
            time.sleep(FRAME_TIME - elapsed)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
