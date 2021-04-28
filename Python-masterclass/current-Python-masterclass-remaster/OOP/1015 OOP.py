#######################
# EECS1015 - York University
#
# Card and CardDeck
#
#######################
from random import shuffle


# 0-51 cards (1-52 cards in non Python language)
# 13 cards per suit, 4 suits per deck
# 2  3  4  5  6  7  8  9 10  J  Q  K A  replace X with id in row
# 00,01,02,03,04,05,06,07,08,09,10,11,12 (2-A Heart)   X//13=0
# 13,14,15,16,17,18,19,20,21,22,23,24,25 (2-A Diamond) X//13=1
# 26,27,28,29,30,31,32,33,34,35,36,37,38 (2-A Clubs)   X//13=2
# 39,40,41,42,43,44,45,46,47,48,49,50,51 (2-A Spades)  X//13=3
# CARD IDs mapping                      replace Y with 0-52
# 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12   Y%13->0-12
# '2' '3' '4' '5' '6' '7' '8' '9''10' 'J' 'Q' 'K' 'A'
class Card:
    # LUT=Look Up Table
    # 0-12
    suitLUT = {0: "H", 1: "D", 2: "C", 3: "S"}
    cardLUT = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, cardID):
        valid = 0 <= cardID < 52
        assert valid, "cardID {} must be between 0 and 52".format(cardID)
        self.cardID = cardID

    def getFaceValue(self):
        faceValue = self.cardID % 13  # modules by 13 gives us the facevalue
        return faceValue  # why?  cardID / 13 -> remainder is the facevalue

    def getSuitChar(self):
        suitIndex = self.cardID // 13  # integer divide maps to suit
        suitValue = Card.suitLUT[suitIndex]  # card for this suit 0-3
        return suitValue

    def getCardString(self):
        faceValue = self.getFaceValue()
        faceChar = Card.cardLUT[faceValue]
        suitChar = self.getSuitChar()
        card = "{} [{}]".format(faceChar, suitChar)
        if faceChar != '10':
            card = " " + card  # add a lead space to non-10 cards
        return card

    def printCard(self):
        print(self.getCardString())

    # end of Card class


class CardDeck:
    def __init__(self, shuffleFlag=False):

        # instance variables!
        self.deckList = []
        self.topCardIndex = 0  # keep track of topCard index

        for i in range(52):  # make list 0-51
            self.deckList.append(i)
        if shuffleFlag:
            shuffle(self.deckList)

    def reorder(self):
        self.deckList.sort()
        self.topCardIndex = 0

    def reshuffle(self):
        shuffle(self.deckList)
        self.topCardIndex = 0

    def dealTopCard(self):
        assert self.topCardIndex <= 51, "Deck is empty"
        cardID = self.deckList[self.topCardIndex]
        newCard = Card(cardID)
        self.topCardIndex += 1
        return newCard

    def numCardsLeft(self):
        remainingCards = 52 - self.topCardIndex
        return remainingCards

    # end of CardDeck class


# This function is not part of class
def printNCards(deck, number=52):
    for i in range(number):
        card = deck.dealTopCard()
        card.printCard()


def main():
    carddeck = CardDeck()
    print("--JUST CREATED--")
    printNCards(carddeck, 10)
    print("Cards remaining %d" % (carddeck.numCardsLeft()))
    print("--AFTER SHUFFLE--")
    carddeck.reshuffle()
    printNCards(carddeck, 20)
    print("Cards remaining %d" % (carddeck.numCardsLeft()))
    print("--AFTER SORT  --")
    carddeck.reorder()
    printNCards(carddeck)
    print("Cards remaining %d" % (carddeck.numCardsLeft()))


if __name__ == "__main__":
    main()
