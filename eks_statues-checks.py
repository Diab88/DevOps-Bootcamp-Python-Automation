import boto3
import schedule
boto3.setup_default_session(profile_name='hypatos-prod-us')
client = boto3.client('eks',region_name="us-east-1")


def check_eks_status():
    clusters = client.list_clusters()['clusters']
    for cluster in clusters:
        response = client.describe_cluster(
        name=cluster
        )
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info ['version']
    print(f"Cluster {cluster } status is {cluster_status}")
    print (f"cluster endpoint: {cluster_endpoint} ")
    print(f"Cluster version {cluster_version}")

schedule.every(5).seconds.do(check_eks_status)

while True:
    schedule.run_pending()