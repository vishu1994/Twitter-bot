#!/usr/bin/env python
# coding: utf-8

# In[7]:


from dotenv import load_dotenv
load_dotenv()
import os
import json
import utility
import pymongo
def main():
    bearer_tokken=utility.get_bearer_tokken()
    keys = utility.oauth_credential()
    end_point_url= "https://api.twitter.com/2/users/{}/mentions"
    url = utility.create_url(keys["my_id"],end_point_url)
    parameter = "tweet.fields"
    value = "created_at" 
    params = utility.get_params(parameter,value)
    headers = utility.headers(bearer_tokken)
    endpoint_response = utility.connect_to_endpoint_get(url,params,headers)
    return endpoint_response  
    
def show_tweet(json_response):
      print(json.dumps(json_response, indent=4, sort_keys=True))

def tweet_ids(json_response):  
    id_list = []
    for tweet_id in range(len(json_response["data"])):  
        id_list.append(json_response["data"][tweet_id]["id"])
    return id_list
if __name__=="__main__":
    endpoint_response = main()
    endpoint_response

