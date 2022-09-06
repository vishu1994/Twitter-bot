#!/usr/bin/env python
# coding: utf-8

# In[26]:


#OAuth 1.0a 
from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json  

consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("Access_tokken")
access_token_secret = os.environ.get("Access_tokken_secret")
id = os.environ.get("my_id")
for to_follow in not_followed_followers.main():
    if to_follow!=id:
        payload = {'target_user_id': f'{to_follow}'}

    # Make the request
        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

    # Making the request
        response = oauth.post(
            "https://api.twitter.com/2/users/{}/following".format(id), json=payload)

        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )

        print("Response code: {}".format(response.status_code))

        json_response = response.json()
        print(json.dumps(json_response, indent=4, sort_keys=True))
    else:
        print("No unfollowed followers")


# In[ ]:




