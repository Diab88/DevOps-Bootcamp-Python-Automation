import boto3

boto3.setup_default_session(profile_name='default')
ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

instance_id = "i-0436756c8d5365ae5"
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name':'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)
instance_volumes = volumes['Volumes'][0]
print(instance_volumes)

ec2_client.describe