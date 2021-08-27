import boto3
client = boto3.client('s3')
import json
bucket_name = 'demobucket2903'
bucket_policy = {
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"PublicRead",
      "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject","s3:GetObjectVersion"],
      "Resource":["arn:aws:s3:::demobucket2903/*"]
    }
  ]
}
bucket_policy = json.dumps(bucket_policy)
print(bucket_policy)
print(client.put_bucket_policy(Bucket = bucket_name, Policy = bucket_policy))
