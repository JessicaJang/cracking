import math

def smaller_root(a, b, c):
	discriminant = b*b - 4*a*c
	if discriminant < 0:
		print('Error: No real solutions')
	elif discriminant == 0:
		solution = (-b) / (2*a)
		print('Solution : ' + str(solution))
	else:
		sol1 = ((-b) + math.sqrt(discriminant)) / (2*a)
		sol2 = ((-b) - math.sqrt(discriminant)) / (2*a)
		print('Solution1: '+ str(sol1))
		print('Solution2: '+ str(sol2))


smaller_root(1,2,3)
smaller_root(3,6,1)
smaller_root(8,9,4)





