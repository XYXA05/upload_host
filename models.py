from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ForeignKeyConstraint
from database import Base
from typing import List, Union
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class UserCreate_File(Base):
    __tablename__ = "UserCreate_File"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    position = Column(Integer(), index=True)
    content_type = Column(String(10), nullable=False)
    file_path = Column(String(255), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("UserCreate", back_populates="files")




class User_3D_File_model(Base):
    __tablename__ = "User_3D_File_model"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    content_type = Column(String(255), nullable=False)
    file_path = Column(String(255), nullable=False)

    new_build_apartment_id = Column(Integer, ForeignKey("new_build_apartment.id"))
    User_3D_File = relationship("ItemCreate", back_populates="d3_object")


class File_new_build_apartment_ItemCreate_about(Base):
    __tablename__ = "File_new_build_apartment_ItemCreate_about"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    content_type = Column(String(10), nullable=False)
    file_path = Column(String(255), nullable=False)

    item_create_about_id = Column(Integer, ForeignKey("new_build_apartment_about.id"))
    item_create_about = relationship("ItemCreate_about", back_populates="files")

class File_new_build_apartment_aerial_survey_360(Base):
    __tablename__ = "File_new_build_apartment_aerial_survey_360"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    date = Column(String(30), index=True)
    content_type = Column(String(10), nullable=False)
    file_path = Column(String(255), nullable=False)

    new_build_apartment_id = Column(Integer, ForeignKey("new_build_apartment.id"))
    apartment_aerial = relationship("ItemCreate", back_populates="aerial_survey")


class File_new_build_apartment(Base):
    __tablename__ = "File_new_build_apartment"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    position = Column(Integer(), index=True)
    content_type = Column(String(10), nullable=False)
    file_path = Column(String(255), nullable=False)

    new_build_apartment_id = Column(Integer, ForeignKey("new_build_apartment.id"))

    new_build_apartment = relationship("ItemCreate", back_populates="files")



class File_new_build_apartment_construction_monitoring(Base):
    __tablename__ = "File_new_build_apartment_construction_monitoring"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    position = Column(Integer(), index=True)
    date = Column(String(30), index=True)
    namber_build_andsection =Column(String(25), index=True)
    content_type = Column(String(10), nullable=False)
    file_path = Column(String(255), nullable=False)

    new_build_apartment_id = Column(Integer, ForeignKey("new_build_apartment.id"))

    new_build_apartment = relationship("ItemCreate", backref="construction_monitoring_files")    



class File_description(Base):
    __tablename__ = "File_description"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    #position = Column(Integer(), index=True)
    content_type = Column(String(10), nullable=False)
    file_path = Column(String(255), nullable=False)

    new_build_apartment_description_id = Column(Integer, ForeignKey("new_build_apartment_description.id"))

    new_build_apartment = relationship("ItemsCreateDescription", back_populates="files")


