"""
File: quadratic_solver.py
Name:
-----------------------
This program implements a console-based solver for a
quadratic equation.

It asks the user to input three values a, b, and c,
and computes the roots of the equation:
ax^2 + bx + c = 0.

The output format should match the sample run shown
in the Assignment 2 handout.
"""

import math


def main():
	"""
	TODO:
	"""
	print('Welcome to Quadratic Solder')
	a = int(input("a: "))
	b = int(input('b: '))
	c = int(input('c: '))
	discriminant =b*b-4*a*c
	if discriminant > 0:
		x1 = (-b + math.sqrt(discriminant)) / (2 * a)
		x2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print(x1, x2)
	elif discriminant == 0:
		y = (-b + math.sqrt(discriminant)) / (2 * a)
		print(y)
	else:
		print(str('No_real_roots'))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
