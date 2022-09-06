from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json

bearer_token = os.environ.get("Bearer_tokken")

def create_url(following_user_id):
    user_id = following_user_id
    return f"https://api.twitter.com/2/users/{user_id}/following"


def get_params():
    return {"user.fields": "created_at"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FollowingLookupPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    following_user_id = os.environ.get("my_id")
    url = create_url(following_user_id)
    params = get_params()   
    json_response = connect_to_endpoint(url, params)
    following_list = len(json_response["data"])
    empty_list = []
    for following_id in range(following_list):
        empty_list.append(json_response["data"][following_id]["id"])
        
    return empty_list


if __name__ == "__main__":
    main_return = main()
    print(main_return)