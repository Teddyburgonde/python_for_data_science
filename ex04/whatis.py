import sys

if len(sys.argv) - 1 == 0:
	pass 
elif len(sys.argv) - 1 > 1:
	print("AssertionError: more than one argument is provided")
else:
	arg = sys.argv[1]
	try:
		number = int(arg)
		if number % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except ValueError:
		print("AssertionError: argument is not an integer")

