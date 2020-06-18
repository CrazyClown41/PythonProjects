def getString():
    inputString = str(input("Enter Word: "))
    return inputString

def changeCase(inputString):
    if inputString.islower():
        inputString = inputString.upper()
        print(inputString)
    else:
        print("Something went wrong.")

changeCase(getString())
