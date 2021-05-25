newlist = [1,2,3,4,5]

def randumSum(num):

    #start writing your code here
    num1 = newlist[2]
    num2 = newlist[3]

    newSum = num1 + num2
    # print(newSum)

    if newSum == num:
        return "Valid"
    else:
        return "Invalid"


print(randumSum(5))

# Naive method to find a pair in a list with the given sum
def findPair(A, sum):
 
    # consider each element except the last
    for i in range(len(A) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(A)):
 
            # if the desired sum is found, print it
            if A[i] + A[j] == sum:
                print("Pair found", (A[i], A[j]))
                return
 
    # No pair with the given sum exists in the list
    print("Pair not found")
 
 
if __name__ == '__main__':
 
    A = [8, 7, 2, 5, 3, 1]
    sum = 10
 
    findPair(A, sum)


