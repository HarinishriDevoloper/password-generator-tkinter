
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

Black = "#000000"


def generate_password():
    # Check if the website and email fields are filled
    if not website_entry.get() or not email_entry.get():
        messagebox.showwarning(title="Warning", message="Please fill in the 'Name' and 'Email/Username' fields to generate a password.")
        return  # Exit the function if these fields are not filled
    
    # Check if the password entry is already filled
    if password_entry.get():
        return  # Exit the function if there's already a password

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



root = Tk()
root.title("Password Manager")
root.config(padx=100, pady=100,bg="pink")

welcome_label = Label(root, text="Welcome to Password Generator", bg="pink",font=("Arial", 30, "bold"))
welcome_label.grid(row=0, column=1)


canvas = Canvas(height=500, width=700,bg="pink",highlightthickness=0)
logo_img = PhotoImage(file="ss.png")
canvas.create_image(300, 300, image=logo_img)
canvas.grid(row=1, column=1)


frame = Frame(root,bg="pink")
frame.grid(row=2, column=0, columnspan=3, pady=20)


website_label = Label(frame, text="Name:",bg="pink",font=("Arial", 20, "bold"))
website_label.grid(row=0, column=0)
email_label = Label(frame, text="Email/Username:",bg="pink",font=("Arial", 20, "bold"))
email_label.grid(row=1, column=0)
password_label = Label(frame, text="Password:",bg="pink",font=("Arial", 20, "bold"))
password_label.grid(row=2, column=0)


website_entry = Entry(frame, width=35,font=('Arial 15'))
website_entry.grid(row=0, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(frame, width=35,font=('Arial 15'))
email_entry.grid(row=1, column=1, columnspan=2)
password_entry = Entry(frame, width=21,font=('Arial 15'))
password_entry.grid(row=2, column=1)

generate_password_button = Button(frame, text="Generate Password",font=("Arial", 10, "bold") ,command=generate_password)
generate_password_button.grid(row=2, column=2)
add_button = Button(root, text="Add", width=36, font=("Arial", 15, "bold"),command=save)
add_button.grid(row=3, column=1, columnspan=2)

root.mainloop()