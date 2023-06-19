
import os
import winreg

def registry_analysis(key_path):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        print("\nRegistry Key: ", key_path)
        for i in range(0, winreg.QueryInfoKey(key)[1]):
            value = winreg.EnumValue(key, i)
            print(value[0], ":", value[1])
        winreg.CloseKey(key)
    except WindowsError:
        print("Cannot access the key")

if __name__ == "__main__":
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    registry_analysis(key_path)
