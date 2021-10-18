from exception.EndSequenceCollisionException import EndSequenceCollisionException
from exception.LenException import LenException
from image import ImageStreamWriter
from os.path import exists

filename = input("Enter filename: ")

if not exists(filename):
    print("File doesn't exist")
    exit(1)

bytes = input("Enter text to be inserted into image: ").encode("ASCII")

writer = ImageStreamWriter(filename)

try:
    writer.write(bytes)
    print("Text has been successfully embedded into image")
except LenException as e:
    print("Text len exceeded maximum len " + str(e.max_len))
except EndSequenceCollisionException as e:
    print("Text contains sequence used for text termination")
