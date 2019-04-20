#!/usr/bin/python
import math

## https://web.archive.org/web/20100617074625/http://gist.github.com/242402
# Graham Scan O(n log n) - Tom Switzer <thomas.switzer@gmail.com>
TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

def turn(p, q, r):
	return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def _keep_left(hull, r):
	while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
			hull.pop()
	if not hull or hull[-1] != r:
		hull.append(r)
	return hull

def convex_hull(points):
	"""Returns points on convex hull of an array of points in CCW order."""
	points = sorted(points)
	l = reduce(_keep_left, points, [])
	u = reduce(_keep_left, reversed(points), [])
	return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l
##	

n = int(raw_input())
hull = [tuple(map(float, raw_input().split(" "))) for _ in range(n)]
hull = convex_hull(hull)[::-1]


## https://stackoverflow.com/a/13545089
def mostfar(j, n, s, c, mx, my): # advance j to extreme point
	xn, yn = hull[j][0], hull[j][1]
	rx, ry = xn*c - yn*s, xn*s + yn*c
	best = mx*rx + my*ry
	while True:
		x, y = rx, ry
		xn, yn = hull[(j+1)%n][0], hull[(j+1)%n][1]
		rx, ry = xn*c - yn*s, xn*s + yn*c
		if mx*rx + my*ry >= best:
			j = (j+1)%n
			best = mx*rx + my*ry
		else:
			return (x, y, j)

min_solution = None
			
n = len(hull)
iL = iR = iP = 1				# indexes left, right, opposite
pi = 4*math.atan(1)
for i in range(n-1):
	dx = hull[i+1][0] - hull[i][0]
	dy = hull[i+1][1] - hull[i][1]
	theta = pi-math.atan2(dy, dx)
	s, c = math.sin(theta), math.cos(theta)
	yC = hull[i][0]*s + hull[i][1]*c

	xP, yP, iP = mostfar(iP, n, s, c, 0, 1)
	if i==0: iR = iP
	xR, yR, iR = mostfar(iR, n, s, c,  1, 0)
	xL, yL, iL = mostfar(iL, n, s, c, -1, 0)
	area = (xR-xL)*(yP-yC)
	
	if min_solution is None or min_solution[0] > area:
		w, h = xR-xL, yP-yC
		L, R = hull[iL], hull[iR]
		xC = hull[i][0]*c - hull[i][1]*s
		tL = (c*L[0]-s*L[1], c*L[1]+s*L[0])
		tR = (c*R[0]-s*R[1], c*R[1]+s*R[0])
		
		x_0 = tL[0]
		x_1 = tR[0]
		y_0 = yC
		y_1 = yC+h
		
		s, c = math.sin(-theta), math.cos(-theta)
		p0 = (c*x_0-s*y_0, c*y_0+s*x_0)
		p1 = (c*x_0-s*y_1, c*y_1+s*x_0)
		p2 = (c*x_1-s*y_1, c*y_1+s*x_1)
		p3 = (c*x_1-s*y_0, c*y_0+s*x_1)
		
		min_solution = (
			area, 
			(p0, p1, p2, p3),
		)
	
##


points = sorted(min_solution[1])
# points = min_solution[1]

print(round(min_solution[0], 1)	)
print(
	"\n".join(
		" ".join(
			str(round(j, 1) if round(j, 1) != 0 else 0.0) 
			for j in i
		)
		for i in points
	)
)

