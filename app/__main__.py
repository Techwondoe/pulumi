"""An AWS Python Pulumi program"""
import json

import pulumi
from pulumi_aws import s3


def public_read_policy_for_bucket(bucket_name: str):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                f"arn:aws:s3:::{bucket_name}/*",
            ]
        }]
    })


# Create an AWS resource (S3 Bucket) https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucket/
bucket = s3.Bucket('techwondoe-public-bucket',
                   acl=s3.CannedAcl.PUBLIC_READ,
                   versioning=s3.BucketVersioningArgs(enabled=True))

# Export the name of the bucket
bucket_name = bucket.id
bucket_policy = s3.BucketPolicy(resource_name='bucket-policy',
                                bucket=bucket_name,
                                policy=bucket_name.apply(public_read_policy_for_bucket))

pulumi.export('bucket_name', bucket_name)
