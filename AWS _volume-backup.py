import boto3
import schedule

boto3.setup_default_session(profile_name='default')
ec2_client = boto3.client('ec2', region_name="us-east-1")
def create_volume_snapshots():
    volumes = ec2_client.describe_volumes()
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)

schedule.every(30).seconds.do(create_volume_snapshots)

while True:
    schedule.run_pending()