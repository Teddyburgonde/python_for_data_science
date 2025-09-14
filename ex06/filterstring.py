import sys
from ft_filter import ft_filter

def main():
	if len(sys.argv) != 3:
		print("AssertionError: the arguments are bad")
		return
	
	try:
		number = int(sys.argv[2])
	except ValueError:
		print("AssertionError: the arguments are bad")
		return
	
	words = sys.argv[1].split()
	filtered = ft_filter(lambda w: len(w) > number, words)
	print(filtered)

if __name__ == "__main__":
	main()