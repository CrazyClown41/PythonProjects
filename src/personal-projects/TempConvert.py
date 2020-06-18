def getInitTemp():
    temp = float(input("Enter Inital Temperature: "))
    return temp

def tempConvert(temp):
    finalTemp = ((temp - 32) * 5/9)
    return float(finalTemp)

def printResults(finalTemp):
    print("After Conversion : % 5.2f" %(finalTemp))

printResults(tempConvert(getInitTemp()))



