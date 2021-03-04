import letters_game as l_g  # letters_game 
import numbers_game as n_g  # numbers_game
import sys

if __name__ == "__main__":
    while True:
        which_game = input("Letters or numbers(l/n): ")
        if which_game == 'l':
            l_g.play()
        elif which_game == 'n':
            n_g.play()
        else:
            sys.exit()
