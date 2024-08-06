from fastapi import Depends, APIRouter, Form, HTTPException, File, Query, UploadFile, logger
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import Annotated, List, Optional
import crud, schemas, models
from database import SessionLocal, engine
import shutil
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/upload_file_about/{user_id}", response_model=schemas.File_new_build_apartment_ItemCreate_abouts)
async def upload_multiple_files_compan(
    user_id: int,
    files: List[UploadFile],
    db: Session = Depends(get_db)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    uploaded_files = await crud.upload_file_about(db, files, user_id)
    return uploaded_files

@router.get("/get_image_about/{item_create_about_id}")
async def get_image_owner( item_create_about_id: int, db: Session = Depends(get_db)):
    file_path = crud.get_image_item_path_by_position_and_id(db, item_create_about_id)
    if not file_path:
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type='image/jpeg') 


@router.post("/upload_file_compan/{item_id}", response_model=schemas.UserCreate_Files)
async def upload_multiple_files_compan(
    item_id: int,
    position: int,
    files: List[UploadFile],
    db: Session = Depends(get_db)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    uploaded_files = await crud.usercreate_file(db, files, item_id, position)
    return uploaded_files

@router.get("/get_image_owner/{position}/{owner_id}")
async def get_image_owner(position: int, owner_id: int, db: Session = Depends(get_db)):
    file_path = crud.get_image_path_by_position_and_id_owner(db, position, owner_id)
    if not file_path:
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type='video/mp4') 


@router.post("/upload/{new_build_apartment_id}", response_model=schemas.Files)
async def upload_multiple_files(
    new_build_apartment_id: int,
    files: List[UploadFile],
    position: int,
    db: Session = Depends(get_db)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    uploaded_files = await crud.upload_files(db, files, position, new_build_apartment_id)
    return uploaded_files

@router.get("/get_image/{position}/{new_build_apartment_id}")
async def get_image(position: int, new_build_apartment_id: int, db: Session = Depends(get_db)):
    file_path = crud.get_image_path_by_position_and_id(db, position, new_build_apartment_id)
    if not file_path:
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type='video/mp4') 



@router.post("/upload_description/{new_build_apartment_description_id}", response_model=schemas.File_descriptions)
async def upload_multiple_files_deckription(
    new_build_apartment_description_id: int,
    files: List[UploadFile],
    db: Session = Depends(get_db)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    uploaded_files = await crud.upload_files_plan(db, files, new_build_apartment_description_id)
    return uploaded_files


@router.get("/get_image_description/{new_build_apartment_description_id}")
async def get_image_description(new_build_apartment_description_id: int, db: Session = Depends(get_db)):
    file_path = crud.get_image_path_by_id_description(db, new_build_apartment_description_id)
    if not file_path:
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type='image/jpeg')







@router.post("/upload_monitoring/{new_build_apartment_id}", response_model=schemas.File_construction_monitorings)
async def upload_multiple_files_monitoring(
    new_build_apartment_id: int,
    files: List[UploadFile] = File(...),
    position: int = Form(...),
    date: str = Form(...),
    namber_build_andsection: str = Form(...),
    db: Session = Depends(get_db)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    uploaded_files = await crud.upload_file_construction_monitoring(db, files, new_build_apartment_id, position, date, namber_build_andsection)
    return uploaded_files


@router.get("/get_images_metadata/{new_build_apartment_id}", response_model=schemas.File_construction_monitorings)
async def get_images_metadata(new_build_apartment_id: int, db: Session = Depends(get_db)):
    files = crud.get_images_by_new_build_apartment_id(db, new_build_apartment_id)
    
    if not files:
        raise HTTPException(status_code=404, detail="Files not found")


    metadata_list = [
        schemas.File_construction_monitoring(
            id=file.id,
            file_url=f"/get_image_monitoring/{file.id}",
            content_type=file.content_type,
            position=file.position,
            date=file.date,
            namber_build_andsection=file.namber_build_andsection,
            new_build_apartment_id=file.new_build_apartment_id
        ) for file in files
    ]
    
    return schemas.File_construction_monitorings(files=metadata_list)

@router.get("/get_image_monitoring/{file_id}")
async def get_image_monitoring(file_id: int, db: Session = Depends(get_db)):
    file = db.query(models.File_new_build_apartment_construction_monitoring).filter(
        models.File_new_build_apartment_construction_monitoring.id == file_id
    ).first()
    
    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    return StreamingResponse(open(file.file_path, "rb"), media_type=file.content_type)


@router.post("/upload_monitoring_360/{new_build_apartment_id}", response_model=schemas.File_new_build_apartment_aerial_survey_360s)
async def upload_multiple_files_monitoring_360(
    new_build_apartment_id: int,
    files: List[UploadFile] = File(...),
    date: str = Form(...),
    db: Session = Depends(get_db)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    uploaded_files = await crud.upload_file_monitoring_360(db, files, date, new_build_apartment_id)
    return uploaded_files



@router.get("/get_image_description_360_metadata/{new_build_apartment_description_id}", response_model=schemas.File_new_build_apartment_aerial_survey_360s)
async def get_images_metadata(new_build_apartment_description_id: int, db: Session = Depends(get_db)):
    files = crud.get_image_path_by_position_and_id_monitoring_monitoring_360(db, new_build_apartment_description_id)
    
    if not files:
        raise HTTPException(status_code=404, detail="Files not found")

    metadata_list = [
        schemas.File_new_build_apartment_aerial_survey_360(
            id=file.id,
            file_url=f"/get_image_description_360/{file.id}",
            content_type=file.content_type,
            date=file.date,
            file_path=file.file_path  # Add file_path to the initialization
        ) for file in files
    ]
    
    return schemas.File_new_build_apartment_aerial_survey_360s(files=metadata_list)

@router.get("/get_image_description_360/{file_id}")
async def get_image_monitoring_360(file_id : int, db: Session = Depends(get_db)):
    file = db.query(models.File_new_build_apartment_aerial_survey_360).filter(
        models.File_new_build_apartment_aerial_survey_360.id == file_id
    ).first()

    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    return StreamingResponse(open(file.file_path, "rb"), media_type=file.content_type)






@router.post("/3d_object/{new_build_apartment_id}", response_model=schemas.User_3D_File_models)
async def upload_3d_model(
    new_build_apartment_id: int,
    files: List[UploadFile],
    db: Session = Depends(get_db)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    uploaded_files = await crud.upload_3d_model(db, files, new_build_apartment_id)
    return uploaded_files


@router.get("/get_3d_object/{new_build_apartment_id}", response_model=schemas.User_3D_File_models)
async def get_3d_models(new_build_apartment_id: int, db: Session = Depends(get_db)):
    files = crud.get_3d_models(db, new_build_apartment_id)
    if not files:
        raise HTTPException(status_code=404, detail="Files not found")
    
    file_responses = []
    for file in files:
        file_response = schemas.User_3D_File_model(
            id=file.id,
            file_url=file.file_path,
            content_type=file.content_type
        )
        file_responses.append(file_response)
    
    return schemas.User_3D_File_models(files=file_responses)
