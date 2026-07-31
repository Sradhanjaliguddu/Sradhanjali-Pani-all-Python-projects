import pyperclip
import os

FILE_NAME = "passwords.txt"

def save_password():
    website = input("Enter website: ")
    password = input("Enter password: ")
    with open(FILE_NAME, "a") as f:
        f.write(f"{website}<||>{password}\n")
    print("Password saved.")

def get_password():
    website = input("Enter website: ")
    if not os.path.exists(FILE_NAME):
        print("No passwords stored yet.")
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            stored_website, stored_password = line.strip().split("<||>", 1)
            if stored_website == website:
                print(f"Password for {website}: {stored_password}")
                try:
                    pyperclip.copy(stored_password)
                    print("Password copied to clipboard.")
                except Exception:
                    pass
                return
    print("No password found for that website.")

def main():
    while True:
        # print("Password Manager")
        print("1. Save a password")
        print("2. Get a password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            save_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

main()