import base64
import shutil

def imageGenerator(imgstr):
    try:
        imgdata = base64.b64decode(imgstr)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
        shutil.move('some_image.jpg','./uploadedImages')
        print('Image created successfully')
    except:
        print("Error in string to image conversion")