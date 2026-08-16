from S1E7 import Baratheon, Lannister


# --- My notes ---
# King inherits from BOTH Baratheon and Lannister, and those two
# already inherit from Character. Drawn out, it looks like a diamond:
#
#              Character
#              /       \
#       Baratheon     Lannister
#              \       /
#                King
#
# This is the classic "diamond problem" of multiple inheritance.
# Python solves it with the C3 linearization algorithm (the subject
# mentions it): it builds one deterministic Method Resolution Order
# (the MRO) so Character only gets initialised once. You can print
# King.__mro__ to see the exact order Python picked.
#
# Because of that MRO, King("Joffrey") ends up running, in order:
#   Baratheon.__init__ -> (via super()) Lannister.__init__
#                       -> (via super()) Character.__init__
# then control returns UP the chain: Lannister's own lines run
# (family_name/eyes/hairs = Lannister values), and finally Baratheon's
# own lines run *after* that and overwrite them again with the
# Baratheon values. That's why Joffrey ends up looking like a full
# Baratheon even though Lannister briefly "wins" in the middle - the
# "weird"/"trap" part of this exercise.
class King(Baratheon, Lannister):
    """The 'false king': Joffrey, product of two families at once."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for King."""
        super().__init__(first_name, is_alive)

    # The subject asks us to use Properties to control how the
    # physical traits get changed. A property makes a normal-looking
    # attribute access (self.eyes = "blue") secretly run our own code.
    # Here that code just stores the value into __dict__ under the
    # same name, so `eyes`/`hairs` still show up as plain keys when
    # you print __dict__ - only *how* you're allowed to read/write
    # them goes through our code, not where they live.
    @property
    def eyes(self):
        """Getter for the eyes color (goes through a property)."""
        return self.__dict__["eyes"]

    @eyes.setter
    def eyes(self, value):
        """Setter for the eyes color (goes through a property)."""
        self.__dict__["eyes"] = value

    @property
    def hairs(self):
        """Getter for the hairs color (goes through a property)."""
        return self.__dict__["hairs"]

    @hairs.setter
    def hairs(self, value):
        """Setter for the hairs color (goes through a property)."""
        self.__dict__["hairs"] = value

    # Note: Baratheon.__init__ / Lannister.__init__ (ex01) do plain
    # "self.eyes = ..." assignments. Since `self` here is a King
    # instance, and King defines `eyes`/`hairs` as properties, those
    # assignments automatically go through the setters above - no
    # extra code needed for that to happen, that's just how Python
    # attribute lookup works (a property on the class always wins
    # over a plain instance attribute of the same name).

    # These four methods are the public interface the tester actually
    # calls. They just delegate to the properties above, so every
    # read/write of eyes/hairs from the outside is guaranteed to pass
    # through the property (and could be validated/logged there later
    # if we wanted to).
    def get_eyes(self):
        """Getter for eyes."""
        return self.eyes

    def set_eyes(self, eyes):
        """Setter for eyes."""
        self.eyes = eyes

    def get_hairs(self):
        """Getter for hairs."""
        return self.hairs

    def set_hairs(self, hairs):
        """Setter for hairs."""
        self.hairs = hairs
