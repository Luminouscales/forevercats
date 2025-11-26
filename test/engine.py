# The backend for Forevercats

import random
from functools import partial


debug = True # Shows background stuff like flag changes and locked dialogue flags
placeholder = "A Bytecat is sleeping here."

# All tags, globally
tbl_flags = {
    'exampleflag': False,
}

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
    'Electrochemistry': False,
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


# Example DoSkillCheck partial
DSC_temp = partial( DoSkillCheck, 
    "[] ",
    ""
)

# Example room function
def gotoDebugIntro():
    texthub = "Example room"
    inp_testhub = ["Option 1", "Option 2", "Option 3"] # Note how these are strings in ONE table

    intro = True
    while intro:
        treeinput = doinput(texthub, inp_testhub)

        match treeinput:
            case 1: PrintNested("Option 1 response")
            case 2: PrintNested("Option 2 response")
            case 3: PrintNested("Option 3 response")
