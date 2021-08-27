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
import glob
files = glob.glob('C:\\Users\\Aayush\\3D Objects\\s3//*')
print(files)
args = {'ACL': 'public-read'}
for file in files:
     upload_files(file, 'demobucket2903', args = args)
     print('uploaded',file)