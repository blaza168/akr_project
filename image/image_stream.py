from PIL import Image


class ImageStream(object):

    STEP = 3
    END_SEQUENCE = [0b00, 0b00, 0b00, 0b00, 0b00]

    def __init__(self, path):
        self.path = path
        self.image = Image.open(path, "r")
        self.pixels = self.image.load()

    def get_available_bytes(self):
        """
        Each *STEP* byte can carry 6 bits of information.
        Len of end sequence is subtracted from total number of usable bits
        :return: Number of bytes that can be hidden in image
        """
        img_size = self.image.size()
        pixel_count = img_size[0] * img_size[1]
        available_pixels = pixel_count // ImageStream.STEP
        available_bits = available_pixels * 6 - len(ImageStream.END_SEQUENCE)
        return available_bits // 8

    def _pixel_positions(self):
        """
        :return: Generator of usable pixels' indexes which are used to store information
        """
        cols = self.image.size()[0]
        for i in range(self.get_available_bytes()):
            move = i * ImageStream.STEP
            if move % cols == 0:
                return cols - 1, move // cols - 1
            row_index = move // cols
            col_index = move % cols - 1
            yield col_index, row_index
