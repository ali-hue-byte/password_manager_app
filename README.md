# Password Manager App

A secure and user-friendly password manager built with **Python** and **CustomTkinter**, featuring password storage, generation, and strength checking. Passwords are encrypted with **Fernet symmetric encryption** and protected with a master password.

## Features

- **Master Password Protection** – Secure your app with a master password.
- **Password Storage** – Safely store multiple passwords in an encrypted JSON file.
- **Password Strength Checker** – Evaluate password strength as Weak, Medium, or Strong.
- **Password Generator** – Generate random strong passwords.
- **Show/Hide Passwords** – Toggle password visibility for convenience.
- **Delete & Update Passwords** – Manage saved passwords easily.
- **Simple GUI** – Built with CustomTkinter for a modern, clean interface.
- **Windows Executable** – Run the app directly without installing Python.

## Installation

### Requirements

- Python 3.9+
- Required Python packages:
```bash
pip install customtkinter cryptography
```

## Windows Executable

A precompiled `.exe` file is included, so you can run the app on Windows without installing Python.

## Usage

**Run the app:**

```bash
python password_manager.py
```

Or use the `.exe` file.

**Set a master password** on first launch or enter your existing master password.

### Checker Tab

- Enter a password to see its strength.
- Reset the form anytime.

### Manager Tab

- Add new passwords.
- Generate random strong passwords with the "Generate Password" button.


### Passwords are encrypted

- Stored securely in `passwords.json`.
- Master password salt saved in `salt`.

## Security Notes

- Master password is hashed using SHA-256 with a salt.
- All passwords are encrypted using Fernet symmetric encryption.
- Never share your master password.

## Project Story

This project started as a simple command-line password checker. The original goal was only to check if a password was strong enough. While working on it, I wanted more than just a CLI tool, so I added a graphical interface. Even then, the project did not feel very useful.

I asked myself: what do I actually need from this project?
I realized that instead of only checking passwords, I needed a way to *store my own passwords*. That is when I decided to turn the project into a password manager.

After finishing this part, I showed the project to a friend. Instead of only liking the idea, he said he would actually use it. This made me think seriously about security. One question immediately came to my mind: what if someone gets access to the passwords file?

To solve this, I started looking for ways to encrypt the data. I discovered the cryptography library and used it to encrypt the stored passwords. However, I soon realized a problem: encryption requires a secret key, and storing a static key would defeat the purpose if someone obtained it.

Because of this, I continued researching and learned about key derivation functions (KDFs). I changed the design so the application asks the user for a master password at startup and derives the encryption key from it instead of storing one.

Finally, I needed a secure way to verify the master password. I learned about password hashing and implemented it so the application stores only a salted hash of the password, never the password itself.

This project evolved by repeatedly questioning each solution and improving it, turning a simple idea into a more secure and practical application.

## Screenshots
<img width="1393" height="1051" alt="image" src="https://github.com/user-attachments/assets/bf0b2c26-807e-46a7-92c0-bbf79a0dbb6d" />

<img width="1393" height="1048" alt="Screenshot 2025-12-23 105917" src="https://github.com/user-attachments/assets/6effe432-d70f-4d00-b78d-f74c9ce85bca" />




