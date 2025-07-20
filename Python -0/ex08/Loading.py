
def ft_tqdm(lst: range):
    """
    Custom implementation of tqdm progress bar using a generator.
    """
    total = len(lst)  # total number of items in the list
    bar_width = 50  # width of the bar

    for i, val in enumerate(lst):  # enumerate is a function that returns the
        # index and the value of the item in the list
        percent = (i + 1) / total  # calculate the percentage of the progress
        filled = int(percent * bar_width)  # calculate the number of blocks
        bar = "=" * filled + ">" + " " * (bar_width - filled - 1)  # create bar
        print(f"\r{int(percent * 100)}%|[{bar}]| {i + 1}/{total}", end="")
        yield val
    print()  # Newline after the loop ends

# 1. What is a generator?
# A generator is like a smart function that gives you items one at a time,
#  using yield, instead of returning a full list at once.

# 83%|[==========================================>         ]| 277/333
# This is called a progress bar, and the goal of this exercise is to:

# Build a function called ft_tqdm

# That acts like tqdm, a real Python library

# It should print the bar as your program loops through numbers
# tqdm is a Python library that provides a progress bar and other utilities for
#  terminal-based applications.

# 🔍 What's yield?
# yield lets us build a special kind of function called a generator.

#  What is yield?
# yield is like return, but smarter.

# return → gives you a final result and ends the function.

# yield → gives you a value, pauses, remembers where it left off, and continues
#  next time the function is called.

# 🔁 Difference between return and yield
# return	                    yield
# Stops the function Pauses and remembers where it was
# Returns one final value	Returns values one by one, like a for-loop
