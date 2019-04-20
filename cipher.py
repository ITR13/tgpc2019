n = 3
letters = {}
for i in range(26):
	letters[chr(i+ord('a'))] = chr((i+n)%26+ord('a'))
	letters[chr(i+ord('A'))] = chr((i+n)%26+ord('A'))
	
print("".join(map(lambda x: letters[x] if x in letters else x, input())))