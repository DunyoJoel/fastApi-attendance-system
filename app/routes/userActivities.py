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
    return departments.create(request, db,current_user)


@router.delete('/department/{id}',  response_model=schemas.ShowDepartment, tags = ['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return departments.destroy(id, db)

@router.put('/department/update',  response_model=schemas.ShowDepartment, tags = ['Admin'])
async def update(request:schemas.UpdateDepartment, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
      
    )):
    return departments.update(request.id, request, db)


@router.get('/department/{id}',  response_model=schemas.ShowDepartment, tags = ['Admin'])
async def show_department(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return departments.show(id, db)


@router.get('/department/', response_model=List[schemas.DepartmentWithAdmin], tags = ['Admin'])
async def show_department_all(db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return departments.get_all(db)





@router.delete('/role/{id}', response_model=schemas.ShowRole, tags = ['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowRole = Security(
        oauth2.get_current_active_user,
       
    )):
    return roles.destroy(id, db)


@router.post('/role/add', response_model=schemas.ShowRole, tags = ['Admin',])
async def create_department(request:schemas.CreateRole, 
                            db: Session = Depends(get_db),
                              current_user: schemas.ShowAdmin = Security(
                                 oauth2.get_current_active_user
        
    )):
    return roles.create(request, db,current_user)



