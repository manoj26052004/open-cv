import cv2
import numpy as np

# Load the input image and the template image of the watch
image = cv2.imread(r"C:\Users\sanja\OneDrive\Desktop\easy program\WhatsApp Image 2024-03-27 at 08.40.21_29ac4062.jpg")
template = cv2.imread(r"C:\Users\sanja\OneDrive\Desktop\easy program\WhatsApp Image 2024-03-27 at 09.45.16_beffc0b1.jpg", cv2.IMREAD_GRAYSCALE)


# Ensure both images have the correct data type and dimensions
if image.ndim != 2:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if template.ndim != 2:
    print("Error: Template must be a grayscale image.")
    exit()

# Perform template matching
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Set a threshold for template matching results
threshold = 0.8
locations = np.where(result >= threshold)

# Draw bounding boxes around detected watches
for loc in zip(*locations[::-1]):
    cv2.rectangle(image, loc, (loc[0] + template.shape[1], loc[1] + template.shape[0]), (0, 255, 0), 2)

# Display the output image with detected watches
cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
