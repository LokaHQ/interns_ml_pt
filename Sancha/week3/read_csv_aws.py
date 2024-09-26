import boto3
import csv

s3 = boto3.client(
    's3',
    aws_access_key_id='XYZACCESSKEY',
    aws_secret_access_key='XYZSECRETKEY',
    region_name='eu-west-3'
)
iam = boto3.client('iam')

filename = 'file.csv'
bucket_name = 'bucket-test'

s3.create_bucket(Bucket=bucket_name)
s3.upload_file(filename, bucket_name, filename)

#TODO AssumeRolePolicyDocument
response = iam.create_role(
    AssumeRolePolicyDocument='string',
    Path='/',
    RoleName='role-test',
)

response = iam.attach_role_policy(
    RoleName='role-test', PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole')

obj = s3.get_object(Bucket=bucket_name, Key=filename)
data = obj['Body'].read().decode('utf-8').splitlines()
records = csv.reader(data)
headers = next(records)
print('headers: %s' % (headers)) 
for eachRecord in records:
    print(eachRecord)