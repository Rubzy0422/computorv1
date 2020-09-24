import sys 
import re
import math



# Python3 implementation of the approach 
import math 
  
# Recursive function that returns square root 
# Geeks for geeks === contributed by 29AjayKumar 
# of a number with precision upto 5 decimal places 
def sqrt(n):
	_root = n/2
	_sum = n/4
	absv = lambda n : -1 * n if n < 0 else n
	while (absv(_root * _root - n) > 0.000001):
		if _root * _root > n:
			_root -= _sum
		else:
			_root += _sum
		_sum = _sum / 2
	return round(_root, 7) 

def input_check(argv):
	if (len(argv) != 2):
		print("Invalid input, please Input one string as argument")
		sys.exit()
	else:
		pattern = re.compile(r'\s+')
		arr = re.split(pattern, argv[1])
		return max_exponentional(arr)

def modif_array(arr):
	lst = []
	for i, x in enumerate(arr):
		if (i > 0 and arr[i - 1] == '-'):
			arr[i] = '-' + arr[i]

	for i, x in enumerate(arr):
		if (not (x == '-' or x == '+')):
			lst.append(x)
	return lst

def solve(b,c):
	if (not b == 0):
		print("The solution is:\n" + str(-c / b))
	else:
		print("Cannot divide by zero, I don't have a solution!")
	
def discriminant(a,b,c):
	disc = (b**2) - (4*a*c)
	if (disc > 0):
		print("Discriminant is strictly positive, the two solutions are:")
		print((-b-sqrt(disc))/(2*a))
		print((-b+sqrt(disc))/(2*a))

	if (disc == 0):
		print("Discriminant is zero, the solution is:")
		print((-b-sqrt(disc))/(2*a))
		print((-b+sqrt(disc))/(2*a))
	if (disc < 0):
		print("Discriminant is strictly negative, solution only with imaginary numbers")

def negative(arr):
	tmp = []
	for i, x in enumerate(arr):
		if x[0] == '-':
			tmp.append(x[1:])
		elif (x == '*'):
			tmp.append(x)
		else:
			tmp.append('-' + x)
	return tmp

def display(num):
	if (num > 0):
		return '+ ' + str(num)
	else:
		return  str(num)

def multiply(arr, i):
	lst = arr[i-1:i+2]
	del arr[i-1:i+2]
	num1 = 1
	exp = ""
	exp1 = ""
	exp2 = ""

	if (re.search('\\^',lst[2])):
		snum = lst[2][:lst[2].find('^')-1]
		exp1 = lst[2][lst[2].find('^')-1:]
		if (snum != ""):
			num1 = float(lst[2][:lst[2].find('^')-1])
	else:
		num1 = float(lst[2])

	num2 = 1
	if (re.search('\\^',lst[0])):
		snum = lst[0][:lst[0].find('^')-1]
		exp2 = lst[0][lst[0].find('^')-1:]
		print(exp2)
		if (snum != ""):
			num2 = float(lst[0][:lst[0].find('^')-1])
	else:
		num2 = float(lst[0])
			
	if (exp1 != ""):
		exp = exp1
	elif (exp2 != ""):
		exp = exp2
	
	arr.insert(i -1 , str(num1 * num2) + exp)

def simplify_equation(arr1):
	cba = [0,0,0]
	char = 'x'
	for i in range(3):
		for x in arr1:
			if (re.search('\\^' + str(i), x)):
				#print(x[:x.find('\\^')-1])
				if (x[:x.find('^')-1] == ""):
					cba[i] += 1
				elif (x[:x.find('^')-1] == '-'):
					cba[i] += -1
				else:
					cba[i] += float(x[:x.find('^')-1])
				char = x[x.find('^')-1]
			if (not re.search('\\^', x) and x == '*' and i == 0):
				cba[0] += float(x)
	return (cba[2], cba[1], cba[0], char)
	
def reduce_equation(left, right):
	while ('*' in left):
		multiply(left, left.index('*'))
	while ('*' in right):
		multiply(right, right.index('*'))

	left = modif_array(left)
	right = negative(modif_array(right))
	left.extend(right)

	a,b,c,char = simplify_equation(left)

	reduced = ""
	if (a != 0):
		reduced = reduced + display(a) + char + '^2' + " "
	if (b != 0):
		reduced = reduced + display(b) + char  + " "
	if (c != 0):
		reduced = reduced + display(c)

	print("Reduced form:", reduced + '= 0')
	if (a != 0):
		discriminant(a,b,c)
	elif (b != 0):
		solve(b,c)
	else:
		print("all the real numbers are solution or invalid")

def power_balance(arr):
	lst2 = []
	# set powers
	for i, x in enumerate(arr):
		if (re.search('[a-zA-Z]+',x)):
			if (not re.search('\\^', x)):
				x += '^1'
				lst2.append(x)
			else:
				if (re.search('\\^0', x)):
					x = '1'
				lst2.append(x)
		else:
			lst2.append(x)
	return lst2

def max_exponentional(lst):
	arr = power_balance(lst)
	res = (list(filter(lambda x: '^' in x, arr)))
	_max = 0
	for x in res:
		x = float(x[x.find('^')+1:])
		if (x > _max):
			_max = x
	if (_max <= 2 and _max > 0):
		print("Polynomial degree:", int(_max))
		return arr
	elif (_max == 0):
		print("all the real numbers are solution or invalid equasion")
		sys.exit()
	else:
		print("The polynomial degree is stricly greater than 2, I can't solve")
		sys.exit()

def solve_equasion():
	lst = input_check(sys.argv)
	if '=' in lst:
		eqindex = lst.index('=')
		left = lst[:eqindex]
		right = lst[eqindex+1:]
		if (len(right) < 1):
			print("Invalid input, pleae make sure the right hand of the equasion is populated")
		reduce_equation(left, right)
	else:
		print("Equals not found!")
		sys.exit()

solve_equasion()