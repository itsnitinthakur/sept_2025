import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 grayscale image
image = np.zeros((100, 100), dtype=np.uint8)
image[40:60, 40:60] = 255  # White square
plt.imshow(image, cmap='gray')
plt.savefig('day1_output.png')
plt.show()