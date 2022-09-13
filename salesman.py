rom sys import maxsize
from itertools import permutations
V = 4

def travellingSalesmanProblem(graph, s):
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:
		current_pathweight = 0
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]
		min_path = min(min_path, current_pathweight)

	return min_path

if _name_ == "_main_":
	graph = [[0, 10, 15, 45], [10, 0, 32, 25],
			[15, 35, 0, 39], [20, 52, 30, 0]]
	s = 0
	print(travellingSalesmanProblem(graph, s))
