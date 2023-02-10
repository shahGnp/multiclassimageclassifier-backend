from fastapi import FastAPI, UploadFile, File
import shutil
import os
import loadandpredict as loadandpredict
from pydantic import BaseModel
import createImage

class req(BaseModel):
    imgstr: str

app=FastAPI()

# @app.post("/")
# async def root(file: UploadFile = File(...)):
#     with open(f'{file.filename}',"wb")as buffer:
#         try:
#             os.mkdir('./uploadedImages/')
#         except:
#             pass
#         shutil.copyfileobj(file.file,buffer)
#         shutil.move(file.filename,"./uploadedImages")
#         print('Image was uploaded: ',file.filename)
#         prediction=loadandpredict.predict()
#         print(prediction)
#         shutil.rmtree('./uploadedImages')
#     return {"class":prediction}

@app.post("/predict/")
async def root(req: req):
        try:
            os.mkdir('./uploadedImages/')
        except:
            pass
        
        createImage.imageGenerator(req.imgstr)
        prediction=loadandpredict.predict()
        print(prediction)
        shutil.rmtree('./uploadedImages')
        return {"class":prediction}
