from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.security.hashing import Hash
from app.models import model 
from app.utils import schemas


def create(request: schemas.CreateRole, db: Session, current_user):
    role = db.query(model.Role).filter(model.Role.role_name == request.role_name).first()
    if role:
        raise HTTPException(status_code= 303,
                            detail =f"User with the rolename { request.role_name} already exist")
    else: 
        new_role = model.Role(role_name =request.role_name,
                               admin_id = current_user.id)      
                              
                              
                              
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        return new_role



def show(id: int, db: Session):
    role = db.query(model.Role).filter(model.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with the id {id} is not available")
    return role

# def showLoginUser(current_user, db: Session):
#     loginUser =db.query(model.User, model.Sensor).outerjoin(model.Sensor).filter(model.User.id == current_user.id).first()
#     if not loginUser:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return loginUser
  

def get_all(db: Session):
    roles = db.query(model.Role,model.Admin).outerjoin(model.Admin).all()
    print(roles)

    return roles



def destroy(id: int, db: Session):
    role = db.query(model.Role).filter(model.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")
    db.delete(role)
    db.commit()
    return role


def update(id: int, request: schemas.ShowRole, db: Session):
    role = db.query(model.Role).filter(model.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")

    role.role_name =request.role_name
   
    db.commit()
    db.refresh(role)
    return role



def showRole(db: Session, rolename: str ):
    role = db.query(model.Role).filter(model.Role.rolename == rolename).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with the id {rolename} is not available")
    return role

def get_by_name(rolename: str, db: Session):
    role = db.query(model.Role).filter(
        model.Role.rolename == rolename).first()
    return role