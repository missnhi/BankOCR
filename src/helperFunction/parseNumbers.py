
def parseNumbers(text):
    # for number 1 and 4 with no character in the 1st line - text[0]
    if (text[0] == '\n'):
        text[0] = ' ' * 27

    number = [line.replace('\n', '')for line in text]
    digit = ''
    # Split each entry into 3x3 cells for a digit
    for i in range(0, 3, 3):
        digit = number[0][i:i + 3] + number[1][i:i + 3] + number[2][i:i + 3]

    return digit
