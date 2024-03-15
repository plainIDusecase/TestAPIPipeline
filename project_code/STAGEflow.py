import requests
import json
from token_function import get_token
from export_function import get_policy
from validate_function import check_pass
from import_function import check_completion
from DEVflow.py import get_policy_code

clientId = "POOGAATPV9DWOHZDYGMT"
clientSecret =  "tasoUG8Ls2b3P8n17Yzh9V4PHmd97DyZ"
BEARER_TOKEN = get_token(clientId,clientSecret)


env1Id = "81e1bbda-00cf-4092-8238-4a9bba540f6d"
authWs1Id = "db31e1a0-2746-4131-b719-bbb21297e483"
env2Id = "c3192543-bee5-40ee-87eb-3fd95853f22f"
authWs2Id = "43419dfc-16b3-4b0d-8d7a-13a936ac02e8"
approval = True

policyCodes = get_policy_code()

for policy in policyCodes:
  [passfail,completed]=check_pass(env1Id,BEARER_TOKEN,policy,authWs1Id)
  if passfail == [] and completed is True and approval is True:
    isComplete = check_completion(env2Id, BEARER_TOKEN, policy, authWs2Id)
    if isComplete is True:
        policyCode = get_policy(env2Id,policyId,BEARER_TOKEN)
        env3Id = "c3895c00-9e78-4990-9342-4f296222a0a2"
        authWs3Id = "3c8017f4-fe6b-46ff-aff0-05014de21acc"
        #Validate the policy that was moved to STAGE
        [passfail,completed]=check_pass(env2Id,BEARER_TOKEN,policyCode,authWs2Id)

        approval = True
        if passfail == [] and completed is True and approval is True:
            print("Proceed")
            #Put code here to import
            isComplete = check_completion(env3Id, BEARER_TOKEN, policyCode, authWs3Id)
            if isComplete is True:
                print("Successfully moved the policy to PROD")
                print("Move policy to PROD folder and push to GitHub")
                file_path = f"GitPlace/PROD/policyCode"
                #with open(file_path, "w") as outfile:
                #    outfile.write(policyCode)
                #push_to_github("GitPlace/PROD","policyCode","Pushed to PROD")

            else:
                print("Failed to shift policy to PROD. Raise Ticket")
        else:
            print("Failed to validate policy in STAGE. Raise Ticket")

    else:
        print("Failed to move policy to STAGE. Raise Ticket")

