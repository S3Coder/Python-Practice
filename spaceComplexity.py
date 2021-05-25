#Space Complexity for O(1)

def display_cube(items):

    results = pow([items[0],3]) #O(1)
    print(results);

item = [1,2,3,4,5]
display_cube(item)



#Space Complexity for O(n)


def all_cubes(items):
    results = []

    for item in items:
        results.append(pow(item,3)) #O(n) As it depends on the number of elements in the array

    print(results)

items = [2,3,4,5,6]
all_cubes(items)