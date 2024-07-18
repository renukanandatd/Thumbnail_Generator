import boto3
import io
from PIL import Image

s3 = boto3.client('s3')

def handler(event, context):
    # Get the bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download the image from S3 into memory
    response = s3.get_object(Bucket=bucket, Key=key)
    file_content = response['Body'].read()

    # Open the image using Pillow
    with Image.open(io.BytesIO(file_content)) as img:
        # Create a thumbnail
        img.thumbnail((128, 128))

        # Save the thumbnail to a BytesIO object
        thumbnail_buffer = io.BytesIO()
        img.save(thumbnail_buffer, format=img.format)
        thumbnail_buffer.seek(0)

    # Upload the thumbnail to S3
    thumbnail_bucket = 'DestinationBucket'
    thumbnail_key = 'thumbnails/{}'.format(key)
    s3.upload_fileobj(thumbnail_buffer, thumbnail_bucket, thumbnail_key)

    return {
        'statusCode': 200,
        'body': 'Thumbnail created and uploaded successfully!'
    }
