import re

def isPalindrome1(str1):
	j = len(str1)-1
	for i in str1:
		if i == str1[j]:
			j -= 1
		else: 
			return False
	return True

def isPalindrome2(str1):
	forw = ''.join(re.findall(r'[a-z]+', str1.lower()))
	back = forw[::-1]
	return forw == back

# print(isPalindrome2("abbbba'"))

a = 'adaaa'
b = 'asda'

j = a[::-1]

val = ''.join(re.findall(r'[a-z]', a))
# val = '\n'.join(re.findall(r'[a-z]'))
print(val)