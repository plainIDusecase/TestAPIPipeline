import requests
import json

def get_token(clientId,clientSecret):
    #Get Token
    url = "https://api.eu1.plainid.io/api/1.0/api-key/token"
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": clientId,
        "client_secret": clientSecret
    }
    response = requests.post(url, headers=headers, data=data, verify = False)

    #Pass Token Onto Future Functions
    data = response.json()
    extract_data = data['access_token']
    BEARER_TOKEN = str(extract_data)

    return BEARER_TOKEN
