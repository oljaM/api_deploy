from fastapi import FastAPI, UploadFile, File
import uvicorn
from prediction.prediction import read_imagefile, predict

api = FastAPI()

#root '/' endpoint
@api.get("/")
def root():
    return {"ok": "API connected"}

@api.post('/predict')
async def predict_image(file: UploadFile = File(...)):
    #Read the file uploaded by the user
    image = read_imagefile(await file.read())
    #Make prediction
    prediction = predict(image)

    return prediction

if __name__ == "__main__":
    uvicorn.run(api, port=8080, host='0.0.0.0')
