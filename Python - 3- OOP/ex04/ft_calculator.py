class calculator:
    """A calculator class that performs vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        res = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the addition of two vectors."""
        res = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the subtraction of two vectors."""
        res = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
