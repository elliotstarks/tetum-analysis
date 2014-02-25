#unigraph = ["a", "e", "i", "o", "u", "b", "c", "d", "f", "g", "h", "j",
#	"k", "l", "m", "ñ", "p", "r", "s", "t", "u", "w", "x", "y", "z"]

#digraph = ["ii", "oo", "uu", "in", "im", ]

#globals

#TODO check 'i~' == 'i' from data
#TODO check apparent 7 missing letters w/ hearne

unchanged_graphemes = ["a", "e", "i", "o", "u", "b", "d", "f", "g", "h", "k", "l", "p",
        "s", "t", "u", "z"]

outString = ""

def checkTrigraphs(inString, index):
'''checks if the three characters starting at index map to a trigraph'''
        global outString
        match = True

        if inString[index:index+3] == "uun":
                outString += "u~:"
        elif inString[index:index+3] == "een":
                outString += "e~:"
        elif inString[index:index+3] == "oon":
                outString += "o~:"
        elif inString[index:index+3] == "aan":
                outString += "a~:"
        else:
                #print "tri not found: " + inString[index:index+3]
                match = False

        return match

def checkDigraphs(inString, index):
'''checks if the two characters starting at index map to a digraph'''
        global outString
        match = True

        if inString[index:index+2] == "ii":
                outString += "i:"
        elif inString[index:index+2] == "oo":
                outString += "o:"
        elif inString[index:index+2] == "im":
                outString += "i~"
        elif inString[index:index+2] == "un":
                outString += "u~"
        elif inString[index:index+2] == "en":
                outString += "e~"
        elif inString[index:index+2] == "em":
                outString += "e~"
        elif inString[index:index+2] == "on":
                outString += "o~"
        elif inString[index:index+2] == "om":
                outString += "o~"
        elif inString[index:index+2] == "an":
                outString += "a~"
        elif inString[index:index+2] == "am":
                outString += "a~"
        elif inString[index:index+2] == "im":
                outString += "i~"
        elif inString[index:index+2] == "ll":
                if (index > 0 and inString[index - 1] == 'i'):
                        outString += "l"
                else:
                        outString += "il"
#TODO check lh symbol
#        elif inString[index:index+2] == "lh":
#                return True
#                outString += "something"
        elif inString[index:index+2] == "nh":
                outString += "n_0"
        elif inString[index:index+2] == "ng":
                outString += "N"
        elif inString[index:index+2] == "rr":
                outString += "r"
        else:
                #print "bi not found: " + inString[index:index+2]
                match = False

        return match

def checkUnigraphs(inString, index):
'''checks if the character at index maps to anything'''
        global outString
        global unchanged_graphemes
        match = True

        if inString[index] in unchanged_graphemes:
                outString += inString[index]
        elif inString[index] == 'c':
                outString += "k"
        elif inString[index] == 'j':
                outString += "z"
        elif inString[index] == 'ñ':
                if index > 0 and inString[index - 1] == 'i':
                        outString += "n"
                else:
                        outString += "in"
        elif inString[index] == 'r':
                outString += "4"
        elif inString[index] == 'w':
                outString += "b"
        elif inString[index] == 'x':
                outString += "s"
        elif inString[index] == 'y':
                outString += "j"
        else:
                #print "uni not found: " + inString[index]
                match = False

        return match

def tetumToSampa(inString):
        global outString
        outString = ""
        i = 0
        strLen = len(inString)
        matched = False
        
        while (i < strLen):
                print "new loop: {}".format(i)

                matched = checkTrigraphs(inString, i)
               # print outString
                if matched == True:
                        i += 3
                else:
                        matched = checkBigraphs(inString, i)
                        if matched == True:
                                i += 2
                        else:
                                matched = checkUnigraphs(inString, i)
                                i += 1

                if matched == False:
                        print "outString so far: " + outString + "index: {}".format(i)
                        print "No othography to SAMPA match found at " + inString[i-1:]
                        return

        print outString
