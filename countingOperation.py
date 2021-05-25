students = ["sibil","sarjam","soren","starku","gaming"] #O(1)

def printName(students):
    first = students[0] #O(1)
    total = 0 #O(1)
    newlist = [] #O(1)

    for student in students:
        total += 1 #O(n)
        newlist.append(student) #O(n)


    print(newlist) #O(1)
    return total #O(1)

print(printName(students)) # O(6 + 2n) => O(n)