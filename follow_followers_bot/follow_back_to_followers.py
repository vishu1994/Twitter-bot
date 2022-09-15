#!/usr/bin/env python
# coding: utf-8

# In[5]:


#OAuth 1.0a 
from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json 
import not_followed_followers
import utility
from requests_oauthlib import OAuth1Session
    
def get_response(url,payload,user_data):
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
    print(json.dumps(json_response, indent=4, sort_keys=True))
    
def follow_back(url,user_data):
    if not_followed_followers.main():
        for to_follow in not_followed_followers.main():
            if to_follow!=id:
                payload = {'target_user_id': f'{to_follow}'}
                # Making the request
                get_response(url,payload,user_data)
            else:
                print("you can't follow yourself")
    else:
        print("No one is remain for follow back")

    
def main():
    user_data = utility.oauth_credential()
    url = "https://api.twitter.com/2/users/{}/following"
    follow_back(url,user_data)

if __name__=="__main__":
    main()



