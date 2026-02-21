from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its format and pixels content in RGB format.

    Args:
        path (str): Path to the image file.

    Returns:
        np.array: Numpy array of the image pixels.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("File not found")

        with Image.open(path) as img:
            if img.format not in ("JPEG", "JPG"):
                print("Error: Image format must be JPEG or JPG.")
                return np.array([])
            # print(f"The format of image is: {img.format}")

            # Convert to RGB
            img = img.convert("RGB")

            # Convert to numpy array
            arr = np.array(img)

            # print(f"The shape of image is: {arr.shape}")
            # print(arr)
            return arr

    except Exception as e:
        print(f"Error: {e}")
        return np.array([])
