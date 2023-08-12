import json

def create_password():
    draft = []
    passwords_list = []

    websites = input("What website: ")
    username = input("What username: ")
    passwords = input("What password: ")

    draft.append(websites)
    draft.append(username)
    draft.append(passwords)
    passwords_list.append(draft)

    with open("passwords.json", "w") as outfile:
        json.dump(passwords_list, outfile)

def make_account():
    # Load existing accounts from the file or create an empty list if the file is empty or not present
    try:
        with open("accounts.json", "r") as infile:
            info = json.load(infile)
    except FileNotFoundError:
        info = []

    login_or_create = input("Login or create an account: ")
    if login_or_create == "create":
        create(info)
    elif login_or_create == "login":
        login(info)
    else:
        print("Invalid option!")

def create(file):
    user = input("Create username: ")
    # Check if the username already exists in the file
    for account in file:
        if user == account['username']:
            print("Username already used, try again.")
            create(file)
            return  # Stop the function if the username already exists

    password = input("Create password: ")
    file.append({'username': user, 'password': password})  # Store username and password as a dictionary

    # Save the updated list to the file
    with open("accounts.json", "w") as outfile:
        json.dump(file, outfile)

    print("Account created!")
    create_password()

def login(file):
    user = input("Login with username: ")
    password = input("Login with password: ")

    # Check if the entered username and password match any of the stored accounts
    for account in file:
        if user == account['username'] and password == account['password']:
            print("Logged in!")
            create_password()
            return  # Stop the function if login is successful

    print("Incorrect username or password.")

make_account()
