import json


def load_employees():
    try:
        with open("employees.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)


def calculate_salary(hourly_wage):
    return hourly_wage * 40 * 52


def create_employee(name, ssn, phone, email, hire_date, hourly_wage):
    salary = calculate_salary(hourly_wage)

    employee = {
        "employee_id": generate_employee_id(),
        "name": name.title(),
        "ssn": ssn,
        "phone": phone,
        "email": email,
        "hire_date": hire_date,
        "hourly_wage": hourly_wage,
        "annual_salary": salary
    }

    return employee


def search_employees(search_term):
    employees = load_employees()
    search_term = search_term.lower()

    results = []

    for employee in employees:
        if (
            search_term in str(employee["employee_id"])
            or search_term in employee["name"].lower()
            or search_term in employee["email"].lower()
            or search_term in employee["phone"]
            or search_term in employee["ssn"]
            or search_term in str(employee["hourly_wage"])
            or search_term in str(employee["annual_salary"])
        ):
            results.append(employee)

    return results


def search_by_field(field_name, search_value):
    employees = load_employees()
    results = []

    for employee in employees:
        if field_name in employee:
            if str(employee[field_name]).lower() == str(search_value).lower():
                results.append(employee)

    return results

def update_employee(employee_id, updated_data):
    employees = load_employees()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            employee["name"].lower() == updated_data.name.title()
            employee["phone"] = updated_data.phone
            employee["email"] = updated_data.email
            employee["hourly_wage"] = updated_data.hourly_wage
            employee["annual_salary"] = calculate_salary(updated_data.hourly_wage)

            save_employees(employees)

            return employee

    return None

def delete_employee(employee_id):
    employees = load_employees()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            employees.remove(employee)
            save_employees(employees)
            return employee

    return None


def generate_employee_id():
    employees = load_employees()

    if len(employees) == 0:
        return 1001

    highest_id = max(employee["employee_id"] for employee in employees)

    return highest_id + 1


def patch_employee(employee_id, patch_data):
    employees = load_employees()

    for employee in employees:
        if employee["employee_id"] == employee_id:

            if patch_data.name is not None:
                employee["name"] = patch_data.name.title()

            if patch_data.ssn is not None:
                employee["ssn"] = patch_data.ssn

            if patch_data.phone is not None:
                employee["phone"] = patch_data.phone

            if patch_data.email is not None:
                employee["email"] = patch_data.email

            if patch_data.hire_date is not None:
                employee["hire_date"] = patch_data.hire_date

            if patch_data.hourly_wage is not None:
                employee["hourly_wage"] = patch_data.hourly_wage
                employee["annual_salary"] = calculate_salary(patch_data.hourly_wage)


            save_employees(employees)

            return employee

    return None
