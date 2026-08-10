import pandas as pd
from datetime import datetime
import sys
from awsglue.utils import getResolvedOptions


ARG_LIST = ["bucket_name", "file_prefix"]
para = getResolvedOptions(sys.argv, ARG_LIST)

bucket_name = para["bucket_name"]
file_prefix = para["file_prefix"]

s3_source_url = f"s3://{bucket_name}/{file_prefix}/"

print(f"Bucket_name --> {bucket_name}")
print(f"file_prefix --> {file_prefix}")
print(f"S3_Source_URL --> {s3_source_url}")

now = datetime.now()
formatted_date_time = int(now.strftime("%Y%m%d%H%M%S"))

target_s3_url = (
    "s3://event-driven-pipeline-target-20-july/"
    "target/orders/"
    + str(formatted_date_time)
    + ".parquet"
)

print(f"Target_S3_URL --> {target_s3_url}")

df = pd.read_csv(s3_source_url)
print(df)

df.drop_duplicates(inplace=True)
df = df.reset_index(drop=True)

df.to_parquet(target_s3_url, index=False)

print("Data Stored Successfully")
