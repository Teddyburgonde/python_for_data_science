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
	Convert a string into Morse code.
	"""
	result = []
	for c in text:
		if c.upper() not in MORSE_CODE:
			raise ValueError("Invalid character")
		result.append(MORSE_CODE[c.upper()])
	return " ".join(result)


def main():
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