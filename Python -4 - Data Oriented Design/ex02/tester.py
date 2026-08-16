from callLimit import callLimit


def main():
    """Run the subject's scenario: two functions, two independent
    call limits, called side by side in a loop."""

    @callLimit(3)
    def f():
        """Print f() - allowed up to 3 calls."""
        print("f()")

    @callLimit(1)
    def g():
        """Print g() - allowed up to 1 call."""
        print("g()")

    for _ in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
