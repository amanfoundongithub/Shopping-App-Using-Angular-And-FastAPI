from fastapi import File, UploadFile, status, APIRouter
from fastapi.responses import JSONResponse
from firebase_admin import storage
import os

import firebase_admin
from firebase_admin import credentials

# Firebase configuration
firebase_config = {}


# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    "storageBucket": ""
})

image_router = APIRouter()

@image_router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save file to a temporary location
    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as f:
        f.write(await file.read())

    # Upload file to Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(file.filename)
    blob.upload_from_filename(temp_file_path)

    # Make file publicly accessible
    blob.make_public()

    # Remove temporary file
    os.remove(temp_file_path)

    content = {
        "url": blob.public_url
    }
    
    return JSONResponse(content = content, status_code = status.HTTP_201_CREATED)
