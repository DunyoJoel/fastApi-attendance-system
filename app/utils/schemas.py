from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime




class CreateUser(BaseModel):
    fullname: str
    department: str
    location: str
    contact: str
    device: str
    dateAdded : datetime
    isActive: bool = None

    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    id: int
    fullname: str
    department: str
    location: str
    contact: str
    isActive: bool
    dateAdded: datetime
    
    class Config():
        orm_mode = True

class CreateAttendance(BaseModel):
    userId: int
    action: str
    
    class Config():
        orm_mode = True

class ShowAttendance(BaseModel):
    id: int
    userId: int
    action: str
    actionTime: datetime
    
    class Config():
        orm_mode = True



class CreateDepartment(BaseModel):
    department_name: str
    

    class Config():
        orm_mode = True

class ShowDepartment(BaseModel):
    id: int
    department_name: str
    admin_id : int
    dateAdded: datetime
    
    class Config():
        orm_mode = True




class CreateAdmin(BaseModel):
    admin_name: str
    contact : str
    email : str
    password : str
    

    class Config():
        orm_mode = True

class ShowAdmin(BaseModel):
    id: int
    admin_name: str
    contact : str
    email : str
    dateAdded : datetime
    isActive: bool = None
    
    class Config():
        orm_mode = True




class CreateRole(BaseModel):
    rolename : str
    department : str
    dateAdded : datetime
    isActive: bool = None

    class Config():
        orm_mode = True

class ShowRole(BaseModel):
    id: int
    rolename : str
    department: str
    isActive: bool
    dateAdded: datetime
    
    class Config():
        orm_mode = True




class TokenPayload(BaseModel):
    email: str = None
    contact: str = None
    exp: int = None