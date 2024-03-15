import requests
import json
from token_function import get_token
from export_function import get_policy
from validate_function import check_pass
from import_function import check_completion
from gitup import push_to_github

clientId = "POOGAATPV9DWOHZDYGMT"
clientSecret =  "tasoUG8Ls2b3P8n17Yzh9V4PHmd97DyZ"
BEARER_TOKEN = get_token(clientId,clientSecret)
print(BEARER_TOKEN)


env1Id = "81e1bbda-00cf-4092-8238-4a9bba540f6d"
#policyId = "d2c89847-1c51-4a73-8366-b08f8aa900d9"
policyId = "2397c3d8-87c4-4eb0-9e2e-501f19f3cb77"
policyCode = get_policy(env1Id,policyId,BEARER_TOKEN)
print(policyCode)

print("Export policy from DEV. Move policy to DEV folder and push to Git")
file_path = f"GitPlace/DEV/policyCode"
with open(file_path, "w") as outfile:
    outfile.write(policyCode)
push_to_github("GitPlace/DEV","policyCode","Pushed to DEV")

#authWs1Id = "2bb830cf-8382-493f-a8ae-90322c057ba4"
authWs1Id = "db31e1a0-2746-4131-b719-bbb21297e483"
#env2Id = "db1a02b5-d2fa-4014-bccd-8539fce0d988"
#authWs2Id = "b23c17f7-86d2-4a53-b26d-3c0b4bc52159"
env2Id = "c3192543-bee5-40ee-87eb-3fd95853f22f"
authWs2Id = "43419dfc-16b3-4b0d-8d7a-13a936ac02e8"
approval = True

#Validate the policy in DEV
[passfail,completed]=check_pass(env1Id,BEARER_TOKEN,policyCode,authWs1Id)
if passfail == [] and completed is True and approval is True:
    print("Proceed")
    #Put code here to import
    isComplete = check_completion(env2Id, BEARER_TOKEN, policyCode, authWs2Id)
    if isComplete is True:
        print("Successfully moved the policy to STAGE")
        print("Move policy to STAGE folder and push to GitHub")

        file_path = f"GitPlace/STAGE/policyCode"
        with open(file_path, "w") as outfile:
            outfile.write(policyCode)
        push_to_github("GitPlace/STAGE","policyCode","Pushed to STAGE")

        #If STAGE passes approval, export from STAGE and move to PROD
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
                with open(file_path, "w") as outfile:
                    outfile.write(policyCode)
                push_to_github("GitPlace/PROD","policyCode","Pushed to PROD")

            else:
                print("Failed to shift policy to PROD. Raise Ticket")
        else:
            print("Failed to validate policy in STAGE. Raise Ticket")

    else:
        print("Failed to move policy to STAGE. Raise Ticket")
