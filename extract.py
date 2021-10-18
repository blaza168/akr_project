from image import ImageStreamReader
from os.path import exists

filename = input("Enter filename of image: ")

if exists(filename):
    reader = ImageStreamReader(filename)
    text = reader.read()

    print("Text extracted from image: " + text.decode("ASCII"))
else:
    print("File doesn't exist")
