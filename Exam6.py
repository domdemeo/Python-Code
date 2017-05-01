import Epic

Suspects = ["Miss Scarlet", "Col Mustard", "Mr Green"]
Weapons = ["Candlestick","Wrench","Pipe"]

def TotalPossibilities(Suspects, Weapons):              
    TotalPossibilities = []                             #Generates a list of al of the possible possibilities for both supects and murder weapons
    for s in Suspects:
        for w in Weapons:
            TotalPossibilities.append("%s with the %s" % (s, w))
    return TotalPossibilities

def NarrowSuspects(Possibilities, Suspects, Weapons):
    Clue = Epic.userString("Is the clue a suspect or a weapon? (Please Enter Either a S or W Only!):")   #section for users to enter either suspects and weapons
    if Clue.upper() == "S":
        SuspectorWeapon = Epic.userString("Enter the innocent person's name. (Please Enter name exactly as it Appears!) (%s):" % Suspects)
    if Clue.upper() == "W":
        SuspectorWeapon = Epic.userString("Enter the weapon that was not used (Please Enter the name of the Weapon exactly as it Appears!) (%s):" % Weapons)
    else:
        print "You have entered invalid input please enter exact input as instructed"
    InvalidInput = []
    for item in Possibilities:
        if SuspectorWeapon.upper() in item.upper():                 #clears invaild input and removes invalid items from the possiblites list
            InvalidInput.append(item)
    for i in InvalidInput:
        Possibilities.remove(i)
    return Possibilities

def main():
    Possibilities = TotalPossibilities(Suspects, Weapons)           #creates total possiblities to be widdled down
    while len(Possibilities) > 1:
        print "There are currently %s possibilities left." % len(Possibilities)
        NarrowPossibilities = NarrowSuspects(Possibilities, Suspects, Weapons)              #narrows supects and weapons and leaves total number of possiblites left and prints out results 
    print "There is only one possibility left."
    print "It was %s! who killed the Victim!" % Possibilities[0]
    
main()