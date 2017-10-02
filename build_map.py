# Import some packages from matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# Import the "numpy" package for working with arrays
import numpy as np 
# Uncomment the next line for use in a Jupyter notebook
#%matplotlib inline

# Define the filename, read and plot the image
image = mpimg.imread('IMG/robocam_2017_07_08_20_28_09_991.jpg')
# Define a function to perform a color threshold
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    ####### TODO 
    # Create an empty array the same size in x and y as the image 
    binary_image = np.zeros_like(img[:, :, 0])
    # Apply the thresholds for RGB and 
    red_above = img[:,:,0] > rgb_thresh[0]
    green_above = img[:,:,1] > rgb_thresh[0]
    blue_above = img[:,:,2] > rgb_thresh[0]
    above_threshold = red_above & green_above & blue_above
        # assign 1's where threshold was exceeded
    binary_image[above_threshold] = 1
    return binary_image

# Define color selection criteria
###### TODO: MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
red_threshold = 160
green_threshold = 160
blue_threshold = 160
######
rgb_threshold = (red_threshold, green_threshold, blue_threshold)

# pixels below the thresholds
colorsel = color_thresh(image, rgb_thresh=rgb_threshold)

# Display the original image and binary               
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 7), sharey=True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)

ax2.imshow(colorsel, cmap='gray')
ax2.set_title('Your Result', fontsize=40)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show() # Uncomment if running on your local machine

