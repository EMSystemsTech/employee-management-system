Employee Management System

Overview

This project is a Python-based employee management system designed to simulate real-world employee workflow operations and data management processes.

The system demonstrates structured program flow, operational logic, user interaction handling, and workflow-oriented system design using Python.

Features

- Employee record management
- Menu-driven workflow system
- User input handling
- Data organization and retrieval
- Operational workflow structure
- Logic-based program navigation

Skills Demonstrated

- Python
- Workflow system design
- Program structure
- User input validation
- Operational logic
- Data handling
- Systems thinking
- Backend workflow concepts

Project Structure

This repository contains:

- Python source files
- Workflow logic
- Menu navigation systems
- Data handling operations

Future Improvements

- Database integration
- GUI interface
- Authentication system
- Reporting tools
- Modular refactoring
- Cloud integration
- Role-based access controls

Engineering Focus

This project reflects a systems-oriented approach to workflow automation, operational design, and structured backend logic using Python.

## Refactor Improvements (June 2026)

- Converted employee records from nested lists to dictionaries
- Added JSON persistence
- Added hire date tracking
- Added salary calculation automation
- Added general employee search
- Added field-specific employee search
- Added formatted phone and SSN display
- Refactored menu system into reusable functions
- Prepared backend architecture for React integration

## FastAPI Backend Update

This project now includes a FastAPI backend version of the Employee Management System.

### Backend Features

- JSON-based employee data persistence using `employees.json`
- Employee service layer in `services/employee_service.py`
- Auto-generated `employee_id` values
- Full CRUD API support:
  - `GET /employees`
  - `GET /employees/id/{employee_id}`
  - `GET /employees/search/{search_term}`
  - `POST /employees`
  - `PUT /employees/id/{employee_id}`
  - `PATCH /employees/id/{employee_id}`
  - `DELETE /employees/id/{employee_id}`
- Swagger API documentation available at `/docs`
- Prepared for future React frontend integration

### Run the API

Install dependencies:

```bash
pip install fastapi uvicorn
