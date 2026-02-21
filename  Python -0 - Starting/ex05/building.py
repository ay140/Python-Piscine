import sys


def count_characters(text: str) -> None:
    """
    Counts and prints the number of uppercase letters,
    lowercase letters, digits, punctuation, and spaces in the input text.
    """
    total_chars = len(text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())

    punctuation_chars = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    punctuation = sum(1 for c in text if c in punctuation_chars)

    print(f"The text contains {total_chars} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Main entry point. Handles argument parsing and user input.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")

        count_characters(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
