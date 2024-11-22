from src.parser import parser
from src.helperFunction.checkSum import checkSum

def isValidAccount(text):
    accountList = parser(text)
    for acc in accountList:
        if '?' in acc:
            accountList[accountList.index(acc)] = acc + ' ILL'
        else:
            if (checkSum(acc) == False):
                accountList[accountList.index(acc)] = acc + ' ERR'

    return  accountList