import boto3
client = boto3.client('s3')
bucket_name = 'demobucket2903'
def upload_files(file_name, bucket, object_name=None, args=None):
       if object_name is None:
           object_name = file_name
       response = client.upload_file(file_name, bucket, object_name, ExtraArgs = args)
       print(response)
conf = {
     'ErrorDocument':{'Key':'error.html'},
     'IndexDocument':{'Suffix':'index.html'}
}
print(client.put_bucket_website(Bucket=bucket_name,WebsiteConfiguration=conf))
print(client.get_bucket_website(Bucket= bucket_name))
upload_files('C:\\Users\\Aayush\\3D Objects\\s3\\index.html.txt','demobucket2903',object_name='index.html.txt')
