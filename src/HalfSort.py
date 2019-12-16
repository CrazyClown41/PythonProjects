def getList():
    list = []
    input_string = input("Enter a list numbers or elements separated by space: ")
    list = input_string.split()
    return list

def split(list):
    splitList = list.split()
    return splitList

def sort(splitList):
    sortedList = splitList.sort()
    return sortedList

sort(split(getList()))
