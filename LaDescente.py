"""

 	Objectif
Écrivez le programme permettant de détruire les montagnes pour pouvoir attérir. Pour cela, tirez sur la montagne la plus haute.
 	Règles
Au début de chaque tour de jeu, vous recevez en entrée la hauteur de chaque montagne de gauche à droite.
Avant la fin du tour de jeu, vous devez indiquer la montagne la plus haute pour tirer dessus.

Tirer sur une montagne ne fera qu'en détruire une partie. Votre vaisseau descend à chaque passe.
import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    mountains = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print("4")
Conditions de victoire
Vous gagnez si vous détruisez la montagne la plus haute à chaque tour
Height of mountain 0 : 9
Height of mountain 1 : 8
Height of mountain 2 : 7
Height of mountain 3 : 6
Height of mountain 4 : 5
Height of mountain 5 : 4
Height of mountain 6 : 3
Height of mountain 7 : 2   
"""
import sys
import math

while True:
    mountains = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        mountains.append(mountain_h)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print(max(range(8), key=mountains.__getitem__), flush=True)
"""
Timeout: your program did not write to the standard output in due time.
 
Height of mountain 0 : 9
Height of mountain 1 : 8
Height of mountain 2 : 7
Height of mountain 3 : 6
Height of mountain 4 : 5
Height of mountain 5 : 4
Height of mountain 6 : 3
Height of mountain 7 : 2
"""

"""
Solution
while True:print(max([(int(input()),x)for x in range(8)])[1])

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
while True:
    max = max_num = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if max < mountain_h:
            max = mountain_h
            max_num = i
    # The index of the mountain to fire on.
    print(max_num)
"""