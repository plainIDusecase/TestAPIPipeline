import requests
import json

#env2Id = "db1a02b5-d2fa-4014-bccd-8539fce0d988"
#auth2WsId = "b23c17f7-86d2-4a53-b26d-3c0b4bc52159"
#Import Policy into Environment2
def check_completion(env2Id, BEARER_TOKEN, policyCode, authWs2Id):

    url2 = f"https://api.eu1.plainid.io/api/1.0/policies/{env2Id}"
    headers = {
        "Authorization": "Bearer " + BEARER_TOKEN,
        "accept": "application/json"
    }

    data = {
        "policyCode": policyCode,
        "authWsId": authWs2Id,
        "language": "rego"
    }

    response = requests.post(url2, headers=headers, json = data, verify = False)

    data = response.json()

    policycompleted = data['data']['isPolicyCompleted']
    #policycompleted = data.get('isPolicyCompleted', False)
    return policycompleted
