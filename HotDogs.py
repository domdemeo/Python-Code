import time
import random
import Epic

def RandomDogs():
    Tom = random.randrange(1, 5)
    Sally = random.randrange(1, 5)              # selects random number between 1 to 5
    Fred = random.randrange(1, 5)
    RandomDogs = [Tom,Sally,Fred]
    return RandomDogs 
    
def Competition():
    Run = True
    
    Competitor1 = {'Tom':0,}
    Competitor2 = {'Sally':0}
    Competitor3 = {'Fred':0}
    
    WinnerScore = 0
    WinnerName = ""

    
    print "Ready set eat!"
    while Run:
        print "Chomp... Chomp... Chomp..."
        print ""
        time.sleep(1)
        HotDogs = RandomDogs()
        Competitor1['Tom'] += HotDogs[0]                #adds random number to player 
        Competitor2['Sally'] += HotDogs[1]
        Competitor3['Fred'] += HotDogs[2]
        
        print "Tom has eaten %s hot dogs!" % Competitor1['Tom']
        print "Sally has eaten %s hot dogs!" % Competitor2['Sally']         #prints out current point in time # of hot dogs eaten 
        print "Fred has eaten %s hot dogs!" % Competitor3['Fred']
        
        if Competitor1['Tom'] >= 50:                # looks if anyone has won
            Run = False
            WinnerScore = 50
            WinnerName = "tom"
        
        elif Competitor2['Sally'] >= 50:
            Run = False
            WinnerScore = 50
            WinnerName = "sally"
        
        elif Competitor3['Fred'] >= 50:
            Run = False
            WinnerScore = 50
            WinnerName = "fred"
            
    return WinnerName
    
def Guess():
    Guess = Epic.userString()                                 #ask user for their Guess and turn it to lowercase
    Guess = Guess.lower()

    
def main():
    Guess = Epic.userString("Pick a winner. Type Either: Sally or Fred or Tom): ")
    WinnerName = Competition()                  # runs random eating contest 
    
    if Guess.title() == WinnerName:                     #compaires winner to prediction prints out if you were right or wrong 
        print ""
        print "Good job you guessed right %s wins!" % WinnerName
    else:
        print ""
        print "Sorry But you guessed wrong. %s wins!" % WinnerName
            
    
main()
    
