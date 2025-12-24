import time
print("Welcome to your personal journal!")

journal = "journal.txt"

def add_entry():
    entry = input("Write your journal entry:\n")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("journal", "a") as file:
        file.write("Time:" + timestamp)
        file.write(entry + "\n")
    print("Entry added to your journal.")


def view_entries():
    try:
        with open("journal", "r") as file:
            content =file.read() 

            if content.strip() == "":
                print("Your journal is empty.")
            else:
                print("Your journal entries:")
                print(content)
    except FileNotFoundError:
        print("Your journal is empty.")

def delete_entries():
    confirm = input("Conform you want to delete all entries (Y/N)").lower()

    if confirm == "y":
        with open("journal","w") as file:
            file.write("")
            print("Journal content deleted")
    else:
        print("Entries wont be deleted")


while True:
    print("Choose option from (1-4)")
    print("1. Add Entry in journal")
    print("2. View entry in journal")
    print("3. Delete  entry in journal")
    print(" 4.Quit the journal")
    option = input("Enter your choice (1-4)")

    if option == "1":
        add_entry()
    elif option == "2":
        view_entries()
    elif option == "3":
        delete_entries()
    else:
        print("Exiting journal")
        break
