import customtkinter as ctk
import re
import json
import os
import random
import string
from tkinter import messagebox


JSON_FILE = "passwords.json"
#----FUNCTIONS----
def load_passwords():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

def check_strength(pss):

    tests = [len(pss) >= 8,
             bool(re.search(r"[A-Z]", pss)),
             bool(re.search(r"[a-z]", pss)),
             bool(re.search(r"[0-9]", pss)),
             bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pss))]
    return all(tests)

def add_password(name, password):
    strength = "Strong" if check_strength(password) else "Weak"
    data = load_passwords()
    add = True
    for i in data:
        if name == i["name"] :
            i["password"] = password
            i["strength"] = strength
            add = False
            break


    if add:
         data.append({"name": name, "password": password, "strength": strength})
    save(data)
    refresh()

def checkPassword():
    pss = Entry_pss.get()
    tests = [len(pss) >= 8,
             bool(re.search(r"[A-Z]", pss)),
             bool(re.search(r"[a-z]", pss)),
             bool(re.search(r"[0-9]", pss)),
             bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pss))]
    for i,j in zip(check,tests):
        if j :
            i.configure(fg_color="green")
        else :
            i.configure(fg_color="red")

def reset():
    for i in check:
        i.configure(fg_color="red")
    Entry_pss.delete(0,"end")



def save_btn():
    thing = manager_name_entry.get()
    pss = manager_entry.get()
    if thing and pss :
        add_password(thing, pss)
        manager_entry.delete(0, "end")
        manager_name_entry.delete(0, "end")
    else :
        messagebox.showerror("Error", "Please fill in both Name and Password!")



def refresh():
    for widget in manager_list.winfo_children():
        widget.destroy()
    data = load_passwords()

    for i in data:
        frame = ctk.CTkFrame(manager_list, corner_radius=10)
        frame.pack(fill="x", pady=5)

        lbl = ctk.CTkLabel(frame, text=i["name"],width=100, wraplength=100)
        lbl.pack(fill="x",  padx=20,side="left")

        passw = ctk.CTkLabel(frame, text="*"*len(i["password"]),width=100, wraplength=100)
        passw.pack(fill="x", padx=20,side="left")

        x = "green" if i["strength"] == "Strong" else "red"

        stren = ctk.CTkLabel(frame, text=i["strength"], width=50, fg_color=x)
        stren.pack(fill="x", padx=30, side="left")

        def showpss(lbl=passw, pwd=i["password"]):
            lbl.configure(text=pwd)

        def hidepss(lbl=passw, pwd=i["password"]):
            lbl.configure(text="*"*len(pwd))

        hide = ctk.CTkButton(frame, text="Hide",width = 30,command = hidepss)
        hide.pack(fill="x", padx=5,side="left")

        show = ctk.CTkButton(frame, text="Show", width=30, command=showpss)
        show.pack(fill="x", padx=5, side="left")



        def delpsss(pwd=i):
            data = load_passwords()
            data.remove(pwd)
            save(data)
            refresh()

        dell = ctk.CTkButton(frame, text="Delete", width=30, command = delpsss)
        dell.pack(fill="x", padx=5, side="left")


def generate():

    uppers = string.ascii_uppercase
    lowers = string.ascii_lowercase
    numbers = string.digits
    specials = "!@#$%^&*()"
    len_choices = random.randint(2,5)
    chars = []
    pw = ""
    for i in range(len_choices):
        chars += [
            random.choice(uppers),
            random.choice(lowers),
            random.choice(numbers),
            random.choice(specials)
        ]

    random.shuffle(chars)
    for i in chars:
        pw += i
    return pw

def place():
    manager_entry.delete(0, "end")
    manager_entry.insert(0, generate())
#-----SETUP----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Password Manager App")
app.geometry("700x500")
app.resizable(False,False)

tabs = ctk.CTkTabview(app)
tabs.pack(fill="both", expand=True, padx=20, pady=20)
tabs.add("Checker")
tabs.add("Manager")

#----CHECKER TAB----
checker_tab = tabs.tab("Checker")

Entry_pss = ctk.CTkEntry(checker_tab, placeholder_text="Enter password to check")
Entry_pss.pack(pady=10,anchor="center")

Check_Button = ctk.CTkButton(checker_tab, text="Check Password", command=checkPassword)
Check_Button.pack(anchor="center",padx=10)

reset = ctk.CTkButton(checker_tab, text="Reset",command =reset)
reset.pack(pady=10,anchor="center")



requirements = ["At least 8 characters",
                "At least one uppercase letter",
                "At least one lowercase letter",
                "At least one number",
                "At least one special character"]

check =[]
for i in requirements:
    lbl = ctk.CTkLabel(checker_tab, text=i, width=10, fg_color="red", corner_radius=20)
    lbl.pack(fill="x",pady=10,padx=20,anchor="center")
    check.append(lbl)


#---MANAGER TAB---
manager_tab = tabs.tab("Manager")
manager_name_entry = ctk.CTkEntry(manager_tab, placeholder_text="What is it for?")
manager_name_entry.pack(pady=5, padx=10, fill="x")

manager_entry = ctk.CTkEntry(manager_tab, placeholder_text="Enter password")
manager_entry.pack(pady=5, padx=10, fill="x")

generator_button = ctk.CTkButton(manager_tab, text = "Generate Password", command = place)
generator_button.place(x=150,y=87)

save_btn = ctk.CTkButton(manager_tab, text="Save Password",command = save_btn)
save_btn.place(x=350,y=87)

name_lab = ctk.CTkLabel(manager_tab, text="Site / App", width=100,font=("Arial", 18, "bold", "underline"))
name_lab.place(x=55,y=130)

separator = ctk.CTkFrame(manager_tab, width=200, height=2, fg_color="black")
separator.place(x=40, y=165)

password_lab = ctk.CTkLabel(manager_tab, text="Password", width=100,font=("Arial", 18, "bold", "underline"))
password_lab.place(x=190,y=130)

separator2 = ctk.CTkFrame(manager_tab, width=200, height=2, fg_color="black")
separator2.place(x=180, y=165)

strength_lab = ctk.CTkLabel(manager_tab, text="Strength", width=100,font=("Arial", 18, "bold", "underline"))
strength_lab.place(x=315,y=130)

separator3 = ctk.CTkFrame(manager_tab, width=200, height=2, fg_color="black")
separator3.place(x=300, y=165)

actions_lab = ctk.CTkLabel(manager_tab, text="Actions", width=100,font=("Arial", 18, "bold", "underline"))
actions_lab.place(x=450,y=130)

separator4 = ctk.CTkFrame(manager_tab, width=150, height=2, fg_color="black")
separator4.place(x=440, y=165)

manager_list = ctk.CTkScrollableFrame(manager_tab,width=570, corner_radius=20)
manager_list.place(x=10, y=160)




refresh()

app.mainloop()