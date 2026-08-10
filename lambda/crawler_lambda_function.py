import boto3

def lambda_handler(event, context):
    region = "ap-south-1"
    crawler_name = "event-drive-target-crawler"

    glue_client = boto3.client(
        "glue",
        region_name=region
    )

    response = glue_client.start_crawler(
        Name=crawler_name
    )

    print(f"Crawler '{crawler_name}' triggered successfully.")

    return {
        "statusCode": 200,
        "body": f"Crawler '{crawler_name}' triggered successfully."
    }
