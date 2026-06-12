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

from services.employee_service import (
    create_employee,
    load_employees,
    save_employees,
    search_employees,
    search_by_field
)

# Global employee list
employees = []


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
    global employees
    employees = load_employees()

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
            employees = load_employees()
            print("\nEmployee list imported successfully.")

        elif menu == "6":
            save_employees(employees)
            print("\nEmployee list exported successfully.")

        elif menu == "7":
            save_employees(employees)
            print("\nEmployee list saved.")
            print("Thank you and have a great day!")
            break

        else:
            print("\nInvalid option. Please choose 1-7.")

# Start program   
if __name__ == "__main__":
    run_program()

