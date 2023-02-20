from fastapi import APIRouter, Depends, Security, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.utils import schemas, dbConn
from app.security import token
from app.repo import users, roles, attendances,departments,admins

from app.utils.initialUser import User
from app.security import oauth2
from typing import List

router = APIRouter()
get_db = dbConn.get_db



#route for department
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





#route for role
@router.delete('/role/{id}', response_model=schemas.ShowRole, tags = ['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowRole = Security(
        oauth2.get_current_active_user,
       
    )):
    return roles.destroy(id, db)


@router.post('/role/add', response_model=schemas.ShowRole, tags = ['Admin',])
async def create_role(request:schemas.CreateRole, 
                            db: Session = Depends(get_db),
                              current_user: schemas.ShowAdmin = Security(
                                 oauth2.get_current_active_user
        
    )):
    return roles.create(request, db,current_user)

@router.get('/role/{id}',  response_model=schemas.ShowRole, tags = ['Admin'])
async def show_role(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return roles.show(id, db)


@router.get('/role/', response_model=List[schemas.RoleWithAdmin], tags = ['Admin'])
async def show_role_all(db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return roles.get_all(db)

@router.put('/role/update',  response_model=schemas.ShowRole, tags = ['Admin'])
async def update(request:schemas.UpdateRole, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
      
    )):
    return roles.update(request.id, request, db)


#route for user
@router.post('/user/add', response_model=schemas.ShowUser, tags = ['Admin',])
async def create_user(request:schemas.CreateUser, 
                            db: Session = Depends(get_db),
                              current_user: schemas.ShowAdmin = Security(
                                 oauth2.get_current_active_user
        
    )):
    return users.create(request, db,current_user)

@router.get('/user/{id}',  response_model=schemas.ShowUser, tags = ['Admin'])
async def show_user(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return users.show(id, db)

@router.get('/user/', response_model=List[schemas.UserWithAdmin], tags = ['Admin'])
async def show_user_all(db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return users.get_all(db)

@router.put('/user/update',  response_model=schemas.ShowUser, tags = ['Admin'])
async def update(request:schemas.UpdateUser, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
      
    )):
    return users.update(request.id, request, db)
@router.delete('/user/{id}', response_model=schemas.ShowUser, tags = ['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
       
    )):
    return users.destroy(id, db)



#route for admin
@router.post('/admin/add', response_model=schemas.ShowAdmin, tags = ['Admin',])
async def create_admin(request:schemas.CreateAdmin, 
                            db: Session = Depends(get_db),
                              current_user: schemas.ShowAdmin = Security(
                                 oauth2.get_current_active_user
        
    )):
    return admins.create_new_admin(request, db,current_user)

@router.get('/admin/{id}',  response_model=schemas.ShowAdmin, tags = ['Admin'])
async def show_admin(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return admins.show(id, db)

@router.put('/admin/update',  response_model=schemas.ShowAdmin, tags = ['Admin'])
async def update(request:schemas.UpdateAdmin, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
      
    )):
    return admins.update(request.id, request, db)

@router.delete('/admin/{id}', response_model=schemas.ShowAdmin, tags = ['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
       
    )):
    return admins.destroy(id, db)


#route for attendance
@router.get('/attendance/{id}',  response_model=schemas.ShowAttendance, tags = ['Admin'])
async def show_attendance(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return attendances.showAttendance(id, db)


@router.delete('/attendance/{id}', response_model=schemas.ShowAttendance, tags = ['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
       
    )):
    return attendances.destroy(id, db)


@router.get('/attendance/', response_model=List[schemas.ShowAttendance], tags = ['Admin'])
async def show_attendance_all(db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
        
    )):
    return attendances.get_all(db)

@router.put('/attendance/update',  response_model=schemas.ShowAttendance, tags = ['Admin'])
async def update(request:schemas.UpdateRole, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin  = Security(
        oauth2.get_current_active_user,
      
    )):
    return attendances.update(request.id, request, db)


@router.post('/attendance/user_login', response_model=schemas.ShowUser, tags = ['User',])
async def user_login(phone_number: str, 
                            db: Session = Depends(get_db)
                              ):
    return users.userByphoneNumber( phone_number,db)


@router.post('/attendance/user_attendance_login', response_model=schemas.ShowAttendance, tags = ['User',])
async def user_attendance_login(id: int, 
                            db: Session = Depends(get_db)
                              ):
    return attendances.login_attendance( id,db)

@router.post('/attendance/user_attendance_logout', response_model=schemas.ShowAttendance, tags = ['User',])
async def user_attendance_logout(id: int, 
                            db: Session = Depends(get_db)
                              ):
    return attendances.logout_attendance( id,db)