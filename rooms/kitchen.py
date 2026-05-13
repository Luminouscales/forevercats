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

# KITCHEN (ki)

DSC_fridge = partial( DoSkillCheck, 
    "[DEBUGGING] This means no breakfast tomorrow. Just coffee and cigarettes.",
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
    ["[SERENDIPITY] From the window you see a dying soul..."], ]

def gotoKitchen():
    hub_kitchen = True
    texthub = "The kitchen tiles feel cool underneath your sockless paws. An overabundance of white light clashes with the pitch darkness just outside, spotted with street lamps. Distant, nocturnal cars hum through the cracked window."
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
            case 3:
                PrintNested( [["It's oddly clean here, in contrast with the rest of the apartment. You run your claw against the smooth countertop. Feels like home."],
                    ["You're sure that if she actually used this place, it would look much worse."],
                    ["Cooking something together would be fun, the way you do with Shine. Would Mef even be interested? Probably not."],
                    ["The thought of all three of you in the kitchen together is amusing."] ] )
                if ReturnFlag( "lr_wherelighter" ) and not ReturnFlag( "lr_havelighter"):
                    PrintNested( "The bright yellow of your lighter catches your eye. It fits right in the palm of your claw, ready to burn for you again.")
                    SetFlag( "lr_havelighter", True )
            case 4:
                hub_kitchen = False, 
                import rooms.hallway
                rooms.hallway.gotoHallway()