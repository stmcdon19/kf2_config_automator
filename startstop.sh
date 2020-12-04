#!/bin/bash

#Start server
./Binaries/Win64/KFGameSteamServer.bin.x86_64 &

#Grab PID of server running
PID=$!

#Allow 1 minute for map download
sleep 60

#Kill the server
kill $PID