from pathlib import Path

import boto3
from PIL import Image
import io
from utils import decodeb64
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
import os

bucket_name = os.environ['BUCKET_NAME']
endpoint_url = os.environ['ENDPOINT_URL']
access_key = os.environ['ACCESS_KEY']
secret_key = os.environ['SECRET_KEY']

PIC_FOLDER_CONSUMER = 'pics_consumer'
Path(PIC_FOLDER_CONSUMER).mkdir(parents=True, exist_ok=True)
PIC_FOLDER_CONSUMER = Path(PIC_FOLDER_CONSUMER)

s3_client = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)


def upload_image_to_s3(file_path, s3_key):
    try:
        # Upload the file to S3
        s3_client.upload_file(file_path, bucket_name, s3_key, ExtraArgs={'ACL': 'public-read'})
        print(f"File successfully uploaded to {bucket_name}/{s3_key}")
        os.remove(file_path)
        print(f"Deleted local {file_path}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")


def process_and_upload_image_to_s3(encoded_image, filename):
    image_bytes = decodeb64(encoded_image)

    image = Image.open(io.BytesIO(image_bytes))

    # rotate image 90 deg right
    image = image.rotate(angle=90)

    # save image locally
    file_path = PIC_FOLDER_CONSUMER / filename
    image.save(file_path)
    print(f"Image saved locally as {filename}")

    # Upload the image to S3
    upload_image_to_s3(file_path=file_path, s3_key=filename)
