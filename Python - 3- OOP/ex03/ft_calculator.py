class calculator:
    """A calculator class for operations between a vector and a scalar."""

    def __init__(self, vector):
        """Constructor for calculator."""
        self.vector = vector

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
        if object == 0:
            print("Error: Division by zero.")
            return
        self.vector = [float(x / object) for x in self.vector]
        print(self.vector)
