from src.helperFunction.dataBuilder import dataBuilder
from src.helperFunction.prettyPrintDigit import prettyPrintDigit

def parser(text):
    data = dataBuilder()
    #list of entries: every 4 lines = 1 entry
    entries = [text[i:i+4] for i in range(0, len(text), 4)]

    parsed_entries = []
    for index, entry in enumerate(entries):
        entry = [line.replace('\n', '') for line in entry]


        # Add spaces to the end of line such as' - - ...' to make them 27 characters long
        entry = [line + ' ' * (27 - len(line)) if len(line) < 27 else line for line in entry[:3]]

        # Split each entry into 3x3 cells for each digit
        digits = ''
        for i in range(9):
            digit = ''.join(line[i*3:(i+1)*3] for line in entry)

            # if data.get(digit, '?') == '?':
                # prettyPrintDigit(digit)

            digits += data.get(digit, '?')

        parsed_entries.append(digits)
    return parsed_entries