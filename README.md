# AWS_load-data-s3
```markdown
# Project Setup Guide

This guide will walk you through setting up a Python virtual environment, installing necessary packages, and configuring AWS CLI for uploading files to an S3 bucket.

## Prerequisites

- Python 3.x
- AWS CLI
- Internet connection for downloading packages and dependencies

## Steps

### 1. Create and Activate a Python Virtual Environment

```bash
python3 -m venv test
source test/bin/activate
```

### 2. Install Required Python Packages

Install `boto3` for AWS SDK and `botocore` exceptions.

```bash
pip install boto3
pip install botocore
```

### 3. Run Your Python Script

Ensure your script `upload_s3.py` is in the current directory. Execute the script to upload files to S3.

```bash
python3 upload_s3.py
```

Repeat the command if necessary to ensure that the upload completes.

### 4. Configure AWS CLI

If you haven't configured AWS CLI yet, follow these steps:

1. Install AWS CLI.

   On Ubuntu-based systems:

   ```bash
   sudo apt-get update
   sudo apt-get install aws-cli
   ```

   Alternatively, download and install AWS CLI version 2:

   ```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   ```

2. Configure AWS CLI with your credentials.

   ```bash
   aws configure
   ```

   Follow the prompts to enter your AWS Access Key, Secret Key, region, and output format.

### 5. Verify Installation

After installation and configuration, verify the setup by running your script again.

```bash
python3 upload_s3.py
```

### 6. Clean Up

Deactivate the virtual environment if you're done.

```bash
deactivate
```

### Troubleshooting

- If you encounter issues with the AWS CLI installation, ensure that you have `unzip` installed:

  ```bash
  sudo apt install unzip
  ```

- Check your Python script for errors if uploads fail.

## Additional Notes

- Ensure that you have the necessary permissions for the AWS S3 bucket you're interacting with.
- Adjust file paths and configurations as needed based on your project setup.

```

