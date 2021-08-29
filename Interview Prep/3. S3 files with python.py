import logging
import boto3
import os

s3_client = boto3.client('s3',aws_access_key_id = "#", aws_secret_access_key = "#")

def upload_file(file_name='carrot.png', bucket='#', object_name="myimage.png"):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file    
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print("Info: File Uploaded to S3 bucket.")
    except Exception as e:
        logging.error(e)
        return False
    return True

def listallfiles(bucket_name, path):
    all_files = []
    try:

        # RETURN THE DICTIONARY WITH ALL DATA REGARDING THE OBJECTS IN THIS FILE PATH
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix =path)

        # RETURNS THE LIST OF FILES 
        contents = response['Contents']
        
        for each_file in contents:
            all_files.append(each_file["Key"])
        return all_files
    except Exception as e:
        logging.error(e)
        return False

# Function to download a specific file from the s3 bucket, by passing bucket name, file path and local file name 
def download_file(bucket_name, path, localfile):
    try:
        s3_client.download_file(bucket_name, path, localfile)
        return True
    except Exception as e:
        logging.error(e)
        return False