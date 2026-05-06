import hashlib

stored_username = "admin"
stored_password = hashlib.sha256("admin123".encode()).hexdigest()

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_username and hashed_password == stored_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong password")

if attempts == 0:
    print("Account Locked")