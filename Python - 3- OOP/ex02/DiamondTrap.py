from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The false king."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for King."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """Setter for eyes."""
        self.eyes = eyes

    def get_eyes(self):
        """Getter for eyes."""
        return self.eyes

    def set_hairs(self, hairs):
        """Setter for hairs."""
        self.hairs = hairs

    def get_hairs(self):
        """Getter for hairs."""
        return self.hairs
