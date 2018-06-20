import boto3
import json
import re

iamclient = boto3.client('iam')

def checkPermissions(version,arn):
    #pull the policy details to determine what rights are available.
    policyDetails = iamclient.get_policy_version(PolicyArn=arn,VersionId=version)

    #TODO loop through this and make it pretty, and then start building intelligence 
    print(policyDetails)

def IAM():
    print('Beginning IAM enumeration, please wait this may take awhile.')

    #Determine available roles within the account
    print('####################################################')
    print('################ Available Roles ###################')
    print('####################################################')

    availableRoles = iamclient.list_roles()
    for role in availableRoles['Roles']:
        print('RoleName: ' + role['RoleName'])
        print('Description: ' + role['Description'])
        print('Effect: ' + role['AssumeRolePolicyDocument']['Statement'][0]['Effect'])
        print('Service: ' + role['AssumeRolePolicyDocument']['Statement'][0]['Principal']['Service'])
        print('Arn: ' + role['Arn'] + ' RoleId: ' + role['RoleId'])
        print('\n')

    print('Policies Currently Applied Here')
    #pull policies applied 'locally' 
    appliedPolicies = iamclient.list_policies(Scope='Local')
    for policy in appliedPolicies['Policies']:
        version = policy['DefaultVersionId']
        arn = policy['Arn']

        print('PolicyName: ' + policy['PolicyName'])
        print('PolicyId: ' + policy['PolicyId'] + 'Arn: ' + arn)
        print('Verion: ' + str(version))
        checkPermissions(version,arn)

def Main():
    platform = input('Which platform are we in? \n \
    1: AWS \n 2: GCP \n 3: Azure')

    if platform == 1:
        awareness = IAM()
        #users = AWSAwarness.GetUsers()
    else:
        print('Still building')

if __name__ == '__main__':
    Main()

