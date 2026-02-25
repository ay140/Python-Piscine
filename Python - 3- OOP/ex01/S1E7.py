from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Pass is_alive from True to False."""
        self.is_alive = False

    def __str__(self):
        """Return string representation of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return formal string representation of the object."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Pass is_alive from True to False."""
        self.is_alive = False

    def __str__(self):
        """Return string representation of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return formal string representation of the object."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create characters in a chain."""
        return cls(first_name, is_alive)
