def getList():
    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    return list1

def returnLessTen(list1):
    list2 = []
    for x in list1:
        if x < 10:
            list2.append(x)
    return list2

def returnLessFive(list2):
    list3 = []
    for x in list2: 
        if x < 5:
            list3.append(x)
    print(list3)

returnLessFive(returnLessTen(getList()))
