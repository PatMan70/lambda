import boto3

def lambda_handler(event, context):
    # Set your Auto Scaling Group name
    asg_name = 'your_auto_scaling_group_name'

    # Set your AWS region
    region = 'your_aws_region'

    # Set the list of processes to suspend (adjust as needed)
    processes_to_suspend = ['Launch', 'Terminate', 'HealthCheck', 'ReplaceUnhealthy', 'AZRebalance', 'AlarmNotification', 'ScheduledActions', 'AddToLoadBalancer']

    # Create an Auto Scaling client
    asg_client = boto3.client('autoscaling', region_name=region)

    try:
        # Suspend specified processes for the Auto Scaling Group
        asg_client.suspend_processes(AutoScalingGroupName=asg_name, ScalingProcesses=processes_to_suspend)

        return {
            'statusCode': 200,
            'body': 'Auto Scaling Group processes suspended successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
