# Modules required for this to function
import requests
import json
import os
import glob
import winreg
import sys
import winshell
import shutil
import ctypes

# Obtains latest version of ClientAppSettings.json
RCO_url = "https://roblox-client-optimizer.simulhost.com/ClientAppSettings.json"
RCO = requests.get(RCO_url)
RCO_text = RCO.text

# Finds the directory to RCO
user = os.getlogin()
RobloxVersionDir = rf"C:\Users\{user}\AppData\Local\Roblox\Versions"
LatestRobloxVersionDir = max(glob.glob(os.path.join(RobloxVersionDir, "version-*")), key=os.path.getmtime)
RobloxClientSettingsDir = os.path.join(LatestRobloxVersionDir, "ClientSettings", "ClientAppSettings.json")

# If RCO isn't installed, it will be installed
if not os.path.exists(os.path.dirname(RobloxClientSettingsDir)):
    os.makedirs(os.path.dirname(RobloxClientSettingsDir))

# Latest version of RCO writes/overwrites current ClientAppSettings.json
with open(RobloxClientSettingsDir, "w") as f: 
    json.dump(json.loads(RCO_text), f, indent=0)

# Informs user that RCO has been updated/installed and the directory
print("New data has been written to", RobloxClientSettingsDir)

# Auto-startup stuff (im not good at comments)
def show_popup(message, title):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)
def create_key(name: str="default", path: str="")->bool:
    reg_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_WRITE) 
    if not reg_key:
        return False
    winreg.SetValueEx(reg_key, name,0,winreg.REG_SZ,path) 
    reg_key.Close()
    return True
def is_pyinstaller():
    try:
        return getattr(sys, 'frozen', False)
    except AttributeError:
        return False
try:
    path = winshell.startup()
    shutil.copy2('./RCOI.exe',path)
    create_key('RCOInstaller', os.path.join(path,'RCOI.exe'))
    show_popup('RCO is now up-to-date! Enjoy!', 'Success!')
except OSError as err:
    show_popup('An error has occured. Please report this to the github. ' + err, 'whoops')