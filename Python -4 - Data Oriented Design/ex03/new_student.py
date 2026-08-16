import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Return a random 15-letter lowercase id, e.g. 'trannxhndgtolvh'."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


# --- My notes ---
# @dataclass auto-generates __init__ and __repr__ for us from the
# annotated fields below, based on their declaration order - that is
# exactly why the subject says "you must not write __str__/__repr__
# yourself": writing our own would just override (and duplicate) what
# the decorator already builds.
#
# "login" and "id" are computed FROM name/surname, not passed in by
# the caller, so they use field(init=False): that removes them from
# the auto-generated __init__'s parameter list entirely. Trying to
# pass id=... then fails with a plain TypeError, exactly like passing
# an argument no function expects - which is exactly what the subject
# asks for ("must return an error").
# We fill them in with __post_init__, a special method dataclasses
# calls automatically right after __init__ finishes assigning the
# normal fields (name, surname, active) - so name/surname are already
# set and safe to read at that point.
@dataclass
class Student:
    """A student record with an auto-generated login and id."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Fill in the fields that can't come from the constructor."""
        # e.g. name="Edward", surname="agle" -> login="Eagle"
        self.login = self.name[0].upper() + self.surname.lower()
        self.id = generate_id()
