# Simple dialogue maker for Forevercats, version 1.
# Put your desired strings, each in a new line in input.txt
# Then run the code and get your output.txt


import os, sys

selfpath = os.path.dirname(sys.argv[0])
inputpath = selfpath + "\input.txt"
outputpath = selfpath + "\output.txt"

full = "[ "

with open(inputpath, 'r', encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        full = full + '["' + line + '"]' + ', '
    full = full + ']'
    print( full )

with open(outputpath, 'w', encoding="utf-8") as file:
    file.write(full)