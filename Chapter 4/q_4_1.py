# Unit test code from https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_04/p01_route_between_nodes.py 

import unittest
from collections import deque

def is_route(graph, start, end): # Implement with BFS
	print("Test")

	queue = [start]
	visited = []
	while queue:
	 	node = queue.pop(0)

	 	next_node = graph[node]
	 	for i in next_node:
	 		if i == end: return True
	 		if i in visited:
	 			continue
	 		else:
	 			queue.append(i)
	 			visited.append(i)

	return False

class Test(unittest.TestCase):

	# graph is directed and implemented as dictionary
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            assert actual == expected

    # def test_is_route_bfs(self):
    #     for [start, end, expected] in self.tests:
    #         actual = is_route_bfs(self.graph, start, end)
    #         assert actual == expected


if __name__ == "__main__":
    unittest.main()