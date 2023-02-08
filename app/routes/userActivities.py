from fastapi import APIRouter, Depends, Security, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.utils import schemas, dbConn
from app.security import token
from app.repo import users, roles, attendance,departments,admins

from app.utils.initialUser import User
from app.security import oauth2
from typing import List

router = APIRouter()
get_db = dbConn.get_db


@router.post('/department/add', response_model=schemas.ShowDepartment, tags = ['Admin',])
async def create_department(request:schemas.CreateDepartment, 
                            db: Session = Depends(get_db),
                              current_user: schemas.ShowAdmin = Security(
                                 oauth2.get_current_active_user
        
    )):
    print(current_user)
    return departments.create(request, db,current_user)

@router.post('/role/add', response_model=schemas.ShowRole, tags = ['Admin',])
async def create_department(request:schemas.CreateDepartment, 
                            db: Session = Depends(get_db),
                              current_user: schemas.ShowAdmin = Security(
                                 oauth2.get_current_active_user
        
    )):
    print(current_user)
    return departments.create(request, db,current_user)
