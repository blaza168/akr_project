def set_last_2_bits(byte, bits):
    # wipe 2 last bits
    filter = 255 - 3
    byte = byte & filter
    return byte | bits


def get_last_2_bits(byte):
    str = f'{byte:b}'
    result = 0
    if str[-1] == "1":
        result += 1
    if str[-2] == "1":
        result += 2
    return result