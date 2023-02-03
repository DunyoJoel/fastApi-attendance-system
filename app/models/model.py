from sqlalchemy import Column, Integer, String, ForeignKey,DateTime, Boolean, Text
from app.utils.dbConn import Base

from sqlalchemy.orm import relationship

from datetime import datetime



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key =True, index = True)
    name = Column(String)
    department = Column(String, unique=True, index=True)
    location = Column(String,  nullable=True)
    contact = Column(String)
    device = Column(String,  nullable=True)
    dateAdded = Column(DateTime, default=datetime.now)
    isActive = Column(Boolean(), default=True)
    department_id = Column(Integer,ForeignKey("departments.id"))
    role_id = Column(Integer,ForeignKey("roles.id"))
    action_by = relationship("Department", back_populates="User", uselist=False)
    which_role= relationship("Role", back_populates="users")



class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key =True, index = True)
    name = Column(String)
    department = Column(String, unique=True, index=True)
    location = Column(String,  nullable=True)
    contact = Column(String)
    device = Column(String,  nullable=True)
    admin_id = Column(Integer,ForeignKey("admins.id"))
    belongs_to = relationship("User", back_populates="roles")
    dateAdded = Column(DateTime, default=datetime.now)



class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key =True, index = True)
    department_name = Column(String)
    dateAdded = Column(DateTime, default=datetime.now)
    admin_id = Column(Integer,ForeignKey("admins.id"))


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key =True, index = True)
    admin_name = Column(String)
    contact = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    admin_addedby = relationship("Department")
    dateAdded = Column(DateTime, default=datetime.now)



class Attendance(Base):
    __tablename__ = 'attendances'
    id = Column(Integer, primary_key = True, index = True)
    time_in = Column(DateTime, default=datetime.now)
    time_out = Column(DateTime, default=datetime.now)
    userId = Column(Integer,ForeignKey("users.id"))
    action_by =relationship("User", back_populates="attendant", uselist=False)

    
    


