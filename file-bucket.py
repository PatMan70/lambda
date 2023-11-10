import boto3
import logging
import urllib.parse

# Set the S3 bucket name
S3_BUCKET_NAME = 'your-s3-bucket-name'

# Create an S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Log the event details for debugging purposes
    logging.info(f"Received event: {event}")

    # Retrieve information about the uploaded file from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        # Get the content of the uploaded file
        response = s3_client.get_object(Bucket=bucket, Key=key)
        file_content = response['Body'].read().decode('utf-8')

        # Log the content of the file
        logging.info(f"Content of the uploaded file '{key}':\n{file_content}")

        return {
            'statusCode': 200,
            'body': 'File processing successful.'
        }
    except Exception as e:
        logging.error(f"Error processing file '{key}': {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
