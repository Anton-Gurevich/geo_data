import cv2
import numpy as np


def read_and_convert_image(input_file_path, output_file_path):
    # Read the .tif image
    image = cv2.imread(input_file_path, cv2.IMREAD_UNCHANGED)

    # Convert the image data to 'uint8' data type
    if image.dtype != np.uint8:
        # Normalize the data to 0 - 255
        normalized_image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        # Convert to 'uint8'
        image_uint8 = normalized_image.astype(np.uint8)
    else:
        image_uint8 = image

    # Save the image as .png or .jpeg
    cv2.imwrite(output_file_path, image_uint8)


# Example usage
input_file_path = r'..\data\demo_Ein-Quinia_image.tif'
output_file_path = r'..\data\demo_Ein-Quinia_image.png'  # Or change to .jpeg if preferred

read_and_convert_image(input_file_path, output_file_path)