import boto3
from botocore.client import Config
s3 = boto3.client('s3',
endpoint_url='http://172.31.21.248:9000',
aws_access_key_id='khuatthanhphuong',
aws_secret_access_key='12345678',
config=Config(signature_version='s3v4'),
region_name='us-east-1')
s3.download_file('thanhphuong-demo', 'sensor_data (1).csv', 'temp.csv')
print("Download thành công!")
