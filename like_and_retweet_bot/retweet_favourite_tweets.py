#!/usr/bin/env python
# coding: utf-8

# In[20]:


from dotenv import load_dotenv
load_dotenv()
from requests_oauthlib import OAuth1Session
import requests
import os
import json 
import filter_tweets
import follow_back_module
def get_response(url,payload,a):
    oauth = OAuth1Session(
                    a["consumer_key"],
                    client_secret=a["consumer_secret"],
                    resource_owner_key=a["access_token"],
                    resource_owner_secret=a["access_token_secret"],
                )
    response = oauth.post(url.format(a["my_id"]),json=payload)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    
def main():
    user_data = follow_back_module.oauth_credential()
    url = "https://api.twitter.com/2/users/{}/retweets"
    favourite_tweet_id = filter_tweets.main()
    for tweet_id in favourite_tweet_id:
        payload = {"tweet_id":tweet_id}
        c =get_response(url,payload,user_data)

if __name__=="__main__":
    main()
        

