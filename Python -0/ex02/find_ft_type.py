def all_thing_is_obj(object: any) -> int: # any is a type that can be any type and -> int is the return type of the function
    """
    This function prints the type of the given object
    with a specific message depending on the type.
    Always returns 42.
    """
    if isinstance(object, list): # isinstance is a built-in function that checks if the object is an instance of the given type
        print("List :", type(object))
    elif isinstance(object, tuple):
        print("Tuple :", type(object))
    elif isinstance(object, set):
        print("Set :", type(object))
    elif isinstance(object, dict):
        print("Dict :", type(object))
    elif isinstance(object, str) and object == "Brian":
        print("Brian is in the kitchen :", type(object))
    elif isinstance(object, str) and object == "Toto":
        print("Toto is in the kitchen :", type(object))
    else:
        print("Type not found")
    return 42