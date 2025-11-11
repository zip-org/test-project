"""
This file contains code that violates SonarQube Python rules from different versions:
1. S1481 - Unused local variables (before version 9.9)
2. S6262 - Hardcoded AWS region (before version 2025.1, added in 10.x series)
3. S7508 - Redundant PySpark collection functions (version 2025.5+)
"""


# =============================================================================
# Rule S1481: Unused local variables should be removed
# Introduced: Before version 9.9 (available since SonarQube 9.1+)
# Type: Code Smell
# =============================================================================
def example_unused_variables():
    """This function violates S1481 by having unused local variables"""
    used_variable = 10
    unused_variable = 20  # Noncompliant: S1481 - unused local variable
    another_unused = "hello"  # Noncompliant: S1481 - unused local variable

    print(f"Only using: {used_variable}")
    return used_variable


# =============================================================================
# Rule S6262: AWS region should not be set with a hardcoded String
# Introduced: Before version 2025.1 (added in 10.x series, 2024)
# Type: Code Smell
# =============================================================================
import boto3


def create_aws_client_with_hardcoded_region():
    """This function violates S6262 by hardcoding AWS region"""
    # Noncompliant: S6262 - hardcoded AWS region
    client = boto3.client("s3", region_name="us-east-1")
    return client


def another_hardcoded_region_example():
    """Another example of S6262 violation"""
    # Noncompliant: S6262 - hardcoded AWS region
    dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
    return dynamodb


# =============================================================================
# Rule S7508: Redundant collection functions should be avoided
# Introduced: Version 2025.5
# Type: Code Smell
# Description: Unnecessary collection calls within other collection functions
# =============================================================================
from pyspark.sql import SparkSession


def pyspark_redundant_operations():
    """This function violates S7508 with redundant PySpark collection operations"""
    spark = SparkSession.builder.appName("example").getOrCreate()

    data = [1, 2, 3, 4, 5]

    # Noncompliant: S7508 - redundant list() call within list()
    redundant_list = list(list(data))

    # Noncompliant: S7508 - redundant tuple() call within tuple()
    redundant_tuple = tuple(tuple(data))

    # Noncompliant: S7508 - unnecessary list call within set()
    redundant_set = set(list(data))

    return redundant_list, redundant_tuple, redundant_set


if __name__ == "__main__":
    print("Running examples with SonarQube rule violations...")
    example_unused_variables()
    i = 0
    i = 323
    create_aws_client_with_hardcoded_region()
    pyspark_redundant_operations()
