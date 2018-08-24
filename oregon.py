userInput = raw_input("DO YOU NEED INSTRUCTIONS (YES/NO)?")

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
huntingDifficultyLevel = raw_input("?")
print("")

# ENTER EXPENDITURES
expendituresEntered = False
while expendituresEntered == False:
    amountSpentOnOxen = raw_input("HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM?")
    amountSpentOnFood = raw_input("HOW MUCH DO YOU WANT TO SPEND ON FOOD?")
    amountSpentOnAmmunition = raw_input("HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION?")
    amountSpentOnClothing = raw_input("HOW MUCH DO YOU WANT TO SPEND ON CLOTHING?")
    amountSpentOnSupplies = raw_input("HOW MUCH DO YOU WANT TO SPEND ON MISCELLANEOUS SUPPLIES?")
    amountSpent = amountSpentOnOxen + amountSpentOnFood + amountSpentOnAmmunition + amountSpentOnClothing + amountSpentOnSupplies
    if amountSpent <= 700 and amountSpentOnOxen >= 200 and amountSpentOnOxen <= 300:
        expendituresEntered = True
        dollarsLeft = 700 - amountSpent
        print("AFTER ALL OF YOUR PURCHASES, YOU NOW HAVE " + dollarsLeft + " DOLLARS LEFT.")
    else:
        print("")
        print("IMPOSSIBLE")
        print("")

# SET GAMEPLAY VARIABLES
mileage = 0
food = amountSpentOnFood
bullets = amountSpentOnBullets * 50
clothing = amountSpentOnClothing
supplies = amountSpentOnSupplies
cash = 700 - amountSpentOnOxen - amountSpentOnFood - amountSpentOnAmmunition - amountSpentOnClothing - amountSpentOnSupplies

# BEGIN JOURNEY
print("")
print("MONDAY MARCH 29 1847")
print("")
print("TOTAL MILEAGE: " + mileage)
print("FOOD: " + food)
print("BULLETS: " + bullets)
print("CLOTHING: " + clothing)
print("MISC. SUPPLIES: " + supplies)
print("CASH: " + cash)
huntOrContinue = raw_input("DO YOU WANT TO (1) HUNT, OR (2) CONTINUE? ")
print("USER SELECTS: " + huntOrContinue)
