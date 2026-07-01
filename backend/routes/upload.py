from fastapi import APIRouter, UploadFile, File
import shutil #it copies the uploaded file from memory to disk
import os

from utils import extract_text, create_vector_store

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    create_vector_store(text)

    return {
        "message": "Resume uploaded successfully!"
    }