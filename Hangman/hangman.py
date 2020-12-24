import random as rd

def hangman():
    mainword = rd.choice(["pikachu" , "squirtle" , "charmander" , "bulbasaur" , "articuno" , "mew" , "mewtwo" , "meowth" , "persian"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    guess = ''
    turns = 10

    while turns > 0 :
        main = ""

        for letter in mainword:
            if letter in guess:
                main = main + letter
            else:
                main = main + "_ "

        if guess == mainword:
            print("%s is the right pokemon" %(mainword))
            print("Congratulations! You won.")
            break

        print(main)
        currGuess = input("Guess a letter : ")
        if currGuess in validLetters:
            guess = guess + currGuess
        else:
            currGuess = input("Enter a valid character : ")

        if currGuess not in mainword:
            turns-=1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("Few Breaths left! Be Careful!")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You have killed ASH")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")

print("Welcome to the HANGMAN game %s" %(input("Enter your name : ").title()))
print("-----------------------------------")
print("Try to guess the name of pokemon in less than 10 attempts to save ASH")
x = 'y'
while x == 'y':
    hangman()
    x = input("Press y to play again : ")
print()
