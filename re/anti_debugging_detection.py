
import ctypes

def anti_debugging_detection():
    try:
        ctypes.windll.kernel32.IsDebuggerPresent()
    except Exception:
        print("Debugger detected!")
        return True
    else:
        print("No debugger detected.")
        return False

if __name__ == "__main__":
    anti_debugging_detection()
