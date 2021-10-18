class ImageJPGWriter(object):

    def __init__(self, filename):
        self.filename = filename

    def write(self, bytes):
        output_img = open("output.jpg", "wb")
        output_img.write(open(self.filename, "rb").read())
        output_img.write(bytes)
        output_img.close()
