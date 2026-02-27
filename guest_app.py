from auth import login, register

def main():
    print("🔥 Welcome to Raunak Ultra ERP Guest App 🔥")
    while True:
        choice = input("Select option: [1] Register [2] Login [3] Exit: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if register(username, password):
                print("✅ Registered successfully!")
            else:
                print("⚠ Username already exists!")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                print(f"🎉 Welcome {username}!")
            else:
                print("❌ Invalid credentials!")
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice.")

if __name__ == "__main__":
    main()