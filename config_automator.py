import os
import subprocess

#Prompt for map nickname and id
id = input("What is the workshop id for the map you want to add?")

#Place ID in Steamworks
with open('KFGame/Config/LinuxServer-KFEngine.ini','r+') as file:
    line_list = []
    for line in file:
        line_list.append(line)
    file.seek(0)
    steamworks_present = False
    for entry in line_list:
        if entry.startswith("[OnlineSubsystemSteamworks.KFWorkshopSteamworks]"):
            steamworks_present = True
            entry = entry + "ServerSubscribedWorkshopItems=" + id + "\n"
        file.write(entry)
    if not steamworks_present:
        entry = "[OnlineSubsystemSteamworks.KFWorkshopSteamworks]\n" + "ServerSubscribedWorkshopItems=" + id + "\n"
        file.write(entry)

# Call startstop
subprocess.call("./startstop.sh")

# Grab file name
for root, dirs, files, rootfd in os.fwalk('KFGame/Cache/' + id):
    filelist = files
map = filelist.pop()[:-4]

# Data Store Prototype
with open('KFGame/Config/LinuxServer-KFGame.ini','r+') as file:
    line_list = []
    for line in file:
        line_list.append(line)
    file.seek(0)
    for entry in line_list:
        if entry.startswith("[KF-Default KFMapSummary]"):
            entry = map + " KFMapSummary]\nMapName=" + map + "\nMapAssociation=0\nScreenshotPathName=UI_MapPreview_TEX.UI_MapPreview_Placeholder\n\n" + entry
        file.write(entry)

# #Add map to map cycle
with open('KFGame/Config/LinuxServer-KFGame.ini','r+') as file:
    line_list = []
    for line in file:
        line_list.append(line)
    file.seek(0)
    for entry in line_list:
        if entry.startswith("GameMapCycles"):
            entry = entry[:-3] + ',"' + map + '"' + entry[-3:]
        file.write(entry)

