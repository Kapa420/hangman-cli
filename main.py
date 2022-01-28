from os import system
from random import choice
from ascii_art import ascii_art

def get_word():
    with open("./words/data.txt", "r", encoding="utf-8") as word:
        chosen_word = choice([line for line in word])
        new_word = chosen_word.maketrans('áéíóú','aeiou')
        return chosen_word.translate(new_word)

def index_letters(word):
    indices = {}
    for letter in word:
       indices[letter] = [index for index, val in enumerate(word) if val == letter]
    return indices

def print_progress(progress):
    print('\n\n')
    for letter in progress:
        print(letter, end="\t")
    print('\n\n')
    
def verify_input(letter):
    try:
        if len(letter) != 1 or letter.isnumeric():
            raise ValueError("Tiene que ser una letra!")
        return letter.lower()
    except ValueError as ve:
        print(ve)

def HangMan():
    word = get_word().replace("\n","")
    index = index_letters(word)
    secret_word = ["_ " for i in word]
    lifes = 3
    while lifes > 0:
        system("clear")
        print(ascii_art[0])
        system(f"echo 'Tienes {lifes} vidas restantes' | cowsay | lolcat")
        print_progress(secret_word)
        letter_atempt = verify_input(input("Ingrese una letra: "))
        try:
            if letter_atempt in word:
                for position in index.get(letter_atempt):
                    secret_word[position] = letter_atempt
            else:
                lifes -= 1
        except TypeError:
            print(" Pierdes dos vidas! ")
            lifes -= 2   
            input()
    else:    
        system(f" echo 'Perdiste, la palabra era {word}' | cowsay | lolcat")

def run():
    HangMan()

if __name__ == '__main__':
    run()
