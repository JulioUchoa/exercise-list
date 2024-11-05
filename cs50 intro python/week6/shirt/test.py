# import libraries
import sys
import os
from PIL import Image, ImageOps


# define main funciton
def main():
    # checks if sys.argv len is not different from three
    if len(sys.argv) != 3:
        sys.exit("program just accept two command-line arguments")

    # checks if first command-line argument ends with '.png', '.jpg' or '.jpeg'
    elif not sys.argv[1].lower().endswith(".png") and not sys.argv[1].lower().endswith(".jpg") and not sys.argv[1].lower().endswith(".jpeg"):
        sys.exit("first argument does not ends with '.png', '.jpg' nor '.jpeg'")

    # checks if second command-line argument ends with '.png', '.jpg' or '.jpeg'
    elif not sys.argv[2].lower().endswith(".png") and not sys.argv[2].lower().endswith(".jpg") and not sys.argv[2].lower().endswith(".jpeg"):
        sys.exit("second argument does not ends with '.png', '.jpg' nor '.jpeg'")

    # open inputed images(files)
    first_img = sys.argv[1]
    secon_img = sys.argv[2]

    if os.path.splitext(fist_img)[1] != os.path.splitext(second_img)[2]:
        sys.exit("Input and output file extesions must be the same")



    shirt = Image.open(first_img)  # returns <class 'PIL.PngImagePlugin.PngImageFile'>
    rosto = Image.open(secon_img)


    # get the size of the shirt image
    shirt_size = shirt.size
    rosto_size = rosto.size

    # resize second image in acord to shirt lenght and width
    rosto_resized = ImageOps.fit(rosto, shirt_size)

    rosto_resized.paste(shirt, (0,0), shirt)
    ##
    # something is missing here... what is it?
    ##
    rosto_resized.save("iaoe.jpg")
    sys.exit()


if __name__ == '__main__':
    main()