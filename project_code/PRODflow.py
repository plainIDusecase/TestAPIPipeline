import requests
import json
from token_function import get_token
from export_function import get_policy
from validate_function import check_pass
from import_function import check_completion
from STAGEflow import import_to_stage

clientId = "POOGAATPV9DWOHZDYGMT"
clientSecret =  "tasoUG8Ls2b3P8n17Yzh9V4PHmd97DyZ"
BEARER_TOKEN = get_token(clientId,clientSecret)
print(BEARER_TOKEN)


#authWs1Id = "2bb830cf-8382-493f-a8ae-90322c057ba4"
authWs1Id = "db31e1a0-2746-4131-b719-bbb21297e483"
#env2Id = "db1a02b5-d2fa-4014-bccd-8539fce0d988"
#authWs2Id = "b23c17f7-86d2-4a53-b26d-3c0b4bc52159"
env2Id = "c3192543-bee5-40ee-87eb-3fd95853f22f"
authWs2Id = "43419dfc-16b3-4b0d-8d7a-13a936ac02e8"
approval = True

#If STAGE passes approval, export from STAGE and move to PROD
env3Id = "c3895c00-9e78-4990-9342-4f296222a0a2"
authWs3Id = "3c8017f4-fe6b-46ff-aff0-05014de21acc"
#Validate the policy that was moved to STAGE
[passfail,completed]=check_pass(env2Id,BEARER_TOKEN,policyCode,authWs2Id)

policyCode = import_to_stage()
for policy in policyCode:
    isComplete = check_completion(env3Id, BEARER_TOKEN, policyCode, authWs3Id)
    if isComplete is True and approval is True:
        print("Successfully moved the policy to PROD")
        print("Move policy to PROD folder and push to GitHub")

    else:
        print("Failed to shift policy to PROD. Raise Ticket")

