from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json  

Bearer_tokken = os.getenv("Bearer_tokken")


def create_url(client_user_id ):
    user_id = client_user_id
    return f"https://api.twitter.com/2/users/{user_id}/followers"

def get_params():
    return {"user.fields":"created_at,location,description"}

def bearer_Oauth(r):
    r.headers["Authorization"] = f"Bearer {Bearer_tokken}"
    r.headers["User-Agent"] = "v2followersLookupPython"
    return r

def connect_to_endpoint(url,params):
    response = requests.request("GET", url,auth=bearer_Oauth,params=params)
    if response.status_code!=200:
        raise Exception(f"Request returned an error: {response.status_code},{response.text}")
    return response.json()

def main():
    client_user_id = os.environ.get("my_id")
    url = create_url(client_user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    records = len(json_response["data"])
    id_list = [] 
    for record in range(records):
        all_followers_id = json_response["data"][record]["id"]
        id_list.append(all_followers_id)
    return id_list
    
if __name__=="__main__":
    main_data = main()
    print(main_data)

