from aws_cdk import (
    aws_sagemaker as sagemaker
)

class CfnSagemakerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        exec 'print 1'

        sagemaker.CfnNotebookInstance(
            self, "Sensitive",
            instance_type="instanceType",
            role_arn="roleArn"
        )  # Sensitive, no KMS key is set by default; thus, encryption is disabled
        return `num`


class MyClass:
    def __bool__(self):
        return 0 # Noncompliant: Return value of type bool here.
        return 1
        return 2

obj1 = MyClass()
print(bool(obj1)) # TypeError: __bool__ should return bool, returned int