from fastapi import APIRouter
from typing import List, Union
from fastapi import File, UploadFile
from typing import Optional

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.post("/file")
async def create_files(file: bytes = File(...)):
    return {"file_sizes": len(file)}

@router.post("/uploadfile")
async def create_upload_files(file: UploadFile = File(...)):
    result = {
        "filename": file.filename,
        "content-type": file.content_type,
        "read": await file.read()
    }
    return result

#测试程序是否启动
@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}