from statistics import ft_statistics


def main():
    """Run every scenario from the subject, in order."""
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    # Unknown request names ("heheh"/"kdekem" are not real stats):
    # nothing gets printed for this call at all.
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    # No positional data at all -> every requested stat fails to
    # compute -> one "ERROR" line per requested (and recognised) stat.
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
