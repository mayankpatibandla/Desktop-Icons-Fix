"""
desktop_icons_fix.py

This script is used to fix issues related to desktop icons on Windows. It
performs the following tasks:

1. Moves shortcuts from the public desktop to the user's desktop.
2. Deletes cache database files associated with desktop icons.
3. Restarts the Windows Explorer process to apply changes.

Usage:
    - Simply run the application to automatically fix your desktop icons.

Note:
    - The script was designed for Windows 10, but it should also work on
      Windows 11.

Disclaimer:
    - Use this script at your own risk. It performs file operations and system
      process restarts, which could potentially cause unintended consequences.

"""

import os
import shutil

# Move shortcuts from public to user desktop

publicDesktop = os.path.join(os.environ["PUBLIC"], "Desktop")
userDesktop = os.path.join(os.environ["USERPROFILE"], "Desktop")

shortcutExtensions = [".lnk", ".url"]

for f in os.listdir(publicDesktop):
    if os.path.splitext(f)[1] in shortcutExtensions:
        try:
            shutil.move(os.path.join(publicDesktop, f), userDesktop)
        except shutil.Error:
            pass

# Delete cache db files

dbFiles = [os.path.join(os.environ["LOCALAPPDATA"], "IconCache.db")]

cacheDirectory = os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\Windows\Explorer")

for f in os.listdir(cacheDirectory):
    if os.path.splitext(f)[1] == ".db":
        dbFiles.append(os.path.join(cacheDirectory, f))

for f in dbFiles:
    if os.path.exists(f):
        try:
            os.remove(f)
        except PermissionError:
            pass

# Restart explorer.exe

os.system("taskkill /f /IM explorer.exe")
os.system("start explorer.exe")
