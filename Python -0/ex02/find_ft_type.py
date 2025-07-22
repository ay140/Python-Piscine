def all_thing_is_obj(object: any) -> int:
    """
    Detects the type of the object and prints a custom message depending on it.
    If the object is a string, it prints: "<value> is in the kitchen"
    Returns 42 always.
    """

    if isinstance(object, list):
        print("List :", type(object))  # e.g., ['a', 'b']
    elif isinstance(object, tuple):
        print("Tuple :", type(object))  # e.g., ('a', 'b')
    elif isinstance(object, set):
        print("Set :", type(object))  # e.g., {'a', 'b'}
    elif isinstance(object, dict):
        print("Dict :", type(object))  # e.g., {'a': 1}
    elif isinstance(object, str):
        print(f"{object} is in the kitchen :", type(object))  # for any string
    else:
        print("Type not found")
    
    return 42
