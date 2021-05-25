thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])



#while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1



thislist = ["Sibil", "Sarjam", "Soren"]
[print(x) for x in thislist]



fruits = ["mango", "orange", "banana", "Pineapple"]
newList = []

for i in range(len(fruits)):
    newList.append(fruits[i])


print(newList)