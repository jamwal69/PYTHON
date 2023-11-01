countries = {
    "IN": ["India", "Delhi", 1320000000], 
    "US": ["America", "Washington", 320000000],
    "AU": ["Australia", "Canberra", 24000000],
    "CA": ["Canada", "Ottawa", 940000]
}

def view_countries():
    for country_code, country_info in countries.items():
        print(f"{country_code} -> {country_info[0]}, {country_info[1]}, {country_info[2]}")

def add_country(code, name, capital, population):
    countries[code] = [name, capital, population]
    
def delete_country(code):
    del countries[code]
    
while True:
    print("1. View countries")
    print("2. Add a country") 
    print("3. Delete a country")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        view_countries()
    elif choice == "2":
        code = input("Enter country code: ")
        name = input("Enter country name: ")
        capital = input("Enter capital city: ")
        population = int(input("Enter population: "))
        add_country(code, name, capital, population)
    elif choice == "3":
        code = input("Enter country code to delete: ")
        delete_country(code)
    elif choice == "4":
        break
    else:
        print("Invalid choice")