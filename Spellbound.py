import random
import time
from tkinter import *

window = Tk()
window.title("Spellbound")
window["bg"] = "AliceBlue"

print("Instructions:")
print("-> Get the highest score you can by creating three and four letter words from the given letters")
print("-> Each letter can be used only once per word")
print("-> The clear button clears the entered text, and resets the letter buttons")
print("-> The check button checks to see if the entered word is valid")
print("-> 100 points for valid three letter words, 150 points for valid four letter words")
print("-> Feeling stuck? Press the shuffle button to shuffle the letters")
print("-> Click the 'Reveal Answers' button to print all possible words to the console and see which ones you missed!")
print()

# importing and sorting list of valid words
with open("valid.txt") as file_object:
    contents = file_object.read()
list = contents.split()


validWords = []
for i in range(len(list)):
    validWords.append(min(list))
    list.remove(validWords[-1])

# letter choosing algorithm
vowels = []
cons = []
possibleWords = []
guessedWords = []

for i in range(12):
    vowels.append('E')
for i in range(8):
    vowels.append('A')
for i in range(7):
    vowels.append('O')
    vowels.append('I')
for i in range(3):
    vowels.append('U')
for i in range(2):
    vowels.append('Y')


for i in range(9):
    cons.append('T')
for i in range(7):
    cons.append('N')
for i in range(6):
    cons.append('S')
    cons.append('R')
    cons.append('H')
for i in range(4):
    cons.append('D')
    cons.append('L')
for i in range(3):
    cons.append('C')
    cons.append('M')
for i in range(2):
    cons.append('F')
    cons.append('W')
    cons.append('G')
    cons.append('P')
    cons.append('B')
for i in range(1):
    cons.append('V')
    cons.append('Q')
    cons.append('K')
    cons.append('X')
    cons.append('J')
    cons.append('Z')


letters = []
button1 = True
button2 = True
button3 = True
button4 = True
button5 = True
button6 = True
button7 = True

score = 0

entry = StringVar()
l = StringVar()

def randomLetter(letterList, num):
    for i in range(num):
        index = random.randint(0,len(letterList)-1)
        letters.append(letterList[index])

def generateLetters():
    global letters
    global possibleWords
    letters = []
    possibleWords = []
    for i in range(2):
        num = random.randint(0, len(vowels) - 1)
        letters.append(vowels[num])
    for i in range(1):
        temp = random.randint(0, 1)
        if temp == 1:
            num = random.randint(0, len(vowels) - 1)
            letters.append(vowels[num])
        else:
            num = random.randint(0, len(cons) - 1)
            letters.append(cons[num])
    for i in range(4):
        num = random.randint(0, len(cons) - 1)
        letters.append(cons[num])

    for i in range(len(letters)):
        for j in range(len(letters)):
            if j != i:
                for k in range(len(letters)):
                    if k != j and k != i:
                        word = letters[i] + letters[j] + letters[k]
                        if word in validWords:
                            if word not in possibleWords:
                                possibleWords.append(word)
                        for l in range(len(letters)):
                            if l != k and l != j and l != i:
                                word = letters[i] + letters[j] + letters[k] + letters[l]
                                if word in validWords:
                                    if word not in possibleWords:
                                        possibleWords.append(word)

while len(possibleWords) < 60:
    generateLetters()

numWords = StringVar()
numWords.set(f"Number of possible words: {len(possibleWords)}")


def shuffle(list):
    newList = []
    num = 6
    for i in range(7):
        randIndex = random.randint(0,num)
        temp = list[randIndex]
        list.remove(temp)
        newList.append(temp)
        num -= 1
    return newList

letters = shuffle(letters)

def changeColourCorrect():
    entryLabel["bg"] = "LightGreen"
    entryLabel.after(1000,changeBack)

def changeColourIncorrect():
    entryLabel["bg"] = "Crimson"
    entryLabel.after(1000,changeBack)

def changeBack():
    entryLabel["bg"] = "LightBlue"
    clear()

def updateScore():
    global score
    scoreLabel["text"] = f"Score: {score}"

def check(word):
    global guessedWords
    global score
    list = validWords
    correct = False
    while len(list) > 0:
        mid = len(list) // 2  # middle index
        if list[mid] > word:  # item is at the back
            list = list[0:mid]
        elif list[mid] < word:  # item is at the front
            list = list[mid + 1:]
        else:
            if word not in guessedWords:
                wordsLabel["text"] += "\n" + word
                guessedWords.append(word)
                correct = True
                changeColourCorrect()
                if len(word) == 3:
                    score += 100
                else:
                    score += 150
                updateScore()
                break
            else:
                correct = False
                break
    if correct == False:
        changeColourIncorrect()

def showWords():
    print("Answers:")
    for i in range(len(possibleWords)):
        if i == len(possibleWords)-1:
            print(possibleWords[i])
        else:
            print(possibleWords[i], end=", ")





def letter1Pressed():
    global button1
    if button1 == True:
        l = l1Button.cget("text")
        entry.set(entry.get() + l)
        entryLabel["text"] = entry.get()
        button1 = False
        l1Button["bg"] = "Gray"

def letter2Pressed():
    global button2
    if button2 == True:
        l = l2Button.cget("text")
        entry.set(entry.get() + l)
        entryLabel["text"] = entry.get()
        button2 = False
        l2Button["bg"] = "Gray"


def letter3Pressed():
    global button3
    if button3 == True:
        l = l3Button.cget("text")
        entry.set(entry.get() + l)
        entryLabel["text"] = entry.get()
        button3 = False
        l3Button["bg"] = "Gray"

def letter4Pressed():
    global button4
    if button4 == True:
        l = l4Button.cget("text")
        entry.set(entry.get() + l)
        entryLabel["text"] = entry.get()
        button4 = False
        l4Button["bg"] = "Gray"

def letter5Pressed():
    global button5
    if button5 == True:
        l = l5Button.cget("text")
        entry.set(entry.get() + l)
        entryLabel["text"] = entry.get()
        button5 = False
        l5Button["bg"] = "Gray"

def letter6Pressed():
    global button6
    if button6 == True:
        l = l6Button.cget("text")
        entry.set(entry.get() + l)
        entryLabel["text"] = entry.get()
        button6 = False
        l6Button["bg"] = "Gray"

def letter7Pressed():
    global button7
    if button7 == True:
        l = l7Button.cget("text")
        entry.set(entry.get() + l)
        entryLabel["text"] = entry.get()
        button7 = False
        l7Button["bg"] = "Gray"


def clear():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    entry.set("")
    entryLabel["text"] = entry.get()
    button1 = True
    button2 = True
    button3 = True
    button4 = True
    button5 = True
    button6 = True
    button7 = True
    l1Button["bg"] = "LightGray"
    l2Button["bg"] = "LightGray"
    l3Button["bg"] = "LightGray"
    l4Button["bg"] = "LightGray"
    l5Button["bg"] = "LightGray"
    l6Button["bg"] = "LightGray"
    l7Button["bg"] = "LightGray"

def shuffleLetters():
    global letters
    letters = shuffle(letters)

    l1 = StringVar()
    l1.set(letters[0])
    l1Button["text"] = l1.get()

    l2 = StringVar()
    l2.set(letters[1])
    l2Button["text"] = l2.get()

    l3 = StringVar()
    l3.set(letters[2])
    l3Button["text"] = l3.get()

    l4 = StringVar()
    l4.set(letters[3])
    l4Button["text"] = l4.get()

    l5 = StringVar()
    l5.set(letters[4])
    l5Button["text"] = l5.get()

    l6 = StringVar()
    l6.set(letters[5])
    l6Button["text"] = l6.get()

    l7 = StringVar()
    l7.set(letters[6])
    l7Button["text"] = l7.get()

    clear()







l1Frame = Frame(window,
                relief = RAISED,
                borderwidth = 1,
                width=50,
                height=50
                )
l1Frame.grid(
    row=0,
    column=0,
    padx = 5, pady = 5
)
l1 = StringVar()
l1.set(letters[0])
l1Button = Button(l1Frame,
                width=5,
                height=3,
                font=("Avenir", 12),
                text=l1.get(),
                bg="LightGray",
                command = letter1Pressed
                )
l1Button.pack()

l2Frame = Frame(window,
                relief = RAISED,
                borderwidth = 1,
                width=50,
                height=50
                )
l2Frame.grid(
    row=0,
    column=1,
    padx = 5, pady = 5
)
l2 = StringVar()
l2.set(letters[1])
l2Button = Button(l2Frame,
                width=5,
                height=3,
                font=("Avenir", 12),
                text=l2.get(),
                bg="LightGray",
                command = letter2Pressed
                )
l2Button.pack()

l3Frame = Frame(window,
                relief = RAISED,
                borderwidth = 1,
                width=50,
                height=50
                )
l3Frame.grid(
    row=0,
    column=2,
    padx = 5, pady = 5
)
l3 = StringVar()
l3.set(letters[2])
l3Button = Button(l3Frame,
                width=5,
                height=3,
                font=("Avenir", 12),
                text=l3.get(),
                bg="LightGray",
                command = letter3Pressed
                )
l3Button.pack()

l4Frame = Frame(window,
                relief = RAISED,
                borderwidth = 1,
                width=50,
                height=50
                )
l4Frame.grid(
    row=0,
    column=3,
    padx = 5, pady = 5
)
l4 = StringVar()
l4.set(letters[3])
l4Button = Button(l4Frame,
                width=5,
                height=3,
                font=("Avenir", 12),
                text=l4.get(),
                bg="LightGray",
                command = letter4Pressed
                )
l4Button.pack()

l5Frame = Frame(window,
                relief = RAISED,
                borderwidth = 1,
                width=50,
                height=50
                )
l5Frame.grid(
    row=0,
    column=4,
    padx = 5, pady = 5
)
l5 = StringVar()
l5.set(letters[4])
l5Button = Button(l5Frame,
                width=5,
                height=3,
                font=("Avenir", 12),
                text=l5.get(),
                bg="LightGray",
                command=letter5Pressed
                )
l5Button.pack()

l6Frame = Frame(window,
                relief = RAISED,
                borderwidth = 1,
                width=50,
                height=50
                )
l6Frame.grid(
    row=0,
    column=5,
    padx = 5, pady = 5
)
l6 = StringVar()
l6.set(letters[5])
l6Button = Button(l6Frame,
                width=5,
                height=3,
                text=l6.get(),
                font=("Avenir", 12),
                bg="LightGray",
                command = letter6Pressed
                )
l6Button.pack()

l7Frame = Frame(window,
                relief = RAISED,
                borderwidth = 1,
                width=50,
                height=50
                )
l7Frame.grid(
    row=0,
    column=6,
    padx = 5, pady = 5
)
l7 = StringVar()
l7.set(letters[6])
l7Button = Button(l7Frame,
                width=5,
                height=3,
                font=("Avenir",12),
                text=l7.get(),
                bg="LightGray",
                command = letter7Pressed
                )
l7Button.pack()





# shuffle button
shuffleFrame = Frame(
    window,
    relief = RAISED,
    borderwidth = 1,
    width=50,
    height=50
)
shuffleFrame.grid(
    row=1,
    column=4,
    columnspan=3,
    padx = 3, pady = 3
)
shuffleButton = Button(
    shuffleFrame,
    width=15,
    height=1,
    font=("Avenir",10),
    bg="SteelBlue",
    fg="White",
    text="Shuffle",
    command=shuffleLetters
)
shuffleButton.pack()

# entry label
entryFrame = Frame(
    window,
    relief = RAISED,
    borderwidth = 1,
    width=50,
    height=50
)
entryFrame.grid(
    row=1,
    column=0,
    columnspan=3,
    padx = 5, pady = 5
)
entryLabel = Label(
    entryFrame,
    text=entry.get(),
    font=("Avenir",12),
    fg = "Black",
    bg = "LightBlue",
    width = 15,
    height = 2
)
entryLabel.pack()

# check button
checkFrame = Frame(
    window,
    borderwidth = 1,
    bg="AliceBlue",
    width=50,
    height=50
)
checkFrame.grid(
    row=1,
    column=3,
    padx = 5, pady = 5
)
checkButton = Button(
    checkFrame,
    width=5,
    height=1,
    font=("Avenir",10),
    bg="SteelBlue",
    fg="White",
    text="Check",
    command = lambda: check(entry.get())
)
checkButton.pack()
clearButton = Button(
    checkFrame,
    width=5,
    height=1,
    font=("Avenir",10),
    bg="SteelBlue",
    fg="White",
    text="Clear",
    command = clear
)
clearButton.pack(
    pady=5
)

# correct words list
wordsFrame = Frame(
    window,
    relief = RAISED,
    borderwidth = 1,
    width=50,
    height=50
)
wordsFrame.grid(
    row=3,
    column=0,
    columnspan=3,
    padx = 5, pady = 5
)
wordsLabel = Label(
    wordsFrame,
    width=17,
    height=20,
    font=("Avenir",8),
    fg="White",
    bg="SteelBlue",
    text="Words found:",
    anchor="n",
    justify=LEFT
)
wordsLabel.pack()

scoreFrame = Frame(
    window,
    relief = RAISED,
    borderwidth = 1,
    width=50,
    height=50
)
scoreFrame.grid(
    row=2,
    column=0,
    columnspan=3,
    padx = 5, pady = 5
)
scoreLabel = Label(
    scoreFrame,
    width=13,
    height=2,
    font=("Avenir",10),
    fg="White",
    bg="#396a93",
    text="Score: 0",
    anchor="w",
    justify=LEFT
)
scoreLabel.pack()

numWordsFrame = Frame(
    window,
    borderwidth = 1,
    bg="AliceBlue",
    width=50,
    height=50
)
numWordsFrame.grid(
    row=2,
    column=3,
    columnspan=3,
    padx = 5, pady = 5
)
numWordsLabel = Label(
    numWordsFrame,
    width=25,
    height=1,
    font=("Avenir",8),
    fg="White",
    bg="SteelBlue",
    text=numWords.get(),
)
numWordsLabel.pack()
showWordsButton = Button(
    numWordsFrame,
    width=25,
    height=1,
    font=("Avenir",8),
    bg="SteelBlue",
    fg="White",
    text="Reveal Answers",
    command = showWords
)
showWordsButton.pack(
    pady=5
)

window.mainloop()


