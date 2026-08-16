from new_student import Student


def main():
    """Run both scenarios from the subject: a valid student, then an
    attempt to set the auto-generated 'id' field by hand."""
    student = Student(name="Edward", surname="agle")
    print(student)
    print("---")
    # The norm forbids any uncaught exception, even the ones we are
    # deliberately triggering to prove a point - so this has to be
    # wrapped in a try/except instead of being left to crash.
    try:
        bad_student = Student(name="Edward", surname="agle", id="toto")
        print(bad_student)
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
