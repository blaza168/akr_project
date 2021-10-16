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


def read_by_2_bits(bytes):
    for byte in bytes:
        str = f'{byte:b}'
        str = "0" * (8 - len(str)) + str
        for i in range(0, 8, 2):
            yield int(str[i: i+2], 2)
