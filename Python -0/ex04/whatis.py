import sys # module to get the command line arguments These are stored in a list called sys.argv.

def main():
    """
    Reads a number from command-line arguments and prints if it's even or odd.
    Handles invalid input with AssertionError.
    """
    try:
        if len(sys.argv) == 1:
            # No argument given → do nothing
            pass
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            arg = sys.argv[1]
            try:
                number = int(arg)  # This will raise ValueError for things like "--1" or "3.5"
            except ValueError:
                raise AssertionError("argument is not an integer")

            if number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")

    except AssertionError as msg:
        print(f"AssertionError: {msg}")

if __name__ == "__main__":
    main()

# 🚨 What is AssertionError?
# 📌 In Python:
# An AssertionError is a type of error that happens when an assert or raise AssertionError(...) fails.

# You can use it when:

# You expect something to be true

# But it turns out not true, and you want to stop the program and show an error