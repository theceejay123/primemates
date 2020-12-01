# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    # define characters and narrator
    $ narrator = nvl_narrator
    $ p = Character("[playername]", color="#C8FFC8")
    $ a = Character("Angelo", color="#000080")
    $ sam = Character("Sam", color="#C8C8FF")
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
    # define all sounds
    $


# The game starts here.

label start:

    jump start_game

label start:

    scene bg room

    play music "chillguitar.mp3"

    narrator "PLAYER HOME – December 14"

    p """
    
    Exhausted.
    
    I haven’t even started unpacking the boxes downstairs.
    
    It hasn’t been long since I arrived, and I already dread the cold snow wasteland that is Messadonna..
    
    The sun is still shining brightly through the window, but I remember how fast that changes in the winter.
    
    If I hurry up, I may still make it in time to shower and clean up before I head to the park to meet up with my old friend, Sam. We have a lot to catch up on, and I may not be as used to this neighborhood as I used to be. 

    I wouldn’t want to show up a mess, especially since it’s been over a year since I last saw them…

    In a couple weeks, I will be starting my first day at Mackena High School. Sam has offered to give me a tour of the school after they are finished writing their final exams during the first semester of exam week.
    
    I’m extremely excited to see some old faces, as I am to meet new ones. 

    I’ve spent the last few years tirelessly studying day and night to perform at the peak of what it truly means to be an academic. 

    But, this year, it will be different.

    I strive to be an excellent student in all shapes and forms, and frankly, my extracurriculars have been lacking… 

    And so, in order to secure my scholarships I must  join one of the many clubs that Mackena High has to offer.

    Maybe it’ll even teach me a thing or two. Something I would have never experienced just studying at home.

    Maybe I’ll find myself partaking in the fine arts, I’ve always appreciated the elegance of it. 

    Or maybe, something to do with Makenna’s music program! That could be fun! I could join the photography club, the debate team, or maybe even the school musical! 

    The options are truly endless. And although it may be quite exhausting, I could even help out a sports team. 

    It’s wonderful that Mackena High has such great facilities. There truly is something for every student.

    And more importantly… maybe this year… I’ll meet someone truly special! 

    someone with wit. 

    someone who appreciates personal space.

    someone confident. 

    someone charming.

    someone romantic. 

    someone down to earth. 

    or someone who doesn’t take themselves too seriously. 

    But in the end, all that matters is someone who I can truly be myself around.

    …

    """

    play sound "alarm.mp3"

    p "ahh"

    play sound "alarm.mp3"

    p "Oh! I better get going or I’m going to be late!”

    bg park

    narrator "You hurry off to the nearby park. It’s been a while but all it doesn’t seem that much has changed since you moved away."

    narrator "The tall evergreen trees still line the street, and the squirrels still scurry across the fences towards bird feeders dusted with snow. It’s just how you remember it."

    narrator "When you arrive, you find a familiar face waving at you from the park bench. It’s your friend Sam."

    show sam normal

    sam "Hey [playername]"

    sam "Long time no see! How’s the family?"

    P "Hey Sam! Everyone’s doing well. Mom got her old job at the hospital back, she;s working night shifts for now but she’s hoping that’ll change sometime soon."

    Sam "Good for her, she’s always been such a hard worker. I’m sure the other nurses are happy to have her back on the team."

    sam "And how’s your Dad? Still force-feeding his homemade chili to the neighbours?"

    P "Of course he is, I haven’t been gone that long. He just made a fresh pot this morning. They said they’d love to see you and your family soon. Maybe have another karaoke night."

    Sam "I’ll let them know. I’ll be sure to do my vocal warmups and save some room for your dad’s chili."

    Sam "Anyways, i’m glad to hear everyone is well. I know it’s stressful for you guys when your dad has to move around for work.

    p   "Yeah, I’m just glad I’m back in familiar territory. Aside from the school, of course."

    Sam	"Do you still need a tour around the old place? Or will you be alright on your own?”

    return

    return
