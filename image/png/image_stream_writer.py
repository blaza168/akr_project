from __future__ import absolute_import

from exception.EndSequenceCollisionException import EndSequenceCollisionException
from exception.LenException import LenException
from image.png.image_stream import ImageStream
from binary.utils import set_last_2_bits, read_by_2_bits


class ImageStreamWriter(ImageStream):

    def __init__(self, path):
        super().__init__(path)

    def write(self, text):
        """
        :param bytes: Bytes that will be included into image
        """
        bytes = bytearray(text)

        if len(text) > self.get_available_bytes():
            raise LenException(self.get_available_bytes())
        if self._end_sequence in bytes:
            raise EndSequenceCollisionException(self._end_sequence)

        for end_seq in ImageStream.END_SEQUENCE:
            bytes.append(end_seq)
        bits_gen = read_by_2_bits(bytes)
        for col, row in self._pixel_positions():
            pixel = self.pixels[col, row]
            red, green, blue = pixel[0], pixel[1], pixel[2]
            r_bits, g_bits, b_bits = next(bits_gen, None), next(bits_gen, None), next(bits_gen, None)

            if r_bits is None:
                break

            r_embedded = set_last_2_bits(red, r_bits)
            g_embedded = green
            b_embedded = blue
            if g_bits is not None:
                g_embedded = set_last_2_bits(green, g_bits)
            if b_bits is not None:
                b_embedded = set_last_2_bits(blue, b_bits)

            new_pixel = (r_embedded, g_embedded, b_embedded)
            self.pixels[col, row] = new_pixel

        self.image.save("embedded.png")

