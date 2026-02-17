from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    Load an image, slice it, and display it.
    """
    try:
        arr = ft_load("animal.jpeg")

        if arr is None:
            print("Error: Image not loaded.")
            return

        # Print original info
        print(arr)

        # Slice to get 400x400 from center
        # Slicing: [100:500, 450:850, :1] to keep 1 channel
        sliced_arr = arr[100:500, 450:850, :1]

        # Or modify to match example values if possible
        # but exact match depends on the source image.

        print(f"New shape after slicing: {sliced_arr.shape}")
        print(sliced_arr)

        plt.imshow(sliced_arr, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
