class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee ID: {self.employee_id}\nName: {self.name}")


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Salary: ${self.salary}/year\nEmployee Type: Full-Time")


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def display_info(self):
        super().display_info()
        print(f"Hourly Rate: ${self.hourly_rate}\nHours Worked: {self.hours_worked}\nEmployee Type: Part-Time")


# Example usage
full_time_employee = FullTimeEmployee("John Doe", 101, 60000)
part_time_employee = PartTimeEmployee("Jane Smith", 102, 20, 25)

print("Full-Time Employee Information:")
full_time_employee.display_info()

print("\nPart-Time Employee Information:")
part_time_employee.display_info()
