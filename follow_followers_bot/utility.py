#!/usr/bin/env python
# coding: utf-8

# In[76]:


from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json
from requests_oauthlib import OAuth1Session

def get_bearer_tokken():
    bearer_tokken = os.environ.get("Bearer_tokken")
    return bearer_tokken

def oauth_credential():
    my_dict = {"consumer_key":os.environ.get("API_KEY"),
               "consumer_secret":os.environ.get("API_KEY_SECRET"),
               "access_token":os.environ.get("Access_tokken"),
               "access_token_secret":os.environ.get("Access_tokken_secret"),
               "my_id":os.environ.get("my_id")
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
    
def connect_to_endpoint(url,params,headers):
    response = requests.get(url,headers=headers,params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_response(url,payload,a):
    oauth = OAuth1Session(
                    a["consumer_key"],
                    client_secret=a["consumer_secret"],
                    resource_owner_key=a["access_token"],
                    resource_owner_secret=a["access_token_secret"],
                )
    response = oauth.get(url.format(a["my_id"]),json=payload)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    return json_response


# In[ ]:




