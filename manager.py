from cryptography.fernet import Fernet
import os
from getpass import getpass

KEY_FILE = "key.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


DATA_FILE = "passwords.enc"

def encrypt_password(password, key):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode())



def add_password():
    key = load_key()

    site = str(input("Site Name: ")).strip()
    username = str(input("Username: ")).strip()
    password = getpass("Password (hidden): ").strip()

    if not site or not username or not password:
        print("All Fields Required.")
        return
    
    encrypted_pw = encrypt_password(password, key)

    with open(DATA_FILE,"ab") as f:
        f.write(f"{site},{username},".encode() + encrypted_pw + b"\n")

    print(f"Saved credentials for {site}.")


def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password).decode()

def view_passwords():
    if not os.path.exists(DATA_FILE):
        print("No Passwords Saved.")
        return
    
    key = load_key()

    with open(DATA_FILE, "rb") as f:
        for line in f:
            try:
                site, username, encrypted_pw = line.strip().split(b",", 2)
                decrypted_pw = decrypt_password(encrypted_pw, key)
                print(f"Site: {site.decode()} | Username: {username.decode()} | Password: {decrypted_pw}")
            except Exception as e:
                print("Error Reading Entries:", e)

def main():
    while True:
        print("\n==== Password Manager ====")
        print("1. Add Password")
        print("2. View Saved Passwords")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        match choice:
            case "1":
                add_password()
            case "2":
                view_passwords()
            case "3":
                print("Exiting Program.")
                break

            case _:
                print("Invalid Option. Try Again.")

                
if __name__ == "__main__":
    main()