"""
Extra edge-case tests for Day 4 (Data Oriented Design), beyond what
the subject's own tester.py checks. Not part of the graded turn-in.
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


def _fresh_import(path, name):
    """Import (or re-import) `name` from `path`, isolated per test."""
    sys.path.insert(0, path)
    if name in sys.modules:
        del sys.modules[name]
    mod = importlib.import_module(name)
    sys.path.pop(0)
    return mod


def _raises_typeerror(fn):
    """Return True if calling fn() raises a TypeError, else False."""
    try:
        fn()
        return False
    except TypeError:
        return True


def _capture(fn):
    """Call fn() and return everything it printed, as a string."""
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()


def _ex03_path():
    """Return the path to ex03's new_student.py source file."""
    import os
    return os.path.join("ex03", "new_student.py")


def test_ex00(report):
    """Exercise ft_statistics: known values, empty data, edge sizes."""
    mod = _fresh_import("ex00", "statistics")
    ft_statistics = mod.ft_statistics

    def compute_textbook():
        """Request mean/var/std on a classic textbook dataset."""
        ft_statistics(2, 4, 4, 4, 5, 5, 7, 9, a="mean", b="var", c="std")

    out = _capture(compute_textbook)
    # classic textbook example: mean 5, population var 4, std 2
    report.check("mean of textbook set", "mean : 5.0" in out)
    report.check("population variance (divide by n, not n-1)",
                 "var : 4.0" in out)
    report.check("population std", "std : 2.0" in out)

    def compute_no_data():
        """Ask for a mean with no positional data at all."""
        ft_statistics(a="mean")

    out = _capture(compute_no_data)
    report.check("no data at all -> ERROR, no crash", out.strip() == "ERROR")

    def compute_unknown_stat():
        """Ask for a stat name that doesn't exist."""
        ft_statistics(1, 2, 3, a="not_a_real_stat")

    out = _capture(compute_unknown_stat)
    report.check("unknown stat name -> silently ignored (no output)",
                 out.strip() == "")

    def compute_even_median():
        """Ask for a median on an even-length dataset."""
        ft_statistics(1, 2, 3, 4, a="median")

    out = _capture(compute_even_median)
    report.check("even-length median is the average of the middle two",
                 out.strip() == "median : 2.5")

    def compute_single_quartile():
        """Ask for a quartile on a single-value dataset."""
        ft_statistics(42, a="quartile")

    single = _capture(compute_single_quartile)
    report.check("single-value quartile doesn't crash",
                 single.strip() == "quartile : [42.0, 42.0]")


def test_ex01(report):
    """Exercise square/pow and the outer/inner closure counter."""
    mod = _fresh_import("ex01", "in_out")
    square, mypow, outer = mod.square, mod.pow, mod.outer

    report.check("square(4) == 16", square(4) == 16)
    report.check("pow(2) == 4 (2**2)", mypow(2) == 4)

    c1 = outer(2, square)
    c2 = outer(2, square)
    v1a, v1b = c1(), c1()
    v2a = c2()
    report.check("two counters don't share state (no hidden global)",
                 v2a == 4 and v1a == 4 and v1b == 16)

    # outer() must not touch module/global scope at all - check
    # actual code lines only, so mentions of "global" inside comments
    # (e.g. explaining why we use nonlocal instead) don't count.
    import inspect
    code_lines = [line.split("#", 1)[0]
                  for line in inspect.getsource(mod).splitlines()]
    report.check(
        "no 'global' statement used anywhere in in_out.py",
        not any(line.strip().startswith("global ") for line in code_lines))


def test_ex02(report):
    """Exercise callLimit: shared vs independent per-function counters."""
    mod = _fresh_import("ex02", "callLimit")
    callLimit = mod.callLimit

    calls = []

    @callLimit(2)
    def h():
        """Record a call and report success."""
        calls.append(1)
        return "ran"

    r1 = h()
    r2 = h()
    out = _capture(lambda: h())
    report.check("first call under limit runs the function", r1 == "ran")
    report.check("second call under limit runs the function", r2 == "ran")
    report.check("function body only actually executed twice",
                 len(calls) == 2)
    report.check("third call (over limit) prints an Error line",
                 "call too many times" in out)

    # independence between two differently-limited functions
    @callLimit(1)
    def i():
        """A function with its own, separate call-limit counter."""
        return "i-ran"

    @callLimit(1)
    def j():
        """Another function, must not share i()'s counter."""
        return "j-ran"

    report.check("i() unaffected by j()'s own counter",
                 i() == "i-ran" and j() == "j-ran")


def test_ex03(report):
    """Exercise the Student dataclass: login, id, and locked fields."""
    mod = _fresh_import("ex03", "new_student")
    Student = mod.Student

    s = Student(name="john", surname="SMITH")
    report.check("login capitalises first letter, lowercases surname",
                 s.login == "Jsmith")
    report.check("active defaults to True", s.active is True)
    report.check("id is a 15-char lowercase string",
                 len(s.id) == 15 and s.id.isalpha() and s.id.islower())

    s2 = Student(name="john", surname="SMITH")
    report.check("two students get different random ids", s.id != s2.id)

    def make_with_login():
        """Try (and fail) to set login directly via the constructor."""
        return Student(name="a", surname="b", login="x")

    def make_with_id():
        """Try (and fail) to set id directly via the constructor."""
        return Student(name="a", surname="b", id="x")

    report.check("passing login= is rejected",
                 _raises_typeerror(make_with_login))
    report.check("passing id= is rejected",
                 _raises_typeerror(make_with_id))

    import dataclasses
    report.check("Student is a real dataclass",
                 dataclasses.is_dataclass(Student))

    src = open(_ex03_path()).read()
    report.check("class does not define __str__", "def __str__" not in src)
    report.check("class does not define __repr__", "def __repr__" not in src)


def main():
    """Run all edge-case checks for the Day 4 exercises."""
    report = Report()
    test_ex00(report)
    test_ex01(report)
    test_ex02(report)
    test_ex03(report)
    print()
    if report.failures:
        print(f"{report.failures} check(s) FAILED")
        sys.exit(1)
    print("All edge-case checks passed.")


if __name__ == "__main__":
    main()
