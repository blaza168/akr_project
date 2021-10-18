from binary.utils import extract_extension
from image.jpg.image_jpg_reader import ImageJPGReader
from image.jpg.image_jpg_writer import ImageJPGWriter
from image.png.image_stream_writer import ImageStreamWriter
from image.png.image_stream_reader import ImageStreamReader


def get_reader(filename):
    extension = extract_extension(filename)
    if extension == "jpg":
        return ImageJPGReader(filename)
    else:
        return ImageStreamReader(filename)


def get_writer(filename):
    extension = extract_extension(filename)
    if extension == "jpg":
        return ImageJPGWriter(filename)
    else:
        return ImageStreamWriter(filename)
