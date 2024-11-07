def stringCompression(stringList):

    index = 0
    i = 0
    n = len(stringList)

    while i < n:
        cur_char = stringList[i]
        count = 0
        while i < n and cur_char == stringList[i]:
            count += 1
            i += 1

        stringList[index] = cur_char
        index += 1
        if count > 1:
            for digit in str(count):
                stringList[index] = digit
                index += 1


    return index