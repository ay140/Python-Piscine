from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def transpose_image(arr):
    """
    transpose method without library.
    """
    if len(arr.shape) == 3:
        rows, cols, channels = arr.shape
        transposed = np.zeros((cols, rows, channels), dtype=arr.dtype)
        for i in range(rows):
            for j in range(cols):
                transposed[j, i] = arr[i, j]
    else:
        rows, cols = arr.shape
        transposed = np.zeros((cols, rows), dtype=arr.dtype)
        for i in range(rows):
            for j in range(cols):
                transposed[j, i] = arr[i, j]
    return transposed


def main():
    """
    Load an image, slice it, manually transpose it, and display it.
    """
    try:
        arr = ft_load("animal.jpeg")
        if arr is None:
            print("Error: Image not loaded")
            return

        # Slice to 400x400 (Zoom step)
        sliced_arr = arr[100:500, 450:850, :1]

        # Display shape as per requirements
        print(f"The shape of image is: {sliced_arr.shape}")
        print(sliced_arr)

        transposed_arr = transpose_image(sliced_arr)

        # If the result is (400, 400, 1), remove last dim for (400, 400)
        # to match example output
        if transposed_arr.shape[2] == 1:
            transposed_arr = transposed_arr.reshape(
                transposed_arr.shape[0], transposed_arr.shape[1]
            )

        print(f"New shape after Transpose: {transposed_arr.shape}")
        print(transposed_arr)

        plt.imshow(transposed_arr, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
