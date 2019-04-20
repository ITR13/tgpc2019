from decimal import *

pos1 = [int(i) for i in input().split(",")]
pos2 = [int(i) for i in input().split(",")]

dx = abs(pos1[0]-pos2[0])
dy = abs(pos1[1]-pos2[1])

print(dx+dy)

def nCr(n, r):
	div = r, n-r
	if div[0] < div[1]:
		div = n-r, r

	result = 1
	for i in range(div[0]+1, n+1):
		result *= i
	for i in range(2, div[1]+1):
		result //= i
	return result
		
		
print(nCr(dx+dy, dx if dy > dx else dy))
	