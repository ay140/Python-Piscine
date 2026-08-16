from S1E9 import Character, Stark


def main():
    """Run every check for exercise 00 (abstract Character + Stark)."""
    # Stark is a *concrete* class (it implements the abstract "die"
    # method), so we can create real instances of it.
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    print("---")

    # Character is *abstract* (it inherits from ABC and has an
    # @abstractmethod). Python refuses to build an object straight
    # from it - trying to do so raises a TypeError.
    # The norm says "no uncaught exception is allowed", even for the
    # errors we are asked to test, so this has to live inside a
    # try/except instead of crashing the program.
    try:
        Character("hodor")
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
