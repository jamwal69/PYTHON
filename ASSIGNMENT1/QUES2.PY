import re

def get_full_name():
  while True:
    name = input("Enter your full name (min 2 words): ")
    name_words = name.split()
    if len(name_words) >= 2:
      return name
    else:
      print("Invalid name. Please enter your first and last name.")
      
def get_password():
  while True:
    password = input("Enter a password (min 8 chars, 1 digit, 1 uppercase): ")
    if len(password) >= 8 and re.search(r"\d", password) and re.search(r"[A-Z]", password):
      return password
    else:
      print("Invalid password. Please try again.")

def get_first_name(full_name):
  return full_name.split()[0]

full_name = get_full_name()
password = get_password()
first_name = get_first_name(full_name)

print(f"Thank you {first_name} for registering!")