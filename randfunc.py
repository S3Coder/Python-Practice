numList = [1, 2, 3, 4, 5, 6] #O(1)

def randomFunction():
    total = 0 #O(1)
    all_integer = True #O(1)


    for num in numList:
        print(num) #O(n)

    for num1 in numList: 
        for num2 in numList: 
            print(num1,num2) #n square
            total += 1 #n square

    msg = "Rule 5 - Remove all non-dominants" #O(1)
    return total #O(1)

print(randomFunction(numList)) #O(5 + n + 2n square)

# => #O(5 + n + 2n square)
# => #O(n + 2n square)
# => #O(2n square)
# => #O(n square)