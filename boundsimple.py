n = int(input())

X = [None, None]
Y = [None, None]

def set_v(v, arr):
	if arr[0] is None:
		arr[0], arr[1] = v, v
		return
	if arr[0] > v:
		arr[0] = v
	if arr[1] < v:
		arr[1] = v
	
for _ in range(n):
	x, y = tuple([int(i) for i in input().split(" ")])
	set_v(x, X)
	set_v(y, Y)
	
print((X[1]-X[0])*(Y[1]-Y[0]))
	