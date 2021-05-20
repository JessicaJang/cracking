import unittest

def conversion(N, M):
	diff = N ^ M
	count = 0

	while diff != 0:
		if diff & 1 == 1: count += 1
		diff = diff >> 1

	return count

class Test(unittest.TestCase):
	# class variable or instance variable
	test = [(29, 15, 2)]

	def test_conversion(self):
		for N, M, res in self.test:
			actual = conversion(N, M)
			assert res == actual

if __name__=="__main__":
	unittest.main()

