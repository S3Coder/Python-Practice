numList = [1,2,3,4,5] #0(1)

def func(numList):
    total = 0 #0(1)

    for num1 in numList:
        for num2 in numList: 
            print(num1,num2) #n sq
            total += 1 #n sq


    return total

print(func(numList)) #(2 + 2 n sq) => n sq according to the bigo rules

#if there are 2 list then the time complexity becomes n * m

numList = [1,2,3,4,5] #0(1)
numList1 = [1,2,3]

def func(numList):
    total = 0 #0(1)

    for num1 in numList1: #n
        for num2 in numList: #m 
            print(num1,num2) #n * m
            total += 1 #n * m


    return total

print(func(numList))