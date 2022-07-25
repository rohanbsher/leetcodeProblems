
def sortString(str1):
	val = str1.lower().split()
	print(sorted(val))

def sortString2(str1):
	return ' '.join(sorted(str1.split(), key=str.casefold))

str1 = "how are You"
sortString(str1)
# print(sortString2(str1))