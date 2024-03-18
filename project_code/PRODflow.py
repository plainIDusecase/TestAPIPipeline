import requests
import json
from token_function import get_token
from export_function import get_policy
from validate_function import check_pass
from import_function import check_completion
from STAGEflow import import_to_stage

clientId = "POOGAATPV9DWOHZDYGMT"
clientSecret =  "tasoUG8Ls2b3P8n17Yzh9V4PHmd97DyZ"
BEARER_TOKEN = get_token(clientId, clientSecret)
print(BEARER_TOKEN)

authWs1Id = "db31e1a0-2746-4131-b719-bbb21297e483"
env2Id = "c3192543-bee5-40ee-87eb-3fd95853f22f"
authWs2Id = "43419dfc-16b3-4b0d-8d7a-13a936ac02e8"
approval = True

env3Id = "c3895c00-9e78-4990-9342-4f296222a0a2"
authWs3Id = "3c8017f4-fe6b-46ff-aff0-05014de21acc"

# Try-except block to handle exceptions
try:
    policyCode = import_to_stage()
    for policy in policyCode:
        try:
            isComplete = check_completion(env3Id, BEARER_TOKEN, policyCode, authWs3Id)
            if isComplete and approval:
                print("Successfully moved the policy to PROD")
                print("Move policy to PROD folder and push to GitHub")
            else:
                print("Failed to shift policy to PROD. Raise Ticket")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print("Skipping this policy and continuing...")
except Exception as e:
    print(f"Error occurred: {str(e)}")
    print("Aborting the process...")

