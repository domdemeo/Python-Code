import Epic 

Value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
Suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def CreateDeck(Value, Suit):
    NormalDeck = ["%s of %s" % (v, s) for v in Value for s in Suit]
    return NormalDeck

def Shuffle(NormalDeck):
    SplitDeck1 = NormalDeck[:26]
    SplitDeck2 = NormalDeck[26:]
    
    ShuffledDeck = []

    for i in range(26):
        ShuffledDeck.append(SplitDeck1[i])
        ShuffledDeck.append(SplitDeck2[i])
    return ShuffledDeck
    
def Deal(ShuffledDeck):
    Hand = ShuffledDeck[:5]
    return Hand
    
def main():
    NormalDeck = CreateDeck(Value, Suit)
    DeckShuffles = 0;
    NumberOfShuffles = Epic.userInt("Please Enter Number of Times You Would Like The Deck Shuffled: ")
    
    while DeckShuffles < NumberOfShuffles:
        ShuffledDeck = Shuffle(NormalDeck)
        DeckShuffles += 1
    print Deal(ShuffledDeck)
    
main()