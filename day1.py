x = 200
print(isinstance(x, int))

name = "Sibil"
print(name.find("i"))

myList = ["Sibil", "Sarjam", "Soren"]

myList1 = list((2,3,4,5))
print(myList1)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist1 = ["apple", "banana", "cherry"]
thislist1.append("Jack Fruit")
print(thislist1)
thislist1.pop()
print(thislist1)
if "apple" in thislist1:
  print("Yes, 'apple' is in the fruits list")