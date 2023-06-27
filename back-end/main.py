from typing import Union

from fastapi import FastAPI, UploadFile, File
import os
from PIL import Image
import numpy as np

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this list with the appropriate origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# async def upload_image(file: UploadFile):
@app.post("/upload")
async def upload_image(file: UploadFile, upload_folder: str = "./image"):
    # Get the file extension
    file_ext = os.path.splitext(file.filename)[1].lower()


    # Check if the file extension is a valid image format
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    if file_ext not in valid_extensions:
        return {"error": "Invalid file format. Please upload an image."}

    # Create a file path with the correct extension
    file_path = f"{upload_folder}/{file.filename}"
    # file_path_with_ext = file_path + file_ext
    file_path_with_ext = file_path
    print(f"jjjjjjjjjjjjjjjjjjj{file_path_with_ext}")

    # Save the uploaded file with the correct extension
    with open(file_path_with_ext, "wb") as buffer:
        buffer.write(await file.read())
    # image path
    image = Image.open(f"{upload_folder}/{file.filename}")
    image = image.convert("RGB")
    rgb_array = np.array(image)
    print(f"array: {rgb_array}")

    # TODO


    return {"label": "file_path",
            "caries": "file_path",
            "non_caries": "file_path",
            "f_caries": "f_caries"}