
from __future__ import print_function
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import glob
import cv2
import argparse
import numpy as np
import cv2
from multiprocessing.pool import ThreadPool


def build_filters():
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 16):
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5*kern.sum()
        filters.append(kern)
    return filters

def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum

def process_threaded(img, filters, threadn = 8):
    accum = np.zeros_like(img)
    def f(kern):
        return cv2.filter2D(img, cv2.CV_8UC3, kern)
    pool = ThreadPool(processes=threadn)
    for fimg in pool.imap_unordered(f, filters):
        np.maximum(accum, fimg, accum)
    return accum

def load_images_from_folder(input):
    images = []
    for filename in os.listdir(input):
        img = cv2.imread(os.path.join(input, filename))
        filters = build_filters()
        res = process_threaded(img, filters)
        cv2.imwrite(os.path.join(output_data , filename), res)
        #cv2.imwrite(os.path.join(output_data, img))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gabor')
    parser.add_argument('--input', required=True, help='Path for input image')
    parser.add_argument('--output', required=True, help='Path for output image')
    args = parser.parse_args()
    current_directory = os.getcwd()
    input_data = os.path.join(current_directory, args.input)
    output_data = os.path.join(current_directory, args.output)
    load_images_from_folder(input_data)
