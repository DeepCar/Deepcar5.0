import math
import cv2
import os
import cv2 as cv
import numpy as np


def gaussianSmoothing(image):
    imageArray = np.array(image)
    gaussianArr = np.array(image)
    sum = 0

    for i in range(3, image.shape[0] - 3):
        for j in range(3, image.shape[1] - 3):
            sum = applyGaussianFilterAtPoint(imageArray, i, j)
            gaussianArr[i][j] = sum

    return gaussianArr


def applyGaussianFilterAtPoint(imageData, row, column):
    sum = 0
    for i in range(row - 3, row + 4):
        for j in range(column - 3, column + 4):
            sum += gaussian_filter[i - row + 3][j - column + 3] * imageData[i][j]

    return sum

def getGradientX(imgArr, height, width):
    imageData = np.empty(shape=(height, width))
    for i in range(3, height - 5):
        for j in range(3, imgArr[i].size - 5):
            if liesInUnderRegion(imgArr, i, j):
                imageData[i + 1][j + 1] = None
            else:
                imageData[i + 1][j + 1] = prewittAtX(imgArr, i, j)

    return abs(imageData)


def getGradientY(imgArr, height, width):
    imageData = np.empty(shape=(height, width))
    for i in range(3, height - 5):
        for j in range(3, imgArr[i].size - 5):
            if liesInUnderRegion(imgArr, i, j):
                imageData[i + 1][j + 1] = None
            else:
                imageData[i + 1][j + 1] = prewittAtY(imgArr, i, j)

    return abs(imageData)


def getMagnitude(Gx, Gy, height, width):
    gradientData = np.empty(shape=(height, width))
    for row in range(height):
        for column in range(width):
            gradientData[row][column] = ((Gx[row][column] ** 2 + Gy[row][column] ** 2) ** 0.5) / 1.4142
    return gradientData


def getAngle(Gx, Gy, height, width):
    gradientData = np.empty(shape=(height, width))
    angle = 0
    for i in range(height):
        for j in range(width):
            if Gx[i][j] == 0:
                if Gy[i][j] > 0:
                    angle = 90
                else:
                    angle = -90
            else:
                angle = math.degrees(math.atan(Gy[i][j] / Gx[i][j]))
            if angle < 0:
                angle += 360
            gradientData[i][j] = angle
    return gradientData


def localMaximization(gradientData, gradientAngle, height, width):
    gradient = np.empty(shape=(height, width))
    numberOfPixels = np.zeros(shape=(256))
    edgePixels = 0

    for row in range(5, height - 5):
        for col in range(5, image[row].size - 5):
            theta = gradientAngle[row, col]
            gradientAtPixel = gradientData[row, col]
            value = 0

            # Sector - 1
            if (0 <= theta <= 22.5 or 157.5 < theta <= 202.5 or 337.5 < theta <= 360):
                if gradientAtPixel > gradientData[row, col + 1] and gradientAtPixel > gradientData[row, col - 1]:
                    value = gradientAtPixel
                else:
                    value = 0

            # Sector - 2
            elif (22.5 < theta <= 67.5 or 202.5 < theta <= 247.5):
                if gradientAtPixel > gradientData[row + 1, col - 1] and gradientAtPixel > gradientData[
                    row - 1, col + 1]:
                    value = gradientAtPixel
                else:
                    value = 0

            # Sector - 3
            elif (67.5 < theta <= 112.5 or 247.5 < theta <= 292.5):
                if gradientAtPixel > gradientData[row + 1, col] and gradientAtPixel > gradientData[row - 1, col]:
                    value = gradientAtPixel
                else:
                    value = 0

            # Sector - 4
            elif 112.5 < theta <= 157.5 or 292.5 < theta <= 337.5:
                if gradientAtPixel > gradientData[row + 1, col + 1] \
                        and gradientAtPixel > gradientData[row - 1, col - 1]:
                    value = gradientAtPixel
                else:
                    value = 0

            gradient[row, col] = value

            # If value is greater than one after non maxima suppression
            if value > 0:
                edgePixels += 1
                try:
                    numberOfPixels[int(value)] += 1
                except:
                    print('Out of range gray level value', value)

    print('Number of Edge pixels:', edgePixels)
    return [gradient, numberOfPixels, edgePixels]


def pTile(percent, imageData, numberOfPixels, edgePixels, file):
    # Number of pixels to keep
    threshold = np.around(edgePixels * percent / 100)
    sum, value = 0, 255
    for value in range(255, 0, -1):
        sum += numberOfPixels[value]
        if sum >= threshold:
            break

    for i in range(imageData.shape[0]):
        for j in range(imageData[i].size):
            if imageData[i, j] < value:
                imageData[i, j] = 0
            else:
                imageData[i, j] = 255

    print('For', percent, '- result:')
    print('Total pixels after thresholding:', sum)
    print('Threshold gray level value:', value)
    #     plt.imshow(imageData, cmap='gray')
    cv2.imwrite('Outputs/' + str(percent) + "_percent.jpg", imageData)

def liesInUnderRegion(imgArr, i, j):
    return imgArr[i][j] == None or imgArr[i][j + 1] == None or imgArr[i][j - 1] == None or imgArr[i + 1][j] == None or \
           imgArr[i + 1][j + 1] == None or imgArr[i + 1][j - 1] == None or imgArr[i - 1][j] == None or \
           imgArr[i - 1][j + 1] == None or imgArr[i - 1][j - 1] == None

def prewittAtX(imageData, row, column):
    sum = 0
    horizontal = 0
    for i in range(0, 3):
        for j in range(0, 3):
            horizontal += imageData[row + i, column + j] * prewittX[i, j]
    return horizontal

def prewittAtY(imageData, row, column):
    sum = 0
    vertical = 0
    for i in range(0, 3):
        for j in range(0, 3):
            vertical += imageData[row + i, column + j] * prewittY[i, j]
    return vertical

if __name__ == "__main__":

    gaussian_filter = (1.0 / 140.0) * np.array([[1, 1, 2, 2, 2, 1, 1],
                                                [1, 2, 2, 4, 2, 2, 1],
                                                [2, 2, 4, 8, 4, 2, 2],
                                                [2, 4, 8, 16, 8, 4, 2],
                                                [2, 2, 4, 8, 4, 2, 2],
                                                [1, 2, 2, 4, 2, 2, 1],
                                                [1, 1, 2, 2, 2, 1, 1]])

    prewittX = (1.0 / 3.0) * np.array([[-1, 0, 1],
                                       [-1, 0, 1],
                                       [-1, 0, 1]])

    prewittY = (1.0 / 3.0) * np.array([[1, 1, 1],
                                       [0, 0, 0],
                                       [-1, -1, -1]])


    path = 'C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Output/Gradient'
    image_dir = "C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Images/a"
    output_dir= "C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Output/Gradient"
    output_dir2 = "C:/Users/Amiran/Desktop/Second-ISI/headlights/Feature Extraction/main-headlight/Output/Contour"
    #for name in glob.glob("Images/*.jpg"):
    for _, _, image_names in os.walk(image_dir):
        for image_name in image_names:
            if '.jpg' in image_name:

                filepath = os.path.join(image_dir, image_name)
                dstpath = os.path.join(output_dir, image_name)
                dstpath2 = os.path.join(output_dir2, image_name)
                image = cv2.imread(filepath, 0)
        #image = cv2.imread(name, 0)
         #image = cv2.imread('Images/75.jpg', 0)
                height = image.shape[0]
                width = image.shape[1]

    # Normalized Gaussian Smoothing
                gaussianData = gaussianSmoothing(image)
    # Normalized Horizontal Gradient
                Gx = getGradientX(gaussianData, height, width)
    # Normalized Vertical Gradient
                Gy = getGradientY(gaussianData, height, width)
    # Normalized Edge Magnitude
                gradient = getMagnitude(Gx, Gy, height, width)
    # Edge angle
                gradientAngle = getAngle(Gx, Gy, height, width)
                print(gradientAngle.shape)
    #cv2.imwrite('Outputs/im_output.jpg', gradient)

    # Enhancement Brightness (image brightness enhancer)
    # read the image
    #image = cv2.imread('Outputs/im_output.jpg')

                alpha = 3  # Contrast control (1.0-3.0)
                beta = 100  # Brightness control (0-100)

                adjusted = cv2.convertScaleAbs(gradient, alpha=alpha, beta=beta)
         #cv2.imshow('original', gradient)
         #cv2.imshow('adjusted', adjusted)
         #cv2.waitKey()
         #im = cv2.imread('Outputs/im_output.jpg')
         #im = Image.open("Outputs/im_output.jpg")
         # image brightness enhancer
         #enhancer = ImageEnhance.Brightness(im)
         #factor = 5  # gives original image
         #im_output = enhancer.enhance(factor)
         #im_output.save('Outputs/original-image.png')
        #cv2.imwrite('Output/Gradient/im_output.jpg', adjusted)
                cv2.imwrite(dstpath, adjusted)


                img = cv.imread(dstpath)
                # cv.imshow("Solo Travel", img)
                blank = np.zeros(img.shape, dtype='uint8')
                # cv.imshow("Blank", blank)

                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                # cv.imshow("Gray", gray)

                blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
                # cv.imshow("Blur",blur)

                canny = cv.Canny(blur, 125, 175)
                #cv.imshow("Canny", canny)

                contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
                print(f"Number of contours => {len(contours)}")

                cv.drawContours(blank, contours, -1, (255, 255, 255), 9)
                #cv.imshow("Contour Drawn", blank)

                ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
                # cv.imshow("thresh", thresh)

                contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

                # cv.waitKey(0)
                cv2.imwrite(dstpath2, blank)





