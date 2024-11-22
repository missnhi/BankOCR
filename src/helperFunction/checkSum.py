'''
account number:  3  4  5  8  8  2  8  6  5
position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1

checksum calculation:
(d1+2*d2+3*d3+...+9*d9) mod 11 = 0

return a boolean value
'''
def checkSum(accountNumber):
    accountNumber = accountNumber[::-1]
    sum = 0
    # each account has 9 digits
    for i, digit in enumerate(accountNumber):
        sum += int(digit) * (i + 1)
    return sum % 11 == 0