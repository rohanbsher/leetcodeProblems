class IsomorphicStrings():
	def __init__(self):
		pass

	def isIsomorphic(self,str1,str2):
		dict1 = {}
		dict2 = {}

		for i,j in zip(str1, str2):
			if (i not in dict1 and j not in dict2):
					dict1[i] = j
					dict2[j] = i
			elif (dict1.get(i) != j or dict2.get(j) != i):
				return False
		return True