from image.png.image_stream_writer import ImageStreamWriter
from image.png.image_stream_reader import ImageStreamReader

text = input("Enter text to be embedded into image: ").encode("ASCII")

writer = ImageStreamWriter("img.png")

writer.write(text)

reader = ImageStreamReader("embedded.png")
text = reader.read()

print("Text extracted from image: " + text.decode("ASCII"))