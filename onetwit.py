import json
import os
from dotenv import load_dotenv, find_dotenv
import requests

# r=requests.get('https://twitter.com/elonmusk/status/1555442024127537153')
load_dotenv(find_dotenv())
BearerToken = os.getenv('BEARER_TOKEN')


def create_url():
    ids = "ids=1555442024127537153"
    return f"https://api.twitter.com/2/tweets?{ids}"


def bearer_oauth(r):

    r.headers["Authorization"] = f"Bearer {BearerToken}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):  # sourcery skip: raise-specific-error
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
