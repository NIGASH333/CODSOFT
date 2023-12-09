import random
import string
import tkinter as tk

# Function to create a unique and secure password
def generate_password(length):
    # Combine various characters to form a strong password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate and display a password based on user input
def generate_password_and_display():
    # Retrieve the desired password length from user input
    password_length = int(length_entry.get())
    
    # Generate a unique password using the specified length
    generated_password = generate_password(password_length)
    
    # Display the generated password with a personalized message
    password_label.config(text="Your Nigash Password: " + generated_password)

# Set up the main window for the Nigash Password Generator
root = tk.Tk()
root.title("Nigash Password Generator")
root.configure(bg="darkgrey")

# Create a user-friendly interface with labels, entry box, and button
length_label = tk.Label(root, text="Choose your password length:", bg="darkgrey", fg="white", font=("bold", 12))
length_label.pack(pady=10)

length_entry = tk.Entry(root, font=("bold", 12))
length_entry.pack(pady=10, ipadx=10, ipady=5)

generate_button = tk.Button(root, text="Generate Your Nigash Password", command=generate_password_and_display, bg="green", fg="white", font=("bold", 12))
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Your Nigash Password will appear here:", bg="darkgrey", fg="white", font=("bold", 12))
password_label.pack(pady=10)

# Run the Nigash Password Generator
root.mainloop()


