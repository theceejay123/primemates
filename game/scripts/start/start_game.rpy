#  Start of Prime Mates

label start_game:
    scene bg room
    with fade
    play music[chillguitar, chillpiano] fadeout 0.5 fadein 0.5

    "PLAYER HOME --- December 14th"
    nvl clear

    # Player
    p """
    Exhausted.

    I haven’t even started unpacking the boxes downstairs.

    It hasn’t been long since I arrived, and I already dread the cold snowy wasteland that is {b}Messadonna{/b}.

    The sun is still shining brightly through the window, but I remember how fast that changes in the winter.

    If I hurry up, I may still make it in time to shower and clean up before I head to the park to meet up with my old friend, Sam. 
    
    We have a lot to catch up on, and I may not be as used to this neighborhood as I used to be.

    I wouldn’t want to show up a mess, especially since it’s been over a year since I last saw them…

    In a couple weeks, I will be starting my first day as a junior student at {b}Mackena High School{/b}. 
    
    Sam has offered to give me a tour of the school, after they have finished writing their final exams during exam week.
    
    I’m extremely excited to see some old faces, as I am to meet new ones. 
    
    I’ve spent the last few years tirelessly studying day and night to maintain myself at peak academic performance. 
    
    But, this year, it will be different.
    
    Although I strive to be an excellent student in all shapes and forms, frankly, my extracurriculars have been lacking… 
    
    And so, in order to secure my scholarships I must  join one of the many clubs that Mackena High has to offer.
    
    Maybe it’ll even teach me a thing or two. Something I would have never experienced just studying at home.
    
    Maybe I’ll find myself partaking in the fine arts, I’ve always appreciated the elegance of it. 
    
    Or maybe, something to do with Makenna’s music program! 
    
    That could be fun! I could join the photography club, the debate team, or maybe even the school musical! 
    
    The options seem endless. And although it may be a little exhausting, maybe I could even help out a sports team. 
    
    It’s wonderful that Mackena High has such great facilities. There truly is something for every student.
    
    And more importantly…{p}Maybe this year I’ll meet someone special! 
    
    Someone witty. 
    
    Someone who appreciates personal space.
    
    Someone confident. 
    
    Someone charming.
    
    Someone romantic. 
    
    Someone down to earth. 
    
    Or perhaps just someone who doesn’t take themselves too seriously. 
    
    But in the end, all that really matters is that I can be myself around them.

    """
    stop music
    play sound alarm

    p "Ahhhh!!"

    stop sound

    p "Oh! I better get going or I’m going to be late"

    play music jazzyguitar

    scene bg park with fade

    play sound bird

    "You hurry off to the nearby park. It’s been a while but it doesn’t seem like that much has changed since you moved away."
    nvl clear

    "The tall evergreen trees still line the street, and the squirrels still scurry across the fences towards bird feeders dusted with snow. It’s just how you remember it."
    nvl clear

    "When you arrive, you find a familiar face waving at you from the park bench. It’s your friend Sam."
    nvl clear

    sam "Hey!"

    show sam normal at left

    sam "Long time no see! How’s the family?"

    p   "Hey Sam! Everyone’s doing well."

    p   "Mom's got her old job at the hospital back, she's working night shifts for now but she’s hoping that’ll change sometime soon."

    sam "Good for her, she’s always been such a hard worker. I’m sure the other nurses are happy to have her back on the team."

    sam "And how’s your Dad? Is he still force-feeding his homemade chili to the neighbours?"

    p   "Of course he is, I haven’t been gone that long. He just made a fresh pot this morning."

    p "They said they’d love to see you and your family soon. Maybe have another karaoke night."

    sam "I’ll let them know. I’ll be sure to do my vocal warmups and save some room for your dad’s chili."

    sam "Anyways, I’m glad to hear everyone is well. I know it’s stressful for you guys when your dad has to move around for work."

    p   "Yeah, I’m just glad I’m back in familiar territory. Aside from the school, of course."

    sam "Do you still need a tour around the old place? Or will you be alright on your own?"

    stop sound

label prologue:
    menu:
        "Continue":

            p "Well it's been a while. It would help to have you show me around."
            jump tour_start

        "Skip Prologue":
            "{b}Warning, there is a lot of content you will miss by skipping the prologue, are you sure?{/b}"
            nvl clear

    menu:
        "Yes":
            jump prologue_end

        "No":
            jump prologue

label tour_start:

    sam "Let’s start with the tour then!"

    sam "In that case, let's head to the mall first, since it’s closest and so much has changed since you’ve last been there."

    sam "Let’s go!"

    hide sam

    scene bg worldmap with fade

    "{b}This is the World Map.{/b}"
    nvl clear

    "{b}From here you can travel to different locations. Currently you are at the park. Indicated by the symbol.{/b}"
    nvl clear

    "{b}To enter any location. Simply click the icon above the name.{/b}"
    nvl clear

    "Coding Start World Map Interactables"

    sam "We’re not quite done yet! Let’s hit the mall before we go there."

    "Coding End"
    nvl clear

    scene bg mall with fade

    "You both make your way inside the mall. Much to your surprise, it seems like a lot has changed. There are many unfamiliar stores in spots where you last remember there being a different one."
    nvl clear

    show sam normal at left

    p "Wow. It's nearly completely different."

    sam "I know right? The food court in particular got a huge renovation about a year and a half ago."

    sam "Anyways, onwards to the main event!"

    "Coding Start Exit Scene"
    nvl clear

    "{b}To leave the current location, click the return icon on the bottom left of the screen.{/b}"
    nvl clear

    scene bg worldmap with fade

    "Coding Start World Map Interactable"

    "If player clicks House and Park"
    nvl clear

    sam "We’re not quite done yet! We’ve only got a few more stops at the school!"

    scene bg school with fade

    play music[chillguitar, chillpiano] fadeout 0.5 fadein 0.5

    "You both arrive at Mackena High."
    nvl clear

    "The school entrance on it's own seems a cut above the other school’s you’ve attended. The large courtyard is decorated with maroon flags sporting a symbol of an ape."
    nvl clear

    sam "Welcome to Makenna High!"

    sam "I know it’s a little intimidating at first, but I promise it’s not as scary as it seems!"

    p "Well it's about as intimidating as it is exciting! I can’t wait to see what’s inside!"

    "{b}This is the School Map.{/b}"
    nvl clear

    "{b}From here you have access to every location at school. Head into Foyer to get started!{/b}"
    nvl clear

    scene bg foyer with dissolve

    "The foyer is lined with trophy cases and pictures of Mackenna’s previous graduating classes."
    nvl clear

    sam "This is the foyer where students usually hang out and chat between classes."

    sam "Let’s head out these back doors.{p}"

    scene bg schoolback with dissolve

    "You can see a flag post close by and a field with goalposts and bleachers in the distance."
    nvl clear

    sam "This is another place that always seems to be full of people. Lots of students use the flag pole as a meeting spot."

    sam "Let’s head back inside for now."

    scene bg hallway with dissolve
    play sound hallway

    "The hallway is lined with classrooms, lockers, and the occasional maroon flag."
    nvl clear

    sam "This is one of the main hallways in the school. It can get pretty crowded during class change."

    sam "I’ll show you the library next, it’s right over there. Come with me!"

    stop sound

    scene bg library with dissolve

    "There are long tables at the center of the library and couches along the perimeter. All of the walls are completely covered with books."
    nvl clear

    sam "Here we are! This is where some people come to study, usually in groups. It’s a nice quiet hangout spot."

    p "I can’t get over how many books there are!"

    sam "Yeah, the library is super well stocked. It’s not the best if you want to study alone though; I’ll show you where that is."

    scene bg study with dissolve

    "Desks line the room, some separated by dividers. A few desktop computers sit at the back of the room."
    nvl clear

    sam "Here’s the best place to study. Hence the name; {i}study room{/i}"

    p "Such a creative name."

    sam "Just wait until you see the {i}music room{/i}"

    scene bg music with dissolve

    "One long, stretching wall is completely lined with instruments of all sorts. Guitars, basses, drums, pianos, and so much more."
    nvl clear

    p "Well it certainly lives up to its name."

    sam "It certainly does. Lots of different music classes take place here, and whenever there aren't any classes, people would come in on their free time to play music."

    sam "Anyways, let’s continue."

    scene bg pool with dissolve

    "You see several pool tables as well as a couple of couches against the window. Several racks at the center of the room holds pool cues."
    nvl clear

    p "This is so cool, I’ve never seen a school with a billiards club before!"

    sam "It is pretty cool, isn’t it? I wish i knew how to play. The people who usually hang out here are super cute."

    p "All the more reason to learn."

    sam "That’s true. Maybe we’ll play a game here later this year and be each other's wingmen."

    sam "Though, nobody is here right now so there’s no real point in staying. Let’s keep going."

    scene bg gym with dissolve

    "You walk into the massive open gym. You see various types of equipment, the bleachers, and the many coloured grid lines on the floor."
    nvl clear

    p "Woah, this is humongous!"

    sam "I know. It’s the pride of the school. Everything happens in here. Pep rallies, outside events, performances, you name it."

    sam "It has nearly enough space to hold almost a thousand people, even with the stage set up."

    sam "Let’s keep going before your jaw drops to the floor completely."

    scene bg weights with dissolve

    "Inside you find padded flooring unique to the weight room. Machines, racks, weights and all variations of exercise equipment are scattered evenly throughout the room."
    nvl clear

    sam "So, if your jaw wasn’t hanging low enough, this is our weight room!"

    p "This…{p}This certainly seems expensive…"

    sam "I’m not quite sure how much it costs but I’d have to agree."

    sam "The best part here is the environment. All types of students come in here to do their thing, everyone’s respectful."

    sam "We’re almost done, one last bunch of places to go!"

    scene bg club with dissolve

    "Walking by, Sam tells you about the various club rooms in school. Some of the rooms are multi-purpose shared by multiple clubs while some are dedicated. You stop in front of a bulletin board."
    nvl clear

    show board

    sam "...So all the rooms I just showed you were all club rooms."

    sam "This here is the bulletin board showing the names of all the active clubs in school as well as their club room number and their scheduled time slots."

    p "There sure are a lot of clubs in this school. I didn’t even know bird watching needed its own club!"

    sam "I know. Anything with enough members with a teacher supervisor can become a club."

    p "I was interested in joining one of the clubs actually… there seem to be a few openings here."

    sam "Just go see the supervisor when school starts if you ever find yourself interested in joining one."

    sam "It will say right here on the board where you can find them."

    p "That’s good to know!"

    sam "Well, that’s pretty much everything important. We’ll take a brief look at where to find your classes on our way back out of school."

    p "That sounds like a great idea."

    "..."

    scene bg school with fade

    sam "So that was the tour of Mackena High! It’s a lot to take in, I’m sure."

    p "Yeah, it absolutely is."

    p "But I think I’ve got the gist of things, and it’ll only get better when school starts."

    sam "That’s the spirit! Just keep up that attitude and you’ll be absolutely terrific!"

    p "Thanks for showing me around.{p}Shall we head back to my place? My dad would love another homemade chili victim."

    sam "Absolutely! If anything, it would be my pleasure.{p}Let’s go!"

    "After an eventful day of seeing the city, catching up with your old friend, and stuffing your face with chili,  you retire for the day."
    nvl clear

    scene bg room with fade

    "...{p}"

    "You spend the next couple of weeks preparing your school supplies. Inside your backpack lies everything on the list of required supplies and personal items."
    nvl clear

    "In the meantime, your family visits Sam’s family and vice versa, showing each other your new living spaces."
    nvl clear

    "Both you and your parents have spent the holiday season to spend as much time catching up with old friends as possible."
    nvl clear

    "In what seems like the blink of an eye, weeks pass, and the first day of school arrives."
    nvl clear

    scene bg room

    play music[chillguitar, chillpiano] fadeout 0.5 fadein 0.5

    "{b}Player Room: January 6th{/b}"
    nvl clear

    p "Today’s the day! The first day of school!"

    p "With so much nervous energy building up the past couple of weeks, I don’t know how I’ll manage…{p}But I’m excited nonetheless!"

    p "I hope that there’s still good options up on the club posting board."

    p "Aside from my studies, I think that will be the most pivotal in deciding how the rest of my year will turn on out."

    p "Fingers crossed!"

    play sound phone

    "{i}%(playername)s received a notification on the phone Icon.{/i}"
    nvl clear

    p "That must be Sam. I didn’t want to go to school by myself on the first day so I asked them to come by so we could go together."

    p "Although I should be more used to transferring schools by now, I still can’t help but be nervous each time."

    p "I should see what they said."

    "Coding Start Phone"
    nvl clear

    p "My contacts list is a little empty at the moment…"

    p "I hope that changes in a few weeks!"

    "{b}As the game progresses, certain dialogue can be accessed through a form of texting or calling. Much like dialogue you will encounter with the characters, it is important to check your phone frequently.{/b}"
    nvl clear

    "{b}You will be notified at home if you have received a message, or if you are eligible to start a conversation with a character after school.{/b}"
    nvl clear

    "{b}In some cases, dialogue will not progress without checking your phone, so make sure to check it at all times!{/b}"
    nvl clear

    play sound notification

    "{i}It seems that Sam has left a message.{/i}"
    nvl clear

    sam "Be there soon!"

    play sound knock

    "As if on cue, you hear a sudden knocking at your door. You quickly rush over to answer it. It’s Sam."
    nvl clear

    stop sound

    show sam normal at left

    sam "I’m here!"

    p "You’re so early! We’ve still got almost an hour before school starts!"

    sam "Well, seeing as it’s your first day, I personally wanted to be here to make sure you were prepared and had everything you needed!"

    sam "I’ll pack and re-pack your stuff for you. Go on and get yourself dressed and washed up!"

    p "A-alright. I’ll get to it right away!"

    hide sam normal

    "You grab an outfit out of your dresser and flash it to Sam for approval."
    nvl clear

    "Sam seems to have already begun rummaging through your backpack, crossing off a familiar supplies list. Sam seems to have brought their own."
    nvl clear

    p "How’s this for first impressions?"

    show sam normal at left

    sam "In my opinion, you’ll look great in anything you wear. But yes, that’s a terrific choice!"

    p "Thanks!"

    p "By the way, have you eaten breakfast?"

    sam "Not yet, I figured your dad would be excited to show me a new recipe of his."

    p "He is. I’ll let him know you’re hungry."

    p "I’ll be right back!"

    hide sam normal

    "You spend some time washing up and getting changed. You invite Sam for breakfast afterwards.{p}The rest of the morning goes by eventfully."
    nvl clear

    p "Well, it’s about time to leave. See you later Mom and Dad!"

    show sam normal at right

    show dad at left

    show mom at center

    dad "Make sure to make as many friends as you can! More taste testers for my new chili recipe…"

    mom "Oh be quiet. You take care %(playername)s. And thank you, Sam."

    sam "No problem!"

    p "Let’s get going!"

    scene bg map with fade

    "Code Unfinished"
    nvl clear

    scene bg school with dissolve

    "Much different from the view from a couple of weeks ago, the vast open courtyard seems to have relatively shrunk in size as the crowds of students flood in towards the building."
    nvl clear

    "Still the sheer volume of students at a glance have spread out filling out every vacant space, making the school look momentarilly larger."
    nvl clear

    "You can see that there are students of all backgrounds, each dressed uniquely to their own preference, coloring the field in a bright and vivid mosaic."
    nvl clear

    p "Wow…{p}It looks much bigger now that I’m actually here during classes…"

    show sam normal at left

    sam "The worst part is, as you’ll soon find out is the traffic. Which is why I came to pick you up so early."

    sam "Though I suppose it’s good that the students here are quite punctual."

    p "I’m glad I have a person on the inside to show me around. It would have been embarrassing to be late because I was at the back of the pack"

    sam "Of course!"

    sam "Typically, we have an assembly in the gym later on in the day as a kind of an {i}opening ceremony{/i} type thing."

    sam "It’s usually just to let the students know of any changes and what not. But first we’ll get you to your homeroom class for attendance."

    hide sam normal

    scene bg hallway

    play sound hallway

    "Walking through the school, you notice that there are many papers hung up in the hallways."
    nvl clear

    "Various application forms, advertising, school notice signs have been strung along the bulletin boards in the hallway."
    nvl clear

    "After a short while, you arrive in class."
    nvl clear

    show sam normal

    sam "It doesn’t really matter where you sit by the way so just pick anywhere you’d like. Anyways, I’ll see you at lunch time!"

    p "See you!"

    hide sam normal

    stop sound

    scene bg class

    "You enter the classroom."
    nvl clear

    "Inside there seems to be a few students already seated. The room appears to be organized and well spaced, with roughly 24 desks arranged in gridlike rows."
    nvl clear

    "The teacher, a friendly-looking balding man in a checkered shirt, greets you briefly and gestures towards the few remaining vacant seats."
    nvl clear

    "There seems to be a vacant spot by the window, at the back corner of the class, by the front and just by the door."
    nvl clear

    "Where would you like to sit?"
    nvl clear

    menu:

        "By the window.":
            jump seat

        "At the back.":
            jump seat

        "At the front.":
            jump seat

        "By the door.":
            jump seat

label seat:

    "You quickly find an empty seat to sit down. After a few more students arrive, the teacher quickly begins class."
    nvl clear

    show teacher

    t "Hello students~"

    t "I’m glad to see that all of you have made it back from your {i}hopefully{/i} relaxing winter holidays."

    t "As with the new semester, we also have a brand new face here today."

    t "I’d like to call your name first, and when I call you, please stand up, tell us your name, and a little bit about yourself."

    "You stand up. Although a bit nervous, you confidently introduce yourself."
    nvl clear

    t "%(playername)s"

    p "Hello! I am %(playername)s."

    p "Due to my dad’s career, I’ve had to transfer from school to school. This will be the last time I transfer, so I hope to get along with the rest of the class!"

    play sound smallapplause

    t "Thank you, that was wonderful"

    stop sound

    t "So, now we know that %(playername)s is here, let’s get on with the rest of attendance!"

    "A few of the students quickly introduce themselves as you take a seat."
    nvl clear

    "The attendance goes by quickly. Shortly after, the announcements come on followed by a very bright and energetic voice."
    nvl clear

    stop music

    play sound mic

    sn "Helllllllloooo Mackenamites!"

    play music[chillguitar, chillpiano] fadeout 0.5 fadein 0.5

    sn "It is me, Charlie! And I have returned yet again as the school's news idol!"

    sn "As you all know, today is the first day of school for the second time this year!"

    sn "As such, I will be calling down the classes for the semester assembly!"

    "The roll call goes by relatively quickly. You suppose that it’s due to the very organized structure of the building. After a while, your class is called down to the gymnasium."
    nvl clear

    "…"
    nvl clear

    scene bg gym

    play sound hallway

    "The gym is packed full of students, strewn along the bleachers that have been set up along the back wall."
    nvl clear

    "You notice Sam in the distance waving at you as they sit along with their classmates."
    nvl clear

    "After everyone has finished taking a seat, the speakers turn on and a deep voice cuts through the clambering of the crowd."
    nvl clear

    show principal

    stop sound

    play sound mic

    pr "Hello students."

    pr "I would like to welcome you all back here for another semester at Mackena High."

    pr "I would also like to welcome those who will be spending their first semester here."

    pr "I hope that you find Mackena High to be a very friendly and supportive environment."

    pr "I would just like to address that the washroom on the third floor is strictly forbidden."

    "Your teacher, who is sitting near you, turns to you."
    nvl clear

    hide principal

    show teacher

    t "It’s not actually forbidden. It’s simply out of order. He just likes to say that."

    hide teacher

    "The rest of the assembly goes by uneventfully."
    nvl clear

    "As you return to class, you find yourself better acquainted with the other students."
    nvl clear

    scene bg class

    "The remainder of class goes by smoothly, and during transitions you have no issues in finding your other classes. As if in no time at all, it’s lunch time."
    nvl clear

    "You leave and head to the club corridor as you wait for Sam."
    nvl clear

    scene bg hallway

    play sound hallway

    "Taking a look at the bulletin board, you notice that many of the clubs have been filled up since you last checked it weeks ago."
    nvl clear

    show board

    "It appears that the only club available is the Rugby Club, as the manager."
    nvl clear

    p "Darn!"

    p "I thought there were way more options than this!"

    p "If I want to stay on top of my scholarships, I don’t think I have any other choice…"

    p "It says here to talk to the supervisor… which happens to be Ms. F."

    hide board

    show sam normal

    sam "Hey! Did you wait long!"

    p "Hey Sam! I was just looking at the club bulletin board. It seems the only club available is the Rugby club…"

    sam "I would have never pinned you for a rugby player…"

    p "No it’s as the club manager. Do you happen to know where to find Ms. F?"

    sam "She’s the school librarian. We’ve got time so I’ll head over there with you."

    stop sound

    scene bg library

    show sam normal at left

    sam "Here we are, she’s just over there by the front desk."

    "..."
    nvl clear

    p "Uhm… excuse me."

    "After a short moment of fumbling, Ms. F greets you at the front desk."
    nvl clear

    show librarian at right

    mt "Hello there, how can I help you?"

    p "I heard you were the supervisor for the school rugby team."

    p "I was wondering if I could join."

    mt "A new member! Absolutely! The team would be so delighted!"

    mt "May I have your name?"

    p "It’s %(playername)s."

    mt "Excellent. The first meeting will be in club room 14 after school."

    mt "Do you happen to know anything about the sport? If you don’t I’d be more than happy to give you a summary."

    menu:

        "Accept.":

            jump accept_summary

        "No, it's alright.":
            jump skip_library

label accept_summary:

    p "That would be wonderful."

    mt "Alright, this may take a moment."

    mt "First of all, Rugby is a contact sport played mainly in teams of 15 or 7."

    mt "The main noticeable difference between the two is the available space. Since it is more crowded in 15s there are different tactics."

    mt "Otherwise, the rules are largely the same."

    mt "With teams of 15, the games last about 80 minutes while teams of 7 have games going on for 15 minutes."

    mt "Unfortunately due to the lack of interest, the school only has a 7s rugby team."

    mt "The defining aspect of the sport centers around how the ball must always {b}travel backwards{/b}."

    mt "This forces the players to run it forward or alternatively they can risk possession by kicking it instead."

    mt "The goal for each team is to take the rugby ball all the way down onto the other team's endzone for a {b}Try{/b}, which is the rugby term for a goal or a touchdown."

    mt "This is done by placing the ball down on the end zone, {b}this is worth 5 points{/b}."

    mt "Afterwards, they can attempt a {b}conversion worth 2 points{/b} by kicking the ball through the field goal typically from where the ball was placed down."

    mt "Alternatively, they can kick the ball through the field goal by a {b}drop kick{/b}."

    mt "This is a style of kicking where the ball must first bounce off the ground anytime during open play for {b}3 points.{/b}"

    mt "Usually, at the high school level, the game comes to a stop for {b}scrums{/b}, {b}penalties{/b} and {b}line-outs{/b}. Which I will leave for the coach to explain to you."

    mt "If that doesn’t make sense right away, I’m sure you will catch on quickly in the club."

    p "I will try my best!"

    jump library_tutorial

label skip_library:

    p "No it’s alright. I’m familiar with the sport."

    mt "That’s great! If you have any specific questions, the coach would be more than willing to answer all your questions."

label library_tutorial:

    p "Thank you. In that case, I’ll drop by right after my classes are done after school!"

    mt "Anytime, if you ever have any questions about anything, please come see me."

    scene bg hallway

    play sound hallway

    show sam normal

    sam "Would you like me to come with you later on?"

    p "It’s alright, I should be fine. These things are my responsibility after all."

    sam "Alright. Well, I suppose we should have lunch and get to class."

    p "My dad said to share my lunch with you today. You’ll have to let him know how it tastes."

    hide sam normal

    "Lunch period goes by eventfully."
    nvl clear

    stop sound

    scene bg class

    "The rest of the classes for the rest of the day act as introduction for all the content for the semester."
    nvl clear

    "You diligently map out a study plan during each class for better efficiency."
    nvl clear

    p "If I’m going to be busy with the club, I have to make sure I’m on top of my school work!"

    "In no time, the bell rings and classes for the day are over."
    nvl clear

    "The excitement of the first day keeps momentum as you make way to club room 14. Shrugging off the nervousness, you head inside."
    nvl clear

    scene bg club

    p "It doesn’t seem like anybody is here yet…"

    p "Rugby is a bit of a rough sport…{p}I hope that the members are gentler in person."

    show coach at left

    hc "Oh. A new member?"

    p "Oh! Hello! I’m hoping I could be, I saw that this team needed a manager and I thought that I could have the honor."

    play sound hc

    hc "Relax.{p}The members would be more than delighted to have you on the team. I’m the coach for the team. I’m not a teacher so just call me coach."

    stop sound

    p "It’s nice to meet you. I’m %(playername)s."

    hc "Do you know anything about the sport?"

    p "I know a little bit. Ms. F. said I could come to you if I have any questions."

    hc "Absolutely, but we’ll go on about that on our first practice. For now we’ll wait for the members to arrive so we can introduce ourselves."

    "…"
    nvl clear

    show Angelo at right

    "The first member walks in."
    nvl clear

    a "Heya coach. You get drunk during new years again this year?"

    hc "Hey, quiet down! Don’t you remember how Ms. F. berated me last time?"

    hc "Anyway, come over here and meet your new team manager, %(playername)s."

    a "Ah! Sorry that I didn’t notice you right away! I’m Angelo."

    p "It’s alright!"

    a "We’ve been looking for a manager all year. I’m glad you’re interested."

    a "...{p}I suppose I should say a little more about myself."

    a "I’m the team captain. I play as number 5, the fly-half."
    nvl clear

    a "I’m not sure if it matters to you but I’ll in my junior year. It’s nice to meet you!"

    p "It’s nice to meet you too!"

    "As he gently shakes your hand, his deeper tone catches you slightly off guard."
    nvl clear

    "His initial presence gives off the sense that he has a more laid back nature, complemented with a hint of humor."
    nvl clear

    "His confidence and friendly posture all seem to indicate that you will be in good hands."
    nvl clear

    hide Angelo

    "..."
    nvl clear

    "Your first impressions of the team are that of familial intimacy, although it’s a bit daunting, the environment overall feels to be quite welcoming."
    nvl clear

    "Everyone seems to know each other well in a very comfortable setting."
    nvl clear

    "Although it may take some time getting used to, the prospects of being their manager seem like it will turn out to be interesting."
    nvl clear

    hide Angelo

    hc "Alright, let’s give one round of applause for the new member."

    play sound smallapplause

    stop music

    hc "Now, let’s get started."

    stop sound

    play music[epic] fadeout 1.0 fadein 1.0

    hc "I understand that the team has done well in the past couple of years, we’ve shown tenacity and skill showing all the other schools that we are not to be underestimated."

    hc "But, despite our efforts, we have never come out on top."

    hc "I know that for some of you, this will be your final year."

    hc "As I know what each of your plans are after graduation, this means that this is also your last chance to bring home a trophy."

    hc "I know that each of you have talent, and where talent fails, hard work pulls through."

    hc "As your coach, I will not let you down. I will work you through every pain and obstacle you must endure on the field."

    hc "And with the logistical help of our new manager, you can persevere with focus."

    hc "As such, I trust that each of you will keep up practicing diligently. I hope to see the best of the best performance."

    hc "Do you all understand!?"

    play sound whoo

    play sound smallapplause

    "The room erupts with a resounding agreement."
    nvl clear

    stop sound

    stop music

    hc "Alright. That’s all for today. First practice will be in on the weekend in two weeks at noon. I expect to see you all there on time. You are all dismissed!"

    play music[chillguitar, chillpiano]  fadeout 0.5 fadein 0.5

    hc "%(playername)s. You are all set to go, I have received your school information from Ms. F.{p}Welcome to the team."

    p "It’s my pleasure!"

    play sound smallapplause

    stop sound

    hide coach

    show Angelo

    a "I’m sorry I can’t stay longer, %(playername)s. But I’ve still got to run around school and talk to a few more teachers."

    a "I’ll see you around!"

    p "That’s alright! Take care!"

    "..."
    nvl clear

    play sound schoolbell

    "..."
    nvl clear

    stop sound

    "After a productive day. You head home."
    nvl clear

    stop music

    play music[chillguitar, chillpiano] fadeout 0.5 fadein 0.5

    scene bg home with fade

    p "I’m home!"

    show dad at left

    dad "How was school kiddo?"

    p "It was great! I met some interesting characters and I can already expect that this semester will be a fun one!"

    dad "I’m glad to hear that."

    dad "Anyway, your mother will be working the evening shifts for now. Unfortunately, that’s the only position that they have available at the moment."

    p "That’s alright. It’s only for a short while."

    p "Anyway, I’m gonna get to my room and get myself organized for the semester."

    dad "Sounds like a great idea."

    scene bg room

    "You head upstairs to organize your courses into their own separate folders, each sectioned off into the units discussed earlier in your classes."
    nvl clear

    "You pin up a fresh new year calendar, scribbling in the school schedule as well as  upcoming rugby practices."
    nvl clear

    p "I should always keep this up to date for upcoming events just in case I forget…"

    "{b}Throughout the month, there will be a two week cycle. The first week will always consist of two school days: Tuesday and Thursday.{/b}"
    nvl clear

    "{b}Afterwards, the second week will follow with one school day and a day off on the weekend.{/b}"
    nvl clear

    "{b}This cycle will occur at the end of every second week for a total of two cycles each month.{/b}"
    nvl clear

    p "I’ll cross out each passing day, just so I don’t get confused…"

    "{b}The days will cycle between day and evening. On a day cycle, you will have the opportunity to interact with all the available characters attending school that day.{/b}"
    nvl clear

    "{b}Once you have returned home, the game will progress into the evening cycle. Primarily you will have the option to text available characters.{/b}"
    nvl clear

    "{b}When certain criteria are met, the option to attend special events may also become available to you.{/b}"
    nvl clear

    "…"
    nvl clear

    p "Well, it’s getting pretty late. That should be enough preparation for the entire semester!"

    play sound notification

    "{i}You have 1 unread message. {/i}"
    nvl clear

    "You open your messages. Sam has sent a text."
    nvl clear

    sam "Hey! How did joining the club go?"

    p "Although I was a little nervous at first, it went well!"

    p "The coach and supervisor seem to be quite friendly. The same goes for all the other players too. They all seem to get along quite well."

    sam "That’s wonderful!"

    sam "In that case… has anybody caught your eye yet?"

    p "Well. They do all seem quite charming in their own way."

    p "I’m not sure. I’ve only just gotten back to the city and into a new school. I wouldn’t want to rush anything…"

    sam "So the answer is, all of them.{p}But, of course, I understand your point."

    "{b}Upon reaching a certain point in a character’s dialogue, you will encounter a Go Out With Me! event in which that character will ask you out romantically.{/b}"
    nvl clear

    "{b}In these moments, you will have the opportunity to date only one player, unlocking further dialogue and content for that player exclusively.{/b}"
    nvl clear

    "{b}Although you are restricted to one relationship, you will have the opportunity to break up with that player in the form of another Go Out With Me! event.{/b}"
    nvl clear

    "{b}In this case, accepting the new proposal will end your current relationship.{/b}"
    nvl clear

    "{b}Regardless, you will be able to get to know each character as they will independently have corresponding story lines.{/b}"
    nvl clear

    p "If I change my mind, you will be the first to know."

    sam "Well, that’s all I wanted to know! Haha. I’ll see you at school tomorrow!"

    p "See you!"

    "..."
    nvl clear

    p "What a long day..."

    p "With a new school, and new people…{p}There sure is a lot to look forward to!"

    p "For now, I suppose I should get to bed. I wouldn’t want to be late tomorrow morning..."

    "..."
    nvl clear

label prologue_end:
    jump chapter_one
