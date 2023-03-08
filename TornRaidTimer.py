import sys
import os

def execute():
    os.system('cls')
    counter = 0
    while True:
        counter = counter + 1
        if int(counter) > int(slots):
            print ("Restart? (Yes/No)")
            r1 = input("<  ")
            if r1 == "Y" or r1 == "Yes" or r1 == "y" or r1 == "yes":
                datacollect()
            else:
                menu()
        else:
            pass
        hours = int(points)/(int(counter)*3600)
        minutes = (hours % 1)*60
        seconds = (minutes % 1)*60
        print ("{} player(s) will take the territory in {} hours {} minutes and {} seconds.".format(int(counter), int(hours // 1), int(minutes // 1), int(seconds // 1)))
        continue

def datacollect():
    global points
    global slots
    os.system('cls')
    print("")
    print("Enter current amount of respect of the territory:")
    points = input("<  ")
    print ("Enter the amount of slots of the territory:")
    slots = input("<  ")
    execute()

def helpscreen():
    os.system('cls')
    print("")
    print("This is a simple script that helps you calculate the amount of time that will be needed to take a territory in Torn.")

def menu():
    print("   ")
    print(".1   START   1.")
    print(".2   HELP    2.")
    print("")
    print("    .......")
    menuchoice = input("<  ")
    if menuchoice == "1" or menuchoice == "start" or menuchoice == "Start" or menuchoice == "START":
        datacollect()
    elif menuchoice == "2" or menuchoice == "help" or menuchoice == "Help" or menuchoice == "HELP":
        helpscreen()
    else:
        exit()

menu()