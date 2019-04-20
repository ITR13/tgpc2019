parts  = [int(i) for i in input().split(" ")]
needed = [int(i) for i in input().split(" ")]
assert(len(parts)==len(needed))

count = min([i//j for i, j in zip(parts, needed) if j > 0])

print(count)
print(" ".join([
	str(i-j*count)
	for i, j in zip(parts, needed)
]))
