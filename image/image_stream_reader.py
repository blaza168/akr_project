from __future__ import absolute_import
from .image_stream import ImageStream
from binary.utils import get_last_2_bits


class ImageStreamReader(ImageStream):

    class ByteStream(object):

        def __init__(self):
            self.bytes = bytearray()
            self.byte = 0
            self.counter = 0

        def append(self, two_bits):
            self.byte = self.byte << 2
            self.byte = self.byte | two_bits

            if self.counter == 3:
                self.bytes.append(self.byte)
                self.byte = 0
                self.counter = 0
            else:
                self.counter += 1

        def finished(self):
            """
            :return: False if bytestream doesn't contain end sequence
            """
            if len(self.bytes) <= len(ImageStream.END_SEQUENCE):
                return False
            for i in range(len(ImageStream.END_SEQUENCE)):
                index = -1 - i
                if ImageStream.END_SEQUENCE[index] != self.bytes[index]:
                    return False

            return True

        def get_bytes(self):
            return self.bytes[:-2]

    def read(self):
        """
        Extract hidden bytes from image
        :return: bytes
        """
        stream = ImageStreamReader.ByteStream()
        position_gen = self._pixel_positions()
        while not stream.finished():
            col, row = next(position_gen)
            pixel = self.pixels[col, row]
            rgb = [pixel[0], pixel[1], pixel[2]]
            for i in range(3):
                color = rgb[i]
                embedded_bits = get_last_2_bits(color)
                stream.append(embedded_bits)
                if stream.finished():
                    break

        return stream.get_bytes()

