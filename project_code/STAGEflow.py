import requests
import json
from token_function import get_token
from export_function import get_policy
from validate_function import check_pass
from import_function import check_completion
from DEVflow import get_policy_codes


def import_to_stage():
    clientId = "POOGAATPV9DWOHZDYGMT"
    clientSecret = "tasoUG8Ls2b3P8n17Yzh9V4PHmd97DyZ"
    BEARER_TOKEN = get_token(clientId, clientSecret)

    env1Id = "81e1bbda-00cf-4092-8238-4a9bba540f6d"
    authWs1Id = "db31e1a0-2746-4131-b719-bbb21297e483"
    env2Id = "c3192543-bee5-40ee-87eb-3fd95853f22f"
    authWs2Id = "43419dfc-16b3-4b0d-8d7a-13a936ac02e8"
    approval = True

    policies = get_policy_codes()
    print(policies)

    for policyTuple in policies:
        try:
            policyId, policyCode, *extra_values = policyTuple
            #Validate the policy exported from DEV
            [passfail, completed] = check_pass(env1Id, BEARER_TOKEN, policyCode, authWs1Id)
            if passfail == [] and completed is True and approval is True:
                correctCodes.append([policyId, policyCode])
                #Import policy from DEV into STAGE
                isComplete = check_completion(env2Id, BEARER_TOKEN, policyCode, authWs2Id)
                if isComplete is True:
                    completePolicies.append([policyId, policyCode])
                    #Export policy from STAGE
                    policyCode = get_policy(env2Id, policyId, BEARER_TOKEN)
                    env3Id = "c3895c00-9e78-4990-9342-4f296222a0a2"
                    authWs3Id = "3c8017f4-fe6b-46ff-aff0-05014de21acc"
                    # Validate the policy that was moved to STAGE
                    [passfail, completed] = check_pass(env2Id, BEARER_TOKEN, policyCode, authWs2Id)
                    approval = True
                    if passfail == [] and completed is true and approval is True:
                        return policyCode
                else:
                    print("Policy issue")
            else:
                print("Policy issue")
        except Exception as e:
            print(f"Error processing policy: {e}")

import_to_stage()
