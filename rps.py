moves = ["stein", "saks", "papir"]
selected = input().split(" ")

s = selected[0] + " vs " + selected[1]

if selected[0]==selected[1]:
	print("Uavgjort, "+s)
elif (moves.index(selected[0])+1)%3 == moves.index(selected[1]):
	print("Spiller en vant, "+s)
else:
	print("Spiller to vant, "+s)