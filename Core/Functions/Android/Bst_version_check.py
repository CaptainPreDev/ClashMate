def read_bluestacks_version():
    keys_to_check = [
        r"SOFTWARE\BlueStacks_nxt",
        r"SOFTWARE\WOW6432Node\BlueStacks_nxt"  # fallback for 32-bit apps on 64-bit Windows
    ]

    for subkey in keys_to_check:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey)
            value, regtype = winreg.QueryValueEx(key, "Version")
            winreg.CloseKey(key)
            return value
        
        except Exception as e:
            print(f"Error accessing {subkey}: {e}")
    
    return "Version not found"

version = read_bluestacks_version()
print("BlueStacks Version:", version)