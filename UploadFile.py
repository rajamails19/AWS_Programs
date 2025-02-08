import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Upload file to S3
bucket_name = "your-bucket-name"
file_name = "test.txt"
s3.upload_file(file_name, bucket_name, file_name)

print(f"File {file_name} uploaded to {bucket_name}")
