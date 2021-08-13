#Uno Game Template

#Card Class
class Card:
    c=""
    t=""
    n=""

    def __init__(self,colour, type, number):
        self.c = colour
        self.t = type
        self.n = number

    def print_card(self):
        print(f"{self.c} {self.t} {self.n}")

def play(colour, type, number):
    #this method determines the card to play
    #a simple strategy of playing a card with the same colour is provided
    #the parameter passed is the card that is face up
    #for a playable card - print the card and remove it from the hand
    #otherwise print 'pick up'

    for i in range(len(cards)):
        if cards[i].c == colour and colour != "-":
            cards.pop(i).print_card() #print and remove card
            return

    for i in range(len(cards)):
        if cards[i].t == type:
            if cards[i].n == number:
                cards.pop(i).print_card()
                return

    for i in range(len(cards)):
        if cards[i].c == "-":
            newColour = ""
            # red, blue, green, yellow
            colourCounts = [0,0,0,0]
            for j in range(len(cards)):
                if cards[j].c == "r":
                    colourCounts[0] += 1
                if cards[j].c == "b":
                    colourCounts[1] += 1
                if cards[j].c == "g":
                    colourCounts[2] += 1
                if cards[j].c == "y":
                    colourCounts[3] += 1
            mostCommon = max(colourCounts)
            if colourCounts[0] == mostCommon:
                newColour = "Change to: red"
            elif colourCounts[1] == mostCommon:
                newColour = "Change to: blue"
            elif colourCounts[2] == mostCommon:
                newColour = "Change to: green"
            elif colourCounts[3] == mostCommon:
                newColour = "Change to: yellow"
            cards.pop(i).print_card() #print and remove card
            print(newColour)
            return

    print("Pick up")


"""Main Program"""
cards = [] #a list of cards
while True:
    choice = input("'add' to add a card, 'play' to play a card, 'print' to print: ")
    if choice == 'add':
        card = input("3 character code to add: ")
        cards.append(Card(card[0],card[1],card[2]))
    elif choice == 'play':
        card = input("3 character code of card facing up: ")
        play(card[0],card[1],card[2])
    elif choice == 'print':
        for c in cards:
            c.print_card()
    elif choice == 'exit':
        break
