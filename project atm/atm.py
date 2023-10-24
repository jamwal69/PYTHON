# User details dictionary
users = {
  "user1": {"name": "User 1", "password": "pass1", "balance": 5000},
  "user2": {"name": "User 2", "password": "pass2", "balance": 5000},
  "user3": {"name": "User 3", "password": "pass3", "balance": 5000},
  "user4": {"name": "User 4", "password": "pass4", "balance": 5000},
  "user5": {"name": "User 5", "password": "pass5", "balance": 5000}
}

# Admin details
admin = {"userid": "admin", "password": "adminpass", "balance": 1000000} 

# Login function
def login(userid, password):
  if userid in users:
    if password == users[userid]["password"]:
      print("Login successful!")
      return True
    else:
      print("Invalid password!")
  else:
    print("Invalid userid!")
  return False

# Deposit function  
def deposit(userid, amount):
  users[userid]["balance"] += amount
  print("Deposit successful!")

# Withdraw function
def withdraw(userid, amount):
  if amount > users[userid]["balance"]:
    print("Insufficient balance!")
  else:
    users[userid]["balance"] -= amount
    print("Withdraw successful!")

# Balance function
def check_balance(userid):
  print(f"Balance: {users[userid]['balance']}")

# Admin menu function
def admin_menu():
  print("\n***** Admin Menu *****")
  print("1. Check Total Balance")
  print("2. Deposit Cash")
  print("3. Logout")
  
  choice = input("\nEnter your choice: ")
  
  if choice == "1":
    total = admin["balance"]
    for user in users.values():
      total += user["balance"]
    print(f"Total balance: {total}")
  
  elif choice == "2":
    amount = int(input("Enter amount to deposit: "))
    admin["balance"] += amount
    print("Deposit successful!")

  elif choice == "3":
    pass

  else:
    print("Invalid choice!")

# User menu function
def user_menu(userid):

  print("\n***** User Menu *****")
  
  print("1. Deposit Cash")
  print("2. Withdraw Cash")
  print("3. Check Balance")
  print("4. Logout")
  
  choice = input("\nEnter your choice: ")

  if choice == "1":
    amount = int(input("Enter amount to deposit: "))
    deposit(userid, amount)

  elif choice == "2":
    amount = int(input("Enter amount to withdraw: "))
    withdraw(userid, amount)

  elif choice == "3":
    check_balance(userid)

  elif choice == "4":
    pass

  else:
    print("Invalid choice!")

# Main menu
while True:

  print("\n***** Welcome to ABC Bank ATM *****")

  print("1. Admin Login")
  print("2. User Login")

  choice = input("\nEnter your choice: ")

  if choice == "1":
    userid = input("Enter admin userid: ")
    password = input("Enter admin password: ")

    if login(userid, password):
      admin_menu()
    else:
      print("Invalid userid or password!")

  elif choice == "2":
    userid = input("Enter userid: ")
    password = input("Enter password: ")

    if login(userid, password):
      user_menu(userid)
    else:
      print("Invalid userid or password!")

  else:
    print("Invalid choice!")