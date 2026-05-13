import rooms.scripts as d
from functools import partial

DoSkillCheck = d.DoSkillCheck
PrintNested = d.PrintNested
doinput = d.doinput
debug = d.debug
SetFlag = d.SetFlag
ReturnFlag = d.ReturnFlag
skip = d.skip
DoConditional = d.DoConditional
FakeInput = d.FakeInput


def lr_mephsequence():
    ###
    def leavemeph():
        PrintNested( "[ELECTROCHEMISTRY] Whatever, sure. It'll be stuck in your head now. Good luck falling asleep later.")
        DSC_goodwork(wait=True)

    tree1 = ["...why would I do that?", "Examine the baggie.", "Leave the baggie where it is."]

    txt1 = [["Reluctantly, you place your right claw on the table and lean down."], 
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
        ]
    
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
        gotoLivingRoom()
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
                                DSC_comedown(wait=True)
                                PrintNested( txt3 )
                                PrintNested("Finally hitting your brain like an orgasm, drowning all your thoughts in a woozy, giddy haze...", fake="Let yourself be happy.")
                                
                                slamit()

                case 3:
                    leavemeph()
                    choice = False

    else:
        PrintNested("[ELECTROCHEMISTRY] Thank god you looked under here. You don't see any more gifts, butttt be sure to comb the floor later. There's definitely some delicious crumbs to find.")



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
    "[ELECTROCHEMISTRY] This is the natural environment of the afterparty. I can't blame anyone - the spirals of alcohol abuse aren't a time to be neat and tidy. You know that. The sight is homely to you.",
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
    "[ENCYCLOPEDIA] Actually, did you not leave your lighter in the kitchen? You absent-mindedly emptied your pockets a few hours ago.",
    "Encyclopedia"
)
DSC_sdmefwantweed = partial( DoSkillCheck, 
    "[SERENDIPITY] Someone runs their paw pad against the flint wheel. The air remains cold.",
    "Serendipity"
)
DSC_afmefwantweed2 = partial( DoSkillCheck, 
    "[ARS FELINE] We will tell you, there's a cat out there who could really use some soft haziness in their grey, floppy ears.",
    "Ars feline"
)
DSC_lxwantweed = partial( DoSkillCheck, 
    "[ELECTROCHEMISTRY] No, no, felines. WE would really like to smoke, too.",
    "Electrochemistry"
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

lr_seqceiling = "Gaze at the ceiling."
lr_seqceiling_r = [["Nothing notable. The honey lamp hurts your soft, furtive gaze."], 
    ["Little grey clouds of spider webs hang loosely from the corners of the room, long desolate."],
    ["The upstairs neighbours are quiet. It is the middle of the night, after all. The crickets outside agree."],
    [DSC_sdangry]]
    # FIXME If a skill function is the last in a table, it will force you to skip twice if it doesn't play
    # Just fix it later

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
            SetFlag("lr_wherelighter", True)
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
        else:
            if DSC_afmefwantweed2(wait=True):
                DSC_lxwantweed(wait=True)
            lr_eventjoint_consider()
    # If it's gone
    else:
        if ReturnFlag("lr_smokedjoint"):
            PrintNested( "A cigarette tarantula lies buried in the ash, preying on the empty joint." )
        else:
            PrintNested( "A cigarette tarantula lies buried in the ash, its leg butts sticking out in a silent prowl." )

lr_seqtrash_undertable = "Check the destruction under the table."

lr_seqtrash_goback = "Focus on something else than trash, finally."

lr_inputs = [lr_seqceiling, lr_seqtrash, lr_seqhallway ]

lr_trash_inputs = [lr_seqtrash_bowl, lr_seqtrash_undertable, lr_seqtrash_goback ]

livingroomhub = "The living room feels like an epicentre of conciousness, white popcorn walls and a " \
"yellow ceiling light protecting you from the crushing unknown of the dark, distant city streets. Even the window curtains are squinting, scared of the horizon, only letting" \
"a few black stripes through. At least the various tables feel cozy under their blankets of empty packagings and random items."

def gotoLivingRoom():
    hub_livingroom = True
    texthub = livingroomhub
    while hub_livingroom:
        treeinput = doinput( texthub, lr_inputs )
        match treeinput:
            case 1: PrintNested( lr_seqceiling_r )
            case 2: 
                PrintNested( lr_seqtrash_r )
                gotoLivingRoom_trash()
            case 3:
                import rooms.hallway
                rooms.hallway.gotoHallway()
