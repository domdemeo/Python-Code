import Epic 

Value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']              #Defines values of deck an suit of cards 
Suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def CreateDeck(Value, Suit):
    NormalDeck = ["%s of %s" % (v, s) for v in Value for s in Suit]             #combines the suit and the vaules to create 52 cards with different values
    return NormalDeck

def Shuffle(NormalDeck):
    SplitDeck1 = NormalDeck[:26]
    SplitDeck2 = NormalDeck[26:]
    
    ShuffledDeck = []                               #interlaces half the deck with the otehr half and only does 52 cards

    for i in range(26):
        ShuffledDeck.append(SplitDeck1[i])
        ShuffledDeck.append(SplitDeck2[i])
    return ShuffledDeck
    
def Deal(ShuffledDeck):
    Hand = ShuffledDeck[:5]             #deals top 5 card in the new shuffled deck
    return Hand
    
def main():                                         #creates the deck then shuffles it then prints out the top 5 cards to the user after they enter the number of shuffles they desire 
    NormalDeck = CreateDeck(Value, Suit)
    DeckShuffles = 0;
    NumberOfShuffles = Epic.userInt("Please Enter Number of Times You Would Like The Deck Shuffled: ")
    
    while DeckShuffles < NumberOfShuffles:
        ShuffledDeck = Shuffle(NormalDeck)
        DeckShuffles += 1
    print Deal(ShuffledDeck)
    
main()