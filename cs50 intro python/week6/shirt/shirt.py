import os
import sys
from PIL import Image, ImageOps

def main():
        # checks if number of command line arguments are bigger than three
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # checks if number of command line arguments are smaller than three
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # checks if inpts has the correct extention
    elif os.path.splitext(sys.argv[1])[1].lower() not in [".png", ".jpg", ".jpeg"] or os.path.splitext(sys.argv[2])[1].lower() not in [".png", ".jpg", ".jpeg"]:
        sys.exit("Invalid Input")

    # checks if input and output extensions are the same
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("input and ouput have different extensions")

    # open the input with Image.open
    try:
        before = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # open shirt
    shirt = Image.open("shirt.png")

    # get size of the shirt
    shirt_size = shirt.size

    # resize 'face'=before image to fit shirts one
    before_resized = ImageOps.fit(before, shirt_size)

    # paste shirt into face
    before_resized.paste(shirt, shirt)

    # create output image
    before_resized.save(sys.argv[2])

if __name__ == '__main__':
    main()