import Epic

Suspects = ["Miss Scarlet", "Col Mustard", "Mr Green"]
Weapons = ["Candlestick","Wrench","Pipe"]

def TotalPossibilities(Suspects, Weapons):
    TotalPossibilities = []
    for s in Suspects:
        for w in Weapons:
            TotalPossibilities.append("%s with the %s" % (s, w))
    return TotalPossibilities

def NarrowSuspects(Possibilities, Suspects, Weapons):
    Clue = Epic.userString("Is the clue a suspect or a weapon? (Please Enter Either a S or W Only!):")
    if Clue.upper() == "S":
        SuspectorWeapon = Epic.userString("Enter the innocent person's name. (Please Enter name exactly as it Appears!) (%s):" % Suspects)
    if Clue.upper() == "W":
        SuspectorWeapon = Epic.userString("Enter the weapon that was not used (Please Enter the name of the Weapon exactly as it Appears!) (%s):" % Weapons)
    else:
        print "You have entered invalid input please enter exact input as instructed"
    InvalidInput = []
    for item in Possibilities:
        if SuspectorWeapon.upper() in item.upper():
            InvalidInput.append(item)
    for i in InvalidInput:
        Possibilities.remove(i)
    return Possibilities

def main():
    Possibilities = TotalPossibilities(Suspects, Weapons)
    
    while len(Possibilities) > 1:
        print "There are currently %s possibilities left." % len(Possibilities)
        NarrowPossibilities = NarrowSuspects(Possibilities, Suspects, Weapons)
    print "There is only one possibility left."
    print "It was %s! who killed the Victim!" % Possibilities[0]
    
main()
