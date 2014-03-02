""" Generic string comparison algorithm  """
"""

"""
import collections

# 'feature': grapheme1, grapheme2, grapheme3, ... , 

# the following sampa features are taken as a union of phonemes from the
# wikipedia articles on tetum and portuguese phonologies.

#consonants
voiced = ['m', 'b', 'v', 'n', 'd', 'z', 'l', 'r', '4', 'dZ', 'Z', 'J', 'L', 'j',
	 'g', 'w', 'R', 'R\\']

bilabial = ['m', 'p', 'b']
labiodental = ['f', 'v']
alveolar = ['n', 't', 'd', 's', 'z', 'l', 'r', '4']
post_alveolar = ['tS', 'dZ', 'S', 'Z']
palatal = ['J', 'L', 'j']
velar = ['k', 'g', 'w']
uvular = ['R', 'R\\']
glottal = ['h']

nasal = ['m', 'n', 'J']
stop = ['p', 'b', 't', 'd', 'tS', 'dZ', 'k', 'g']
fricative = ['f', 'v', 's', 'z', 'S', 'Z', 'h']
lateral_approximant = ['l', 'L', 'R']
trill = ['r', 'R\\']
flap = ['4']
approximant = ['j', 'w']

# vowels
# TODO need central open vowel symbol for SAMPA
# TODO finish portuguese vowels
closed = ['i', 'i~', 'e']
mid = ['e', 'o']
open_ = []

front = ['i', 'e']
central = []
back = ['u', 'o']


phon_dict = {'voiced' : voiced, 'nasal' : nasal, 'bilabial' : bilabial,
	'labiodental' : labiodental, 'alveolar' : alveolar,
	'post_alveolar' : post_alveolar, 'palatal' : palatal,  'velar' : velar,
	'uvular' : uvular, 'glottal' : glottal, 'nasal' : nasal, 'stop' : stop,
	'fricative' : fricative, 'lateral_approximant' : lateral_approximant,
	'trill' : trill, 'flap' : flap, 'approximant' : approximant,
	'closed' : closed, 'mid' : mid, 'open' : open_, 'front' : front,
	'central' : central, 'back' : back, 'front' : front}

#regular lcs algorithm, calculating min # edits required to match 2 strings
def regular_lcs(matrix, outer, inner, word1, word2):
	D = matrix
	j = outer
	i = inner
	str1 = word1
	str2 = word2

	print 'comparing ' + str1[i-1] + ' to ' + str2[j-1]
	# If both chars equal -> dist unchanged
	if str1[i-1] == str2[j-1]:
		D[j][i] = D[j-1][i-1]
	else:
		D[j][i] =  min(D[j-1][i], D[j][i-1], D[j-1][i-1]) + 1

def feature_compare(matrix, outer, inner, word1, word2):
	D = matrix
	j = outer
	i = inner
	str1 = word1
	str2 = word2

	print 'comparing ' + str1[i-1] + ' to ' + str2[j-1]
	# If both chars equal -> dist unchanged
	comp_total = 0
	for feature in phon_dict.values():
		if str1[i-1] in feature and str2[j-1] in feature:
			# TODO make an actual evaluation procedure
			comp_total = comp_total + 1

	#TODO need floating points in matrix, not ints
	D[j][i] =  comp_total # / len (phon_dict)

#garbage function for testing
def other_foo(matrix, outer, inner, word1, word2):
	D = matrix
	j = outer
	i = inner
	str1 = word1
	str2 = word2

	D[j][i] = 5


#assigns which comparison routine we want - will be a CLA to specify
evaluate = feature_compare

# Convert phonetic string to list of phonemes
def listify(phonetic_string):
	multi_char_pre  = ['d', 't', 'R', 'i']
	multi_char_post = ['Z', 'S', '\\', '~']	
	phonetic_list = []
	dynamic_index = 0
	skips = 0

	for i in range(len(phonetic_string)):
		dynamic_index=i+skips
		if dynamic_index < len(phonetic_string):
			if phonetic_string[dynamic_index] in multi_char_pre:
				if phonetic_string[dynamic_index+1] in multi_char_post:
					phonetic_list.append(phonetic_string[dynamic_index] + phonetic_string[dynamic_index+1])
					skips+=1
					continue
			phonetic_list.append(phonetic_string[dynamic_index])

	print phonetic_list


#   main
#   input : 2 strings
def lcs(str1, str2):
    
	across = len(str1)
	down = len(str2)
	print across,down
	a = 1

    # Initialize (row+1)*(column+1) distance matrix
	D = [[0 for i in range(0, across + 1)] for j in range(0, down + 1)]

	#populate distances for str1 and empty string
	for i in range(1, across + 1):
		D[0][i] = i

	#populate distances for str2 and empty string
	for j in range(1, down + 1):
		D[j][0] = j


	for j in range(1, down + 1):
	
		for i in range(1, across + 1):
		
			evaluate(D,j,i, str1, str2)

		print 'D: '
		for row in D:
			print row
	            


#lcs("hi","ho")
#lcs("hello","elepoant")
#lcs("abcd","efgh")
