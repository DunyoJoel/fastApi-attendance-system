from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.security.hashing import Hash
from app.models import model 
from app.utils import schemas


def create(request: schemas.CreateDepartment, db: Session):
    department = db.query(model.Department).filter(model.Department.department_name  == request.department_name ).first()
    if department:
        raise HTTPException(status_code= 303,
                            detail =f"department with the department name { request.department_name} already exist")
    else: 
        new_department = model.Department(department_name =request.department_name,
                               department_name = request.department_name,
                              date= request.dateAdded
                              )
                              
                              
        db.add(new_department)
        db.commit()
        db.refresh(new_department)
        return new_department



def show(id: int, db: Session):
    department = db.query(model.Department).filter(model.Department.id == id).first()
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with the id {id} is not available")
    return department

# def showLoginUser(current_user, db: Session):
#     loginUser =db.query(model.User, model.Sensor).outerjoin(model.Sensor).filter(model.User.id == current_user.id).first()
#     if not loginUser:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return loginUser
  

def get_all(db: Session):
    departments = db.query(model.Department).filter(model.Department.action_by == None).all()
    return departments



def destroy(id: int, db: Session):
    department = db.query(model.Department).filter(model.Department.id == id).first()
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"department with id {id} not found")
    db.delete(department)
    db.commit()
    return department


def update(id: int, request: schemas.ShowDepartment, db: Session):
    department = db.query(model.Department).filter(model.Department.id == id).first()
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"departments with id {id} not found")

    department.department_name =request.department_name
    
    department.dateAdded = request.dateAdded
   
    db.commit()
    db.refresh(department)
    return department



def showDepartment(db: Session, department_name: str ):
    department = db.query(model.Department).filter(model.Departmentr.department_name == department_name).first()
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with the id {department_name} is not available")
    return department

def get_by_name(department_name: str, db: Session):
    department = db.query(model.Department).filter(
        model.Department.department_name == department_name).first()
    return department