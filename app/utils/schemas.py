from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime




class CreateUser(BaseModel):
    id: int
    fullname: str
    location: str
    phone_number: str
    device: str
    isActive: bool
    dateAdded: datetime

    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    id: int
    fullname: str
    location: str
    phone_number: str
    device: str
    isActive: bool
    dateAdded: datetime
    
    class Config():
        orm_mode = True

class UpdateUser(BaseModel):
    id: int
    fullname: str
    location: str
    phone_number: str
    device: str
    isActive: bool
    dateAdded: datetime
    
    class Config():
        orm_mode = True


class CreateAttendance(BaseModel):
    time_in : str=None
    time_out : str=None
    userId : str=None
    
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

class UpdateDepartment(BaseModel):
    id: int
    department_name: str
   
    
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

class UpdateAdmin(BaseModel):
    id: int
    admin_name: str
    contact : str
    email : str
    password : str
    dateAdded : datetime
    isActive: bool = None
    
    

    class Config():
        orm_mode = True



class CreateRole(BaseModel):
    role_name : str
  
    class Config():
        orm_mode = True

class ShowRole(BaseModel):
    id: int
    role_name : str
    admin_id : int
    dateAdded: datetime
    
    class Config():
        orm_mode = True




class TokenPayload(BaseModel):
    email: str = None
    contact: str = None
    exp: int = None

class DepartmentWithAdmin(BaseModel):
  Department:ShowDepartment=None
  Admin:ShowAdmin=None
  class Config():
        orm_mode = True

        
class RoleWithAdmin(BaseModel):
  Role:ShowRole=None
  Admin:ShowAdmin=None
  class Config():
        orm_mode = True

class UpdateRole(BaseModel):
    id: int
    role_name: str
   
    
    class Config():
        orm_mode = True


class UserWithAdmin(BaseModel):
    User:ShowUser
    Admin:ShowAdmin

  
    class Config():
        orm_mode = True

class ShowAttendance(BaseModel):
    id: int
    time_in : str=None
    time_out : str=None
    attend_date: datetime
    
    class Config():
        orm_mode = True