# sourcery skip: raise-specific-error
import json
import os
from dotenv import load_dotenv, find_dotenv
from requests_oauthlib import OAuth1Session


load_dotenv(find_dotenv())
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')

payload = {"text": "This why I am here!"}

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(
            response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
