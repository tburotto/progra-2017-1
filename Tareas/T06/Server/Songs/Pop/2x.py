import struct


def ecualizador(path):
    with open(path, "rb") as file:
        info = bytearray()
        header = bytearray()
        a = 0
        while True:
            a += 1
            b = file.read(1)
            if 24 < a <= 26:
                header.extend(b)
            else:
                info.extend(b)
                if a == 10000:
                    break

    palabra1 = header[0]
    palabra2 = header[1]
    print(palabra1, palabra2)
    f = struct.unpack("h", header)
    print(f)

if __name__ == "__main__":
    ecualizador("Justin Bieber - Sorry.wav")