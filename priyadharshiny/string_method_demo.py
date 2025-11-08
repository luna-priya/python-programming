original = "Hello World"
lowered = original.lower()
print("lowercase: ", lowered)

uppered = original.upper()
print("uppercase: ", uppered)

messy = "  Python  "
cleaned = messy.strip()
print("After strip: ", cleaned)

text = "Java is powerful"
updated = text.replace("Java", "Python")
print("after update: ", updated)

sentance = "Python is easy to learn"
words = sentance.split()
print("Split result: ", words)

text = "Learning Python is fun"
position = text.find("Learning")
print("Found at index: ", position)

heading = "Welcome to Python Programming"
formatted = heading.title()
print("Title case: ", formatted)

msg = "hello WORLD"
cleaned = msg.capitalize()
print("Capitalize result: ", cleaned)

greeting = "Hello everyone"
print(greeting.startswith("Hello"))
print(greeting.startswith("Hi"))

print(greeting.endswith("everyone"))
print(greeting.endswith("Hello"))

sentance = "Python is easy. Python is powerful. Python is popular."
count = sentance.count("Python")
print("Count result: ", count)

name = "Python"
print(name.isalpha())

mixed = "Python3"
print(mixed.isalpha())

num = "123"
print(num.isdigit())

bad_input = "year2025"
print(bad_input.isdigit())

code = "abc123"
print(code.isalnum())

value = "abc 123"
print(value.isalnum())

words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)

