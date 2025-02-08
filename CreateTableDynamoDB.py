import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Create a new table
table_name = "UsersTable"
response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[{"AttributeName": "user_id", "KeyType": "HASH"}],
    AttributeDefinitions=[{"AttributeName": "user_id", "AttributeType": "S"}],
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
)

print(f"Table {table_name} created successfully!")
