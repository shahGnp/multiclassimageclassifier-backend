from fastapi import FastAPI, UploadFile, File
import shutil
import os
import app.loadandpredict as loadandpredict

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
        prediction=loadandpredict.predict()
        print(prediction)
        shutil.rmtree('./uploadedImages')
    return {"class":prediction}