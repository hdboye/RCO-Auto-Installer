# Modules required for this to function
import requests
import json
import os
import glob
import sys
import winshell
import shutil
import ctypes

def show_popup(message, title):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)

# Obtains latest URL
RCOu_url = "https://hdboye.github.io/curRCO/cur.txt"
RCOu = requests.get(RCOu_url,headers={'Cache-Control': 'no-cache'})
RCOu_text = RCOu.text.strip()
if(RCOu.text == "xxx"):
    show_popup('We\'re sorry, there is currently no reliable source to get RCO from. Please check back later!', 'No reliable source')
    sys.exit()

# Obtains latest version of ClientAppSettings.json
RCO = requests.get(RCOu_text)
print(RCO.text)

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
    json.dump(json.loads(RCO.text), f, indent=0)

# Informs user that RCO has been updated/installed and the directory
print("New data has been written to", RobloxClientSettingsDir)

# Auto-startup stuff (im not good at comments)
try:
    path = winshell.startup()
    try:
        shutil.copy2(os.path.realpath(sys.executable),path)
    except:
        print('ok nvm')
    show_popup('RCO is now up-to-date! Enjoy!', 'Success!')
except OSError as err:
    show_popup('An error has occured. Please report this to the github. ' + err, 'whoops')