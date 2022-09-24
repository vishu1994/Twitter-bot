#!/usr/bin/env python
# coding: utf-8

# In[15]:


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
    all_tweets = utility.connect_to_endpoint_get(url,params,headers)
    show_tweet(all_tweets)
    return all_tweets  
    
def show_tweet(json_response):
      print(json.dumps(json_response, indent=4, sort_keys=True))
        
if __name__=="__main__":
    tweets_in_user_mentioned = main()

