""" Class for translating tetum to SAMPA format """
# coding=UTF-8

#TODO check 'i~' == 'i' from data
#TODO check apparent 7 missing letters w/ hearne
class tetumSampa(object):


	def __init__(self):
		self.unchanged_graphemes = ["a", "e", "i", "o", "u", "b", "d", "f", "g", "h", "k", "l", "p",
			"s", "t", "u", "z", "n"]
		self.inString = ""
		self.outString = ""
		self.index = 0
		self.matched = False

	def checkTrigraphs(self):
		'''checks if the three characters starting at self.index map to a trigraph'''
		self.matched = True

		if self.inString[self.index:self.index+3] == "uun":
				self.outString += "u~:"
		elif self.inString[self.index:self.index+3] == "een":
				self.outString += "e~:"
		elif self.inString[self.index:self.index+3] == "oon":
				self.outString += "o~:"
		elif self.inString[self.index:self.index+3] == "aan":
				self.outString += "a~:"
		elif self.inString[self.index:self.index+3] == "iin":
				self.outString += "i~:"
		else:
				#print "tri not found: " + self.inString[self.index:self.index+3]
				self.matched = False

	def checkDigraphs(self):
		'''checks if the two characters starting at self.index map to a digraph'''
		self.matched = True

		if self.inString[self.index:self.index+2] == "ii":
			self.outString += "i:"
		elif self.inString[self.index:self.index+2] == "oo":
			self.outString += "o:"
		elif self.inString[self.index:self.index+2] == "uu":
			self.outString += "u:"
		elif self.inString[self.index:self.index+2] == "in":
			self.outString += "i~"
		elif self.inString[self.index:self.index+2] == "un":
			self.outString += "u~"
		elif self.inString[self.index:self.index+2] == "en":
			self.outString += "e~"
		elif self.inString[self.index:self.index+2] == "em":
			self.outString += "e~"
		elif self.inString[self.index:self.index+2] == "on":
			self.outString += "o~"
		elif self.inString[self.index:self.index+2] == "om":
			self.outString += "o~"
		elif self.inString[self.index:self.index+2] == "an":
			self.outString += "a~"
		elif self.inString[self.index:self.index+2] == "am":
			self.outString += "a~"
		elif self.inString[self.index:self.index+2] == "im":
			self.outString += "i~"
		elif self.inString[self.index:self.index+2] == "ll":
			if (self.index > 0 and self.inString[self.index - 1] == 'i'):
				self.outString += "l"
			else:
				self.outString += "il"
	#TODO check lh symbol
	#        elif self.inString[self.index:self.index+2] == "lh":
	#                return True
	#                self.outString += "something"
		elif self.inString[self.index:self.index+2] == "nh":
			self.outString += "n_0"
		elif self.inString[self.index:self.index+2] == "ng":
			self.outString += "N"
		elif self.inString[self.index:self.index+2] == "rr":
			self.outString += "r"
		else:
			#print "bi not found: " + self.inString[self.index:self.index+2]
			self.matched = False

	def checkUnigraphs(self):
		'''checks if the character at self.index maps to anything'''
		self.matched = True

		if self.inString[self.index] in self.unchanged_graphemes:
			self.outString += self.inString[self.index]
		elif self.inString[self.index] == 'c':
			self.outString += "k"
		elif self.inString[self.index] == 'j':
			self.outString += "z"
		elif self.inString[self.index] == 'ñ':
			if self.index > 0 and self.inString[self.index - 1] == 'i':
				self.outString += "n"
			else:
				self.outString += "in"
		elif self.inString[self.index] == 'r':
			self.outString += "4"
		elif self.inString[self.index] == 'w':
			self.outString += "b"
		elif self.inString[self.index] == 'x':
			self.outString += "s"
		elif self.inString[self.index] == 'y':
			self.outString += "j"
		elif self.inString[self.index] == 'v':
			self.outString += "b"
		elif self.inString[self.index] == 'á':
			self.outString += "a"
		elif self.inString[self.index] == 'ó':
			self.outString += "o"
		elif self.inString[self.index] == 'ú':
			self.outString += "u"
		elif self.inString[self.index] == 'é':
			self.outString += "e"
		elif self.inString[self.index] == 'í':
			self.outString += "i"
		else:
			print "uni not found: " + self.inString[self.index]
			self.matched = False

	def doTrans(self, tetumWord):
		self.inString = tetumWord
		strLen = len(self.inString)
		self.outString = ""
		self.index = 0
		self.matched = False
		    
		while (self.index < strLen):
			#print "new loop: {}".format(self.index)

			self.checkTrigraphs()
			#print self.outString
			if self.matched == True:
				self.index += 3
			else:
				self.checkDigraphs()
				if self.matched == True:
					self.index += 2
				else:
					self.checkUnigraphs()
					self.index += 1

				if self.matched == False:
					#print "self.outString so far: " + self.outString + "self.index: {}".format(self.index)
					return

		print self.outString
