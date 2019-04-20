sentence = input()

vowels = "aeiouyæøå"

def get(c):
	if not c[1].isalpha() or c[1] in vowels:
		return c[0]
	return c[0]+"o"+c[1]
	
print("".join(map(get, zip(sentence, sentence.lower()))))