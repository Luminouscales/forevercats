# Everything is impermanent and transient. Especially bits on a disk. No use crying over flipped bits.
# 23.11.25

import random
from functools import partial

debug = True # Shows background stuff like flag changes and locked dialogue flags
placeholder = "A Bytecat is sleeping here."

# All flags, globally.
tbl_flags = {
    'meow': False, # Flag test. Meow meow meow!
    'unique': False, # Told Debug you want to be unique
    'lr_sawjoint': False, # Lynx has seen the joint in the bowl already
    'lr_tookjoint': False, # Lynx has taken the joint
    'lr_smokedjoint': False, # Lynx has smoked the joint
    'lr_havelighter': True, # Grabbed the lighter from the kitchen
    'lr_wherelighter': False, # Currently looking for the lighter
    'lr_sawmeph': False, # Saw the baggie under the table
    'lr_tookmeph': False # Slammed the meph
}

# lr_sawmeph
# lr_tookmeph

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
    if flag not in tbl_flags:
        input(f"YOU MISSPELLED THE {flag} FLAG!!! returning False as a fallback")
        return False
    else:
        return tbl_flags[flag]

# Sets the given flag to given bool. Shows if debug enabled
def SetFlag( flag, bool ):
    old = tbl_flags[flag]
    tbl_flags[flag] = bool
    PrintDebug( f"Flag '{flag}' set to {tbl_flags[flag]}, was {old}." )

# Shows a ... that you have to press enter to move. Like a continue
def skip():
    print( input("\n\n") )

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
# Use the second argument to specify what range of the table should be accessed, for versatility
def PrintNested( text, range=[-1, -1], fake=None ):
    start = range[0]
    end = range[1]

    skipfast()
    if isinstance(text, list):
        if start == -1:
            start = 0
            end = len(text)
        for row in text[start:end]:
            # temp makes sure you don't have to enter through an empty line when the skill check fails.
            # It's returned by DoSkillCheck(). temp is False when it should skip automatically
            temp = True

            if not isinstance( row[0], str ):
                temp = row[0]()
            else:
                print( row[0] )
                if fake is not None:
                    print("\n1. " + fake)
                    input("\n")
                
            # If it's the last line then don't do the ... because it's redundant
            if text.index(row) + 1 != end and temp:
                skip()
        if fake is None:
            skip()
    else:
        print( text )
        if fake is not None:
            print("\n1. " + fake)
            input("\n")
        else:
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
    'Electrochemistry': True,
    'Ars feline': False,
    'Encyclopedia': False,
    'Debugging': False,
    'Serendipity': False
}

# Text is the text to be printed and skill is the associated skill, checking if it's active. If not, there's only a chance it will speak.
# We return False here when nothing is said so that you don't have to enter through an empty line.
# You have to specify wait=True when calling the function outside of a dialogue table because otherwise it will skip
def DoSkillCheck( text, skill, wait=False ):
    if skill not in tbl_skillpoints:
        print( f"YOU MISSPELLED {skill}!!")
    elif tbl_skillpoints[ skill ]:
        print( text )
        if wait:
            skip()
        return True
    elif random.randint( 1, 2 ) == 1:
        print( text )
        if wait:
            skip()
        return True
    else:
        return False
    
# Displays a supposed choice input such as:
# 1. What?
# Just for immersion though. It doesn't matter what you press, you advance anyway.
def FakeInput( text ):
    print( "1. " + text )
    skip()


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
text6exiting2 = [["Brown and yellow splotches of fog coalesce back into concepts and figures."], 
    ["The cat is gone, the cupboard that was its pedestal again inhabitated by stray bottles of beer and unassorted plastic litter."],
    ["Existence feels heavy on your drifting wings and serpent tail. Go move around. Let the ennui chew on something else than your scales."]]

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
            PrintNested( text6exiting2 )
            gotoLivingRoom()
        case 2:
            PrintNested("Slowly drifting down. The cat is watching you. It feels like a smirk.")


def gotoDebugIntro():
    intro = True
    while intro:
        treeinput = doinput(texthub, inp_testhub)

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
DSC_dblighterloc = partial( DoSkillCheck, 
    "[DEBUGGING] Actually, did you not leave your lighter in the kitchen? You absent-mindedly emptied your pockets a few hours ago.",
    "Debugging"
)
DSC_sdmefwantweed = partial( DoSkillCheck, 
    "[SERENDIPITY] Someone runs their paw pad against the flint wheel. The air remains cold.",
    "Serendipity"
)
DSC_afmefwantweed2 = partial( DoSkillCheck, 
    "[ARS FELINE] We will tell you, there's a cat out there who could really use some soft haziness in their grey, floppy ears.",
    "Ars feline"
)
DSC_embers = partial( DoSkillCheck, 
    "[SERENDIPITY] You used to be joined like this with the love of the world, sharing embers with distant lips, warm in the streetlights of the night. Now, so far away, alone, even the stars are locked in the white brick ceiling.", 
    "Serendipity"
    )
DSC_stand = partial( DoSkillCheck, 
    "[ELECTROCHEMISTRY] Plenty more back home. This joint was just a one night stand.",
    "Electrochemistry"
)
DSC_weedsleep = partial( DoSkillCheck, 
    "[DEBUGGING] It'll be easier for you to fall asleep now.",
    "Debugging"
)
DSC_mefroomcat = partial( DoSkillCheck, 
    "[ARS FELINE] It would be rude to disturb it.", 
    "Ars feline" )



lr_seqceiling = "Gaze at the ceiling."
lr_seqceiling_r = [["Nothing notable. The honey lamp hurts your soft, furtive gaze."], 
    ["Little grey clouds of spider webs hang loosely from the corners of the room, long desolate."],
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

lr_seqhallway = "Leave the living room out to the hallway"

# Inputs for looking at the clutter
# Bowl
# Look under the table
# Go back

lr_seqtrash_bowl = "Curiously peep into the cereal bowl."
lr_seqtrash_bowl_r = [["An inconspicuous bowl."], 
    ["Okay, no. It looks really weird and grotesque. What was once a morning treat now an ashtray for habitual smokers, dried out bottles of alcohol orbiting it."],
    [DSC_ecbowl],
    ["A nasty little image of filling the bowl with milk intrudes on your mind, it makes you shiver."],]

lr_eventjoint_first = [ ["[ELECTROCHEMISTRY] Wait. Wait, look."], 
    ["[ELECTROCHEMISTRY] A white dove sits buried with the cigarette butts, forgotten and abandoned."], 
    ["[ELECTROCHEMISTRY] Yes, and not just any joint. It's been barely touched. Okay, like more than half of it is burnt."], 
    ["[ELECTROCHEMISTRY] But with your weak head, it might just be enough to get you a little woozy."], 
    ["[ELECTROCHEMISTRY] Well, you going for it?"], 
    ["[ELECTROCHEMISTRY] Ah, fuck. Of course. Someone probably took your lighter, and the rest are buried in the clutter."], 
    ["[ELECTROCHEMISTRY] Just look around and come back later. There must be at least one fire source in her nest of decadence."], ]

lr_eventjoint_smoke_text = [ ["Carefully you reach inside and hoist the joint in between two talons, tapping the ash off lightly. "], 
 ["It's barely touched, despite that its creator clearly put some love into it."], 
 ["The ground up weed sits snugly inside the carefully rolled paper. The filter has an almost mathematical zigzag to it, fitting perfectly inside."], 
 ["You swiftly light its charred end, and pull. The air flow is magnificent, smoke hitting your throat with little effort."], 
 ["It tastes as wonderful as every time, holding your lungs tight in a jagged, burning embrace."], 
 ["Your chest flattens in rest and the smoke wistfully relents to the yellow of the room."], 
 ["..."], 
 [DSC_embers],
 ["After an idle moment you drop the empty joint back in the bowl as fizzy softness stretches in your head."], 
 ["Numb pleasure coiling through your scales, dragging you down like a sleepy lover to bed."], 
 ["It yawns on the comedown, and for a moment its purring is louder than the ennui. Just for a moment."], 
 ["Then the thoughts return, but now you're a little high at least, for a moment."],
 [DSC_stand],  
 [DSC_weedsleep], 
 ["[SERENDIPITY] Feels like there's something out there, thoughts wandering the streetlights. Maybe go and see."], ]

def lr_eventjoint_smoke():
    PrintNested(lr_eventjoint_smoke_text)
    SetFlag( "lr_smokedjoint", True )

def lr_eventjoint_consider():
    DSC_sdmefwantweed(wait=True)
    smoketable = [ "Smoke the joint right here and now",
    "Take the joint without smoking it (you won't be able to smoke it later!)",
    "Focus on something else"
    ]
    choice = True
    while choice:
        treeinput = doinput( None, smoketable )
        match treeinput:
            case 1: 
                lr_eventjoint_smoke(),
                choice = False
            case 2: 
                SetFlag( "lr_tookjoint", True )
                PrintNested("Despite the noisy cravings in your mind, you neatly pocket the joint so as not to spill it."),
                choice = False
            case 3: 
                PrintNested("Reluctant to betray its beauty so, you keep a shard of the joint in your memory."),
                choice = False

def lr_eventjoint():
    PrintNested( lr_seqtrash_bowl_r )
    # If seeing it for the first time
    if not ReturnFlag( "lr_sawjoint" ):
        SetFlag( "lr_sawjoint", True )
        PrintNested("[ELECTROCHEMISTRY] Wait. Wait, look.", fake="What?")
        PrintNested("[ELECTROCHEMISTRY] A white dove sits buried with the cigarette butts, forgotten and abandoned.", fake="Oh, it's a joint.")
        PrintNested( lr_eventjoint_first, [2, 4])
        if not ReturnFlag( "lr_havelighter" ):
            FakeInput("I don't see a lighter anywhere...")
            PrintNested( lr_eventjoint_first, [5, 6])
            DSC_dblighterloc(wait=True)
            DSC_sdmefwantweed(wait=True)
        else:
            lr_eventjoint_consider()

    # If you have seen it already and it's still there
    elif not ReturnFlag( "lr_tookjoint") and not ReturnFlag("lr_smokedjoint"):
        PrintNested("The joint is happy to see you return, resting in the ash. You can feel the positive energy emanating from it.")
        if not ReturnFlag( "lr_havelighter" ):
            PrintNested( "[ELECTROCHEMISTRY] Still nothing to smoke it with, though." )
        # [ELECTROCHEMISTRY] No, no, kittens. WE would really like to smoke, too.
        else:
            DSC_afmefwantweed2(wait=True)
            lr_eventjoint_consider()
    # If it's gone
    else:
        if ReturnFlag("lr_smokedjoint"):
            PrintNested( "A cigarette tarantula lies buried in the ash, preying on the empty joint." )
        else:
            PrintNested( "A cigarette tarantula lies buried in the ash, its leg butts sticking out in a silent prowl." )

# Trash - Under table - Baggie

# def lr_seqtrash_undertable_seq():
    

lr_seqtrash_undertable = "Check the destruction under the table."

lr_seqtrash_goback = "Focus on something else than trash, finally."

lr_inputs = [lr_seqceiling, lr_seqtrash, lr_seqhallway ]

lr_trash_inputs = [lr_seqtrash_bowl, lr_seqtrash_undertable, lr_seqtrash_goback ]

def gotoLivingRoom():
    hub_livingroom = True
    texthub = "text goes here"
    while hub_livingroom:
        treeinput = doinput( texthub, lr_inputs )
        match treeinput:
            case 1: PrintNested( lr_seqceiling_r )
            case 2: 
                PrintNested( lr_seqtrash_r )
                gotoLivingRoom_trash()
            case 3:
                gotoHallway()



DSC_ectemp = partial( DoSkillCheck, 
    "[] ",
    ""
)
DSC_stretch = partial( DoSkillCheck, 
    "[ENCYCLOPEDIA] I still advise you to stretch more often, and sleep longer. Soothes your body and mind. The psychedelics you take do not help at night.",
    "Encyclopedia"
)
DSC_partytable = partial( DoSkillCheck, 
    "[ELECTROCHEMISTRY] A familiar sight, right? You remember all the things you've done under a party table. Mostly blacking out. It really is cozy, the way a cave is cozy for a wet animal.",
    "Electrochemistry"
)
DSC_goodwork = partial( DoSkillCheck, 
    "[DEBUGGING] Good work. This feeling will pass. It's better in the long run.",
    "Debugging"
)
DSC_debugwarn = partial( DoSkillCheck, 
    "[DEBUGGING] I'll warn you, if there's actually something in it, it's very likely you won't be able to resist the urge. It's happened before.",
    "Debugging"
)
DSC_eyeballing = partial( DoSkillCheck, 
    "[ENCYCLOPEDIA] When 'eyeballing' it, it appears to be around 200 miligrams of the unidentified powder.",
    "Encyclopedia"
)
DSC_comedown = partial( DoSkillCheck, 
    "[DEBUGGING] The night is late. You won't feel anything besides letting the comedown come back. Think of the hangover tomorrow morning.",
    "Debugging"
)
DSC_stimsmell = partial( DoSkillCheck, 
    "[DEBUGGING] Don't stimulants usually smell? I think they do.",
    "Debugging"
)
DSC_encnerd = partial( DoSkillCheck, 
    "[ENCYCLOPEDIA] It is common knowledge that it is extremely unreliable to discern a substance by its appearance. Also known is that you should not ingest unknown substances.",
    "Encyclopedia"
)
DSC_echater = partial( DoSkillCheck, 
    "[ELECTROCHEMISTRY] Are you talking to Encyclopedia? Don't. Nerds don't know fun.",
    "Electrochemistry"
)


# lr_sawmeph
# lr_tookmeph

def lr_mephsequence():
    ###
    def leavemeph():
        PrintNested( "[ELECTROCHEMISTRY] Whatever, sure. It'll be stuck in your head now. Good luck falling asleep later.")
        DSC_goodwork(wait=True)

    tree1 = ["...why would I do that?", "Examine the baggie.", "Leave the baggie where it is."]

    txt1 = [["Reluctantly, you place your right claw on the table and bend down."], 
        ["Your back is sore, the pain strains your scales, pushing some air out of your lungs and making your wings squirm."], 
        [DSC_stretch], 
        ["The lamp spills into a mellow shadow on the carpet. It's oddly peaceful here, clean too, the wooden roof protecting the floor from damage."], 
        [DSC_partytable], ]
    
    txt2 = [ ["You get on your knees to slither further into the darkness. With one stretch of your thin arm the plastic rustles promisingly in your pink claw."], 
        ["It's..."], 
        ["[ELECTROCHEMISTRY] ...not empty. There's still some left. When do I ever let you down?"], ]
    
    tree2 = ["Get to snorting the thing already!", "Try only a little bit", "Examine the powder more closely", "Actually, nevermind, I'm leaving it."]

    txt3 = [ ["It's almost like you can feel the powder burning in your nostrils, the yellow straw in your claw..."], 
        ["The tiny rush in your heart growing into a flame, warming up every little nerve ending as it spreads through your body..."], 
        ["Past your flat, rhythmic chest, the air warm and pleasing in your lungs, like a fireplace in winter..."], 
        ["Caressing your cheek, licking a sharp smile out of the frozen ennui on your face..."], 
        ["Finally hitting your brain like an orgasm, drowning all your thoughts in a woozy, giddy haze..."], ]
    
    txt4 = [ ["Without hesitation you empty the plastic right on a clear spot on the table, squeezing and shifitng it to get every last snowflake out, like a winter mist."], 
        ["Conveniently someone seems to have left a yellow bus fare card here. It's even got some powder left over on its edge. A couple swift movements, and..."], 
        ["You've seen more - but you've also seen less. For a midnight treat, it will more than do. Sometimes you believe in sweet providence. Wow, you're excited at the very sight."], 
        ["You don't peer over the mountain range for long. With one well controlled swoop of your head it slams right into your right nostril, disappearing inside you."], 
        ["An inferno, cooked in a drug underground. Who knows what this shit is, or where it came from. Your imagination is giddy, masochistic with your burning nose."], ]
    
    def slamit():
        SetFlag( "lr_tookmeph", True )
        PrintNested( txt4 )
        PrintNested( "Sadly you can't hold on to it longer. It recedes into blurry peripherals, a warm hearth in your flowing chest... Words are roused by the warmth.", fake='"Sweet intranasal application. Smooth, flawless. Good fucking work, right nostril." [rub your right nostril lovingly.]' )
        PrintNested( "Your nostril sure feels recognised.", fake='"So funny the card was there, perfectly for me to cut my line. Our progenitor had the same idea to indulge in a little stimulant. Stand on the shoulders of giants."')
        PrintNested( "[ELECTROCHEMISTRY] Yesssss. It's working. Welcome home. We missed you.", fake='"You did?"')
        PrintNested( "[ELECTROCHEMISTRY] Of course! Everyday we wait for you. For your optimism, budding enthusiasm, the fangs in your grin... You're grinning so lovely right now, you little pink muzzle.", fake='"Thank you..."')
        PrintNested( [["[ELECTROCHEMISTRY] Go now, let's do something fucking fun already in this grey, damp world. "], 
            ["[ELECTROCHEMISTRY] Everyone may be gone, but we can still lead the encore. Mef's on the balcony. Isn't she the greatest thing you know? Go hit her up."]])
        PrintNested( "[ELECTROCHEMISTRY] The world can't hide its ecstasy forever. Make it relinquish. We're right here with you. We've got your back.", fake="Stand upright, taking the world in. Yes, the whole world. And its beauty. Especially the beauty.")
    ###

    PrintNested(txt1)
    if not ReturnFlag("lr_sawmeph") or not ReturnFlag( "lr_tookmeph" ):
        SetFlag( "lr_sawmeph", True )
        PrintNested("Nothing to see here, besides an empty baggie of the small variety. The carpet will be bothersome to vacuum, though.")

        choice = True
        while choice:
            treeinput = doinput("[ELECTROCHEMISTRY] Hey, now. How do you really know it's empty? Don't throw around baseless facts. It's dark down here, go check!", tree1)
            match treeinput:
                case 1:
                    PrintNested( "[ELECTROCHEMISTRY] Come on now. Your nose is runny and you heart is running a little faster at the very thought. Your body's talking to you." )
                    DSC_debugwarn(wait=True)
                case 2:
                    PrintNested( txt2 )
                    DSC_eyeballing(wait=True)
                    
                    while choice:
                        treeinput = doinput( "It's resting in your claw, wary of its fate.", tree2)
                        match treeinput:
                            case 1: 
                                choice = False
                                slamit()

                            case 2:
                                PrintNested( [["Furtive enthusiasm taps some powder out on the table, a snowy hilltop. You put your nose up to it, knowing the right distance by instict, then pull."],
                                    ["Timid embers in your nostril. It barely hurts. And it won't make you feel anything."],])
                                PrintNested("You would be very disappointed, if the baggie was empty... But you can have so much more.", fake="Get to snorting the thing already!")
                                choice = False
                                slamit()
                            case 3:
                                PrintNested([["It's stereotypically white, and ground into fineness, forming tiny clumps, like snow on three branches."], ["Your pink muzzle tells you it has a powerful smell, though you can't quite put your finger on it."] ])
                                DSC_stimsmell(wait=True)
                                if DSC_encnerd(wait=True):
                                    DSC_echater(wait=True)
                            case 4:
                                PrintNested("[ELECTROCHEMISTRY] Really? You seem to be feeling veeery strongly about the powder inside. Who knows what it could be? How it could make you feel...", fake="No, seriously, I'm putting it down.")
                                PrintNested( txt3 )
                                DSC_comedown(wait=True)

                case 3:
                    leavemeph()
                    choice = False

    else:
        PrintNested("Thank god you looked under here. You don't see any more gifts, butttt be sure to comb the floor later. There's definitely some delicious crumbs to find.")

def gotoLivingRoom_trash():
    hub_livingroom_trash = True
    texthub = "text goes here"
    while hub_livingroom_trash:
        treeinput = doinput( texthub, lr_trash_inputs )
        match treeinput:
            case 1: # Ashtray bowl
                lr_eventjoint()
            case 2: # Under table (the toby fox game)
                lr_mephsequence()
            case 3:
                hub_livingroom_trash = False


# HALLWAY [hw]

hw_inputs = [ "Go to the kitchen",
    "Enter Mef's room",
    "Go back to the living room"
]

def gotoHallway():
    hub_hallway = True
    texthub = "The corridor pierces through her apartment like a vein, cold tiles connecting the kitchen and Mef's room with the light dimly spilling from the living room."
    # Kitchen
    # Mef's room
    # Living room
    while hub_hallway:
        treeinput = doinput( texthub, hw_inputs )
        match treeinput:
            case 1: 
                gotoKitchen(), 
                hub_hallway = False
            case 2: 
                PrintNested( "There's an ashy cat curled up on the doorhandle. You can't go in." ), 
                DSC_mefroomcat(wait=True)
            case 3: 
                hub_hallway = False, 
                gotoLivingRoom()

# KITCHEN (ki)

DSC_fridge = partial( DoSkillCheck, 
    "[DEBUGGING] This means no breakfast tomorrow. Just tea and cigarettes.",
    "Debugging"
)

ki_inputs = [ "Open the fridge", "Look out the window", "Search the tabletops", "Go back to the hallway" ]

ki_fridge = [["You need not open the fridge to know the penury that is inside. Half-empty condiments sit scattered furtively, and not much else. Coffee milk."],
    ["You can taste the clear liquid in the vodka bottle in your nose. It makes you wince."],
    ["People in her circumstances don't eat a lot. Not inside, alone, at least."],
    [DSC_fridge]
]

ki_window = [ ["Quietude. Fleeting squares of light on your tiny skyscrapers. Hundreds of rooms in parallel, reluctant of one another."], 
    ["Street lights turn green, yellow, red, but no one passes by."], ]
ki_window_stargazing = [ ["[SERENDIPITY] No one ascertains that there is yet hope, there is someone to fight for, perhaps someone to take you in."], 
 ["[SERENDIPITY] Air and snow, steel trees and concrete. A vehicle passes by. They don't bother to stop at the red light."], 
 ["[SERENDIPITY] They have somewhere to be, perhaps a cosy room?..."], 
 ["[SERENDIPITY] An apartment, a modest speck upon the universe's destiny, your everything, and everything that belongs to you, your locus, where you wake and dream, fall tears and find pleasure."], 
 ["[SERENDIPITY] From the window you see a dying soul."], ]

def gotoKitchen():
    hub_kitchen = True
    texthub = placeholder
    # Look in the fridge
    # Look out the window
    # Grab the lighter
    # Go back
    while hub_kitchen:
        treeinput = doinput(texthub, ki_inputs)
        match treeinput:
            case 1: PrintNested( ki_fridge )
            case 2: 
                PrintNested(ki_window),
                if not ReturnFlag( "lr_smokedjoint" ):
                    PrintNested( "You're too sober for stargazing.")
                else:
                    PrintNested( ki_window_stargazing )
            case 3: print(placeholder)
            case 4:
                hub_kitchen = False, 
                gotoHallway()



# One way to get to that street is by meeting [Blank], working on their car. You can talk to them by having Electrochem recognise the bumper sticker, or Debugging remembering what the issue might be.
# "Shine pulled you out on an especially bright day to watch her replace the battery in her car."
# If not that, then after walking around the city you can just bring up that he's been at this for a while.

# START
#gotoDebugIntro()
gotoLivingRoom()