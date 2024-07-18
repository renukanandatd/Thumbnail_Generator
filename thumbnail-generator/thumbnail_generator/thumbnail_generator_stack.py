from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_s3_notifications as s3n
)
from constructs import Construct

class ThumbnailGeneratorStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the source S3 bucket
        source_bucket = s3.Bucket(self, "SourceBucket")

        # Create the destination S3 bucket
        destination_bucket = s3.Bucket(self, "DestinationBucket")

        # Create the Lambda function
        thumbnail_lambda = _lambda.Function(
            self, 'ThumbnailFunction',
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler='thumbnail.handler',
            code=_lambda.Code.from_asset('lambda/thumbnail.zip')
        )

        
        source_bucket.grant_read(thumbnail_lambda)
        destination_bucket.grant_write(thumbnail_lambda)

        
        notification = s3n.LambdaDestination(thumbnail_lambda)
        source_bucket.add_event_notification(s3.EventType.OBJECT_CREATED, notification)
