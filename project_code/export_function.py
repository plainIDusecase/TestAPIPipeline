import requests
import json

#env1Id = "0a8d654f-7dfe-4cb0-939f-ca25d2845ded"
#policyId = "d2c89847-1c51-4a73-8366-b08f8aa900d9"

def get_policy(env1Id,policyId,BEARER_TOKEN):
#Export Policy from Environment1

    url = f"https://api.eu1.plainid.io/api/1.0/policies/{env1Id}/{policyId}"
    headers = {
        "Authorization": "Bearer " + BEARER_TOKEN,
        "accept": "application/json"
    }
    params = {
        "language": "rego"
    }
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(url, headers=headers, params=params, verify=False)
    print(response.json())


    #Pass PolicyCode onto Future Functions
    data = response.json() # replace json_string with your JSON object
    policyCode = data['data']['policyCode']
    print(policyCode)

    return policyCode




