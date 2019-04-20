import re

haystack = input()
key = input().replace("_", ".")

matches = list(re.finditer(key, haystack))
print([m.start(0) for m in matches])
print("\n".join([m.group(0) for m in matches]))