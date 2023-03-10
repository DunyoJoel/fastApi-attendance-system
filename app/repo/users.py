from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.security.hashing import Hash
from app.models import model 
from app.utils import schemas


def create(request: schemas.CreateUser, db: Session,current_user):
    user = db.query(model.User).filter(model.User.fullname == request.fullname).first()
    if user:
        raise HTTPException(status_code= 303,
                            detail =f"User with the name { request.fullname} already exist")
    else: 
        new_user = model.User(fullname =request.fullname,
                              location = request.location,
                              phone_number = request.phone_number,
                              device= request.device,
                              dateAdded= request.dateAdded,
                              admin_id  = current_user.id 
                              )
                              
                              
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user



def show(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user


def userByphoneNumber(phone_number: str, db: Session):
    user = db.query(model.User).filter(model.User.phone_number == phone_number).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the phone number  {phone_number} is not available")
    return user
# def showLoginUser(current_user, db: Session):
#     loginUser =db.query(model.User, model.Sensor).outerjoin(model.Sensor).filter(model.User.id == current_user.id).first()
#     if not loginUser:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return loginUser
  

def get_all(db: Session):
    users = db.query(model.User,model.Admin).outerjoin(model.Admin).all()
    print(users)

    return users

def get_all_admin(db: Session):
    admin = db.query(model.User).filter(model.User.action_by is not None).all()
    return admin

def destroy(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    db.delete(user)
    db.commit()
    return user


def update(id: int, request: schemas.ShowUser, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.fullname = request.fullname
    user.location = request.location
    user.phone_number = request.phone_number
    user.device = request.device
    user.dateAdded = request.dateAdded
    user.isActive = request.isActive
   
    db.commit()
    db.refresh(user)
    return user



def showUser(db: Session, fullname: str ):
    user = db.query(model.User).filter(model.User.fullname == fullname).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {fullname} is not available")
    return user

def get_by_name(contact: str, db: Session):
    user = db.query(model.User).filter(
        model.User.contact == contact).first()
    return user