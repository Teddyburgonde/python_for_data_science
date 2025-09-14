import sys
import string


def count_chars(text: str) -> int:
    """
    Analyze a text and count different types of characters.

    The function iterates through the given string and computes the number of:
        - uppercase letters
        - lowercase letters
        - digits
        - spaces
        - punctuation marks

    :param text:
        The string to analyze.
    :returns:
        A dictionary containing the total number of characters and
        the detailed breakdown (upper, lower, digits, spaces, punctuation).

    :example:
        >>> count_chars("Hello, World! 42")
        {'total': 16, 'upper': 2, 'lower': 8,
        'digits': 2, 'spaces': 2, 'punctuation': 2}
    """
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
        "total": len(text) + 1,
        "upper": upper,
        "lower": lower,
        "digits": digits,
        "spaces": spaces,
        "punctuation": punct
    }


def main():
    """
    Main entry point of the program.

    - Checks command-line arguments.
    - If no argument is provided, asks the user to input a text.
    - If more than one argument is provided, prints an error message.
    - Otherwise, analyzes the given text with `count_chars`
      and prints the statistics.

    :raises AssertionError:
        If more than one argument is provided.
    """
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
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
