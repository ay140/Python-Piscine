import sys
from ft_filter import ft_filter


def main():
    """
    Main entry point. Filters words longer than a given number using ft_filter.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        text = sys.argv[1]
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = text.split()

        # Use lambda + list comprehension + ft_filter
        filtered = ft_filter(lambda w: len(w) > number, words)

        print(filtered)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
