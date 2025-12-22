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

- Add new passwords with a name and value.
- Generate random strong passwords with the "Generate Password" button.
- Show/hide passwords and delete entries as needed.

### Passwords are encrypted

- Stored securely in `passwords.json`.
- Master password salt saved in `salt`.

## Security Notes

- Master password is hashed using SHA-256 with a salt.
- All passwords are encrypted using Fernet symmetric encryption.
- Never share your master password.

