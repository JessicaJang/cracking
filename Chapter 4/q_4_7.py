import unittest
import random
from random import seed
from random import randint

def buildOrder(V, E):
	# Build Graph
	graph = {v: set() for v in V}
	status = {v: 0 for v in V} # 0 is not visited 1 is visited 2 is terminated

	# Assume v is not duplicated
	for v1, v2 in E: graph[v1].add(v2)
	res = []

	# call DFS
	for v in V:
		if status[v] == 0:
			dfs_visit(graph, v, status, res)

	return res[::-1]


def dfs_visit(G, v, status, res):

	status[v] = 1 # change to visited

	for u in G[v]:
		if status[u] == 0:
			dfs_visit(G, u, status, res)

	status[v] = 2
	res.append(v)


class Test(unittest.TestCase):
	# Case 1
	projects = ['a', 'b', 'c', 'd', 'e', 'f']
	dependencies = [('a','d'),
					('f', 'b'),
					('b', 'd'),
					('f', 'a'),
					('d', 'c')]


	tests = [(projects, dependencies, ['f','e','b','a','d','c'])]

	def test_is_route(self):

		print("Number of test: ", len(self.tests))
		for v, e, res in self.tests:
			actual = buildOrder(v,e)
			print(actual)
			assert actual == res

if __name__ == "__main__":
    unittest.main()