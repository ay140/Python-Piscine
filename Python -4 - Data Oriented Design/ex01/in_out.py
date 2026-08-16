def square(x: int | float) -> int | float:
    """Return x squared (x to the power of 2)."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x raised to the power of itself (x to the power of x)."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Build and return a callable "counter" object.

    Every time you call the object this returns, it re-applies
    `function` to its own PREVIOUS result (starting from `x` on the
    very first call) and returns the new value. So:
        c = outer(3, square)
        c()  -> square(3)        -> 9
        c()  -> square(9)        -> 81
        c()  -> square(81)       -> 6561
    """
    # "value" belongs to outer()'s local scope. inner() is a closure:
    # it keeps a reference to that scope even after outer() has
    # returned, which is how it "remembers" the last result between
    # separate calls - all without ever touching a global variable
    # (forbidden by the subject).
    value = x

    def inner() -> float:
        """Apply the stored function to the last value and return it."""
        # "nonlocal" (not "global"!) tells Python that assigning to
        # "value" here should update outer()'s "value", instead of
        # creating a brand new local variable inside inner().
        nonlocal value
        value = function(value)
        return value

    return inner
