# Image
FROM python:3.8.6-buster

COPY api_folder /api_folder
COPY requirements.txt /requirements.txt
COPY prediction /prediction

# RUN allows you to run terminal commands when your image gets created
# Here, we upgrade pip and install the libraries in our requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# local
#CMD uvicorn api_folder.api:api --host 0.0.0.0

# deploy to gcp
CMD uvicorn api_folder.api:api --host 0.0.0.0 --port $PORT