import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, bucket, object_name=None):
    """
    Uploads a file to an S3 bucket.

    :param file_name: The path to the file to be uploaded.
    :param bucket: The name of the S3 bucket.
    :param object_name: The S3 object name. If not specified, file_name is used.
    """
    # If S3 object_name was not specified, use file_name as the default object name
    if object_name is None:
        object_name = file_name

    # Create an S3 client using boto3
    s3_client = boto3.client('s3')

    try:
        # Upload the file to the specified S3 bucket
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("The file was not found")
    except NoCredentialsError:
        # Handle the case where AWS credentials are not available
        print("Credentials not available")

# Example usage of the upload_to_s3 function
if __name__ == "__main__":
    # Specify the file to upload and the S3 bucket name
    file_name = 'filename.txt'
    bucket = 's3-bucket-name'  # Replace with your actual bucket name
    
    # Call the function to upload the file to S3
    upload_to_s3(file_name, bucket)
