from PIL import Image
import numpy as np

# Create a simple valid image
img = Image.fromarray(np.zeros((257, 450, 3), dtype=np.uint8), 'RGB')
img.save("landscape.jpg")
print("landscape.jpg created")
