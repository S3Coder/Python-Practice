#String concatenation

a = "Sibil"
b = "Soren"

print(a+b)


#String Format
age = 36
games = "Baksetball"
txt = "My name is John, and I am {} , and a {} player"
print(txt.format(age,games))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#Escape character
text = "This weekend is going to be awesome \"Especially today\"."
print(text)

#booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(15))

#Some values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

