# Modules required for this to function
import requests
import json
import os
import glob
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
def is_pyinstaller():
    try:
        return getattr(sys, 'frozen', False)
    except AttributeError:
        return False
try:
    path = winshell.startup()
    try:
        shutil.copy2('./RCOI.exe',path)
    except:
        print('ok nvm')
    show_popup('RCO is now up-to-date! Enjoy!', 'Success!')
except OSError as err:
    show_popup('An error has occured. Please report this to the github. ' + err, 'whoops')