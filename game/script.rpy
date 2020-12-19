# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    # define characters and narrator
    $ narrator = nvl_narrator
    $ p = Character("[playerName]", color="#784BD1")
    $ a = Character('Angelo', color="#007fff")
    $ sam = Character("Sam", color="#35B08B")
    $ dad = Character('Dad')
    $ mom = Character('Mom')
    $ sn = Character('Charlie')
    $ cj = Character('CeeJay')
    $ h = Character('Harold')
    $ d = Character('Daren')
    $ s = Character('Saife', color="#000080")
    $ ch = Character('Christina')
    $ c = Character('Caleb')
    $ hc = Character('Coach')
    $ mt = Character('Ms. Francis')
    $ t = Character('Teacher')
    $ pr = Character('Principal')
    $ m = Character('Marc')
    $ k = Character('Karen')
    $ board = Character('Karen')
    # define all music
    $ audio.chillguitar = './audio/music/chillguitar.mp3'
    $ audio.chillpiano = './audio/music/chillpiano.mp3'
    $ audio.jazzyguitar = './audio/music/jazzyguitar.mp3'
    $ audio.playfuljive = './audio/music/playfuljive.mp3'
    $ audio.epic = './audio/music/epic.mp3'
    # define all sounds
    $ audio.alarm = './audio/sounds/alarm.mp3'
    $ audio.schoolbell = './audio/sounds/schoolbell.mp3'
    $ audio.bird = './audio/sounds/birdchirp.mp3'
    $ audio.hallway = './audio/sounds/hallway.mp3'
    $ audio.smallapplause = './audio/sounds/smallapplause.mp3'
    $ audio.whoo = './audio/sounds/whoo.mp3'
    $ audio.trees = './audio/sounds/windrustletrees.mp3'
    $ audio.hc = './audio/sounds/hcchuckle.mp3'
    $ audio.mic = './audio/sounds/mic.mp3'
    $ audio.pun = './audio/sounds/punlaugh.mp3'
    $ audio.notification = './audio/sounds/phone.mp3'
    $ audio.knock = './audio/sounds/knocking.mp3'

# define all images
image board = im.Scale('./images/backgrounds/bulletin_board.png', 640, 400)

# background images
image bg room = im.Scale('./images/backgrounds/bg_room.jpg', 1280, 720)
image bg school = im.Scale('./images/backgrounds/bg schoolmap.png', 1280, 720)
image bg worldmap = im.Scale('./images/backgrounds/bg worldmap.png', 1280, 720)
image bg music = im.Scale('./images/backgrounds/bg musicroom.png', 1280, 720)
image bg mall = im.Scale('./images/backgrounds/bg mall.jpg', 1280, 720)
image bg foyer = im.Scale('./images/backgrounds/bg foyer.jpg', 1280, 720)
image bg schoolback = im.Scale('./images/backgrounds/bg schoolback.jpg', 1280, 720)
image bg hallway = im.Scale('./images/backgrounds/bg hallway.jpg', 1280, 720)
image bg library = im.Scale('./images/backgrounds/bg library.jpg', 1280, 720)
image bg study = im.Scale('./images/backgrounds/bg study.jpg', 1280, 720)
image bg pool = im.Scale('./images/backgrounds/bg poollounge.jpg', 1280, 720)
image bg gym = im.Scale('./images/backgrounds/bg gym.jpg', 1280, 720)
image bg weights = im.Scale('./images/backgrounds/bg weightroom.jpg', 1280, 720)
image bg club = im.Scale('./images/backgrounds/bg clubroom.jpg', 1280, 720)
image bg park = im.Scale('./images/backgrounds/bg park.jpg', 1280, 720)
image bg class = im.Scale('./images/backgrounds/bg classroom.jpg', 1280, 720)
image bg home = im.Scale('./images/backgrounds/bg livingroom.jpg', 1280, 720)

# The game starts here.
label start:

    python:
        playerName = renpy.input("What is your name?")
        playerName = playerName.strip()

        if not playerName:
            playerName = "Player"

    jump start_game
