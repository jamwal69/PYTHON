# Constants
ADMIN_LOGIN = "1"
USER_LOGIN = "2"
ADMIN_LOGOUT = "3"
MAX_LOGIN_ATTEMPTS = 3
LOCKED_ACCOUNT_MESSAGE = "Account locked. Too many unsuccessful login attempts."
MAX_DEPOSIT_LIMIT_USER = 100000
MAX_DEPOSIT_LIMIT_ADMIN = 300000
MAX_BALANCE_LIMIT_ADMIN = 300000
MAX_WITHDRAW_LIMIT_USER = 50000

# User details dictionary
users = {
    "user1": {"name": "User1", "password": "pass1", "balance": 5000, "login_attempts": 0, "locked": False},
    "user2": {"name": "User2", "password": "pass2", "balance": 5000, "login_attempts": 0, "locked": False},
    "user3": {"name": "User3", "password": "pass3", "balance": 5000, "login_attempts": 0, "locked": False},
    "user4": {"name": "User4", "password": "pass4", "balance": 5000, "login_attempts": 0, "locked": False},
    "user5": {"name": "User5", "password": "pass5", "balance": 5000, "login_attempts": 0, "locked": False}
}

# Admin details
admin = {"userid": "admin", "password": "adminpass", "balance": 1000000}

# Login function
def login(userid, password):
    if userid == admin["userid"] and password == admin["password"]:
        print("Admin login successful!")
        return True
    elif userid in users and not users[userid]["locked"] and password.lower() == users[userid]["password"].lower():
        print("User login successful!")
        users[userid]["login_attempts"] = 0  # Reset login attempts on successful login
        return True
    else:
        print("Invalid userid or password!")
        users[userid]["login_attempts"] += 1
        if users[userid]["login_attempts"] >= MAX_LOGIN_ATTEMPTS:
            users[userid]["locked"] = True
            print(LOCKED_ACCOUNT_MESSAGE)
        return False

# Deposit function
def deposit(userid, amount):
    if userid == admin["userid"]:
        if (admin["balance"] + amount) > MAX_BALANCE_LIMIT_ADMIN:
            print(f"Maximum balance limit for admin exceeded. Depositing {MAX_BALANCE_LIMIT_ADMIN - admin['balance']} instead.")
            amount = MAX_BALANCE_LIMIT_ADMIN - admin['balance']

    if userid == admin["userid"] and amount > MAX_DEPOSIT_LIMIT_ADMIN:
        print(f"Maximum deposit limit for admin exceeded. Depositing {MAX_DEPOSIT_LIMIT_ADMIN} instead.")
        amount = MAX_DEPOSIT_LIMIT_ADMIN
    elif amount > MAX_DEPOSIT_LIMIT_USER:
        print(f"Maximum deposit limit for user exceeded. Depositing {MAX_DEPOSIT_LIMIT_USER} instead.")
        amount = MAX_DEPOSIT_LIMIT_USER

    users[userid]["balance"] += amount

    # Check for balance and print notification
    if users[userid]["balance"] < 75000:
        print("Notification: Your balance is less than 75k.")

    print("Deposit successful!")

# Withdraw function
def withdraw(userid, amount):
    if userid == admin["userid"]:
        print("Admin cannot withdraw money.")
        return

    if amount > MAX_WITHDRAW_LIMIT_USER:
        print(f"Maximum withdrawal limit for user exceeded. Withdrawing {MAX_WITHDRAW_LIMIT_USER} instead.")
        amount = MAX_WITHDRAW_LIMIT_USER

    if amount > users[userid]["balance"]:
        print("Insufficient balance!")
    else:
        users[userid]["balance"] -= amount

        # Check for balance and print notification
        if users[userid]["balance"] < 75000:
            print("Notification: Your balance is less than 75k.")

        print("Withdraw successful!")

# Balance function
def check_balance(userid):
    print(f"Balance: {users[userid]['balance']}")

# Admin menu function
def admin_menu():
    while True:
        print("\n***** Admin Menu *****")
        print(f"{ADMIN_LOGIN}. Check Total Balance")
        print("2. Deposit Cash")
        print(f"{ADMIN_LOGOUT}. Logout")

        choice = input("\nEnter your choice: ")

        if choice == ADMIN_LOGIN:
            total = admin["balance"]
            for user in users.values():
                total += user["balance"]
            print(f"Total balance: {total}")

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            deposit(admin["userid"], amount)
            print("Deposit successful!")

        elif choice == ADMIN_LOGOUT:
            break

        else:
            print("Invalid choice! Please enter a valid option.")

# User menu function
def user_menu(userid):
    while True:
        print("\n***** User Menu *****")
        print("1. Deposit Cash")
        print("2. Withdraw Cash")
        print("3. Check Balance")
        print(f"{ADMIN_LOGOUT}. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            amount = int(input("Enter amount to deposit: "))
            deposit(userid, amount)

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            withdraw(userid, amount)

        elif choice == "3":
            check_balance(userid)

        elif choice == ADMIN_LOGOUT:
            break

        else:
            print("Invalid choice! Please enter a valid option.")

# Main menu
while True:
    print("\n***** Welcome to ABC Bank ATM *****")
    print(f"{ADMIN_LOGIN}. Admin Login")
    print(f"{USER_LOGIN}. User Login")

    choice = input("\nEnter your choice: ")

    if choice == ADMIN_LOGIN:
        userid = input("Enter admin userid: ")
        password = input("Enter admin password: ")

        if login(userid, password):
            admin_menu()
        else:
            print("Invalid userid or password!")

    elif choice == USER_LOGIN:
        userid = input("Enter userid: ")
        password = input("Enter password: ")

        if login(userid, password):
            user_menu(userid)
        else:
            print("Invalid userid or password!")

    else:
        print("Invalid choice! Please enter a valid option.")
