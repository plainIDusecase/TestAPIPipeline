import requests
import json

# Validate Policy from Environment1
def check_pass(env1Id, BEARER_TOKEN, policyCode, authWs1Id):
    url = f"https://api.eu1.plainid.io/api/1.0/policies/{env1Id}/validation"
    headers = {
        "Authorization": "Bearer " + BEARER_TOKEN,
        "accept": "application/json"
    }

    data = {
        "policyCode": policyCode,
        "authWsId": authWs1Id,
        "language": "rego"
    }

    response = requests.post(url, headers=headers, json=data, verify=False)

    data = response.json()
    passfail = data['data']['validationErrors']
    policycompleted = data['data']['isPolicyCompleted']
    print(passfail)
    if passfail == []:
        print("No validation errors")
    else:
        print("Validation errors present. Update the policyCode and create ticket")

    if policycompleted is True:
        print("Policy has completed")
    else:
        print("Policy was not completed. Update the policyCode and create ticket")

    return passfail, policycompleted

