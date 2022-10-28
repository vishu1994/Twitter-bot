#!/usr/bin/env python
# coding: utf-8

# In[20]:


from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json
from requests_oauthlib import OAuth1Session
import pymongo

        
def get_bearer_tokken():
    bearer_tokken = os.environ.get("Bearer_tokken")
    return bearer_tokken

def oauth_credential():
    my_dict = {"consumer_key":os.environ.get("API_KEY"),
               "consumer_secret":os.environ.get("API_KEY_SECRET"),
               "access_token":os.environ.get("Access_tokken"),
               "access_token_secret":os.environ.get("Access_tokken_secret"),
               "my_id":os.environ.get("my_id"),
               "bearer_tokken":os.environ.get("Bearer_tokken")
               }
    return my_dict

def create_url(my_id,end_point):
    user_id = my_id
    return end_point.format(user_id)


def get_params(parameter,value):
    return {parameter:value}

def headers(bearer_token):
    headers = {}
    headers["Authorization"] = f"Bearer {bearer_token}"
    headers["User-Agent"] = "v2UserMentionsPython"
    return headers

def search_tweet_records_in_db(json_response):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Twitter_bot"]
    collection = db["twitter tweets"]
    help_support_tweets = []
    for tweet_ids in json_response["data"]:
        search_id = {"id":tweet_ids["id"]}
        get_id = collection.find_one(search_id)
        if get_id==None:
            help_support_tweets.append(tweet_ids)
            tweets_record_insert(tweet_ids)
        else:
            pass
    return help_support_tweets

def tweets_record_insert(json_response):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Twitter_bot"]
    collection = db["twitter tweets"]
    collection.insert_one(json_response)   
    
def connect_to_endpoint_get(url,params,headers):
    response = requests.get(url,headers=headers,params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def connect_to_endpoint_post(url,params,headers):
    response = requests.post(url,headers=headers,params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()



def get_response(url,payload,user_data):
    oauth = OAuth1Session(
                    user_data["consumer_key"],
                    client_secret=user_data["consumer_secret"],
                    resource_owner_key=user_data["access_token"],
                    resource_owner_secret=user_data["access_token_secret"],
                )
    response = oauth.get(url.format(user_data["my_id"]),json=payload)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    print("Response code: {}".format(response.status_code))
    json_response = response.json()


def post_response(url,payload,user_data):
    oauth = OAuth1Session(
                    user_data["consumer_key"],
                    client_secret=user_data["consumer_secret"],
                    resource_owner_key=user_data["access_token"],
                    resource_owner_secret=user_data["access_token_secret"],
                )
    response = oauth.post(url.format(user_data["my_id"]),json=payload)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    return json_response


# In[ ]:




