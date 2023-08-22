# ⚠️No more updates will be provided to this installer. The JSON file should still stay up-to-date though.⚠️

# RCOInstaller

## ⚠️I DID NOT MAKE RCO⚠️

This is only an alternative client to auto-install RCO. If you would like to use the original RCO installer, please visit [https://github.com/L8X/Roblox-Client-Optimizer]()! Don't submit issues about the optimization here, submit those to the [RCO discord server](https://roblox-client-optimizer.simulhost.com/discord)!

# About

Yet another RCO installer. This one is a fork of ShashTheEpic's RCO-Auto-Installer, which does most of what I wanted the original RCO installer to do except a few things which I added to this project. **THIS PROJECT IS WINDOWS-ONLY!!**

# Features

* Get the latest version of RCO installed to the proper folder, hassle-free.
* Automatically run the program when you start your computer
* Super simple. Run the application once and it's all installed.
* doodoo code written by yours truly

# How to compile

If you have tried running RCOInstaller's python file without compiling, you might've seen a notice (if you are on 1.2 or later) about how you need to compile the program for it to work properly. Here's how to do that.

Firstly, install [git](https://git-scm.com/). Once that's installed, clone the repository using the following command in your terminal.

```
git clone https://github.com/hdboye/RCOInstaller.git
```

Make sure to `cd` to the place you'd like to clone the folder to. You can also [click here](https://github.com/hdboye/RCOInstaller/archive/refs/heads/main.zip) to download and unzip the code manually. Once that's done, run the command `cd RCOInstaller` (or `cd RCOInstaller-main` if you downloaded the code from the site) to access the files in the folder.

Now, install [Python](https://www.python.org/downloads/) (any version should work, but RCOInstaller was made and tested on 3.10.7). Once that's installed, go back to the terminal and run this command to install the dependencies this project uses

```
pip install winshell pyinstaller
```

Once that's finished, run this command.

```
pyinstaller RCOI.pyw --onefile --icon=rbx.ico
```

You can remove the `--onefile` parameter if you don't want it to compile to a single exe and the whole `--icon=rbx.ico` parameter if you want the exe to have a standard PyInstaller icon.

Once that's finished compiling (it might take a small while), you'll have a `dist` folder located in the `RCOInstaller` folder where your compiled EXE will be located.

# FAQ

### Why does this exist?

I never really liked the original RCO installer, mainly because it never seemed to work for me. I don't know if anyone else experienced problems with it but I just found it confusing to use and it didn't put the json file into the folder most of the time. I sought out to make an alternative installer, and RCO-Auto-Installer was a perfect base for it.

### What's the difference between RCO2/RCO3 and RCOInstaller?

It installs the same json files, I just made RCOInstaller to greatly simplify the process.

### How do I use this?

Download the EXE file from [the releases tab](https://github.com/hdboye/RCOInstaller/releases/latest). Open the EXE file. Enjoy.

### My Roblox just updated and the optimizations don't work anymore.

Open the file again, or restart your computer. The first one should be easier though.

### How do I uninstall RCO using RCOInstaller?

Uninstallation is a bit trickier for now. Type `%localappdata%\Roblox\Versions` in the search bar of your pc, then check both folders for a folder called ClientSettings. If you see a folder called ClientSettings, open it and delete the json file that's in there.

# Credits

* [L8X](https://github.com/L8X) and [everyone who contributed to RCO](https://github.com/L8X/Roblox-Client-Optimizer/graphs/contributors) for their [amazing client optimizer project](https://github.com/L8X/Roblox-Client-Optimizer). Huge kudos to them!
* [ShashTheEpic](https://github.com/ShashTheEpic) for writing the base to this in their [RCO-Auto-Installer](https://github.com/ShashTheEpic/RCO-Auto-Installer) project!
