# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# reference https://www.cnblogs.com/poloyy/p/15312290.html
# https://fastapi.tiangolo.com/tutorial/body-fields/
# 框架比较：https://blog.csdn.net/weixin_46364913/article/details/124007850

from typing import List, Union
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/file")
async def create_files(file: bytes = File(...)):
    return {"file_sizes": len(file)}

@app.post("/uploadfile")
async def create_upload_files(file: UploadFile = File(...)):
    result = {
        "filename": file.filename,
        "content-type": file.content_type,
        "read": await file.read()
    }
    return result


#测试程序是否启动
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True, debug=True)