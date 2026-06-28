from fastapi import APIRouter, UploadFile, File
import shutil
import os

import utils
from ats import analyze_resume

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/ats")
async def ats(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    jd_text = utils.extract_text(file_path)

    result = analyze_resume(
        utils.resume_text,
        jd_text
    )

    return result