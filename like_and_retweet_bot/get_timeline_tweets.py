from dotenv import load_dotenv
load_dotenv()
from requests_oauthlib import OAuth1Session
import requests
import os
import json 
import follow_back_module
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
#     print(json.dumps(json_response, indent=4, sort_keys=True))
    return json_response
def main():
    a = follow_back_module.oauth_credential()
    url = "https://api.twitter.com/2/users/{}/timelines/reverse_chronological"
    payload = {'target_user_id':a["my_id"]}
    json_response = get_response(url,payload,a)
    return json_response

if __name__=="__main__":
    c = main()
    print(c)

