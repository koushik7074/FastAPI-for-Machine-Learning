from pydantic import BaseModel, EmailStr
from typing import Optional

# Shared field so that we dont have to repeat them in each class
class EmployeeBase(BaseModel):
    name: str
    email: EmailStr

# For creating employee record
class EmployeeCreate(EmployeeBase):
    pass 

# For updating employee data
class EmployeeUpdate(EmployeeBase):
    pass

# For reading data from database
class EmployeeOut(EmployeeBase):
    id: int


    class Config():
        from_attributes  = True