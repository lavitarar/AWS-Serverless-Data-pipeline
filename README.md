# 🚀 AWS Serverless Data Pipeline

🔗 **GitHub Repository:** https://github.com/lavitarar/AWS-Serverless-Data-pipeline  
🔗 **LinkedIn:** https://www.linkedin.com/in/lavi-tarar

---

## 📌 Project Overview

This project demonstrates an **event-driven serverless data engineering pipeline** built using AWS services.

The pipeline automatically processes order data uploaded to **Amazon S3**. The workflow uses **Amazon SNS, Amazon SQS, AWS Lambda, AWS Glue, AWS Glue Crawler, and Amazon Athena** to create an automated end-to-end data pipeline.

The main objective is to demonstrate how AWS services can be integrated to build a **scalable, automated, and serverless ETL pipeline**.

---

## 🏗️ Architecture

```text
                    Order File Upload
                           │
                           ▼
                    ┌─────────────┐
                    │  Amazon S3  │
                    │ Input Data  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Amazon SNS │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Amazon SQS │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ AWS Lambda  │
                    │ ETL Trigger │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  AWS Glue   │
                    │   ETL Job   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Amazon S3  │
                    │  Processed  │
                    │    Data     │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Glue Crawler│
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Glue Data   │
                    │   Catalog   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Athena    │
                    │ SQL Queries │
                    └─────────────┘
