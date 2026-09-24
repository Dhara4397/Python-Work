correct_password = "1234"
attempts=0
while attempts <3:
    password = input("Enter your password: ")

    if password == correct_password:
     print("Welcome")
     break

    attempts+=1


    if attempts==3:
        print("Access Denied")