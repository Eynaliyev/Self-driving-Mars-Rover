import numpy as np 

# Define a function to convert from cartesian to polar coordinates
def to_polar_coords(xpix, ypix):
	# Calculate distance to each pixel
	dist = np.sqrt(xpix**2 + ypix**2)
	# Caluclate angle using arctangent function
	angles = np.arctan2(ypix, xpix)
	return dist, angles

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
from extra_functions import perspect_transform, color_thresh, rover_coords

image = mpimg.imread('IMG/robocam_2017_07_08_20_28_09_991.jpg')
dst_size = 5 
bottom_offset = 6

source = np.float32([[14, 140], [301 ,140],[200, 96], [118, 96]])
destination = np.float32([[image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset], 
                  [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset],
                  ])

warped = perspect_transform(image, source, destination) # Perform perspective transform 
colorsel = color_thresh(warped, rgb_thresh=(160,160,160)) # threshold the warped image
xpix, ypix = rover_coords(colorsel) # convert to rover-centric coordinates
distances, angles = to_polar_coords(xpix, ypix) # Convert to polar coordinates
avg_angle = np.mean(angles) # Compite the average angle

# Do some plotting
fig = plt.figure(figsize=(12,9))
plt.subplot(221)
plt.imshow(image)
plt.subplot(222)
plt.imshow(warped)
plt.subplot(223)
plt.imshow(colorsel, cmap='gray')
plt.subplot(224)
plt.plot(xpix, ypix, '.')
plt.ylim(-160,160)
plt.xlim(0,160)
arrow_length = 100
x_arrow = arrow_length * np.cos(avg_angle)
y_arrow = arrow_length * np.sin(avg_angle)
plt.arrow(0,0, x_arrow, y_arrow, color='red', zorder=2, head_width=10, width=2)
plt.show()
avg_angle_degrees = avg_angle * 180/ np.pi 
steering = np.clip(avg_angle_degrees, -15, 15)
