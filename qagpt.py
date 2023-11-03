from PIL import Image
import matplotlib.pyplot as plt

# Open the image file
img = Image.open('your file.jpg')
plt.imshow(img)
plt.axis('off')  # Hide axes
plt.show()