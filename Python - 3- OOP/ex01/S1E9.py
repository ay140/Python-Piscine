from abc import ABC, abstractmethod


# --- My notes ---
# ABC = "Abstract Base Class". A class that inherits from ABC and has at
# least one method decorated with @abstractmethod can never be
# instantiated directly (Character("x") will crash). It only exists to
# be a common parent that other classes ("Stark", "Baratheon", ...)
# build on top of and finish implementing.
class Character(ABC):
    """Abstract blueprint for a character: has a name and a life status."""

    def __init__(self, first_name, is_alive=True):
        """Store the character's name and life status (alive by default)."""
        # first_name is required, is_alive defaults to True unless the
        # caller says otherwise (e.g. Stark("Lyanna", False)).
        self.first_name = first_name
        self.is_alive = is_alive

    # This method has no real body (just "pass") on purpose: it is a
    # placeholder that FORCES every subclass to write its own "die".
    # As long as a subclass does not override "die", Python still
    # considers it abstract and refuses to instantiate it too.
    @abstractmethod
    def die(self):
        """Kill this character - unfinished, subclasses must define it."""
        pass


class Stark(Character):
    """A member of House Stark - a concrete Character that can die."""

    # Stark does not need to redefine __init__: it simply reuses
    # Character's constructor as-is (that's inheritance for you).
    # It DOES have to redefine "die" though, because it was left
    # abstract in Character - this is what makes Stark a "concrete"
    # (instantiable) class.
    def die(self):
        """Kill this Stark off by flipping is_alive to False."""
        self.is_alive = False
