import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManagerGUI:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Management System")

        # Create GUI components
        self.name_label = tk.Label(root, text="Name:")
        self.phone_label = tk.Label(root, text="Phone:")
        self.email_label = tk.Label(root, text="Email:")
        self.address_label = tk.Label(root, text="Address:")

        self.name_entry = tk.Entry(root)
        self.phone_entry = tk.Entry(root)
        self.email_entry = tk.Entry(root)
        self.address_entry = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Arrange GUI components
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.address_label.grid(row=3, column=0, padx=5, pady=5)

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        contact_list = "\n".join([f"{contact.name}: {contact.phone_number}" for contact in self.contacts])
        if not contact_list:
            contact_list = "No contacts found."
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = self.name_entry.get().lower()
        result = [contact for contact in self.contacts if search_term in contact.name.lower()]

        if not result:
            messagebox.showinfo("Search Result", "No matching contacts found.")
        else:
            search_result = "\n".join([f"{contact.name}: {contact.phone_number}" for contact in result])
            messagebox.showinfo("Search Result", search_result)

    def update_contact(self):
        old_name = self.name_entry.get().lower()
        new_name = self.phone_entry.get()
        new_phone = self.email_entry.get()
        new_email = self.address_entry.get()
        new_address = self.address_entry.get()

        for contact in self.contacts:
            if contact.name.lower() == old_name:
                contact.name = new_name
                contact.phone_number = new_phone
                contact.email = new_email
                contact.address = new_address
                messagebox.showinfo("Success", "Contact updated successfully.")
                return

        messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get().lower()
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name:
                del self.contacts[i]
                messagebox.showinfo("Success", "Contact deleted successfully.")
                return

        messagebox.showinfo("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerGUI(root)
    root.mainloop()
