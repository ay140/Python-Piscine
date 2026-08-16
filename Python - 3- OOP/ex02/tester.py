from DiamondTrap import King


def main():
    """Testing the King class properties."""
    # King("Joffrey") runs through the whole diamond MRO chain
    # (Baratheon -> Lannister -> Character) - see the comment at the
    # top of DiamondTrap.py for why the dict below ends up looking
    # exactly like a Baratheon.
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
