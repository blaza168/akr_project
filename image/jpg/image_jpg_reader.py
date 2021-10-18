class ImageJPGReader(object):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        read_img = open(self.filename, "rb").read()
        return read_img.split(b'\xff\xd9')[1]