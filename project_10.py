print("<===Contact book===>")

contact_list ={}

while True:
    print(f"Choose option:(1-5)")
    print(f"1. Add contact")
    print(f"2. Edit contact")
    print(f"3. View contact")
    print(f"4. Delete contact")
    print(f"5. Exit")
    option = input("Enter choice 1-5:\n")

    if option == "1":
        name = input("Enter contact name:\n")
        phone = input("Enter contact phone number:\n")
        email = input("Enter contact email:\n")

        contact_list[name]={
            "phone": phone,
            "email": email
        }
        
        for key, value in contact_list.items():
            print(f"{key}: {value}")
    
    elif option == "2":
        name = input("Enter the contact you want to edit:\n")
        print(contact_list)
        if name in contact_list:
            new_phone = input("Enter new phone number:\n")
            new_email = input("Enter new email:\n")
            contact_list["phone"] = new_phone
            contact_list["email"] = new_email
            print(f"Contact updated successfully.")
        else:
            print("Contact not found.")

    elif option == "3":
        if len(contact_list) == 0:
            print("No contacts available.")
        else:
            for key, value in contact_list.items():
                print(f"{key}: {value}")
    elif option == "4":
        name = input("Enter the contact you want to delete")
        if name in contact_list:
            del contact_list["name"]
            del contact_list["phone"]
            del contact_list["email"]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    elif option == "5":
        print("Exiting contact book.")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")

