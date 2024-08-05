from typing import Optional, List
from pydantic import BaseModel


class File_new_build_apartment_ItemCreate_about(BaseModel):
    file_url: str
    content_type: str


class File_new_build_apartment_ItemCreate_abouts(BaseModel):
    files: List[File_new_build_apartment_ItemCreate_about]
    
class File_new_build_apartment_ItemCreate_about_create(BaseModel):
    file_url: str
    content_type: str



class File_construction_monitoring(BaseModel):
    id: int
    file_url: str
    content_type: str
    position: int
    date: str
    namber_build_andsection: str
    new_build_apartment_id: int

class File_construction_monitorings(BaseModel):
    files: List[File_construction_monitoring]

class File_construction_monitoring_create(BaseModel):
    filename: str
    content_type: str
    file_path: str
    position: int
    date: str
    namber_build_andsection: str
    new_build_apartment_id: int


class File_new_build_apartment_aerial_survey_360(BaseModel):
    id: int
    file_url: str
    content_type: str
    date: str
    file_path: str


class File_new_build_apartment_aerial_survey_360s(BaseModel):
    files: List[File_new_build_apartment_aerial_survey_360]

class File_new_build_apartment_aerial_survey_360_create(BaseModel):
    filename: str
    content_type: str
    file_path: str
    date: str
    new_build_apartment_id: int  # Add this field

class UserCreate_File(BaseModel):
    id: int
    file_url: str
    content_type: str
    position: int

class UserCreate_Files(BaseModel):
    files: List[UserCreate_File]

class UserCreate_File_Create(BaseModel):
    filename: str
    content_type: str
    file_path: str
    position: int  
    owner_id: int  


class File(BaseModel):
    id: int
    file_url: str
    content_type: str
    position: int


class Files(BaseModel):
    files: List[File]

class FileCreate(BaseModel):
    filename: str
    content_type: str
    file_path: str
    position: int
    new_build_apartment_id: int



class File_description(BaseModel):
    id: int
    file_url: str
    content_type: str


class File_descriptions(BaseModel):
    files: List[File_description]

class File_descriptionCreate(BaseModel):
    filename: str
    content_type: str
    file_path: str    
    new_build_apartment_description_id: int


class User_3D_File_model(BaseModel):
    id: int
    file_url: str
    content_type: str
    class Config:
        orm_mode = True

class User_3D_File_models(BaseModel):
    files: List[File_description]

class User_3D_File_model_create(BaseModel):
    filename: str
    content_type: str
    file_path: str    
    new_build_apartment_id: int