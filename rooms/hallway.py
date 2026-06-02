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

# HALLWAY [hw]



DSC_mefroomcat = partial( DoSkillCheck, 
    "[ARS FELINE] It would be rude to disturb it.", 
    "Ars feline" )

# /-----------------------------------------------------
# SEQ: MIRROR
# /------------------------------------------------------
# Mirror interaction
# /-----------------------------------------------------

seq_enquire = [["You are a human, along with almost 7 billion other humans on Earth."], 
["That's not all. 'Human' is just an umbrella term for a plethora of sentient, two-legged human species descendant from animals of nature."],
["Being a certain species entails more or less unique and specific species characteristics that belong to your feral form, some of them surreptitious. You seem to know about quite a few."]]

def mir_human():
    if DoSkillCheck(skill="Encyclopedia"):
        choice = True
        while choice:
            treeinput = doinput( "[ENCYCLOPEDIA] Looking at your form, you feel the need to enquire.", ["What am I?", "Don't enquire"] )
            match treeinput:
                case 1:
                    PrintNested( seq_enquire )
                    mir_dragon()
                case 2: choice = False

def mir_dragon():
    choice = True
    while choice:
        treeinput = doinput( "[ENCYCLOPEDIA] You're a dragon. Would you like to know what species specifics that entails?", ["Hit me.", "No, my head hurts too much for this."] )
        match treeinput:
            case 1: 
                mir_dragon_seq()
                choice = False
            case 2: choice = False

def mir_dragon_seq():
    PrintNested("Dragons bear the standard core specifics belonging to reptiles: scales instead of feathers or fur, which, although not as soft, are for example easier to clean; claws instead of paws, which are better suited for worse weather and usually do not require shoes; and long tails of various properties.")
    PrintNested("More uniquely, however, dragons have wings.", fake="So I can fly?")
    seq1 = [ ["No, unfortunately. There are no known human species with the intrinsic ability to fly."],
    ["Your wings are utilised, however, for intrapersonal communication, in conjunction with the tail, called wing-tail expression. Like facial expressions, they are signals for the other person: by flaring, fluttering, staying closed on your back. It's a fascinating direction of study, and I can't go in depth without visual examples."]]
    PrintNested( seq1 )
    PrintNested("A study by Cassiopeia, F. et al. (2006) proved a statistically relevant effect of wing-tail nonverbal expression on intrapersonal rapport. Dragons utilising this method of expression were declared by test subjects as more approachable, friendly and communicative than dragons without them.", fake="I know a specific study and its date but not what day it is? My mind feels soggy and empty.")
    seq2 = [ ["Memory is as fussy as it is perseverant. It is my job to keep data available, no matter how much you try to wipe it. "], 
        ["Either way, this effect was also higher on other dragons, compared to different species. It's good for you to know. "], 
        ["The minutiae of expression is different between cultures and it is usually learnt from a very young age, from parents and peers. Dragons brought up without this kind of modelling exhibit no wing-tail expression. "], 
        ["Wings have a visual aspect to them, also, coming in various shapes and properties. Yours were born this way - they are not the result of damage, as far as I can tell. "], ]
    PrintNested(seq2)
    PrintNested("Though they can contribute or detract from your attractiveness, some dragons have them surgically removed - for body image, though usually for comfort, and even safety in jobs such as construction.", fake="Are my wings attractive?")
    PrintNested("People find them endearing, from what I remember.", fake="That was very comprehensive. Thank you.")
    PrintNested("My pleasure. Knowledge and information can only prepare you. I will return with more as I continue to examine your memory.")

def mirror_hub():
    mir_human()

# /-----------------------------------------------------
# HUB: HALLWAY
# /------------------------------------------------------
# 
# /-----------------------------------------------------

hw_inputs = [ "Go to the kitchen",
    "Enter Mef's room",
    "Look in the mirror",
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
                import rooms.kitchen 
                rooms.kitchen.gotoKitchen(), 
                hub_hallway = False
            case 2: 
                PrintNested( "There's an ashy cat curled up on the doorhandle. You can't go in." ), 
                DSC_mefroomcat(wait=True)
            case 3:
                mirror_hub()
            case 4: 
                hub_hallway = False,
                import rooms.livingroom 
                rooms.livingroom.gotoLivingRoom()