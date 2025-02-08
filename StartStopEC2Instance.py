import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

instance_id = "i-0123456789abcdef0"  # Replace with your instance ID

# Start EC2 instance
ec2.start_instances(InstanceIds=[instance_id])
print(f"EC2 instance {instance_id} started.")

# Stop EC2 instance
ec2.stop_instances(InstanceIds=[instance_id])
print(f"EC2 instance {instance_id} stopped.")
