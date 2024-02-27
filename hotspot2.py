from aws_cdk import (
    aws_efs as efs
)

efs.FileSystem(
    self,
    "example",
    encrypted=False  # Sensitive
)
