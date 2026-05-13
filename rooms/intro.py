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
            import rooms.livingroom
            rooms.livingroom.gotoLivingRoom()
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