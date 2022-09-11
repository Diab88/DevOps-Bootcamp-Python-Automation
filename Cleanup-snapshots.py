import boto3
from operator import itemgetter

boto3.setup_default_session(profile_name='default')
ec2_client = boto3.client('ec2', region_name="us-east-1")

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self']
)

sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

for snap in sorted_by_date[2:]: #all snapshots deleted except first 2
    response = ec2_client.delete_snapshot(
        SnapshotId=snap['SnapshotId']
    )
    print(response)

