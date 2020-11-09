# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    $ ch_eileen = Character("Eileen")
    $ ch_ceejay = Character("Ceejay")

# The game starts here.

label start:

    jump start_game

    return
