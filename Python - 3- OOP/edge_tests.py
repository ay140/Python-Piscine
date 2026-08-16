"""
Extra edge-case tests, beyond what the subject's tester.py checks.
Not part of the graded turn-in - just for extra confidence.
"""
import sys
import importlib


class Report:
    """Tiny helper that prints PASS/FAIL lines and counts the
    failures, without needing a global variable - we just create one
    instance and pass it into every test function instead."""

    def __init__(self):
        """Start with a clean slate: zero failures recorded so far."""
        self.failures = 0

    def check(self, label, condition):
        """Print one PASS/FAIL line for `label` and tally failures."""
        status = "OK " if condition else "FAIL"
        print(f"[{status}] {label}")
        if not condition:
            self.failures += 1


def _raises_typeerror(fn):
    """Return True if calling fn() raises a TypeError, else False."""
    try:
        fn()
        return False
    except TypeError:
        return True


def test_ex00(report):
    """Exercise the abstract Character class and its Stark subclass."""
    sys.path.insert(0, "ex00")
    S1E9 = importlib.import_module("S1E9")
    Character, Stark = S1E9.Character, S1E9.Stark

    report.check("Character() raises TypeError (abstract)",
                 _raises_typeerror(lambda: Character("hodor")))
    report.check("Stark inherits from Character",
                 issubclass(Stark, Character))

    ned = Stark("Ned")
    report.check("default is_alive is True", ned.is_alive is True)
    ned.die()
    report.check("die() flips is_alive to False", ned.is_alive is False)

    lyanna = Stark("Lyanna", False)
    report.check("explicit is_alive=False respected",
                 lyanna.is_alive is False)

    report.check("Character has __doc__", bool(Character.__doc__))
    report.check("Stark has __doc__", bool(Stark.__doc__))
    report.check("Stark.__init__ has __doc__",
                 bool(Stark.__init__.__doc__))
    report.check("Stark.die has __doc__", bool(Stark.die.__doc__))
    sys.path.pop(0)
    for m in ("S1E9",):
        sys.modules.pop(m, None)


def test_ex01(report):
    """Exercise the Baratheon/Lannister families and create_lannister."""
    sys.path.insert(0, "ex01")
    S1E7 = importlib.import_module("S1E7")
    Baratheon, Lannister = S1E7.Baratheon, S1E7.Lannister

    robert = Baratheon("Robert")
    report.check("Baratheon defaults (eyes)", robert.eyes == "brown")
    report.check("Baratheon defaults (hairs)", robert.hairs == "dark")
    report.check("__str__ returns a str", isinstance(str(robert), str))
    report.check("__repr__ returns a str", isinstance(repr(robert), str))
    report.check("__str__ == __repr__ text", str(robert) == repr(robert))

    cersei = Lannister("Cersei")
    report.check("Lannister defaults (eyes)", cersei.eyes == "blue")
    report.check("Lannister defaults (hairs)", cersei.hairs == "light")

    jaine = Lannister.create_lannister("Jaine", True)
    report.check("create_lannister returns a Lannister",
                 isinstance(jaine, Lannister))
    report.check("create_lannister sets first_name",
                 jaine.first_name == "Jaine")
    report.check("create_lannister default is_alive=True",
                 Lannister.create_lannister("X").is_alive is True)

    sys.path.pop(0)
    for m in ("S1E7", "S1E9"):
        sys.modules.pop(m, None)


def test_ex02(report):
    """Exercise the King diamond-inheritance class and its properties."""
    sys.path.insert(0, "ex02")
    DiamondTrap = importlib.import_module("DiamondTrap")
    King = DiamondTrap.King

    report.check(
        "King MRO includes both families",
        {"Baratheon", "Lannister", "Character"}
        <= {c.__name__ for c in King.__mro__})

    joffrey = King("Joffrey")
    report.check("King starts with Baratheon look (eyes)",
                 joffrey.eyes == "brown")
    report.check("King starts with Baratheon look (hairs)",
                 joffrey.hairs == "dark")
    report.check("eyes is a real property on the class",
                 isinstance(King.__dict__.get("eyes"), property))
    report.check("hairs is a real property on the class",
                 isinstance(King.__dict__.get("hairs"), property))

    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")
    report.check("set_eyes updates get_eyes", joffrey.get_eyes() == "blue")
    report.check("set_hairs updates get_hairs",
                 joffrey.get_hairs() == "light")
    report.check("__dict__ still shows plain 'eyes' key",
                 joffrey.__dict__.get("eyes") == "blue")
    report.check("__dict__ still shows plain 'hairs' key",
                 joffrey.__dict__.get("hairs") == "light")

    sys.path.pop(0)
    for m in ("DiamondTrap", "S1E7", "S1E9"):
        sys.modules.pop(m, None)


def test_ex03(report):
    """Exercise the vector-vs-scalar calculator (ex03)."""
    sys.path.insert(0, "ex03")
    ft_calculator = importlib.import_module("ft_calculator")
    calculator = ft_calculator.calculator

    v = calculator([0.0, 1.0, 2.0])
    v + 10
    report.check("__add__ mutates vector", v.vector == [10.0, 11.0, 12.0])

    v2 = calculator([2.0, 4.0])
    v2 * 3
    report.check("__mul__ mutates vector", v2.vector == [6.0, 12.0])

    v3 = calculator([10.0, 20.0])
    v3 - 5
    report.check("__sub__ mutates vector", v3.vector == [5.0, 15.0])

    v4 = calculator([10.0, 20.0])
    v4 / 5
    report.check("__truediv__ mutates vector", v4.vector == [2.0, 4.0])

    v5 = calculator([10.0, 20.0])
    v5 / 0  # must NOT raise, per subject ("no error handling except /0")
    report.check(
        "division by zero is caught (no crash, vector unchanged)",
        v5.vector == [10.0, 20.0])

    sys.path.pop(0)
    sys.modules.pop("ft_calculator", None)


def test_ex04(report):
    """Exercise the two-vector calculator's staticmethods (ex04)."""
    sys.path.insert(0, "ex04")
    ft_calculator = importlib.import_module("ft_calculator")
    calculator = ft_calculator.calculator

    a, b = [5, 10, 2], [2, 4, 3]
    # These are staticmethods: must be callable on the class directly.
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)
    report.check(
        "dotproduct is a staticmethod",
        isinstance(calculator.__dict__["dotproduct"], staticmethod))
    report.check(
        "add_vec is a staticmethod",
        isinstance(calculator.__dict__["add_vec"], staticmethod))
    report.check(
        "sous_vec is a staticmethod",
        isinstance(calculator.__dict__["sous_vec"], staticmethod))

    sys.path.pop(0)
    sys.modules.pop("ft_calculator", None)


def main():
    """Run all edge-case checks for the OOP piscine exercises."""
    report = Report()
    test_ex00(report)
    test_ex01(report)
    test_ex02(report)
    test_ex03(report)
    test_ex04(report)
    print()
    if report.failures:
        print(f"{report.failures} check(s) FAILED")
        sys.exit(1)
    print("All edge-case checks passed.")


if __name__ == "__main__":
    main()
