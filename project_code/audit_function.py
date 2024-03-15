import requests
import json

def do_audit(env1Id, BEARER_TOKEN):

    url2 = f"https://api.eu1.plainid.io/api/1.0/audit-admin/{env1Id}"
    params = {
        "filter[timestamp][gt]":1707800041000,
        "filter[resourceType][eq]": "ROLE"
    }
    headers = {
        "Authorization": "Bearer " + BEARER_TOKEN,
        "accept": "application/json"
    }

    response = requests.get(url2, params = params, headers=headers, verify = False)

    response_data = json.loads(response.text)
    resource_ids = set(item["resourceId"] for item in response_data["data"])
    resource_ids_list = list(resource_ids)
    return resource_ids_list

  
