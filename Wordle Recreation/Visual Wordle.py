from wordleWords import getWord
from wordleWords import wordList
from Wordle import checkWord

rowPosition = 0
columnPosition = 0
secretWord = getWord()

import tkinter as tk

class GUI():

    def __init__(self):
        self.main = tk.Tk()

        self.buttons = {}
        self.guesses = []
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.main.geometry("500x700")

        self.label = tk.Label(self.main, text = "Wordle", font=("Arial", 35))
        self.label.pack(padx=10,pady=10)

        self.guessboard = tk.Frame(self.main)
        for i in range(0, 6):
            self.guessboard.columnconfigure(i, weight = 1)

        for i in range(0,5):
            guess = []
            for x in range(0,6):
                guessLetter = tk.Label(self.guessboard, width = 5, height = 2, text = "||", font = ('Arial', 20))
                guessLetter.grid(row = x, column = i)
                guess.append(guessLetter)
            self.guesses.append(guess)

        self.guessboard.pack(padx = 10, pady = 10)

        self.keyboard = tk.Frame(self.main)
        for i in range(0,1):
            self.keyboard.columnconfigure(i, weight = 1)

        for i in range(0,2):
           for x in range(0,13):
                buttonLetter = self.alphabet[x + i*13]
                button = tk.Button(self.keyboard, width=3, text = str(buttonLetter), font = ("Arial", 12), command = lambda buttonLetter = buttonLetter: self.keyboardPress(buttonLetter))
                button.grid(row=i, column=x)

        self.keyboard.pack(padx=10,pady=10)

        self.main.mainloop()

    def keyboardPress(self, letter):
        global rowPosition
        global columnPosition
        print(f'row: {rowPosition}, column:, {columnPosition}')

        if(not(columnPosition == 6 and rowPosition == 0) and not rowPosition == 5):
            currentPosition = self.guesses[rowPosition][columnPosition]
            currentPosition['text'] = letter
            rowPosition += 1
        
        if rowPosition == 5 and not columnPosition == 6:
            self.isValidWord()

    def isValidWord(self):
        global rowPosition
        global columnPosition

        guess = ''

        for i in self.guesses:
            guess += i[columnPosition].cget('text')

        guess = guess.lower()

        if guess in wordList:
            info = checkWord(guess, secretWord)
            columnPosition += 1
            rowPosition = 0
            self.colorLetters(info)
            
        else:
            for x in range(0, 5):
                currentPosition = self.guesses[x][columnPosition]
                currentPosition['text'] = '||'

            rowPosition = 0

    def colorLetters(self, colorInformation):
        print(f'column: {columnPosition}')

        win = 0
        for x in range(0, 5):
            currentPosition = self.guesses[x][columnPosition - 1]
            currentPosition.config(bg = colorInformation[x]['color'])
            if currentPosition.cget('bg') == 'green':
                win += 1

        if columnPosition == 6:
            self.end('You Lose!', f'The Word was: {secretWord}')
        
        if win == 5:
            self.end('You win!', f'It took you {columnPosition} guesses')
    
    def end(self, *endScreenText):
        self.keyboard.destroy()
        endScreenTexts = []

        for endScreenText in endScreenText:
            self.winScreen = tk.Label(self.main, text = endScreenText, font=("Arial", 23))
            self.winScreen.pack(padx = 10, pady = 10)
            endScreenTexts.append(self.winScreen)

        self.button = tk.Button(text = 'Play Again?', command = lambda: self.playAgainButtonFunctionality(self.winScreen, self.button, *endScreenTexts))
        self.button.pack(padx = 10, pady = 10)

    def playAgainButtonFunctionality(self, *destructions):
        global instance

        columnPosition = 0
        secretWord = getWord()
        self.guessboard.destroy()
        for toDestroy in destructions:
            toDestroy.destroy()

        #GUI()
        #add replay functionality by condensing all window building objects into one constructive function that can be called here and in __init__
        
GUI()

