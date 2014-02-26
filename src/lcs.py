""" Longest common subsequence algorithm  """
"""
 *** BUGS ***
len(str1) != len(str2) -> index out of range

"""

# input : 2 strings
# print : distance (# edits to transform str1<->str2)
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
		
		
			print 'comparing ' + str1[i-1] + ' to ' + str2[j-1]
            # If both chars equal -> dist unchanged
			if str1[i-1] == str2[j-1]:
				D[j][i] = D[j-1][i-1]
			else:
				D[j][i] =  min(D[j-1][i], D[j][i-1], D[j-1][i-1]) + 1

#			print 'D: '
#			for row in D:
#				print row

		print 'D: '
		for row in D:
			print row
	            


#lcs("hi","ho")
#lcs("hello","elepoant")
#lcs("abcd","efgh")

#				D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1]) + 1
