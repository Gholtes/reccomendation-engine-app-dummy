from typing import List, Optional, Any, Dict, AnyStr, Union
from pydantic import BaseModel

#Define Request Schemas
class productRequest(BaseModel):
	'''Defines a train request'''
	product_id: str
	recommendation_count: Optional[int] = 10
	user_id: Optional[str] = None
	location_id: Optional[str] = None

class userRequest(BaseModel):
	user_id: str
	recommendation_count: Optional[int] = 10
	product_category_id: Optional[str] = None
	location_id: Optional[str] = None

class reviewRequest(BaseModel):
	'''Defines a review datapoint'''
	user: str
	item: str
	rating: Optional[int] = 0

class transactionRequest(BaseModel):
	'''Defines a transaction basket datapoint'''
	basket: List[str] #list of product ids 
	user_id: Optional[str] = None

#Define Response Schemas