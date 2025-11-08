my_list = ["apple", "banana", "cherry"]
print(my_list)

number = [1, 2, 3, 4, 5, 6]
print(number)


mixed = ["Hello",99,3.14, True]
print(mixed)


empty_list = []
print(len(empty_list))


fruits = ["apple", "banana", "cherry", "mango"]

first_item = fruits[0]
print("First item: ", first_item)

second_item = fruits[1]
print("Second item: ", second_item)

third_item = fruits[2]
print("Third item: ", third_item)

last_item = fruits[3]
print("last item: ", last_item)

last_item_alt = fruits[-1]
print(":last item using negative index ", last_item_alt)

fruits = ["apple", "banana", "cherry", "mango"]

fruits[1] = "blueberry"
print(fruits)

fruits[-1] = "kiwi"
print(fruits)

fruits[0] = "grape"
print(fruits)


fruits = []


fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)

fruits.insert(1, "orange")
print(fruits)


fruits.extend(["mango", "kiwi"])
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits_reversed = fruits[::-1]
print(fruits_reversed)
