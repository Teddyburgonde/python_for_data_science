import sys
import string

def count_chars(text: str) ->int:
	upper = 0
	lower = 0
	digits = 0
	spaces = 0
	punct = 0
	for char in text:
		if (char.isupper()):
			upper += 1
		elif (char.islower()):
			lower += 1
		elif char.isdigit():
			digits += 1
		elif char.isspace():
			spaces += 1
		elif char in string.punctuation:
			punct += 1

	return {
		"total": len(text),
		"upper": upper,
		"lower": lower,
		"digits": digits,
		"spaces": spaces,
		"punctuation": punct
	}

def main():
	if len(sys.argv) == 1:
		text = input("What is the text to analyze?\n")
	elif len(sys.argv) > 2:
		print("AssertionError: more than one argument is provided")
		return
	else:
		text = sys.argv[1]

	stats = count_chars(text)
	print(f"The text contains {stats['total']} characters:")
	print(f"{stats['upper']} upper letters")
	print(f"{stats['lower']} lower letters")
	print(f"{stats['punctuation']} punctuation marks")
	print(f"{stats['spaces']} spaces")
	print(f"{stats['digits']} digits")

if __name__ == "__main__":
	main()
