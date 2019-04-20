## Fails


def rotate90(point, origin):
	assert(len(point)==2 and len(origin)==2)
	return origin[0] + origin[1]-point[1], origin[1] + point[0]-origin[0]

def lineintersect(a, b):
	if len(a) == 1 and len(b) == 1:
		return a[0]==b[0]
	if len(a) == 2 and len(b) == 1:
		a, b = b, a
	if len(a) == 1 and len(b) == 2:
		return a[0], a[0]*b[0]+b[1]
	
	assert(len(a)==2 and len(b)==2)
	
	if a[0]==b[0]:
		return a[1] == b[1]

	dx = a[0] - b[0]
	dy = b[1] - a[1]
	x = dy/dx
	y = a[0]*x+a[1]
	
	return x, y

def pointintersect(line, point):
	if len(line)==1:
		return point[0] == line[0]

	assert(len(line)==2 and len(point)==2)
	y = line[0]*point[0] + line[1]
	return y==point[1]
	
n = int(input())
antennas = [[float(i) for i in input().split(" ") if len(i)>0] for _ in range(n)]

d = {}

for antenna in antennas:
	if antenna[0] not in d:
		d[antenna[0]] = []
	d[antenna[0]].append(antenna)

sol_line = None
sol_pos = None
for s, couples in d.items():
	if len(couples) < 1 or s < 0:
		continue
	zero = couples[0]
	for antenna in couples[1:]:
		if antenna[1] == zero[1] and antenna[2] == zero[2]:
			continue
		
		middle = (zero[1]+antenna[1])/2, (zero[2] + antenna[2])/2
		p0, p1 = rotate90(zero[1:], middle), rotate90(antenna[1:], middle)
		dx, dy = p0[0]-p1[0], p0[1]-p1[1]
		if dx == 0:
			line = (p0[0],)
		else:
			ratio = dy/dx
			line = (ratio, p1[1]-p1[0]*ratio)
		
		if sol_line is None:
			sol_line = line
			continue
		if sol_pos is None:
			result = lineintersect(sol_line, line)
			if result is True:
				continue
			if result is False:
				print("Inconclusive")
				quit(0)
			sol_pos = result
			continue
		
		if not pointintersect(line, sol_pos):
			print("Inconclusive")
			quit(0)

if sol_pos is None:
	print("Inconclusive")
else:
	print(round(sol_pos[0], 1), round(sol_pos[1], 1))