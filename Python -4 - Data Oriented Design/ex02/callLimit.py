from typing import Any


def callLimit(limit: int):
    """Build a decorator that allows a function to be called at most
    `limit` times, then silently blocks it (with an error message)
    instead of running it.

    This is a "decorator factory": callLimit(3) itself returns the
    actual decorator (callLimiter), which is what gets applied to the
    function with the @ syntax. That extra layer is what lets you
    write @callLimit(3) - a normal decorator wouldn't accept an
    argument like that.
    """
    # "count" lives here, in callLimit()'s scope - each call to
    # callLimit(...) creates a fresh one. That's why @callLimit(3) on
    # f() and @callLimit(1) on g() end up with two totally
    # independent counters instead of sharing one (no global needed).
    count = 0

    def callLimiter(function):
        """Wrap `function` so every call goes through the counter."""

        def limit_function(*args: Any, **kwds: Any):
            """Run `function`, but only while under the call limit."""
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return None
            return function(*args, **kwds)

        return limit_function

    return callLimiter
