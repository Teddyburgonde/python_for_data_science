import sys

MORSE_CODE = {
	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
	'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
	'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
	'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
	'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
	'6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
}

def to_morse(text: str) -> str:
	"""
	Convert a given string into Morse code.

	This function takes a text string, converts each character to uppercase,
	and maps it to its Morse code equivalent using the `MORSE_CODE` dictionary.  
	Spaces are translated into `/`.  

	:param text:
		The input string to convert (letters, digits, and spaces allowed).
	:returns:
		A string representing the input translated into Morse code,
		with Morse symbols separated by spaces.
	:raises ValueError:
		If the string contains characters not present in the `MORSE_CODE` dictionary.

	:example:
		>>> to_morse("SOS")
		'... --- ...'
	"""
	result = []
	for c in text:
		if c.upper() not in MORSE_CODE:
			raise ValueError("Invalid character")
		result.append(MORSE_CODE[c.upper()])
	return " ".join(result)


def main():
	"""
	Main entry point of the program.

	- Validates that exactly one argument is provided (excluding the script name).
	- If the number of arguments is incorrect, prints an AssertionError.
	- Calls `to_morse` to translate the argument into Morse code.
	- Prints the Morse code translation.

	:raises AssertionError:
		- If no argument or more than one argument is given.
		- If the provided string contains invalid characters.
	"""
	if len(sys.argv) != 2:
		print("AssertionError: the arguments are bad")
		return
	try:
		result = to_morse(sys.argv[1])
		print (result)
	except ValueError:
		print("AssertionError: the arguments are bad")
		return

if __name__ == "__main__":
	main()