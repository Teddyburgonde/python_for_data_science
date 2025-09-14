import sys
from ft_filter import ft_filter

def main():
	"""
	Main entry point of the program.

    - Validates command-line arguments.
    - If the number of arguments is incorrect, prints an AssertionError.
    - Converts the second argument into an integer (`number`).
    - Splits the first argument into words.
    - Uses `ft_filter` to keep only the words whose length is greater than `number`.
    - Prints the filtered list.

    :raises AssertionError:
        - If the number of arguments is not exactly 2 (excluding the script name).
        - If the second argument is not an integer.
    """
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