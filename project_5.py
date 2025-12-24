password = ""
lives = 2

while password != "password123" and lives > 0:
    password = input("Enter the password: ")
    if password != "password123":
        print("Wrong password. Try again.")
        lives -= 1

        if lives > 0:
            print(f" You have {lives} lives left.")
        else:
            print("No lives left. Access denied.")
print("Access granted. Welcome!")


