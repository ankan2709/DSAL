def encode(listString):
    encoded_string = []

    for s in listString:
        encoded_string.append(str(len(s)) + "#" + s)
    return "".join(encoded_string)

def decode(string):
    # 5#apple6#banana
    decoded_string = []

    i = 0

    while i < len(string):
        j = i

        while string[j] != "#":
            j += 1
        n = int(string[i:j])
        j += 1
        decoded_string.append(string[j: j+n])
        i = j+n

