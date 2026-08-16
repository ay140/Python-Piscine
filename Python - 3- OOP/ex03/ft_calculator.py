class calculator:
    """A calculator class for operations between a vector and a scalar."""

    def __init__(self, vector):
        """Constructor for calculator."""
        # "vector" here is just a normal Python list of numbers,
        # e.g. [0.0, 1.0, 2.0, ...]. We keep it on the instance so the
        # dunder methods below can read/update it.
        self.vector = vector

    # --- My notes on the dunder methods below ---
    # __add__, __sub__, __mul__, __truediv__ are "magic methods" that
    # Python calls automatically when you write v1 + 5, v1 - 5,
    # v1 * 5, v1 / 5 on a calculator object. "object" here is
    # whatever is on the right of the operator (5 in that example).
    #
    # The subject's prototype declares them as "-> None" (they return
    # nothing), and the tester never wraps the calls in print(...)
    # either - it just does "v1 + 5" on its own line. So the ONLY way
    # the result can show up on screen is if we print it ourselves,
    # inside the method. That's why every method below ends with a
    # print() instead of a return.
    #
    # We also overwrite self.vector with the new values, which lets
    # you chain several operations on the same object one after the
    # other (see v3 - 5 followed by v3 / 5 in tester.py: the division
    # applies to the already-subtracted vector, on purpose).
    def __add__(self, object) -> None:
        """Addition of vector with scalar."""
        self.vector = [float(x + object) for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplication of vector with scalar."""
        self.vector = [float(x * object) for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtraction of scalar from vector."""
        self.vector = [float(x - object) for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Division of vector by scalar."""
        # The subject explicitly says: no error handling needed,
        # EXCEPT for division by zero - so this is the one guard we
        # actually have to write ourselves.
        if object == 0:
            print("Error: Division by zero.")
            return
        self.vector = [float(x / object) for x in self.vector]
        print(self.vector)
