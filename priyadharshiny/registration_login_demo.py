username = input("Enter your username: ")
password = input("Enter your password: ")
email = input("Register your email: ")
print("Registeration successful")

login_usernsme = input("Enter your username: ")
login_password = input("Enter your password: ")

if login_usernsme == username and login_password == password:
    print("Login successful Welcome, " + login_usernsme + "!")
else:
    print("Login failed, Invalied username or password!")