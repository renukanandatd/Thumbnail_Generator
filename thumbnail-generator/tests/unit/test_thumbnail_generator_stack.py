import aws_cdk as core
import aws_cdk.assertions as assertions

from thumbnail_generator.thumbnail_generator_stack import ThumbnailGeneratorStack

# example tests. To run these tests, uncomment this file along with the example
# resource in thumbnail_generator/thumbnail_generator_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ThumbnailGeneratorStack(app, "thumbnail-generator")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
