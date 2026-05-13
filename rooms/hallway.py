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

hw_inputs = [ "Go to the kitchen",
    "Enter Mef's room",
    "Go back to the living room"
]

DSC_mefroomcat = partial( DoSkillCheck, 
    "[ARS FELINE] It would be rude to disturb it.", 
    "Ars feline" )

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
                hub_hallway = False,
                import rooms.livingroom 
                rooms.livingroom.gotoLivingRoom()