
# sudo apt-get install python-matplotlib
# sudo pip install numpy
# sudo apt-get install python-numpy python-scipy 

import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage
from matplotlib import pylab as pl



# Pre define Matrix
csv_matrix = []
initial_matrix=[]

Image_Size_X = 300
Image_Size_Y = 300
Total_Image_Size = 90000 + 8


# File reading 
csv_file = open('Output.csv', 'r')
reader = csv.reader(csv_file)


for row in reader:
    csv_matrix.append(row)

for i in range(8,Total_Image_Size):
    initial_matrix.append(float(csv_matrix[i][3]))

def make_matrix(matrix):
    new_matrix = np.zeros((Image_Size_X, Image_Size_Y), np.float)
    
    for i in range(Image_Size_X):
        for j in range(Image_Size_X):
            new_matrix[j, i] = matrix[Image_Size_X*i + j]
    
    return new_matrix
get_matrix = make_matrix(initial_matrix)

# Normalized Dose
get_matrix_normed = get_matrix / np.max(get_matrix)

# Image Rotation
Rotated_Image = ndimage.rotate(get_matrix_normed  , -90)
plt.title('Proton Beam 150 MeV in WaterPhantom')
plt.imshow(Rotated_Image)
plt.colorbar()
plt.xlabel('X[mm]')
plt.ylabel('Y[mm]')
plt.show()

#-- Extract the line...
# Make a line with "num" points...
x0, y0 = 0, 150 # These are in _pixel_ coordinates!!
x1, y1 = 300, 150
num = 300
x, y = np.linspace(x0, x1, num), np.linspace(y0, y1, num)

# Extract the values along the line, using cubic interpolation
zi = ndimage.map_coordinates(np.transpose(Rotated_Image), np.vstack((x,y))) 

#Image Plot#
fig, axes = plt.subplots(nrows=2)
axes[0].imshow(Rotated_Image)
axes[0].plot([x0, x1], [y0, y1], 'ro-')
axes[0].axis('image')

axes[1].plot(zi)
plt.xlabel('Depth[mm]')
plt.ylabel('Relative Dose')
plt.grid()
plt.show()






