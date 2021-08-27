import boto3
client = boto3.client('s3')
response = client.list_buckets()
print(response)
s3 = boto3.resource('s3')
list(s3.buckets.all())
bucket = s3.Bucket('demobucket2903')
list(bucket.objects.all())
files = list(bucket.objects.all())
print(files)
for file in files:
    client.download_file('demobucket2903', file.key, file.key)
print(files[0].key)