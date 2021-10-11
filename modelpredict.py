from fastai.vision import *
from urllib.request import urlretrieve


class ModelPredict():
 def __init__(self, filename):
  self.filename = filename


def download_model(self):
  if path.exists('export.pkl') == False:
   url = 'https://drive.google.com/file/d/1-CniOQ28yX4w7fa0wPahE1hnOqUQp5UO/view?usp=download'
   filename = 'export.pkl'
   urlretrieve(url,filename)


def predict(self):
  self.download_model()
  learn = load_learner('')
  print(learn)
  img = open_image(self.filename)
  pred_class , pred_idx, outputs = learn.predict(img)
  return str(pred_class)
