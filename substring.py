from difflib import SequenceMatcher 
	  
factor = int(input())
original = input()
split = [original[i:i+factor] for i in range(0, len(original), factor)]
s1 = "".join(split[::2])
s2 = "".join(split[1::2])

s = SequenceMatcher(None, s1, s2, False)
match = s.find_longest_match(0, len(s1), 0, len(s2))
if match.size==0:
	print("None")
else:
	print(s1[match.a:match.a+match.size])