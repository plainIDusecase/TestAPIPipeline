import requests
import json
from token_function import get_token
from export_function import get_policy
from validate_function import check_pass
from import_function import check_completion
from audit_function import do_audit
#from gitup import push_to_github
import os

my_secret = os.environ['TEST']
print("My secret:", my_secret)

def get_policy_codes():
  clientId = "POOGAATPV9DWOHZDYGMT"  
  clientSecret =  "tasoUG8Ls2b3P8n17Yzh9V4PHmd97DyZ"
  BEARER_TOKEN = get_token(clientId,clientSecret)
  print(BEARER_TOKEN)

  env1Id = "81e1bbda-00cf-4092-8238-4a9bba540f6d"
  policyIds = do_audit(env1Id, BEARER_TOKEN)
  print(policyIds)
  policy_codes = []

  for policy in policyIds:
    policyId = policy
    policyCode = get_policy(env1Id,policyId,BEARER_TOKEN)
    policy_codes.append(policyCode)

  return [policyIds,policy_codes]
  
policy_codes_list = get_policy_codes()
print(policy_codes_list)
