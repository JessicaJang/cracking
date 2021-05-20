import unittest

def insertion(N, M, i, j):
	
	for k in range(i, j+1):
		mask = ~(1 << k)
		N = N & mask

	return (N | (M << i))


class Test(unittest.TestCase):

	tests = [(1024, 19, 2, 6, 1100)]

	def test_insertion(self):
		for N, M, i, j, res in self.tests:
			actual = insertion(N, M, i, j)
			print(actual)
			assert res == actual

# main function
if __name__=='__main__':
	unittest.main()
