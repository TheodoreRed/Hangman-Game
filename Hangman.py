import Create_Game
import os
import random


def get_random_word():
    with open("words.txt", "r", encoding="utf-8") as f:
        data = f.read()
        data = list(data.split("\n"))
    return data[random.randint(0, 29)]


def PLAY():
    game = Create_Game.Game(get_random_word())
    while True:
        os.system("cls")
        game.display()
        game.guess_spot(input("Pick letter > "))

        if game.winner():
            os.system("cls")
            game.display()
            print("You win!")
            char = input("Play again (Y/N) > ").upper()
            if char == "Y":
                PLAY()
            else:
                break
        if game.loser():
            os.system("cls")
            game.display()
            print("You Lose!")
            print("The word was " + "\033[1m{}\033[0m".format(game.word))
            print(
                "You got {} out of {}".format(game.get_right_guesses(), len(game.word))
            )
            char = input("Play again (Y/N) > ").upper()
            if char == "Y":
                PLAY()
            else:
                break


if __name__ == "__main__":
    PLAY()
