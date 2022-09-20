#!/usr/bin/env python
# coding: utf-8

# In[7]:


from dotenv import load_dotenv
load_dotenv()
from requests_oauthlib import OAuth1Session
import requests
import os
import json 
import utility
import tweets_in_user_mentioned
def get_response(url,payload,user_credential):
    oauth = OAuth1Session(
                    user_credential["consumer_key"],
                    client_secret=user_credential["consumer_secret"],
                    resource_owner_key=user_credential["access_token"],
                    resource_owner_secret=user_credential["access_token_secret"],
                )
    response = oauth.post(url,json=payload)
    if response.status_code != 201:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    print("Response code: {}".format(response.status_code))
    json_response = response.json()

def main():
    user_credential = utility.oauth_credential()
    url = "https://api.twitter.com/2/tweets"
    user_mentioned_tweets = tweets_in_user_mentioned.main()
    get_tweet_text_record = utility.search_tweet_records_in_db(user_mentioned_tweets)
    for tweet_texts in get_tweet_text_record:
        tweet_texts_in_lowercase = tweet_texts["text"].lower()
        if "help" in tweet_texts_in_lowercase:
            payload = {"text": "I will get back to you on this", "reply": {"in_reply_to_tweet_id": tweet_texts["id"]}}  
            get_response(url,payload,user_credential)
        elif "support" in tweet_texts_in_lowercase:
            payload = {"text": "Reach me via dm", "reply": {"in_reply_to_tweet_id": tweet_texts["id"]}}
            get_response(url,payload,user_credential)
        else:
            payload = {"text": "thankyou i will see it ASAP", "reply": {"in_reply_to_tweet_id": tweet_texts["id"]}}
            get_response(url,payload,user_credential)
            
    return ""

if __name__=="__main__":
    main()

