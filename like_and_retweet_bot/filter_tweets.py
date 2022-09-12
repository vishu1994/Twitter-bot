#!/usr/bin/env python
# coding: utf-8

# In[2]:


from dotenv import load_dotenv
load_dotenv()
from requests_oauthlib import OAuth1Session
import requests
import os
import json 
import get_timeline_tweets
all_tweets = get_timeline_tweets.main()
def main():
    filter_list =["python","coding","Technology","india","stars","isro","NASA"]
    id_for_retweet = []
    for item in range(len(filter_list)):
        for tweet_number in range(len(all_tweets["data"])):
            if filter_list[item] in all_tweets["data"][tweet_number]["text"]:
                print(all_tweets["data"][tweet_number]["text"])
                id_for_retweet.append(all_tweets["data"][tweet_number]["id"])
                print("*"*100)
            else:
                continue 
    return id_for_retweet

if __name__=="__main__":
    c = main()
    print(c)


# In[ ]:




