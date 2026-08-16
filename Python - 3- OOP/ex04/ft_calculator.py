class calculator:
    """A calculator class that performs vector operations."""

    # --- My notes ---
    # This time the tester calls calculator.dotproduct(a, b) directly
    # on the CLASS, without ever writing calculator(...) to make an
    # instance first. A plain method can't be called that way (it
    # always expects a "self" first). @staticmethod is the decorator
    # that removes that requirement: it turns the method into a
    # regular function that just happens to live inside the class's
    # namespace, so no instantiation is needed - exactly what the
    # subject asks for ("without instantiating this class").
    #
    # The subject also says these don't return anything ("-> None")
    # and the tester never prints the calls itself, so - same idea as
    # ex03 - each method has to print its own result.
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        # Dot product = multiply each pair of matching elements, then
        # add all those products together. zip() pairs up V1[i] with
        # V2[i] for every index at once.
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
        # "sous" is French for "under/minus" - this is V1 - V2,
        # element by element.
        res = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
