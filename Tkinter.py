#!/usr/bin/env python
# coding: utf-8

# # Note Taking App

# In[1]:


import tkinter as tk
from tkinter import messagebox, simpledialog

def save_note():
    note_text = text_entry.get("1.0", "end-1c")
    if note_text.strip():
        with open("notes.txt", "a") as file:
            file.write(note_text + "\n")
        text_entry.delete("1.0", tk.END)
        messagebox.showinfo("Note Saved", "Your note has been saved.")
    else:
        messagebox.showwarning("Empty Note", "Please enter some text before saving.")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()
        notes_window = tk.Toplevel(root)
        notes_window.title("Notes")
        notes_text = tk.Text(notes_window, bg="lightyellow", fg="blue")
        notes_text.insert(tk.END, notes)
        notes_text.pack()
    except FileNotFoundError:
        messagebox.showwarning("No Notes Found", "There are no notes to display.")

def clear_notes():
    confirmed = messagebox.askyesno("Confirm", "Are you sure you want to clear all notes?")
    if confirmed:
        with open("notes.txt", "w") as file:
            file.truncate(0)
        messagebox.showinfo("Notes Cleared", "All notes have been cleared.")

def open_specific_note():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        
        note_index = simpledialog.askinteger("Open Note", "Enter the note number you want to open:", minvalue=1, maxvalue=len(notes))
        
        if note_index:
            note_index -= 1  # Adjust to 0-based index
            note = notes[note_index]
            notes_window = tk.Toplevel(root)
            notes_window.title(f"Note {note_index + 1}")
            notes_text = tk.Text(notes_window, bg="lightyellow", fg="blue")
            notes_text.insert(tk.END, note)
            notes_text.pack()
    except FileNotFoundError:
        messagebox.showwarning("No Notes Found", "There are no notes to display.")

root = tk.Tk()
root.title("Note-taking App")

# Text Entry
text_entry = tk.Text(root, height=10, width=40, bg="lightblue", fg="black")
text_entry.pack(pady=10)

# Buttons
save_button = tk.Button(root, text="Save Note", command=save_note, bg="green", fg="white")
view_button = tk.Button(root, text="View Notes", command=view_notes, bg="orange", fg="white")
clear_button = tk.Button(root, text="Clear Notes", command=clear_notes, bg="red", fg="white")
open_button = tk.Button(root, text="Open Note", command=open_specific_note, bg="purple", fg="white")

save_button.pack()
view_button.pack()
clear_button.pack()
open_button.pack()

root.mainloop()


# ## Login and Registration Application

# In[ ]:


#import modules
 
from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()


# ## Simple Website Home Landing Page 

# In[ ]:


#import modules
 
from tkinter import *
import os
from tkinter import PhotoImage
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login",bg="light blue", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green",bg="pink", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")

    Label(text="Bus Pass Management System",fg="white",bg="purple",relief="sunken",borderwidth="5",width="400",height="3").pack()
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login,bg="pink").pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register,bg="pink").pack()
 
    main_screen.mainloop()
 
 
main_account_screen()


# ## Colour Guessing Game

# In[ ]:


import tkinter as tk
import random

# Global variables
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
score = 0

def start_game():
    global score
    score = 0
    update_score()
    next_color()

def update_score():
    score_label.config(text=f"Score: {score}")

def next_color():
    global score
    color = random.choice(colors)
    text = random.choice(colors)

    color_label.config(foreground=color, text=text)

def check_match(selected_color):
    global score
    color = color_label.cget("foreground")

    if selected_color == color:
        score += 1
        update_score()

    next_color()

# Create the main window
root = tk.Tk()
root.title("Color Matching Game")

# Create widgets
instruction_label = tk.Label(root, text="Select the color of the word, not the word itself.")
color_label = tk.Label(root, text="", font=("Helvetica", 24))
score_label = tk.Label(root, text="Score: 0")
start_button = tk.Button(root, text="Start Game", command=start_game)

color_buttons = [tk.Button(root, text=color, width=10, command=lambda color=color: check_match(color)) for color in colors]

# Place widgets on the window
instruction_label.pack()
color_label.pack()
score_label.pack()
start_button.pack()

for button in color_buttons:
    button.pack()

# Start the main loop
root.mainloop()


# In[ ]:




