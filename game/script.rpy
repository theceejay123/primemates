# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    # define characters and narrator
    $ narrator = nvl_narrator
    $ p = Character("[playerName]", color="#784BD1")
    $ a = Character('Angelo', color="#000080")
    $ sam = Character("Sam", color="#35B08B")
    $ dad = Character('Dad')
    $ mom = Character('Mom')
    $ sn = Character('Charlie')
    $ cj = Character('CeeJay')
    $ h = Character('Harold')
    $ d = Character('Daren')
    $ s = Character('Saife')
    $ ch = Character('Christina')
    $ c = Character('Caleb')
    $ hc = Character('Coach')
    $ mt = Character('Ms. Francis')
    $ t = Character('Teacher')
    $ pr = Character('Principal')
    $ m = Character('Marc')
    $ k = Character('Karen')
    # define all music
    $ audio.chillguitar = './audio/music/chillguitar.mp3'
    $ audio.chillpiano = './audio/music/chillpiano.mp3'
    $ audio.jazzyguitar = './audio/music/jazzyguitar.mp3'
    $ audio.playfuljive = './audio/music/playfuljive.mp3'
    # define all sounds
    $ audio.alarm = './audio/sounds/alarm.mp3'
    $ audio.schoolbell = './audio/sounds/schoolbell.mp3'

# define all images

# background images
image bg room = im.Scale('./images/backgrounds/bg_room.png', 1280, 720)


# The game starts here.
label start:

    python:
        playerName = renpy.input("What is your name?")
        playerName = playerName.strip()

        if not playerName:
            playerName = "Player"

    jump start_game
