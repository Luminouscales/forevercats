# Everything is impermanent and transient. Especially bits on a disk. No use crying over flipped bits.

import random
from functools import partial

debug = True # Shows background stuff like flag changes and locked dialogue flags

# All flags, globally.
tbl_flags = {
    'meow': False, # Flag test. Meow meow meow!
    'unique': False, # Told Debug you want to be unique
    'lr_sawjoint': False, # Saw the joint in the bowl already
    'lr_havejoint': False, # Took the joint from the bowl
    'lr_smokedjoint': False, # Smoked the joint
    'lr_havelighter': False, # Picked up your lighter from the kitchen
    'lr_snortedshit': False, # Slammed the unidentified powder from underneath the table
}

# Skillpoints

# Electrochemistry 
# Ars feline
# Encyclopedia
# Debugging

#text = '"Hi, I`m a placeholder cat!"\n'

# Prints only in debug mode. Has a random bracket message because cute
debugroll = [ "DEBUG", "Check this out!", "Meow", "Meow meow", "Thank me later", "Sure!", "Easy.", "Esoteric!", "Prowling" ]
def PrintDebug(text):
    if debug:
        print(f"[{ debugroll[random.randint(0, len(debugroll)-1)] }] {text}")

# Gives the current bool of the flag in string
# booolea yea yea
def ReturnFlag(flag):
    return tbl_flags[flag]

# Sets the given flag to given bool. Shows if debug enabled
def SetFlag( flag, bool ):
    old = tbl_flags[flag]
    tbl_flags[flag] = bool
    PrintDebug( f"Flag '{flag}' set to {tbl_flags[flag]}, was {old}." )

# Shows a ... that you have to press enter to move. Like a continue
def skip():
    print( input("\n...\n") )

# Line skip without pressing enter
def skipfast():
    print( "" )

# Shows the list of possible responses
def doinput( text, table ):
    print( "\n" )

    # You can put None into first value to not show anything
    if text is not None:
        print( text )

    for row in table:
        # A response is in a table if it's conditional. We check [1] if it shows up or not
        if isinstance(row, list):
            if ReturnFlag( row[1] ):
                print( f"{table.index(row) + 1}. {row[0]}" )
            else:
                # Debug shows flag required
                flagstring = ""
                if debug:
                    flagstring = f"({row[1]} is {ReturnFlag(row[1])})"

                print( f"{table.index(row) + 1}. [?] {flagstring}" )
        else:
            print( f"{table.index(row) + 1}. {row}" )

    skipfast()

    # Proofcheck input. Loop if wrong number so you can just choose again. This time hopefully properly
    running = True
    while running:
        response = input("")
        try:
            response = int( response )
        except:
            running = True
        else:
            if response % 1 == 0 and response > 0 and response <= len(table):
                running = False

    return response

# Prints multiple dialogue or a single one.
def PrintNested( text ):
    skipfast()
    if isinstance(text, list):
        for row in text:
            # temp makes sure you don't have to enter through an empty line when the skill check fails.
            # It's returned by DoSkillCheck(). temp is False when it should skip automatically
            temp = True

            # If a value in a dialogue sequence isn't a string it means it's a skillcheck function and we run DoSkillCheck()
            if not isinstance( row[0], str ):
                temp = row[0]()
            else:
                print( row[0] )
                
            # If it's the last line then don't do the ... because it's redundant
            if text.index(row) + 1 != len(text) and temp:
                skip()
        skip()
    else:
        print( text )
        skip()

# Short way to check if dialogue should run depending on flag
def DoConditional( text, flag ):
    if flag:
        PrintNested( text )
    else:
        skip()

# The internal systems of your psyche, with different abilities, thoughts and goals. 
# They're imperfect just like you and will either aid or disadvantage you
# You can choose one which will always talk, the others have only a chance
tbl_skillpoints = {
    'Electrochemistry': True, # Drugs, decadence and the pleasure of having a body. Force ecstasy into your flesh
    'Ars feline': True, # Connection with the kitty realm, also clever thinking and avoiding principles. Pet cats and lie to people
    'Encyclopedia': True, # General knowledge about the items of the world and their histories. Give trivia and be curious
    'Debugging': True, # The ability to approach and solve problems with a cool head, also your bond with technology. Think logically and understand crash logs
    'Serendipity': True # Dreams, premonitions, psychedelia, the fear of obliteration. Talk to your heart and believe what you can't see
}

# Text is the text to be printed and skill is the associated skill, checking if it's active. If not, there's only a chance it will speak.
# We return False here when nothing is said so that you don't have to enter through an empty line.
def DoSkillCheck( text, skill ):
    if skill not in tbl_skillpoints:
        print( f"YOU MISSPELLED {skill}!!")
    elif tbl_skillpoints[ skill ]:
        print( text )
        return True
    elif random.randint( 1, 2 ) == 1:
        print( text )
        return True
    else:
        return False


# Skill check dialogue list
DoSkillCheck_dbsummit = partial( DoSkillCheck, 
    "[DEBUGGING] In retrospect, it is impressive how you got here. Seemingly impossible from the surface, but you reach the altitude of the summit integer by integer.", 
    "Debugging"
)
DSC_eccorporeal = partial( DoSkillCheck, 
    "[ELECTROCHEMISTRY] Lame. Pleasure and corporeality go right paw in paw.", 
    "Electrochemistry"
)
DSC_enunique = partial( DoSkillCheck, 
    "[ENCYCLOPEDIA] Evolution ensures each little leaf of its branch tries different things. For better or for worse.", 
    "Encyclopedia"
)
DSC_encamels = partial( DoSkillCheck, 
    "[ELECTROCHEMISTRY] Distinctly the yellow variant of Dune brand cigarettes. You can tell by the taste.", 
    "Electrochemistry"
)
DSC_afmeowmeow = partial( DoSkillCheck, 
    "[ARS FELINE] The noises of your kin soothe your dry thoughts. A warm lap, somewhere safe.", 
    "Ars feline"
)
DSC_sdcrescent = partial( DoSkillCheck, 
    "[SERENDIPITY] Don't go back. Please. It's nice here.", 
    "Serendipity"
)
DSC_afright = partial( DoSkillCheck, 
    "[ARS FELINE] It's speaking the truth.", 
    "Ars feline"
)


# HUB

# HUB DIALOGUE

if debug:
    texthub = "[DEBUG, THE CODE CAT]\nThe cat is purring quietly. You can't hear it, but you know, because its minute vibrations shake the dewdrops of ennui off your scales.\nIt feels like Debug has got your back.\n"
else:
    texthub = "[DEBUG, THE CODE CAT]\nThe cat is purring quietly. You can't hear it, but you know, because its minute vibrations shake the dewdrops of ennui off your scales.\n"

response1 = '"Can I pet you?"'
text1 = [ ['"Sure, but you won`t feel my fur so it probably won`t be that enjoyable for you."'],
    [ DSC_eccorporeal ] ]
         

response2 = '"This programming stuff is hard."'
text2 = '"You know how it is. Carving the world into something new is understandably challenging."'

response3 = '"Let`s try a special nested sequence."'
text3 = [ ['"Sure! I`ll try to make it simple."'], 
    ['"You know, I`m wondering how we`ll handle all this. But I`m sure you`ll find a way."'],
    [ DoSkillCheck_dbsummit ],
    ['"Coding is all about doing it line by line. Also, I just unlocked a new flag for you. Go try it!"']
]

response4 = ['"How about that special dialogue?"', "meow"]
text4 = [ ['"Right."'], ['"Meow meow meow!"'], ['"That`s it!"'], [DSC_afmeowmeow] ]

response5 = '"Ask me a question."'
text5 = [ ['"Sure."'], ['"Do you desire to be unique?"']]
text5options1 = [ '"Yes."', '"No."' ]
text5a = [['"Hmm, I see!"'], ['"Yes, perhaps everyone strives to become a gem stuck in the crevices of existence."'], [DSC_enunique]]
text5b = [['"Oh."'], ['"How very interesting."'], ['"It`s not surprising. I`ve been watching your thoughts for a long time now."'], ['"I am curious to see where you will find yourself."'] ]

response6 = "I'm really zoned out..."
text6 = [['You are. Air drifts blankly out of your pink muzzle. Feels like a thicket of fog behind your eyes. '], 
         ["Clarity slowly clamping its jaws. If you let it, you won`t be able to go back."], 
         ["Its sharp crescent iris is piercing, waiting. You can smell the foul breath of its pitch black maw."],
         [DSC_sdcrescent]
]
text6unique = "Waiting for its unique little creature."

text6options1 = [ 'Breathe in.', 'Hold your breath for a second longer.' ]
text6exiting = [ ['"Oh, leaving already?"'], 
    ['"That`s okay. Don`t worry - remember we`re always watching."'],
    [ DSC_afright ], 
    ["Debug lights its cigarette on its fur. It crackles briefly, and its fur seems even darker in the orange flicker."], 
    ["The smoke feels thick in your lungs. It smells like solace in comfort."],
    [DSC_encamels],
    ['"Go now. I`m waiting for you."']
]

inp_testhub = [ response1, response2, response3, response4, response5, response6 ]


# HUB SEQUENCES

# Sequence of being unique
def seq_cat_unique():
    PrintNested( text5 )
    match doinput( None, text5options1 ):
        case 1: 
            PrintNested( text5a )
            SetFlag( "unique", True )
        case 2:
            PrintNested( text5b )
            SetFlag( "unique", False )

# Sequence of leaving
def seq_cat_leave():
    PrintNested( text6 )

    if ReturnFlag( "unique" ):
        PrintNested( text6unique )

    match doinput( None, text6options1 ):
        case 1:
            PrintNested( text6exiting )
            skip()
            PrintNested( "..........." )
            PrintNested( "Brown and yellow splotches" )
            intro = False
            goto_LivingRoom()
        case 2:
            PrintNested("Slowly drifting down. The cat is watching you. It feels like a smirk.")


def gotoDebugIntro():
    intro = True
    while intro:
        treeinput = doinput(texthub, inp_testhub)
        #print("\n")
        match treeinput:
            case 1: PrintNested(text1)
            case 2: PrintNested(text2)
            case 3: 
                PrintNested(text3)
                SetFlag( "meow", True ) # Flag: unlock hub meow
            case 4: DoConditional(text4, ReturnFlag( "meow" ) )
            case 5: seq_cat_unique()
            case 6: seq_cat_leave()
            case _: skip()

# LIVING ROOM

# Living room. You were staring at the cupboard
# It's like 3am, but the lights are bright. The balcony door is open, which is cold, so you go to close it and find Mefedron
# You can go to the hallway and kitchen but there's not much point besides looking
# She's smoking and she's coming down from stimulants. Her lighter just broke so you decide to go fetch it from the kitchen
# You bring it back and you talk
# You can also watch the skyline a few times to unlock a locked dialogue option

# living room text hub goes here

# Living room skill dialogue
DSC_sdangry = partial( DoSkillCheck, 
    "[SERENDIPITY] Somewhere, a few metres above your horns, someone sips a sweet, lukewarm tea in the kitchen, unable to sleep. Squinting, they are planning out the words of reprimand.", 
    "Serendipity"
)
DSC_sdshots = partial( DoSkillCheck, 
    "[SERENDIPITY] A couple are still full. Someone filled them, convinced their body could stomach another shot. That time never came.",
    "Serendipity"
)
DSC_ecdump = partial( DoSkillCheck, 
    "[ELECTROCHEMISTRY] This is the natural environment of the afterparty. I can't blame anyone - teeth-clenching peaks of euphoria aren't a time to be neat and tidy. You know that. The sight is homely to you.",
    "Electrochemistry"
)
DSC_ectemp = partial( DoSkillCheck, 
    "[] ",
    ""
)
DSC_ecbowl = partial( DoSkillCheck, 
    "[ELECTROCHEMISTRY] Everyone knows the morning cigarette is the most important meal of the day.",
    "Electrochemistry"
)

lr_seqceiling = "Gaze at the ceiling."
lr_seqceiling_r = [["Nothing notable. The honey lamp hurts your furtive, soft gaze."], ["Little grey clouds of spider webs hang loosely from the corners of the room, long desolate."],
    ["The upstairs neighbours are quiet. It is the middle of the night, after all. The crickets outside agree."],
    [DSC_sdangry]]

lr_seqtrash = "Try to concern yourself with the trash around the room."
lr_seqtrash_r = [["It's dire. The carpet is spikey with crushed fragments of chips."],
    ["The table cloth is begging for a distant laundry day. Prominent stains of various alcohol drinks paint lakes and oceans, like on a geographical map."],
    ["There's a red cereal bowl filled with ash and stubs, surrounded by its many shot glass children."],
    [DSC_sdshots],
    ["A bustling metropolis of glassy vodka skyscrapers is situated near the sofa, shaping and curving the lights of the room into a quiet night life."],
    ["Overall, it looks like shit."],
    [DSC_ecdump],
    ["It'll take a while to make neat again, even for a sober person, and neither you or Mefedron will be sober for a good while. She can use the help nonetheless."]
    ]

# Inputs for looking at the clutter
# Bowl
# Look under the table
# Go back

lr_seqtrash_bowl = "Curiously peep into the cereal bowl."
lr_seqtrash_bowl_r = [["An inconspicuous bowl."], 
    ["Okay, no, it looks really weird and grotesque. What was once a morning treat now an ashtray for habitual smokers, dried out bottles of alcohol orbiting it."],
    [DSC_ecbowl],
    ["A nasty little image of filling the bowl with milk intrudes on your mind and it makes you shiver."],]

# Here you have to check if you have seen the joint and whether you have taken it

lr_eventjoint_first = [[]]

def lr_eventjoint():
    # If seeing it for the first time
    if not ReturnFlag( "lr_sawjoint" ):
        # [ELECTROCHEMISTRY] Wait. Wait, look.
            # What?
        # [ELECTROCHEMISTRY] A white dove sits buried with the cigarette butts, forgotten and abandoned.
            # Oh, it's a joint.
        # [ELECTROCHEMISTRY] Yes, and not just any joint. It's been barely touched. Okay, like more than half of it is burnt.
        # [ELECTROCHEMISTRY] But with your weak head, it might just be enough to get you a little woozy.
        # [ELECTROCHEMISTRY] Well, you going for it?
            # I don't see a lighter anywhere...
        # [ELECTROCHEMISTRY] Ah, fuck. Of course. Someone probably took your lighter, and the rest are buried in the clutter.
        # [ELECTROCHEMISTRY] Just look around and come back later. There must be at least one fire source in her nest of decadence.
        # [DEBUGGING] Actually, did you not leave your lighter in the kitchen? You absent-mindedly emptied your pockets a few hours ago.
        # [SERENDIPITY] Someone runs their paw pad against the flint wheel. The air remains cold.

        print("")
    # If you have seen it already and it's still there
    elif not ReturnFlag( "lr_tookjoint"):
        # The joint is happy to see you return, resting in the ash. You can feel the positive energy emanating from it.
        # [ARS FELINE] We will tell you, there's a cat out there who could really use some soft haziness in their grey, floppy ears.
        # [ELECTROCHEMISTRY] No, no, kittens. WE would really like to smoke, too.
        # ACT: Smoke the join right here and now
        #
        # ACT: Take the joint without smoking it (you won't be able to smoke it later)
        # Despite the noisy cravings in your mind, you neatly pocket the joint so as not to spill it.
        # ACT: Focus on something else.
        print("")
    # If it's gone
    else:
        PrintNested( "A cigarette tarantula lies buried in the ash, its legs sticking out in a silent prowl." )

lr_seqtrash_undertable = "Check the destruction under the table."

lr_seqtrash_goback = "Focus on something else than trash, finally."


inp_livingroomhub = [ lr_seqceiling, lr_seqtrash ]

def goto_LivingRoom_trash():
    hub_livingroom = False
    texthub = "You feel somewhat placid in the clutter, though the serenity hums a latent comedown."
    hub_livingroom_trash = True
    while hub_livingroom_trash:
        treeinput = doinput()

def goto_LivingRoom():
    texthub = "Living room placeholder. The cats forgot to push the file..."
    hub_livingroom = True
    while hub_livingroom:
        treeinput = doinput(texthub, inp_livingroomhub )
        match treeinput:
            case 1: PrintNested( lr_seqceiling_r )
            case 2: 
                PrintNested( lr_seqtrash_r )
                goto_LivingRoom_trash()


# cereal bowl ashtray
    # if you dig deeper with electrochem, you can find a half smoked joint, but you cant smoke it without a lighter
    # you can smoke it or take it and give it to mef for special dialogue
# balcony door
# hallway
# blanket on the couch
# all the litter
    # almost empty baggie. debugging and electrochem fight whether to slam or not
    # if you do you can flirt with mef
# pictures on the walls
    # of mef. mostly her and her owner/her with friends at notable parties or events/a little bit of photography
    # these give flags to talk to mef about if you give her the joint
# mef kisses you if you:
    # give her the joint
    # mention her photography
    # talk to her about her lighter from an ency check
    # if you flirt with her from the baggie


# One way to get to that street is by meeting [Blank], working on their car. You can talk to them by having Electrochem recognise the bumper sticker, or Debugging remembering what the issue might be.
# "Shine pulled you out on an especially bright day to watch her replace the battery in her car."
# If not that, then after walking around the city you can just bring up that he's been at this for a while.

# FIX achievements??

# START
gotoDebugIntro()