# "Everything is impermanent and transient. Especially bits on a disk. No use crying over flipped bits."
# 23.11.25

import random
from functools import partial
import rooms.scripts as d

DoSkillCheck = d.DoSkillCheck
PrintNested = d.PrintNested
doinput = d.doinput
debug = d.debug
SetFlag = d.SetFlag
ReturnFlag = d.ReturnFlag
skip = d.skip
DoConditional = d.DoConditional
FakeInput = d.FakeInput

placeholder = "A Bytecat is sleeping here."

# START
#import rooms.intro
#rooms.intro.gotoDebugIntro()
import rooms.livingroom
rooms.livingroom.gotoLivingRoom()