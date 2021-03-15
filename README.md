# Recommendation Engines
A collection of Recommendation Engines and a simple API for deployment

Feb 2021

Written in Python using ```FastAPI```, ```Numpy```, ```Tensorflow```.

## Usage

#### With Docker...
```
$ export DOCKER_BUILDKIT=0
$ docker image build -t reccomendation-engine-app-dummy .
$ docker run -p 5000:5000 --name re-app -d reccomendation-engine-app-dummy
```

The app will be live on http://localhost:5000

#### ...or without Docker
Run the API with uvicorn:
```
$ uvicorn src.app:app --reload --host 0.0.0.0 --port 5000
```

## Install

If not using docker, install the required packages:
```
pip3 install requirements.txt
```