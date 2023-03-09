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
        days = int(points)/(int(counter)*86400)
        hours = (days % 1)*24
        minutes = (hours % 1)*60
        seconds = (minutes % 1)*60
        if counter == 1:
            print (" {} player     ...   {} day(s) {} hour(s) {} minute(s) and {} second(s).".format(int(counter), int(days // 1), int(hours // 1), int(minutes // 1), int(seconds // 1)))
            continue
        elif counter < 10 and counter > 1:
            print (" {} players    ...   {} day(s) {} hour(s) {} minute(s) and {} second(s).".format(int(counter), int(days // 1), int(hours // 1), int(minutes // 1), int(seconds // 1)))
            continue
        elif counter > 10:
            print (" {} players   ...   {} day(s) {} hour(s) {} minute(s) and {} second(s).".format(int(counter), int(days // 1), int(hours // 1), int(minutes // 1), int(seconds // 1)))
            continue

def datacollect():
    global points
    global slots
    os.system('cls')
    print("")
    print("Enter the total amount of points of the territory:")
    total = input("<  ")
    if int(total) < 0:
        datacollect()
    else:
        pass
    print("Enter the amount of points of the territory that is already taken:")
    taken = input("<  ")
    if int(total) <= int(taken) or int(taken) < 0:
        datacollect()
    else:
        pass
    points = int(total) - int(taken)
    print ("Enter the amount of slots of the territory:")
    slots = input("<  ")
    if int(slots) <= 0:
        datacollect()
    else:
        pass
    execute()

def helpscreen():
    os.system('cls')
    print("")
    print("This is a simple script that helps you calculate the amount of time that will be needed to take a territory in Torn.")
    print("")
    print("Type anything to go back")
    goback = input("<  ")
    if goback == " ":
        menu()
    else:
        menu()

def menu():
    os.system('cls')
    print("                                                  ")
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