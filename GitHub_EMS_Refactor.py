"""
Employee Management System (GitHub Refactor)

Original Project:
Week 4.2 Employee Management System Functionality 4

Refactor Goals:
- Improve maintainability
- Reduce duplicate code
- Separate menu actions into functions
- Prepare for database integration
- Prepare for React frontend integration

Author: Ebony Morrow
"""


# Allows employee records to be stored and loaded using JSON files
import json

# Global employee list
employees = []

# Export Employee list
def write_file():
    with open("employees.json", "w") as file: # Open employees.json in write mode
        json.dump(employees, file, indent=4) # Save employees list to JSON file with readable formatting

# Import Employee list
def read_file():
    try:
        with open("employees.json", "r") as file: # Open employees.json in read mode
            employees.clear() # Clear current employee list before loading file data
            employees.extend(json.load(file)) # Load employee records from JSON file into employees list

    except FileNotFoundError:
        with open("employees.json", "w") as file: # Create a blank employee file if one does not exist
            json.dump([], file) # Create an empty employee list

    except json.JSONDecodeError:
        employees.clear() # Prevent program crash if JSON file is empty or corrupted

    return employees # Send employee list back to the calling function


# Main menu
def display_main_menu():

    main ={
        "1": "Add Employee",
        "2": "View All Employees",
        "3": "Search Employees",
        "4": "Update An Employee",
        "5": "Import Employee\'s",
        "6": "Export Employee\'s",
        "7": "Exit"
    }

    print("\nEmployee Management System\n")
    
    for key, value in main.items():
        print('[', key, ']', value)

# Creating employee functions
def calculate_salary(hourly_wage):
    return hourly_wage * 40 * 52

def create_employee(name, ssn, phone, email, hire_date, hourly_wage):
    salary = calculate_salary(hourly_wage)

    employee = {
        "name": name.title(),
        "ssn": ssn,
        "phone": phone,
        "email": email,
        "hire_date": hire_date,
        "hourly_wage": hourly_wage,
        "annual_salary": salary
    }

    return employee

def get_employee_input():
    print("\nPlease enter employee information:\n")

    name = input("Name: ")
    ssn = input("SSN: ")
    phone = input("Phone: ")
    email = input("Email: ")
    hire_date = input("Hire Date (MM/DD/YYYY): ")
    hourly_wage = float(input("Hourly Wage: $"))

    new_employee = create_employee(name, ssn, phone, email, hire_date, hourly_wage)

    return new_employee

# add employee form after allowing user to decide how many employees to add
def add_employee():
    add_more = "Y"
    
    while add_more == "Y":
        try:
            employee = get_employee_input()
            employees.append(employee)

            print("\nEmployee added successfully.")

            add_more = input("\nAdd another employee? [Y]/[N]: ").upper()
            
        except ValueError:
            print("\nInvalid wage. Please enter a number.")

# Designated employee archive print format
def display_employees(employees):
    
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    for index, employee in enumerate (employees, start=1):

        formatted_ssn = f"{employee['ssn'][:3]}-{employee['ssn'][3:5]}-{employee['ssn'][5:9]}"

        formatted_phone = (
            f"({employee['phone'][:3]}) "
            f"{employee['phone'][3:6]}-{employee['phone'][6:]}"
        )

        print(f"\nEmployee {index}")

        print("Name:", employee["name"])
        print("SSN:", formatted_ssn)
        print("Phone:", formatted_phone)
        print("Email:", employee["email"])
        print("Hire Date:", employee["hire_date"])
        print("Hourly Wage:", f"${employee['hourly_wage']:.2f}")
        print("Annual Salary:", f"${employee['annual_salary']:,.2f}")

# Employee search function: should work using any piece of employee info
def search_employees (search_term):
    search_term = search_term.lower()

    results = []
 
    for employee in employees:
        if (
            search_term in employee["name"].lower()
            or search_term in employee["email"].lower()
            or search_term in employee["phone"]
            or search_term in employee["ssn"]
            or search_term in str(employee["hourly_wage"])
            or search_term in str(employee["annual_salary"])
        ):

            results.append(employee)
                                       
    return results

def search_by_field(field_name, search_value):
    results = []

    for employee in employees:
        if field_name in employee:
            if str(employee[field_name]).lower() == str(search_value).lower():
                results.append(employee)

    return results

def search_employee_menu():
    print("\nHow would you like to search?")
    print("[1] General Search")
    print("[2] Search By Field")

    choice = input("\nChoose search option: ")

    if choice == "1":
        search_term = input("Enter employee name, email, phone, SSN, wage, or salary: ")
        results = search_employees(search_term)
        display_employees(results)

    elif choice == "2":
        print("\nSearchable fields:")
        print("name")
        print("ssn")
        print("phone")
        print("email")
        print("hire_date")
        print("hourly_wage")
        print("annual_salary")

        field_name = input("\nEnter field name: ")
        search_value = input("Enter search value: ")

        results = search_by_field(field_name, search_value)
        display_employees(results)

    else:
        print("\nInvalid search option.")

def view_all_employees():
    display_employees(employees)


# Program script
def run_program():
    read_file()

    while True:
        display_main_menu()
        menu = input("\nPlease choose an option: ")

        if menu == "1":
            add_employee()

        elif menu == "2":
            view_all_employees()

        elif menu == "3":
            search_employee_menu()

        elif menu == "5":
            read_file()
            print("\nEmployee list imported successfully.")

        elif menu == "6":
            write_file()
            print("\nEmployee list exported successfully.")

        elif menu == "7":
            write_file()
            print("\nEmployee list saved.")
            print("Thank you and have a great day!")
            break

        else:
            print("\nInvalid option. Please choose 1-7.")

# Start program   
run_program()
