import boto3, os, mimetypes
from datetime import datetime
from constants import *

s3 = boto3.client('s3')


# 1.
def check_if_bucket_exist(bucket_name: str) -> bool :
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"Le bucket '{bucket_name} existe")

        return True
    except s3.exceptions.NoSuchBucket:
        print(f"Erreur: Le bucket '{bucket_name}' n'existe pas.")
        return False
    
def delete_all_files(bucket_name: str) -> bool:
    try:
        all_key_files = [x["Key"] for x in s3.list_objects(Bucket=bucket_name)["Contents"]]

        for file in all_key_files:
            s3.delete_object(Bucket=bucket_name, Key=file)
        return True

    except:
        return False
    
def upload_dist_folder(bucket_name: str, dist_folder: str):
    for root, _ ,files in os.walk(dist_folder):
        for file in files:
            file_name = os.path.join(root,file).replace("\\", "/")
            s3_file_name = file_name.replace("./dist/", "")

            # Guess the content type based on the file extension
            content_type, _ = mimetypes.guess_type(file_name)

            extra_args = {}
            if content_type:
                extra_args['ContentType'] = content_type

            s3.upload_file(file_name, bucket_name, s3_file_name, ExtraArgs=extra_args)
            print(f"Uploaded {file_name} as {s3_file_name} with content type {content_type}")


def run():
    if(not check_if_bucket_exist(BUCKET_NAME)):
        return
    
    delete_all_files(BUCKET_NAME)
    upload_dist_folder(BUCKET_NAME, DIST_FOLDER)

    print("Consulte les modifs sur : http://cap-nord-bucket.s3-website.eu-west-3.amazonaws.com/index.html")

if __name__ == "__main__":
    run()