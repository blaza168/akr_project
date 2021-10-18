from os.path import exists

from image.factory import get_reader

filename = input("Enter filename of image: ")

if exists(filename):
    reader = get_reader(filename)
    text = reader.read()

    print("Text extracted from image: " + text.decode("ASCII"))
else:
    print("File doesn't exist")
