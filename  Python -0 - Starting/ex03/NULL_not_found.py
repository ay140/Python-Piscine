def NULL_not_found(object: any) -> int:
    """
    Identifies known null-like values and prints label + type.
    Returns 0 if identified, otherwise 1.
    """
    if object is None:
        print("Nothing:", object, type(object))
        return 0
    elif isinstance(object, float) and str(object).lower() == 'nan':
        print("Cheese:", object, type(object))
        return 0
    elif object is False:
        print("Fake:", object, type(object))  # Moved this above Zero
        return 0
    elif isinstance(object, int) and object == 0:
        print("Zero:", object, type(object))
        return 0
    elif isinstance(object, str) and object == '':
        print("Empty:", type(object))
        return 0
    else:
        print("Type not Found")
        return 1
