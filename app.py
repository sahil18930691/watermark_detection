from fastapi import FastAPI, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from modelpredict import ModelPredict
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return "Hello World!!!"


'''
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {
        'request': request,
    })'''


@app.post("/predict/")
async def create_upload_files(request: Request,file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename
    with open(filename, 'wb') as f:
        f.write(contents)
    m = ModelPredict(filename).predict()
    return templates.TemplateResponse("predict.html", {
            "request": request,
            "filename": file.filename,
            "Predict": m
        })