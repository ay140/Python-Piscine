def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate BMI values from lists of heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of BMI values.
    """
    if len(height) != len(weight):
        print("Error: Lists must be the same size.")
        return []

    bmi_values = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            print("Error: List elements must be int or float.")
            return []
        if h <= 0:
            print("Error: Height must be positive.")
            return []
        bmi_values.append(w / (h ** 2))
    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values are above a certain limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): BMI limit.

    Returns:
        list[bool]: List of booleans indicating if BMI is above the limit.
    """
    return [b > limit for b in bmi]
