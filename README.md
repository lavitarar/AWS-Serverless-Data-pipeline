# 🚀 AWS Serverless Data Pipeline

🔗 **GitHub Repository:** https://github.com/lavitarar/AWS-Serverless-Data-pipeline  
🔗 **LinkedIn:** https://www.linkedin.com/in/lavi-tarar

---

## 📌 Project Overview

This project demonstrates an **event-driven serverless data engineering pipeline** built using AWS services.

The pipeline automatically detects a new file uploaded to **Amazon S3**, sends an event through **Amazon SNS and SQS**, triggers **AWS Lambda**, and starts an **AWS Glue ETL job** for data processing.

The processed data is then stored back in **Amazon S3**, catalogued using **AWS Glue Crawler**, and made available for SQL-based analytics using **Amazon Athena**.

---

## 🏗️ Architecture

```text
                    File Upload
                         │
                         ▼
                  ┌─────────────┐
                  │  Amazon S3  │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │  Amazon SNS  │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │  Amazon SQS  │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ AWS Lambda  │
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
```

---

## 🖼️ Architecture Diagram

![AWS Serverless Data Pipeline Architecture](AWS-Data-Pipeline-Project-Structure.png)

---

## 🔄 Data Pipeline Workflow

### 1️⃣ File Upload

A source data file is uploaded to an **Amazon S3 bucket**.

```text
User / Application
        ↓
    Amazon S3
```

### 2️⃣ S3 Event Notification

When a new file arrives, Amazon S3 generates an event notification.

```text
Amazon S3
    ↓
Amazon SNS
```

### 3️⃣ Message Queue

Amazon SNS publishes the event message to Amazon SQS.

```text
SNS
 ↓
SQS
```

SQS provides reliable and decoupled message processing.

### 4️⃣ Lambda Processing

AWS Lambda receives the SQS message and extracts information such as:

- S3 bucket name
- File name
- File path

Lambda then starts the AWS Glue ETL job.

```text
SQS
 ↓
Lambda
 ↓
AWS Glue
```

### 5️⃣ AWS Glue ETL

The Glue job:

- Reads the source file from S3
- Loads the data
- Cleans the data
- Performs transformations
- Writes the processed data back to S3

```text
Raw Data
   ↓
AWS Glue ETL
   ↓
Processed Data
```

### 6️⃣ Glue Crawler

The AWS Glue Crawler scans the processed data and automatically discovers the schema.

```text
Processed S3 Data
       ↓
 Glue Crawler
       ↓
Glue Data Catalog
```

### 7️⃣ Amazon Athena

Amazon Athena is used to query the processed data using SQL.

```text
Glue Data Catalog
       ↓
     Athena
       ↓
   SQL Analytics
```

---

# 📂 Project Structure

```text
AWS-Serverless-Data-pipeline/
│
├── lambda/
│   └── lambda_function.py
│
├── glue/
│   └── glue_job.py
│
├── data/
│   └── sample_data.csv
│
├── AWS-Data-Pipeline-Project-Structure.png
│
└── README.md
```

---

# 📁 Project Files

| File / Folder | Description |
|---|---|
| [`lambda/lambda_function.py`](lambda/lambda_function.py) | AWS Lambda function that receives the SQS event and starts the Glue job |
| [`glue/glue_job.py`](glue/glue_job.py) | AWS Glue ETL script for reading, transforming, and processing data |
| [`data/sample_data.csv`](data/sample_data.csv) | Sample input dataset |
| [`AWS-Data-Pipeline-Project-Structure.png`](AWS-Data-Pipeline-Project-Structure.png) | AWS architecture diagram |
| [`README.md`](README.md) | Project documentation |

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| **Amazon S3** | Stores raw and processed data |
| **Amazon SNS** | Sends event notifications |
| **Amazon SQS** | Provides reliable message queuing |
| **AWS Lambda** | Processes events and triggers Glue |
| **AWS Glue** | Performs ETL and data transformation |
| **AWS Glue Crawler** | Discovers data schema |
| **AWS Glue Data Catalog** | Stores metadata and table definitions |
| **Amazon Athena** | Performs SQL-based analytics |

---

# 🛠️ Technologies Used

- **Python**
- **Pandas**
- **AWS**
- **Amazon S3**
- **Amazon SNS**
- **Amazon SQS**
- **AWS Lambda**
- **AWS Glue**
- **AWS Glue Crawler**
- **AWS Glue Data Catalog**
- **Amazon Athena**
- **SQL**
- **ETL**

---

# ⚙️ Lambda Function

The Lambda function acts as the bridge between the messaging layer and AWS Glue.

### Responsibilities

- Receive SQS event
- Read the S3 event information
- Extract bucket name
- Extract file path
- Pass parameters to AWS Glue
- Start the Glue ETL job

📄 **Source Code:**  
[`lambda/lambda_function.py`](lambda/lambda_function.py)

---

# 🔧 AWS Glue ETL Job

The AWS Glue job performs the main data processing operations.

### Responsibilities

- Read input data from Amazon S3
- Load data into a DataFrame
- Clean the dataset
- Transform the data
- Write processed data to Amazon S3

📄 **Source Code:**  
[`glue/glue_job.py`](glue/glue_job.py)

---

# 📊 Amazon Athena Analytics

After the Glue Crawler creates the table in the Glue Data Catalog, the processed data can be queried using Athena.

### Example Query

```sql
SELECT *
FROM processed_data
LIMIT 10;
```

### Record Count

```sql
SELECT COUNT(*) AS total_records
FROM processed_data;
```

### Grouped Analysis

```sql
SELECT
    category,
    COUNT(*) AS total_records
FROM processed_data
GROUP BY category
ORDER BY total_records DESC;
```

---

# 🔐 Security

The project uses **AWS IAM roles and permissions** to allow AWS services to communicate securely.

Examples include:

- Lambda execution role
- Glue execution role
- S3 access permissions
- SNS permissions
- SQS permissions

No AWS access keys, passwords, or other sensitive credentials are stored in this repository.

---

# 🎯 Key Features

- ✅ Serverless architecture
- ✅ Event-driven data pipeline
- ✅ Automated file ingestion
- ✅ S3-based data storage
- ✅ SNS/SQS message-based architecture
- ✅ Lambda-based orchestration
- ✅ Automated AWS Glue ETL
- ✅ Automated schema discovery
- ✅ SQL analytics using Athena
- ✅ IAM-based access control
- ✅ Scalable cloud architecture

---

# 📚 Data Engineering Concepts Demonstrated

This project demonstrates practical knowledge of:

- ETL Pipelines
- Data Ingestion
- Data Transformation
- Event-Driven Architecture
- Serverless Computing
- Message Queues
- Cloud Data Storage
- Data Lakes
- Data Cataloging
- SQL Analytics
- AWS IAM
- AWS Service Integration

---

# 🚀 How the Pipeline Works

```text
1. Upload file to S3
        ↓
2. S3 generates event
        ↓
3. SNS receives notification
        ↓
4. SNS publishes message to SQS
        ↓
5. SQS triggers Lambda
        ↓
6. Lambda starts Glue ETL job
        ↓
7. Glue processes the data
        ↓
8. Processed data stored in S3
        ↓
9. Glue Crawler discovers schema
        ↓
10. Data Catalog is updated
        ↓
11. Athena queries the data
```

---

# 💡 What I Learned From This Project

Through this project, I gained practical experience in designing and implementing a **serverless AWS data pipeline**.

Key learning areas include:

- Designing event-driven architectures
- Integrating multiple AWS services
- Building automated ETL workflows
- Working with S3-based data lakes
- Implementing Lambda-based orchestration
- Processing data using AWS Glue
- Using SQS for reliable message processing
- Creating metadata using Glue Crawler
- Performing SQL analytics with Athena

---

# 👨‍💻 Author

### Levi

**SQL Developer | Data Engineering Enthusiast**

**Technical Skills:**

`SQL` `Python` `AWS` `ETL` `S3` `Lambda` `Glue` `SNS` `SQS` `Athena`

---

## 🔗 Connect With Me

📌 **GitHub:**  
https://github.com/lavitarar

📌 **LinkedIn:**  
https://www.linkedin.com/in/lavi-tarar

---

## ⭐ Project

If you find this project useful, feel free to ⭐ **Star the repository**.
