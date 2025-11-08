def great():
    print("Welcome to Python function!")

great()
great()
great()


def great_user(name):
    print("Hello, ", name)

great_user("priyadharshiny")
great_user("jerlin")
great_user("vichu")


def square(num):
    return num * num

result = square(5)
print("Square: ", result)
print(square(12))
print(square(120))


def get_max(a, b):
    if a > b:
        return a
    else:
        return b

max_value = get_max(5, 10)
print("Maxmima: ", max_value)


def great_user(name):
    print("Hello, " + name + "!")

names = ["priya", "brisa", "vichu"]
for name in names:
    great_user(name)


def great_default(name="Guest"):
    print("Hello, ", name)

great_default()
great_default("Jerlin")
great_default("vichu")