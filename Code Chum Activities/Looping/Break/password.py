password = "secret"
attempts = 3
while attempts != 0:
    passwordAttempt = input("Enter the password: ")
    if password != passwordAttempt:
        print(f"Access denied! {attempts-1} attempts remaining.")
        attempts -=1
        if attempts == 0:
            print("Access denied!")
    elif passwordAttempt == password:
        print("Access granted!")
        break