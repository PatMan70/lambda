import boto3
import logging

# Set your desired tag key and value
TAG_KEY = 'Environment'
TAG_VALUE = 'Production'

# Create an EC2 client
ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    # Extract instance ID from the CloudWatch Events event
    instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    try:
        # Add the specified tag to the newly launched instance
        ec2_client.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': TAG_KEY, 'Value': TAG_VALUE}
            ]
        )

        logging.info(f'Tagged instance {instance_id} with {TAG_KEY}:{TAG_VALUE}')

        return {
            'statusCode': 200,
            'body': f'Tagged instance {instance_id} with {TAG_KEY}:{TAG_VALUE}'
        }
    except Exception as e:
        logging.error(f'Error tagging instance {instance_id}: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
