name = "Priyadharshiny"
age = 17

print("My name is " + name + ", and I am " + str(age) + " years old")

print("My name is {} and I am {} years old".format(name, age))

print(f"My name is {name} and I am {age} years old")

marks = 87
print(f"Total marks after bonus is {marks + 5}")

def get_percentage(marks):
    return marks / 100 * 100

print(f"Percentage is {get_percentage(marks)} percent")