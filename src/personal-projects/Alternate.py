def getNum():
    num = int(input("Enter how many numbers you want: "))
    return num

def loop(num):
    iterate = num % 2
    for i in range(int(iterate)): 
        print(0, end = " ")  
        for j in range(1):
            print(1, end = " ")

loop(getNum())

# Not Complete Code