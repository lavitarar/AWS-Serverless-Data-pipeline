import json
import boto3


def lambda_handler(event, context):
    print(f"Event Content --> {event}")

    # Create Glue client
    glue = boto3.client("glue")

    # Read SQS message
    body = json.loads(event["Records"][0]["body"])

    # Read SNS message
    message_json = json.loads(body["Message"])

    # Get bucket name and object key
    bucket_name = message_json["Records"][0]["s3"]["bucket"]["name"]
    file_prefix = message_json["Records"][0]["s3"]["object"]["key"]

    print(f"Bucket Name --> {bucket_name}")
    print(f"File Prefix --> {file_prefix}")

    # Start Glue Job
    response = glue.start_job_run(
        JobName="event-driven-glue-job",
        Arguments={
            "--bucket_name": bucket_name,
            "--file_prefix": file_prefix
        }
    )

    print(f"Glue Job Started: {response['JobRunId']}")

    return {
        "statusCode": 200,
        "body": f"Glue Job Started: {response['JobRunId']}"
    }
