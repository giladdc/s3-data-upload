import boto3, botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET


def upload_file_to_s3(file, bucket_name):
    s3 = boto3.client(
       "s3",
       aws_access_key_id=S3_KEY,
       aws_secret_access_key=S3_SECRET
    )
    print(S3_KEY)
    print(S3_BUCKET)
    print(S3_SECRET)
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e
    return str(file.filename)+" uploaded successfully"+'\n'
