"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

from image import Image
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    
    x_pixels, y_pixels, num_channels = image.array.shape

    # We are going to make an empty array so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)

    # This is the most intuitive way (non-vectorized)
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x, y, c] = image.array[x, y, c] * factor
    
    # Vectorized version
    new_im.array = image.array * factor

    return new_im

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, num_channels = image.array.shape

    # We are going to make an empty array so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid
    
    return new_im

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number

    x_pixels, y_pixels, num_channels = image.array.shape

    # We are going to make an empty array so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)

    neighbor_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # My own implementation
                # new_im.array[x, y, c] = image.array[max(0,x - kernel_size//2):min(x_pixels,x + kernel_size//2),max(0,y - kernel_size//2):min(y_pixels,y + kernel_size//2),c].mean()
                
                # Tutorial implementation
                total = 0
                for x_i in range(max(0, x - neighbor_range), min(x + neighbor_range + 1, x_pixels)):
                    for y_i in range(max(0, y - neighbor_range), min(y + neighbor_range + 1, y_pixels)):
                        total += image.array[x_i, y_i, c]
                new_im.array[x, y, c] =  total / (kernel_size**2)

    return new_im

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape

    # We are going to make an empty array so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)

    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0, x - neighbor_range), min(x + neighbor_range + 1, x_pixels)):
                    for y_i in range(max(0, y - neighbor_range), min(y + neighbor_range + 1, y_pixels)):
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]

                        total += image.array[x_i, y_i, c] * kernel_val
                new_im.array[x, y, c] = total
    return new_im

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    x_pixels, y_pixels, num_channels = image1.array.shape

    # We are going to make an empty array so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = np.square(image1.array[ x, y, c]**2 + image2.array[ x, y, c]**2)
    
    return new_im

if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # #let's lighten the lake
    # brightened_im = brighten(lake, 3)
    # brightened_im.write_image('new_lake.png')

    # # Darken
    # darkened_im = brighten(lake, 0.3)
    # darkened_im.write_image('darker_lake.png')

    # Adjust contrast
    # increased_contrast = adjust_contrast(lake, 2, 0.5)
    # increased_contrast.write_image('increased_contrast.png')

    # decreased_contrast = adjust_contrast(lake, 0.5, 0.5)
    # decreased_contrast.write_image('decreased_contrast.png')

    # Blur
    # blurred_lake = blur(lake,7)
    # blurred_lake.write_image('blurred_lake.png')

    # blurred_city = blur(city,7)
    # blurred_city.write_image('blurred_city.png')

    # Applying Sobel Edge detection kernel
    sobel_x_kernel = np.array([
        [ 1,  2,  1],
        [ 0,  0,  0],
        [-1, -2, -1]
    ])
    sobel_y_kernel = np.array([
        [ 1,  0, -1],
        [ 2,  0, -2],
        [ 1,  0, -1]
    ])
    sobel_x = apply_kernel(city, sobel_x_kernel)
    sobel_x.write_image('sobel_x_city.png')

    sobel_y = apply_kernel(city, sobel_y_kernel)
    sobel_y.write_image('sobel_y_city.png')

    edges = combine_images(sobel_x, sobel_y)
    edges.write_image('edges_city.png')

