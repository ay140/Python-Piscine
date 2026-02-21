import sys


def string_to_morse(text: str) -> str:
    """
    Convert a text string to its Morse code equivalent.
    """
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.'
    }

    result = []
    for char in text:
        if char == ' ':
            result.append('/')
        else:
            result.append(morse_dict[char.upper()])
    return ' '.join(result)


def main():
    """
    Main function to convert command line argument to Morse code.
    """
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
        text = sys.argv[1]

        if not all(c.isalnum() or c.isspace() for c in text):
            raise AssertionError("AssertionError: the arguments are bad")

        print(string_to_morse(text))

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
