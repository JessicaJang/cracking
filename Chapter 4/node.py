class Node():
	def __init__(self, item, left=None, right=None):
		self.item = item
		self.left = None
		self.right = None
		self.parent = None

	def disp(self, nesting=0):
		indent = " " * nesting * 2
		output = f"{self.item}\n"
		if self.left is not None:
			output += f"{indent}L:"
			output += self.left.disp(nesting + 1)
		if self.right is not None:
			output += f"{indent}R:"
			output += self.right.disp(nesting + 1)
		return output

	def __str__(self):
		return self.disp()