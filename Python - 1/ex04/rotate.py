from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def transpose_image(arr):
    """
    transpose method without library.
    """
    rows = arr.shape[0]
    cols = arr.shape[1]
    channels = arr.shape[2] if len(arr.shape) == 3 else 1

    # Create empty array with swapped dimensions
    try:
        if len(arr.shape) == 3:
            transposed = np.zeros((cols, rows, channels), dtype=arr.dtype)
            # Nested loops to swap rows (i) and columns (j) manually
            for i in range(rows):
                for j in range(cols):
                    for k in range(channels):
                        # Move pixel at (i, j) to (j, i)
                        transposed[j][i][k] = arr[i][j][k]
        else:
            transposed = np.zeros((cols, rows), dtype=arr.dtype)
            for i in range(rows):
                for j in range(cols):
                    transposed[j][i] = arr[i][j]

        return transposed
    except Exception:
        return np.array([])


def main():
    """
    Load an image, slice it, manually transpose it, and display it.
    """
    try:
        # Load the image
        arr = ft_load("animal.jpeg")
        if arr is None:
            print("Error: Image not loaded")
            return

        # Slice to a 400x400 square (Zoom step from ex03)
        # [rows: 100 to 500, cols: 450 to 850, channels: 0 (Red)]
        sliced_arr = arr[100:500, 450:850, :1]

        # Display shape as per requirements
        print(f"The shape of image is: {sliced_arr.shape}")
        print(sliced_arr)

        # Manually transpose the image (flip rows/cols) without using libraries
        transposed_arr = transpose_image(sliced_arr)

        # If result is (400, 400, 1), remove last dim for (400, 400)
        # to match expected output format "Option B"
        if transposed_arr.shape[2] == 1:
            transposed_arr = transposed_arr.reshape(
                transposed_arr.shape[0], transposed_arr.shape[1]
            )

        print(f"New shape after Transpose: {transposed_arr.shape}")
        print(transposed_arr)

        # Display using grayscale colormap (0=black, 255=white)
        plt.imshow(transposed_arr, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
