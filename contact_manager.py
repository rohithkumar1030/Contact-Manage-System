# contact_manager.py

import csv

def display_menu():
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

def load_contacts(filename="contacts.csv"):
    contacts = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts, filename="contacts.csv"):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Name', 'Phone', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {'Name': name, 'Phone': phone, 'Email': email}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("Contacts List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        contact_index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= contact_index < len(contacts):
            contact = contacts[contact_index]
            print(f"Editing Contact: {contact['Name']}")
            contact['Name'] = input(f"Enter new name (leave blank to keep '{contact['Name']}'): ") or contact['Name']
            contact['Phone'] = input(f"Enter new phone (leave blank to keep '{contact['Phone']}'): ") or contact['Phone']
            contact['Email'] = input(f"Enter new email (leave blank to keep '{contact['Email']}'): ") or contact['Email']
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        contact_index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            contact = contacts.pop(contact_index)
            print(f"Deleted Contact: {contact['Name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    contacts = load_contacts()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()