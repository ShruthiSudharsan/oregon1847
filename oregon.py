userInput = raw_input("DO YOU NEED INSTRUCTIONS (YES/NO)? ")

instructions = """
THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM
INDEPENDENCE, MISSOURI TO OREGON CITY, OREGON 1847.
YOUR FAMILY OF FIVE WILL COVER THE 2040 MILE OREGON TRAIL
IN 5-6 MONTHS --- IF YOU MAKE IT ALIVE.

YOU HAD SAVED $900 TO SPEND FOR THE TRIP, AND YOU'VE JUST
PAID $200 FOR A WAGON. YOU WILL NEED TO SPEND THE REST OF
YOUR MONEY ON THE FOLLOWING ITEMS:

    OXEN - YOU CAN SPEND $200-$300 ON YOUR TEAM THE MORE
    YOU SPEND, THE FASTER YOU'LL GO BECAUSE YOU'LL HAVE
    BETTER ANIMALS.

    FOOD - THE MORE YOU HAVE, THE LESS CHANCE THERE IS OF
    GETTING SICK.

    AMMUNITION - $1 BUYS A BELT OF 50 BULLETS. YOU WILL
    NEED BULLETS FOR ATTACKS BY ANIMALS AND BANDITS, AND
    FOR HUNTING FOOD.

    CLOTHING - THIS IS ESPECIALLY IMPORTANT FOR THE COLD
    WEATHER YOU WILL ENCOUNTER WHEN CROSSING THE
    MOUNTAINS.

    MISCELLANEOUS SUPPLIES - THIS INCLUDES MEDICINE AND
    OTHER THINGS YOU WILL NEED FOR SICKNESS AND EMERGENCY
    REPAIRS.

YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -
OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG
THE WAY WHEN YOU RUN LOW. HOWEVER, ITEMS COST MORE AT
THE FORTS. YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET
MORE FOOD.

WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,
YOU WILL BE TOLD TO TYPE IN A WORD (ONE THAT SOUNDS LIKE A
GUN SHOT). THE FAST YOU TYPE IN THAT WORD AND HIT THE
"RETURN" KEY, THE BETTER LUCK YOU'LL HAVE WITH YOUR GUN.

AT EACH TURN, ALL ITEMS ARE SHOWN IN DOLLAR AMOUNTS EXCEPT
BULLETS. WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A
"$". GOOD LUCK!!!
"""

if userInput == "YES" or userInput == "Yes" or userInput == "yes":
    print(instructions)
    raw_input("PRESS <ENTER> TO CONTINUE") # pause until user presses enter

# SELECT HUNTING DIFFICULTY LEVEL
print("")
print("HOW GOOD A SHOT ARE YOU WITH YOUR RIFLE?")
print("")
print("    (1) ACE MARKSMAN")
print("    (2) GOOD SHOT")
print("    (3) FAIR TO MIDDLIN'")
print("    (4) NEED MORE PRACTICE")
print("    (5) SHAKY KNEES")
print("")
print("ENTER ONE OF THE ABOVE -- THE BETTER YOU CLAIM YOU ARE, THE")
print("FASTER YOU'LL HAVE TO BE WITH YOUR GUN TO BE SUCCESSFUL.")
shootingExpertiseLevel = raw_input("? ")
print("")

# ENTER EXPENDITURES
expendituresEntered = False
while expendituresEntered == False:
    # prompt user to enter expenditure amounts
    amountSpentOnOxen = raw_input("HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM? ")
    amountSpentOnFood = raw_input("HOW MUCH DO YOU WANT TO SPEND ON FOOD? ")
    amountSpentOnAmmunition = raw_input("HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION? ")
    amountSpentOnClothing = raw_input("HOW MUCH DO YOU WANT TO SPEND ON CLOTHING? ")
    amountSpentOnSupplies = raw_input("HOW MUCH DO YOU WANT TO SPEND ON MISCELLANEOUS SUPPLIES? ")
    # cast expenditure variables as integers
    amountSpentOnOxen = int(amountSpentOnOxen)
    amountSpentOnFood = int(amountSpentOnFood)
    amountSpentOnAmmunition = int(amountSpentOnAmmunition)
    amountSpentOnClothing = int(amountSpentOnClothing)
    amountSpentOnSupplies = int(amountSpentOnSupplies)
    # calculate amount spent
    amountSpent = amountSpentOnOxen + amountSpentOnFood + amountSpentOnAmmunition + amountSpentOnClothing + amountSpentOnSupplies
    # determine whether player has spent too much, not enough, or just the right amount
    if amountSpent <= 700 and amountSpentOnOxen >= 200 and amountSpentOnOxen <= 300:
        expendituresEntered = True
        dollarsLeft = 700 - amountSpent
        print("")
        print("AFTER ALL OF YOUR PURCHASES, YOU NOW HAVE " + str(dollarsLeft) + " DOLLARS LEFT.")
    else:
        print("")
        print("IMPOSSIBLE")
        print("")

# SET GAMEPLAY VARIABLES
mileage = 0
oxen = amountSpentOnOxen
food = amountSpentOnFood
bullets = amountSpentOnAmmunition * 50
clothing = amountSpentOnClothing
supplies = amountSpentOnSupplies
gunFireResponseTime = 0
gunFireStartClockTime = 0
insufficientClothingInColdWinter = False
userInput = ""
turnNumber = 1
choiceOfEating = 2
clearedSouthPass = False
clearedBlueMountains = False
injured = False
blizzard = False
ill = False
hostilityOfRider = False
gunFirePrompt = ["BANG", "BLAM", "POW", "WHAM"]
tacticSelectedWhenAttacked = 0
stopAtFort = False
cash = 700 - amountSpentOnOxen - amountSpentOnFood - amountSpentOnAmmunition - amountSpentOnClothing - amountSpentOnSupplies
date = []
date.append("MONDAY MARCH 29 1847")
date.append("MONDAY APRIL 12 1847")
date.append("MONDAY APRIL 26 1847")
date.append("MONDAY MAY 10 1847")
date.append("MONDAY MAY 24 1847")
date.append("MONDAY JUNE 7 1847")
date.append("MONDAY JUNE 21 1847")
date.append("MONDAY JULY 5 1847")
date.append("MONDAY JULY 19 1847")
date.append("MONDAY AUGUST 2 1847")
date.append("MONDAY AUGUST 16 1847")
date.append("MONDAY AUGUST 30 1847")
date.append("MONDAY SEPTEMBER 13 1847")
date.append("MONDAY SEPTEMBER 27 1847")
date.append("MONDAY OCTOBER 11 1847")
date.append("MONDAY OCTOBER 25 1847")
date.append("MONDAY NOVEMBER 8 1847")
date.append("MONDAY NOVEMBER 22 1847")
date.append("MONDAY DECEMBER 6 1847")
date.append("MONDAY DECEMBER 20 1847")
currentDate = date[turnNumber - 1]
day = 0
alive = True
arrived = False

# BEGIN JOURNEY
while alive == True and arrived == False:
    if day != 0 and day != 19:
        mileage = mileage + 108
    elif day == 19:
        mileage = mileage + 96

    print("")
    print(date[day])
    print("")
    print("TOTAL MILEAGE: " + str(mileage))
    print("FOOD: " + str(food))
    print("BULLETS: " + str(bullets))
    print("CLOTHING: " + str(clothing))
    print("MISC. SUPPLIES: " + str(supplies))
    print("CASH: " + str(cash))
    print("")

    '''
    huntOrContinue = raw_input("DO YOU WANT TO (1) HUNT, OR (2) CONTINUE? ")
    print("USER SELECTS: " + huntOrContinue)
    '''
    raw_input("PRESS <ENTER> TO CONTINUE")

    # SET ARRIVED EQUAL TO TRUE ON DECEMBER 20TH.
    # THIS IS A LITTLE HACK ADDED DURING DEVELOPMENT
    # WHICH NEEDS TO BE REMOVED LATER.
    if day == 19:
        arrived = True

    day = day + 1

if alive == True:
    welcomeMessage = """
     PRESIDENT JAMES K. POLK SENDS YOU HIS
           HEARTIEST CONGRATULATIONS

    AND WISHES YOU A PROSPEROUS LIFE AHEAD
               AT YOUR NEW HOME
    """
    print(welcomeMessage)
