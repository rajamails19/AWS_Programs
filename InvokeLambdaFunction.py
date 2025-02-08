import boto3

# Initialize Lambda client
lambda_client = boto3.client('lambda')

# Invoke the Lambda function
response = lambda_client.invoke(
    FunctionName="MyLambdaFunction",
    InvocationType="RequestResponse",
)

print("Lambda Response:", response['Payload'].read().decode("utf-8"))
