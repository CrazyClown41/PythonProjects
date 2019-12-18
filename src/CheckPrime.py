def getNum():
    num = int(input("Enter number to see if it is prime: "))
    return num

def check(num):
    listRange = list(range(1,num+1))
    divisorList = []
    
    for number in listRange:
        if num % number == 0:
            divisorList.append(number)
    
    if divisorList[0] == 1 and divisorList[1] == num:            
        print("Number is prime!")
    else:
        print("Number is not prime.")
    
    print("And these are the divisors of", num, ":", divisorList)

check(getNum())