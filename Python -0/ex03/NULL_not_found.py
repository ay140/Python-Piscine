def NULL_not_found(object: any) -> int:
    """
    Identifies if an object is a known null-like value.
    Prints its label and type, returns 0 if found, 1 if not.
    """
    if object is None:
        print("Nothing:", object, type(object))
        return 0
    elif isinstance(object, float) and str(object).lower() == 'nan':
        print("Cheese:", object, type(object))
        return 0
    elif isinstance(object, int) and object == 0:
        print("Zero:", object, type(object))
        return 0
    elif isinstance(object, str) and object == '':
        print("Empty:", type(object))
        return 0
    elif object is False:
        print("Fake:", object, type(object))
        return 0
    else:
        print("Type not Found")
        return 1