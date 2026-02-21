import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """
    Inverts the color of the image received.
    Allowed operators: =, +, -, *
    """
    try:
        # 255 - array uses '-' operator.
        inverted = 255 - array

        plt.imshow(inverted)
        plt.show()
        return inverted
    except Exception as e:
        print(f"Error in ft_invert: {e}")
        return None


def ft_red(array):
    """
    Keeps only the red color of the image received.
    Allowed operators: =, *
    """
    try:
        # Multiplies by [1, 0, 0] to keep Red (1) and zero out G/B (0).
        # Uses '*' operator.
        red_filtered = array * [1, 0, 0]

        plt.imshow(red_filtered)
        plt.show()
        return red_filtered
    except Exception as e:
        print(f"Error in ft_red: {e}")
        return None


def ft_green(array):
    """
    Keeps only the green color of the image received.
    Allowed operators: =, -
    """
    try:
        green_filtered = array.copy()

        # Subtracts channel from itself to get 0. Uses '-' operator.
        green_filtered[:, :, 0] = (
            green_filtered[:, :, 0] - green_filtered[:, :, 0]
        )
        green_filtered[:, :, 2] = (
            green_filtered[:, :, 2] - green_filtered[:, :, 2]
        )

        plt.imshow(green_filtered)
        plt.show()
        return green_filtered
    except Exception as e:
        print(f"Error in ft_green: {e}")
        return None


def ft_blue(array):
    """
    Keeps only the blue color of the image received.
    Allowed operators: =
    """
    try:
        blue_filtered = array.copy()

        # Direct assignment to 0. Uses '=' operator.
        blue_filtered[:, :, 0] = 0
        blue_filtered[:, :, 1] = 0

        plt.imshow(blue_filtered)
        plt.show()
        return blue_filtered
    except Exception as e:
        print(f"Error in ft_blue: {e}")
        return None


def ft_grey(array):
    """
    Converts the image to grayscale.
    Allowed operators: =, /
    """
    try:
        # Sums the channels (method) and divides by 3 ('/').
        # (R + G + B) / 3
        grey_val = array.sum(axis=2) / 3

        grey_filtered = np.zeros_like(array)

        # Broadcast the grey value to all 3 channels
        grey_filtered[:, :, 0] = grey_val
        grey_filtered[:, :, 1] = grey_val
        grey_filtered[:, :, 2] = grey_val

        plt.imshow(grey_filtered)
        plt.show()
        return grey_filtered
    except Exception as e:
        print(f"Error in ft_grey: {e}")
        return None
