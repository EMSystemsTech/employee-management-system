# Imports for FastAPI using CRUD methodology

from fastapi import FastAPI
from services.employee_service import (
    load_employees,
    search_employees,
    create_employee,
    save_employees,
    update_employee,
    delete_employee,
    patch_employee)
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class EmployeeInput(BaseModel):
    name: str
    ssn: str
    phone: str
    email: str
    hire_date: str
    hourly_wage: float

class EmployeePatch(BaseModel):
    name: Optional[str] = None
    ssn: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    hire_date: Optional[str] = None
    hourly_wage: Optional[float] = None

    
@app.get("/")
def home ():
    return {"message": "EMS API Running"}


@app.get("/employees")
def get_employees():
    employees = load_employees()

    return {"count": len(employees), "employees": employees}


@app.get("/employees/search/{search_term}")
def search_employee(search_term: str):
    results = search_employees(search_term)

    return {"count": len(results), "employees": results}


@app.post("/employees")
def add_employee(employee_input: EmployeeInput):
    employees = load_employees()

    new_employee = create_employee(
        employee_input.name,
        employee_input.ssn,
        employee_input.phone,
        employee_input.email,
        employee_input.hire_date,
        employee_input.hourly_wage)

    employees.append(new_employee)
    save_employees(employees)

    return {"message": "Employee added successfully", "employee": new_employee}


@app.put("/employees/id/{employee_id}")
def update_existing_employee(employee_id: int, employee_input: EmployeeInput):
    employee = update_employee(employee_id, employee_input)

    if employee:
        return {"message": "Employee updated", "employee": employee}

    return {"message": "Employee not found"}

@app.get("/employees/id/{employee_id}")
def get_employee_by_id(employee_id: int):
    employees = load_employees()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    return {"message": "Employee not found"}


@app.delete("/employees/id/{employee_id}")
def delete_existing_employee(employee_id: int):
    deleted_employee = delete_employee(employee_id)

    if deleted_employee:
        return {"message": "Employee deleted successfully", "employee": deleted_employee}

    return {"message": "Employee not found"}


@app.patch("/employees/id/{employee_id}")
def patch_existing_employee(employee_id: int, patch_data: EmployeePatch):
    employee = patch_employee(employee_id, patch_data)

    if employee:
        return{"message": "Employee patched successfully", "employee": employee}

    return {"message": "Employee not found"}
