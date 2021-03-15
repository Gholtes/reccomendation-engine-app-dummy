'''
--------------------------------------------------
File: app.py
--------------------------------------------------
Author: Deloitte Australia 2021

Description: Defines the application that will provide the API for the recommendation engines

Endpoints:
#TODO

Run with 
	$ uvicorn src.app:app --reload --host 0.0.0.0 --port 5000
Or build and run with
	$ export DOCKER_BUILDKIT=0
	$ docker image build -t recommendation-engine-app .
	$ docker run -p 5000:5000 --name re-app -d recommendation-engine-app
--------------------------------------------------
Edit History:

#  | NAME				|  DATE       	| DESC
0  | Grant Holtes       |  11/2/21		| Initial Creation 
--------------------------------------------------
'''
#FastAPI imports
from fastapi import FastAPI, Response, status, Form
from fastapi.responses import HTMLResponse
import traceback
#model and data pipeline imports
import numpy as np
import json
import os
import csv

#Reqest and Response Schemas
from src.schemas import *

#Config HTTP error codes
bad_input_code = 400
out_of_order_code = 400
general_app_error_code = 500

#Initialise key services
app = FastAPI()

@app.get('/')
async def home():
	return {"app":"recommendation Engine API"}

@app.get('/health/', status_code = 204)
async def health():
	print("Health check")

#Core end-points
@app.post('/product/', status_code=200)
def add(request: productRequest, response: Response):
	product_id = request.product_id
	user_id = request.user_id
	location_id = request.location_id
	if location_id:
		message = "Low stock, shipping times may vary"
	else:
		message = None
	recommendations = {i:"P00"+str(i) for i in range(request.recommendation_count)}
	return {product_id, user_id, location_id, message, recommendations}
	
@app.post('/user/', status_code=200)
def add(request: userRequest, response: Response):
	product_category_id = request.product_category_id
	user_id = request.user_id
	location_id = request.location_id
	if location_id or product_category_id:
		message = "Low stock, shipping times may vary"
	else:
		message = None
	recommendations = {i:"P00"+str(i) for i in range(request.recommendation_count)}
	return {product_category_id, user_id, location_id, message, recommendations}

@app.post('/add_review/', status_code=200)
def add(request: reviewRequest, response: Response):
	return {"Status": "Success"}

@app.post('/add_transaction/', status_code=200)
def add(request: transactionRequest, response: Response):
	return {"Status": "Success"}

