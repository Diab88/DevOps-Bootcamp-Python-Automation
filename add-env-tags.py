import boto3

boto3.setup_default_session(profile_name='default')
ec2_client_verginia = boto3.client('ec2', region_name="us-east-1")
ec2_resource_virginia = boto3.resource('ec2', region_name="us-east-1")

instance_ids_verginia = []
reservations_veginia = ec2_client_verginia.describe_instances()['Reservations']
for res in reservations_veginia:
    instances = res['Instances']
    for ins in instances:
        instance_ids_verginia.append(ins['InstanceId'])

response = ec2_resource_virginia.create_tags(
    Resources=instance_ids_verginia,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'test'
        },
    ]
)