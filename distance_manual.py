import re
import sys
import itertools

# X = 10

pattern = re.compile(r"^([^\s]+) til ([^\s]+) = ([0-9]+)$")

lines = sys.stdin.read().splitlines()
# lines = [
# 	"a"*i + " til " + "a"*j + " = 1"
# 	for i in range(1, X+1)
#	for j in range(1, X+1) 
# 	if i != j
# ]


paths = {}
city_names = {}

def n(cities):
	return sum(map(city_names.get, cities))

for line in lines:
	result = pattern.match(line)
	cities = result.group(1, 2)
	distance = int(result.group(3))

	if cities[0] not in city_names:
		city_names[cities[0]] = 1<<len(city_names)
	if cities[1] not in city_names:
		city_names[cities[1]] = 1<<len(city_names)
		
	index = tuple(map(city_names.get, cities))
	paths[index] = (distance, distance)
	paths[index[::-1]] = (distance, distance)
	
if len(city_names) <= 1:
	print(0)
	print(0)
	quit(0)
	

def get_shortest(current, other, l):
	if (current, other) in paths:
		return paths[(current, other)]
		
	shortest, longest = None, None
	for next, remaining in next_shortest(other):
		short, long = get_shortest(next, remaining, l-1)
		distance = paths[(current, next)]
		short += distance[0]
		long += distance[1]

		if shortest is None or shortest > short:
			shortest = short
		if longest is None or longest < long:
			longest = long
	
	return (shortest, longest)

	
def next_shortest(cities):
	n = 0
	while cities >> n > 0:
		if (cities>>n)%2==1:
			yield 1<<n, cities - (1<<n)
		n += 1
			
			
shortest, longest = None, None
for city, remaining in next_shortest((1 << len(city_names)) - 1):
	short, long = get_shortest(city, remaining, len(city_names))
	if shortest is None or shortest > short:
		shortest = short
	if longest is None or longest < long:
		longest = long
		
if shortest is None:
	print(0)
	print(0)
else:
	print(shortest)
	print(longest)		
		