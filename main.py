from fastapi import FastAPI, UploadFile, File
import shutil
import os
import loadandpredict

app=FastAPI()

@app.post("/")
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}',"wb")as buffer:
        try:
            os.mkdir('./uploadedImages/')
        except:
            pass
        shutil.copyfileobj(file.file,buffer)
        shutil.move(file.filename,"./uploadedImages")
        print('Image was uploaded: ',file.filename)
        print(loadandpredict.predict())
        shutil.rmtree('./uploadedImages')
    return {"class":file.filename}