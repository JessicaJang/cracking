import math
import random

def triangle_area(x0,y0,x1,y1,x2,y2):
	side1 = math.sqrt((x0-x1) ** 2 + (y0-y1) ** 2)
	side2 = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
	side3 = math.sqrt((x2-x0) ** 2 + (y2-y0) ** 2)

	length = side1 + side2 + side3
	return length

print(triangle_area(0,0,2,0,0,2))
