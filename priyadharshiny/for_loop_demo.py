fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for number in range(1,6):
    print(number)


text = " Hello World"
for letter in text:
    print(letter)

#break statement in for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# continue statement in for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "apple":
        continue
    print(fruit)