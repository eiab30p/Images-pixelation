
"""
Using openCV I converted an image to look like the retro 8-bit image. It does have a slight issue on the edges where the
program did not read the pixels but I placed a thin border around the image to hide it a bit. If I had a  little
bit more time to play around I could have possibly went around the edges first and then do down to the center.

@author Eddy Verde
"""
""" Below are some resources I used that influenced this idea. """
# https://www.polygon.com/2015/5/13/8595963/a-pixel-artist-renounces-pixel-art
# https://en.wikipedia.org/wiki/Dither

import cv2

"""
The  find_common_value method takes the range of pixels we want to convert to be the same color. 
I did this by collecting the pixels and the color of those pixels in this range. Once I have those I find the 
color sequence that appears the most and make all pixels in that section that color. 

Other possibility would to reloop the pixels already visited and make it the max color 

I put it in the try catch because the loop would go out of bounds at the bottom and the edges. I could do another
formula to see when that error happens go back to the limit and not go beyond that point. I could handle with some 
validation before handling the loop. 
"""


def find_common_value(img, x, y, pixel_size):
    # Initializing my list and dictionary to collect the colors in the area I'm looking at and pixels seen
    pixel_map = []
    color = {}
    try:
        # This is where the Fun is. We are looping within a calculated space to find the common colors.
        for newY in range(y, y+pixel_size):
            for newX in range(x, x+pixel_size):
                # We are now adding the tuple of the pixels into the pixel map.
                pixel_map.append((newX, newY))
                # We are now getting the RGB tuple as our key
                rbg = (img[newX][newY][0], img[newX][newY][1], img[newX][newY][2])
                # we are taking the RGB tuple to see if it is a key well add one it our value if not create the key
                if rbg in color:
                    color[rbg] += 1
                else:
                    color[rbg] = 1
        # Python is amazing by having a max function and that is what happens below by inputting the item
        # ## we want to look up and the key you want to get
        max_color = max(color, key=color.get)

        # Once we got our max we are going to make the max color for all those pixels.
        for i in pixel_map:
            img[i[0]][i[1]][0] = max_color[0]
            img[i[0]][i[1]][1] = max_color[1]
            img[i[0]][i[1]][2] = max_color[2]
    except:
        pass

""""
The border_image method is simple. It just gets the row and col as well as the image and adds a border based on 
the thickness times the row/col. Then we pass that info into openCVs method of copyMakeBorder which we make a
black border. 
"""


def border_image(img, row, col):
    value = 0, 0, 0
    row = int(0.01*row)
    col = int(0.01*col)
    return cv2.copyMakeBorder(img, row, row, col, col, cv2.BORDER_CONSTANT, value=value)

"""
The below method makes a copy of the image and create a new photo. Once that is completed
I get the dimensions of the images row,cols as x_lim and y_lim. I also get a pixel_size 
so I know what range of pixels to skip over as well as which ones to process to make it bit like.
Once the image is completed I add a black border using openCV function "copMakeBorder". Finally 
I display both images.
"""


def pixelated(image_file):

    img = cv2.imread(image_file)
    cv2.imwrite("pixelated_image.jpg", img)
    newImg = cv2.imread("pixelated_image.jpg")
    pixel = newImg

    # Getting the Shape width and weight but something I have no use for. I could do [:2] to eliminate that variable.
    x_lim, y_lim, something = img.shape

    # the double / is to get the floor value of this division so I do not have a decimal value
    pixel_size = x_lim//62

    # Here we are looping through the images and skipping the size where we are going to process of the 8bit
    for y in range(1, y_lim,pixel_size):  # Top to Bottom
        for x in range(1, x_lim, pixel_size):  # Left To Right
            # This is the real fun part, we are going to process a portion of the images by sending
            # ## image, row, col, and the square size
            find_common_value(pixel, x, y, pixel_size)

    # We are adding a border by sending the image, row, and col
    # ## This will return the image
    pixel = border_image(pixel, x_lim, y_lim)

    # We then save the image and shoe the pixelated image and the normal image
    cv2.imwrite("pixelated_image.jpg", pixel)


"""
This is your main so we call many other parameters to send over to be processed. 
"""
if __name__ == "__main__":
    img = "Me.jpg"
    pixelated(img)
    img = cv2.imread(img)
    cv2.imshow("Me.jpg", img)
    pixel = "pixelated_image.jpg"
    pixel = cv2.imread(pixel)
    cv2.imshow("pixelated_image.jpg", pixel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

