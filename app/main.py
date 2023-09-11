"""Clean images using threshold"""

import os
import cv2 as cv


SOURCE_DIR = '/app/source/'
OUTPUT_DIR = '/app/output/'
ALLOWED_FILES = (os.getenv('ALLOWED_FILES') or "").split(',')

def process_draw(filename: str):
    """Clean image using threshold"""
    img = cv.imread(f'{SOURCE_DIR}{filename}', cv.IMREAD_GRAYSCALE)
    img = cv.medianBlur(img, 5)
    _, result = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    cv.imwrite(f"{OUTPUT_DIR}{filename}", result)


def __main__():

    def is_allowed(filename: str):
        return filename.split('.')[-1] in ALLOWED_FILES

    files = [f for f in os.listdir(SOURCE_DIR) if is_allowed(f)]
    total = len(files)
    done = 0

    for file in files:
        process_draw(file)
        done += 1
        print(f'PROGRESS: {done}/{total}')


__main__()
