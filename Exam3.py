import Epic
import random

def Choose(Card1, Card2, Choices):
    CardChoice = {'Run': True, 'Response': ""}                                                                 # Only allows you to pick cards between 0 to 9 and will not allow you to continue with out it 
    
    if Card1 < 0 or Card1 > 9 or Card2 < 0 or Card2 > 9 or Card1 == Card2:
        CardChoice['Response'] = "Your choice is invalid. Please pick different cards and they must be between 0 and 9"
    else:
        CardChoice['Response'] = "Card %i is a %s. \nCard %i is a %s" % (Card1, Choices[Card1], Card2, Choices[Card2])
        
        if Choices[Card1] == Choices[Card2]:                                                                                #adds both cards and card choices 
            CardChoice['Run'] = False
    return CardChoice

Choices= ['bird','dog','snake','fish','cat','mouse','starfish','woodchuck','crab']          #assigns cards and values related to cards 0 to 9

def ShuffleArray(Array):
    RandomCard = random.randint(0,9)
    NewArray = Array[RandomCard]                 #creates new array and then shuffles it randomly 
    Array.append(NewArray)
    random.shuffle(Array)

def main():
    Wins = 0
    Attempts = 0                #Creates scoring 
    Loses = 0
    Run = True

    ShuffleArray(Choices)
    while Run:
        Card1 = Epic.userInt('Pick Your first card From 0 to 9: ')          #user picks card based on prompt 
        Card2 = Epic.userInt('Pick Your second card From 0 to 9:')
        Attempts += 1
        Guess = Choose(Card1, Card2, Choices)
        
        print Guess['Response']                                        #prints out number of times you guessed for card and when you get it correct 
        Run = Guess['Run']
        print 'Attempt %i' %Attempts
        print 'Wins %i' %Wins
        print ' '
    print 'Congrats You Guessed Right! It only took you %i Attempts. You have %i Wins!' % Attempts, Wins
main()




























choices = ['bird','dog','snake','fish','cat','mouse','starfish','woodchuck','crab']
#randomizes choices
def board(choices):
    
    rand = random.randrange(0, 9)
    choices.append(choices[rand])
    #shuffles the choices in the array so that the game board is always different
    random.shuffle(choices)
    
    return choices

#checks the cards picked and ensures tha0t the user enters valid inputs
def cardPicked(first, second):
    
    if first > 9 or first < 0 or second > 9 or second < 0 or first == second:
        print "Invalid Input! You must pick different cards and the card must be a number from 0-9.\n"
        return False
    else:
        return True
        
def main():
    #create the game board with the cards
    board(choices)
    tries = 0 
       
    play = True
    while play:
        tries += 1 #add 1 each time user plays to keep track of how many tries it took them to win
        first = Epic.userInt("Pick the first card to turn over (0-9): ")
        second = Epic.userInt("Pick the second card to turn over (0-9): ")
        #prints out the cards user picked
        print "Card {} is a {}.".format(first, choices[first])
        print "Card {} is a {}." .format(second, choices[second])
    
        cardPicked(first,second)
        if first == second:
            "Can't pick same card"
        #if user's first and second choice were the same cards then they will be prompted that they won
        elif choices[first] == choices[second]:
            print "You win! It took you {} tries." .format(tries)
        
main()