import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a truncated version.

    Args:
        family (list): 2D array (list of lists).
        start (int): Start index for slicing.
        end (int): End index for slicing.

    Returns:
        list: Truncated 2D array.
    """
    if not isinstance(family, list):
        print("Error: Input must be a list.")
        return []

    try:
        # Convert to numpy array to easily check shape and slice
        arr = np.array(family)

        # Check if it's actually 2D (or at least checking shape validity)
        if arr.dtype == object:
            # Rough check for ragged array if elements are lists
            print("Error: Rows must be of the same size.")
            return []

        # Verify it is 2D
        if arr.ndim != 2:
            print("Error: Input must be a 2D array.")
            return []

        print(f"My shape is : {arr.shape}")

        new_arr = arr[start:end]

        print(f"My new shape is : {new_arr.shape}")

        return new_arr.tolist()
    except Exception as e:
        print(f"Error: {e}")
        return []
