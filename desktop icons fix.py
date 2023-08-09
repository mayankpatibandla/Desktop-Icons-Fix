import os
import shutil

# Move shortcuts from public to user desktop

publicDesktop = os.path.join(os.environ['PUBLIC'], 'Desktop')
userDesktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')

for f in os.listdir(publicDesktop):
    if os.path.splitext(f)[1] == '.lnk':
        try:
            shutil.move(os.path.join(publicDesktop, f), userDesktop)
        except shutil.Error:
            pass

# Delete cache db files

dbFiles = [os.path.join(os.environ['LOCALAPPDATA'], 'IconCache.db')]

cacheDirectory = os.path.join(
    os.environ['LOCALAPPDATA'], 'Microsoft\Windows\Explorer')

for f in os.listdir(cacheDirectory):
    if os.path.splitext(f)[1] == '.db':
        dbFiles.append(os.path.join(cacheDirectory, f))

for f in dbFiles:
    if (os.path.exists(f)):
        try:
            os.remove(f)
        except PermissionError:
            pass

# Restart explorer.exe

os.system("taskkill /f /IM explorer.exe")
os.system("start explorer.exe")
