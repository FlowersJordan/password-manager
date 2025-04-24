# 🔐 Password Manager CLI

A simple, secure command-line password manager written in Python. This project demonstrates secure data storage, encryption, and modular CLI design.

---

## 🚀 Features

- Add new credentials (site, username, password)
- Passwords are securely encrypted using Fernet (`cryptography`)
- View stored credentials (requires key)
- Persistent storage in `passwords.enc`
- Hidden password input with `getpass`
- Simple CLI interface with menu navigation

---

## 🛠 Technologies

- Python 3.10+
- `cryptography` (Fernet encryption)
- `getpass` for secure CLI input
- File-based encrypted storage

---

## 🧪 How to Use

### 1. Generate your encryption key (first run only):
```bash
python manager.py  # will auto-run generate_key() if called manually
