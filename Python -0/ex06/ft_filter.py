def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\n\nReturn an iterator yielding those items of iterable for which function(item)\nis true. If function is None, return the items that are true."""
    if function is None:
        return [item for item in iterable if item]  # if function is None
        # filter out all False-equivalent values like 0, False, None, etc.
    return [item for item in iterable if function(item)]
    # else filter out all items where the function returns False


# 🔧 What is the built-in filter() function?
# In Python, filter() is a built-in function that lets you filter elements from
#  a list (or any iterable) based on a condition.

# filter(function, iterable)

# function → returns True or False for each item
# iterable → list or other collection
# It returns only the items where the function returned True

#  A lambda is a shortcut way to define a small function in one line.
# It’s called an anonymous function — meaning: it has no name.
# 🧠 Basic Syntax:
# lambda arguments: expression
# It behaves just like a normal function, but in one line.

# ✅ Example 1 – regular function:
# def square(x):
#     return x * x

# print(square(3))  # Output: 9

# ✅ Example 2 – lambda version:
# square = lambda x: x * x
# print(square(3))  # Output: 9
# x is the argument the function takes and x * x is the expression

# 🧪 Real Use: filtering or mapping

# words = ["hi", "hello", "world", "AI"]

# # Filter words longer than 2 characters
# long_words = list(filter(lambda word: len(word) > 2, words))
# print(long_words)  # ['hello', 'world']

# 🚫 Limits of lambda:
# Only one expression (no if/else, loops, or multi-line logic)

# Best used for small, temporary functions (not big logic)
