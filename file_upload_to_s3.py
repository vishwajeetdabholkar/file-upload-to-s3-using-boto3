import boto3

# Create an S3 client
try:
    s3 = boto3.client(
        's3',
        aws_access_key_id='yourid',
        aws_secret_access_key='yourkey'
    )

    filename = 'test.csv'
    bucket_name = 'your_bucket_name/'

    # Uploads the given file using a managed uploader
    s3.upload_file(filename, bucket_name, filename)

except:
    print("Upload failed")
