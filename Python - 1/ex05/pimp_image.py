import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    try:
        inverted = 255 - array

        plt.imshow(inverted)
        plt.title("Invert")
        plt.show()
        return inverted
    except Exception as e:
        print(f"Error in ft_invert: {e}")
        return None


def ft_red(array):
    """
    Keeps only the red color of the image received.
    """
    try:
        # Check if array is valid/has 3 channels before operations
        # to ensure operator restrictions don't mask fundamental issues?
        # But we must use only restricted operators.
        # "try-except" is a control structure, not an operator on the image.
        # It handles the *execution flow*.
        red_filtered = array * [1, 0, 0]

        plt.imshow(red_filtered)
        plt.title("Red")
        plt.show()
        return red_filtered
    except Exception as e:
        print(f"Error in ft_red: {e}")
        return None


def ft_green(array):
    """
    Keeps only the green color of the image received.
    """
    try:
        green_filtered = array.copy()

        green_filtered[:, :, 0] = (
            green_filtered[:, :, 0] - green_filtered[:, :, 0]
        )
        green_filtered[:, :, 2] = (
            green_filtered[:, :, 2] - green_filtered[:, :, 2]
        )

        plt.imshow(green_filtered)
        plt.title("Green")
        plt.show()
        return green_filtered
    except Exception as e:
        print(f"Error in ft_green: {e}")
        return None


def ft_blue(array):
    """
    Keeps only the blue color of the image received.
    """
    try:
        blue_filtered = array.copy()

        blue_filtered[:, :, 0] = 0
        blue_filtered[:, :, 1] = 0

        plt.imshow(blue_filtered)
        plt.title("Blue")
        plt.show()
        return blue_filtered
    except Exception as e:
        print(f"Error in ft_blue: {e}")
        return None


def ft_grey(array):
    """
    Converts the image to grayscale.
    """
    try:
        grey_val = array.sum(axis=2) / 3

        grey_filtered = np.zeros_like(array)

        grey_filtered[:, :, 0] = grey_val
        grey_filtered[:, :, 1] = grey_val
        grey_filtered[:, :, 2] = grey_val

        plt.imshow(grey_filtered)
        plt.title("Grey")
        plt.show()
        return grey_filtered
    except Exception as e:
        print(f"Error in ft_grey: {e}")
        return None
