from give_bmi import give_bmi, apply_limit


def main():
    print("--- Test 1: Negative Weight ---")
    height = [2.71, 1.15]
    weight = [165.3, -38.4]  # Negative weight
    result = give_bmi(height, weight)
    print(f"Result: {result}")

    print("\n--- Test 2: Invalid Input for apply_limit ---")
    # Passing a string instead of a list of numbers
    try:
        result_limit = apply_limit("not a list", 26)
        print(f"Result with string input: {result_limit}")
    except Exception as e:
        print(f"CRITICAL FAIL: Exception leaked: {e}")

    print("\n--- Test 3: Mixed types in list for apply_limit ---")
    try:
        # List containing a string which cannot be compared to int
        result_mixed = apply_limit([22.5, "oops"], 26)
        print(f"Result with mixed list: {result_mixed}")
    except Exception as e:
        print(f"CRITICAL FAIL: Exception leaked: {e}")

    print("subject main: ")
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
