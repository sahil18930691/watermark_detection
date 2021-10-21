#import fastbook
#fastbook.setup_book()
from fastbook import *
#from fastai.vision.widgets import *
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
#import uvicorn

#import pathlib

#import cv2
#import urllib
#import numpy as np
#import urllib.request as ur
#import json
#from urllib.request import urlopen



'''
#for windows
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = FastAPI()

EXPORT_PATH = pathlib.Path("export.pkl")

learn_inf = load_learner(EXPORT_PATH)
'''



#for server

app = FastAPI()

from pathlib import Path

folder_path = Path('./export.pkl')

learn_inf = load_learner(folder_path)



@app.get("/")
async def root():
    return "Hello World!!!"
'''
@app.get("/predict_from_url")
def predict_from_url(image_url:str):
    ## read as HTTPResponse 
    resp = ur.urlopen(image_url)
    ## read as 1D bytearray
    resp_byte_array = resp.read()
    
    ## returns a bytearray object which is a mutable sequence of integers in the range 0 <=x< 256
    mutable_byte_array = bytearray(resp_byte_array)
    ## read as unsigned integer 1D numpy array
    image = np.asarray(mutable_byte_array, dtype="uint8")
    #image1 = cv2.resize(image, (256, 256))
    ## To decode the 1D image array into a 2D format with RGB color components we make a call to cv2.imdecode
    image1 = cv2.imdecode(image, cv2.IMREAD_COLOR)
    arr1 = cv2.resize(image1, (256, 256))
    gg = learn_inf.predict(arr1)
    diction={"Result":str(gg[0])}
    ghg1=json.dumps(diction)
    data1 = json.loads(ghg1.replace("\'", '"'))
    return(data1)'''

@app.get("/predict_from_url")
def predict_from_url(image_url:str):
    response = requests.get(image_url)
    img = PILImage.create(response.content)
    img_resize=img.resize((256,256))
    timg = TensorImage(image2tensor(img_resize))
    tpil = PILImage.create(timg)
    predictions = learn_inf.predict(tpil)
    predict_dict={"Result":str(predictions[0]),"image_url":image_url}
    predict_json=json.dumps(predict_dict)
    result = json.loads(predict_json.replace("\'", '"'))
    return result   


#predictions = learn_inf.predict(download_url("https://sqy.s3-ap-southeast-1.amazonaws.com/secondaryPortal/637654244036079570-2408210553235323"))
#print(predictions)

@app.get("/predict_url")
def download_url1(image_url:str):
    #img = ' "%s" ' % image_url.strip()
    predictions = learn_inf.predict(download_url(image_url))
    predict_dict={"Result":str(predictions[0]),"image_url":image_url}
    predict_json=json.dumps(predict_dict)
    result = json.loads(predict_json.replace("\'", '"'))
    return result 


'''
async def predict_image(image_url: str):
 
    req = ur.urlopen(image_url)
    #print(req)
    
    
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    arr1 = cv2.resize(arr, (256, 256))
    #print(arr)

    #img = cv2.imdecode(arr1, -1) # 'Load it as it is'
    #print(img)


    gg = learn_inf.predict(arr)
    
    diction={"Result":str(gg[0])}
    ghg1=json.dumps(diction)
    data1 = json.loads(ghg1.replace("\'", '"'))
    return(data1)'''
    

'''    
req = ur.urlopen('https://s3-ap-southeast-1.amazonaws.com/sqy/secondaryPortal/637503833988329299-0303210349584958.jpg')

arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) # 'Load it as it is'



gg = learn_inf.predict(img)
print(gg)

#learn_inf = load_learner('.\\export.pkl')'''
