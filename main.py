from fastapi import FastAPI, HTTPException
from models_val import Employee
from typing import List

# Defining data
# var_name: var_type = [value]
employees_db: List[Employee] = []

app = FastAPI()

# 1. Read all employees=======================================================
@app.get('/employees', response_model=list[Employee])
def get_employees():
    return employees_db

# 2. Read specific employees==================================================
@app.get('/employees/{emp_id}', response_model=Employee)
def get_employee(emp_id: int):
    for idx, employee in enumerate(employees_db):
        if employee.id == emp_id:
            return employees_db[idx]
    raise HTTPException(status_code=404, detail='Employee Not Found')

# 3. Add and employee=========================================================
@app.post('/add_employee', response_model=Employee)
def add_employee(new_employee: Employee):
    for employee in employees_db:
        if employee.id == new_employee.id:
            raise HTTPException(status_code=400, detail='Employee already exists!')
    employees_db.append(new_employee)
    return new_employee

# 4. Update an employee=======================================================
@app.put('/update_employee/{emp_id}', response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for idx, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[idx] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail='Employee not found!')

# 5. Delete an employee=======================================================
@app.delete('/delete_employee/{emp_id}')
def delete_employee(emp_id: int):
    for idx, employee in enumerate(employees_db):
        if emp_id == employee.id:
            del employees_db[idx]
            return {'message': f'Employee with employee_id: {emp_id} has been deleted successfully'}
    raise HTTPException(status_code=404, detail='Employee not found!')