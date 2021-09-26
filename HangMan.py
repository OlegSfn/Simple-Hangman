import random as rn
import ctypes
import sys

# Сбрасывать массив при рестарте
# Разукрашивать угаданные буквы


# Для цветной консоли
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


# Все цвета для консоли
class color:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    
    
words = []
usedLetters = []

with open("HangManWords.txt", 'r', encoding='utf-8') as f:
    for line in f:
        words.append(line.strip())


def chooseWord():      
    global word, wordOpening  
    word = list(rn.choice(words).lower())
    wordOpening = ['*' for i in range(0, len(word))]

def wantRestart():
    wantRestartInp = input("Хотите сыграть ещё раз? -> ")
    if(wantRestartInp.lower() == 'да' or wantRestartInp.lower() == 'y' or wantRestartInp.lower() == 'yes'):
        game()
    else:
        sys.exit
        

def checkLetter(userAnswer):
    isLetter = False
    index = 0

    for x in range(len(wordOpening)):
        if wordOpening[x] != '*':
            wordOpening[x] = word[x]
    
    for letter in word:
        if(letter.lower() == userAnswer.lower()):
            wordOpening[index] = f'{color.red}{letter}{color.end}' 
            isLetter = True  
            
        index += 1

    return isLetter

def GetWordOpening(word):
    return '  '.join(word)

def game():
    chooseWord()
    print(GetWordOpening(wordOpening))
    
    usedLetters.clear()
    score = 100
    x = 12
    while(x != 0):
        if(not '*' in wordOpening):
            print(f"{color.green}Вы выиграли, слово - {GetWordOpening(wordOpening)}. {color.purple}Ваши очки: {score}{color.end}")
            wantRestart()
            
        userAnswer = input('Назовите букву: ').lower()
        while len(userAnswer) > 1 or not userAnswer.isalpha():
            print(f'{color.red}Вы должны ввести одну букву{color.end}')
            userAnswer = input('Назовите букву: ').lower()
        
        if(userAnswer.lower() in usedLetters):
            print(f"{color.cyan}Буква {color.purple}{userAnswer}{color.cyan} уже использована{color.end}")
            continue
        if(checkLetter(userAnswer)):
            usedLetters.append(userAnswer)
            print(GetWordOpening(wordOpening))
        else:
            x -= 1
            score -= 8
            usedLetters.append(userAnswer)
            print(f'{color.yellow}Неверно, буквы {color.purple}{userAnswer}{color.yellow} нет в слове{color.end}')
            print(f"Буквы {color.purple}{usedLetters}{color.end} уже использованы. Осталось {color.purple}{x}{color.end} попыток")
    print(f'{color.red}Вы проиграли, загаданным словом было {color.purple}{word}{color.end}')
    wantRestart()

game()

    
