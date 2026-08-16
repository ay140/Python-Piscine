from S1E9 import Character


# --- My notes ---
# Baratheon and Lannister both inherit from the abstract Character
# class from ex00. Since they implement "die" themselves (instead of
# leaving it abstract), they become concrete: we CAN build real
# Baratheon(...)/Lannister(...) objects straight from them, no need
# to ever touch Character directly.
class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon"""
        # super().__init__(...) calls Character's constructor first,
        # so first_name/is_alive get set the same way for everyone.
        # Then we add the extra fields that only make sense here.
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Pass is_alive from True to False."""
        self.is_alive = False

    # __str__ is what str(obj) / print(obj) uses.
    # __repr__ is what you get in a shell/debugger, or when an object
    # is shown inside a list/dict. Here they return the exact same
    # text, so __repr__ just calls __str__ to avoid repeating code.
    # The important part: both MUST return an actual string (not a
    # tuple, not None, ...) or Python raises a TypeError.
    def __str__(self):
        """Return string representation of the object."""
        return (
            f"Vector: ('{self.family_name}', "
            f"'{self.eyes}', '{self.hairs}')"
        )

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
        return (
            f"Vector: ('{self.family_name}', "
            f"'{self.eyes}', '{self.hairs}')"
        )

    def __repr__(self):
        """Return formal string representation of the object."""
        return self.__str__()

    # @classmethod means this method receives the CLASS itself as
    # first argument (conventionally named "cls") instead of an
    # instance ("self"). That lets us call it directly on the class,
    # Lannister.create_lannister(...), without having an object yet -
    # this is what the subject calls "creating characters in a
    # chain": an alternative constructor/factory for the class.
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create characters in a chain."""
        return cls(first_name, is_alive)
