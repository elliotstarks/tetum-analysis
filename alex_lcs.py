""" Generic strnig comparison algorithm  """
"""

"""
import collections

# 'feature': grapheme1, grapheme2, grapheme3, ... , 
voiced = ['m', 'n', 'b']
nasal = ['m', 'n']
#          stop,
#          sibilant fricative,
#          non-sibilant fricative,
#          approximant,
#          flap,
#          trill,
#          lateral fricative,
#          lateral approx.,
#          lat. flap, 
#          bilabial,
#          labiodental,
#          dental,
#          alveolar,
#          post-alveolar,
#          retroflex,
#          alveolopalatal
#          palatal
#          velar
#          uvular
#          pharyngeal
#          epiglottal
#          glottal

phon_dict = {'voiced' : voiced, 'nasal' : nasal}

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
			# print 'matched' + str(feature)
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
