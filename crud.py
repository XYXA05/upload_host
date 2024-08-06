
import logging
import os
from typing import List, Optional
from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session, joinedload
import models, schemas
from sqlalchemy import and_


async def usercreate_file(db: Session, files: List[UploadFile], user_id: int, position: int):
    uploaded_files = []
    for file in files:
        file_location = f"./uploads/upload_file_company/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        
        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())  # Ensure to await the read method
        
        file_db = schemas.UserCreate_File_Create(
            filename=file.filename,
            content_type=file.content_type,
            file_path=file_location,
            position=position,
            owner_id=user_id
        )
        
        db_file = models.UserCreate_File(**file_db.dict())
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        
        uploaded_file = schemas.UserCreate_File(
            id=db_file.id,
            file_url=file_location,
            content_type=file.content_type,
            position=db_file.position  # Ensure position is set here
        )
        uploaded_files.append(uploaded_file)
    
    return schemas.UserCreate_Files(files=uploaded_files)

def get_image_path_by_position_and_id_owner(db: Session, position: int, owner_id: int):
    file = db.query(models.UserCreate_File).filter(
        models.UserCreate_File.position == position,
        models.UserCreate_File.owner_id == owner_id
    ).first()
    
    if file:
        return file.file_path
    return None

def get_image_item_path_by_position_and_id(db: Session, item_create_about_id: int):
    file = db.query(models.File_new_build_apartment_ItemCreate_about).filter(
        models.File_new_build_apartment_ItemCreate_about.item_create_about_id == item_create_about_id
    ).first()
    
    if file:
        return file.file_path
    return None


async def upload_file_about(db: Session, files: List[UploadFile], user_id: int):
    uploaded_files = []
    for file in files:
        file_location = f"./uploads/about/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        
        file_db = models.File_new_build_apartment_ItemCreate_about(
            filename=file.filename,
            content_type=file.content_type,
            item_create_about_id=user_id,
            file_path=file_location,

        )
        db.add(file_db)
        db.commit()
        db.refresh(file_db)
        
        uploaded_file = schemas.File_new_build_apartment_ItemCreate_about(
            file_url=file_location,
            content_type=file.content_type,
        )
        uploaded_files.append(uploaded_file)
    return schemas.File_new_build_apartment_ItemCreate_abouts(files=uploaded_files)





async def upload_file_compan(db: Session, files: List[UploadFile], new_build_apartment_id: int, position: int):
    uploaded_files = []
    for file in files:
        file_location = f"./uploads/main_page/{file.filename}"

        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        
        file_db = schemas.FileCreate(
            filename=file.filename,
            content_type=file.content_type,
            file_path=file_location,
            position=position,
            new_build_apartment_id = new_build_apartment_id
        )
        
        db_file = models.File_new_build_apartment(**file_db.dict())
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        
        uploaded_file = schemas.File(
            file_url=file_location,
            content_type=file.content_type,
            position = db_file.position,
            id = db_file.id
        )
        uploaded_files.append(uploaded_file)
    
    return schemas.Files(files=uploaded_files)

def get_image_path_by_position_and_id(db: Session, position: int, new_build_apartment_id: int):
    file = db.query(models.File_new_build_apartment).filter(
        models.File_new_build_apartment.position == position,
        models.File_new_build_apartment.new_build_apartment_id == new_build_apartment_id
    ).first()
    
    if file:
        return file.file_path
    return None


async def upload_files_plan(db: Session, files: List[UploadFile], new_build_apartment_description_id: int):
    uploaded_files = []
    for  file in files:
        file_location = f"./uploads/plan/{file.filename}"

        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        
        file_db = schemas.File_descriptionCreate(
            filename=file.filename,
            content_type=file.content_type,
            file_path=file_location,
            new_build_apartment_description_id = new_build_apartment_description_id
        )
        
        db_file = models.File_description(**file_db.dict())
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        
        uploaded_file = schemas.File_description(
            file_url=file_location,
            content_type=file.content_type,
            id = db_file.id

        )
        uploaded_files.append(uploaded_file)
    
    return schemas.File_descriptions(files=uploaded_files)

def get_image_path_by_id_description(db: Session, new_build_apartment_description_id: int):
    file = db.query(models.File_description).filter(
        models.File_description.new_build_apartment_description_id == new_build_apartment_description_id
    ).first()
    
    if file:
        return file.file_path
    return None


async def upload_file_construction_monitoring(db: Session, files: List[UploadFile], new_build_apartment_id: int, position: int, date: str, namber_build_andsection: str):
    uploaded_files = []
    for file in files:
        file_location = f"./uploads/construction_monitoring/{file.filename}"

        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())

        file_db = schemas.File_construction_monitoring_create(
            filename=file.filename,
            content_type=file.content_type,
            file_path=file_location,
            position=position,
            date=date,
            namber_build_andsection=namber_build_andsection,
            new_build_apartment_id=new_build_apartment_id
        )

        db_file = models.File_new_build_apartment_construction_monitoring(**file_db.dict())
        db.add(db_file)
        db.commit()
        db.refresh(db_file)

        uploaded_file = schemas.File_construction_monitoring(
            id=db_file.id,
            file_url=file_location,
            content_type=db_file.content_type,
            position=db_file.position,
            date=db_file.date,
            namber_build_andsection=db_file.namber_build_andsection,
            new_build_apartment_id=db_file.new_build_apartment_id
        )
        uploaded_files.append(uploaded_file)

    return schemas.File_construction_monitorings(files=uploaded_files)


def get_images_by_new_build_apartment_id(db: Session, new_build_apartment_id: int):
    files = db.query(models.File_new_build_apartment_construction_monitoring).filter(
        models.File_new_build_apartment_construction_monitoring.new_build_apartment_id == new_build_apartment_id
    ).all()
    
    return files

async def upload_files(db: Session, files: List[UploadFile], position: int, new_build_apartment_id: int):
    uploaded_files = []
    for file in files:
        file_location = f"./uploads/main_page/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        
        file_db = schemas.FileCreate(
            filename=file.filename,
            content_type=file.content_type,
            file_path=file_location,
            position = position,
            new_build_apartment_id = new_build_apartment_id
        )
        
        db_file = models.File_new_build_apartment(**file_db.dict())
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        
        uploaded_file = schemas.File(
            id = db_file.id,
            file_url=file_location,
            content_type=file.content_type,
            position = db_file.position

        )
        uploaded_files.append(uploaded_file)
    
    return schemas.Files(files=uploaded_files)








async def upload_file_monitoring_360(db: Session, files: List[UploadFile], date: str, new_build_apartment_id: int):
    uploaded_files = []   
    for file in files:
        file_location = f"./uploads/monitoring_360/{file.filename}"

        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        
        file_db = schemas.File_new_build_apartment_aerial_survey_360_create(
            filename=file.filename,
            content_type=file.content_type,
            file_path=file_location,
            date=date,
            new_build_apartment_id=new_build_apartment_id  # Ensure this is added and correct
        )
        
        db_file = models.File_new_build_apartment_aerial_survey_360(**file_db.dict())
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        
        uploaded_file = schemas.File_new_build_apartment_aerial_survey_360(
            id=db_file.id,
            file_url=file_location,
            content_type=db_file.content_type,
            date=db_file.date,
            file_path=file_location
        )
        uploaded_files.append(uploaded_file)
    
    return schemas.File_new_build_apartment_aerial_survey_360s(files=uploaded_files)

async def upload_3d_model(db: Session, files: List[UploadFile], new_build_apartment_id: int):
    uploaded_files = []
    for  file in files:
        file_location = f"./uploads/3d_model/{file.filename}"

        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        
        file_db = schemas.User_3D_File_model_create(
            filename=file.filename,
            content_type=file.content_type,
            file_path=file_location,
            new_build_apartment_id = new_build_apartment_id
        )
        
        db_file = models.User_3D_File_model(**file_db.dict())
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        
        uploaded_file = schemas.User_3D_File_model(
            file_url=file_location,
            content_type=file.content_type,
            id = db_file.id

        )
        uploaded_files.append(uploaded_file)
    
    return schemas.User_3D_File_models(files=uploaded_files)

def get_3d_models(db: Session, new_build_apartment_id: int):
    files = db.query(models.User_3D_File_model).filter(
        models.User_3D_File_model.new_build_apartment_id == new_build_apartment_id
    ).all()
    return files



def get_image_path_by_position_and_id_monitoring_monitoring_360(db: Session, new_build_apartment_id: int):
    files = db.query(models.File_new_build_apartment_aerial_survey_360).filter(
        models.File_new_build_apartment_aerial_survey_360.new_build_apartment_id == new_build_apartment_id
    ).all()
    return files
