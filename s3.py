import boto3
client = boto3.client('s3')
response = client.list_buckets()
print(response)
print(response['Buckets'])
def upload_files(file_name, bucket, object_name=None, args=None):
       if object_name is None:
           object_name = file_name
       response = client.upload_file(file_name, bucket, object_name, ExtraArgs = args)
       print(response)
upload_files('C:\\Users\\Aayush\\3D Objects//2048_0521156.jpg', 'demobucket2903')