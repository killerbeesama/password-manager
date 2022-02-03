from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_password():
    input3.delete(0,END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    input3.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    save_info = messagebox.askokcancel(title="Save password",message="Do you want to save the info?")
    if save_info:
        with open("password-manager/pass_text.txt",mode='a+') as file:
            file.write(f"{input1.get()} | {input2.get()} | {input3.get()}\n")
            input1.delete(0,END)
            input2.delete(0,END)
            input3.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20, bg='black')
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
logo_image = PhotoImage(file="password-manager/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

input1 = Entry(width=52)
input1.grid(column=1, row=1,columnspan=2)
input2 = Entry(width=52)
input2.grid(column=1, row=2,columnspan=2)
input3 = Entry(width=33)
input3.grid(column=1, row=3)

label1 = Label(text="Website:",fg='white',bg='black')
label1.grid(column=0, row=1)
label2 = Label(text="Email/Username:", fg='white',bg='black')
label2.grid(column=0, row=2)
label3 = Label(text="Password",fg='white',bg='black')
label3.grid(column=0, row=3)

button1 = Button(text="Generate Password",command=get_password)
button1.grid(column=2, row=3)
button2 = Button(text="Add",width= 44,command=save_pass)
button2.grid(column=1, row=4,columnspan=2)

window.mainloop()