#!/bin/bash

#Press Win + R, type taskschd.msc, and press Enter.
#Click on "Create Task" in the right-hand pane.

# AWS CLI profile
$AWS_PROFILE = "default"

# RDS instance details
$RDS_HOSTNAME = "sanber-database-1.cluster-ch2a4maeagkl.ap-southeast-1.rds.amazonaws.com"
$RDS_PORT = 3306
$RDS_USERNAME = "admin"
$RDS_PASSWORD = "28032006"
$DATABASE_NAME = "MySQL"

# S3 bucket details
$S3_BUCKET = "sanber-bucket"
$BACKUP_PATH = "backups/rds/$(Get-Date -Format yyyy/MM/dd)"
$BACKUP_FILE = "$DATABASE_NAME_$(Get-Date -Format yyyyMMddHHmmss).sql.gz"
$TEMP_BACKUP_FILE = "D:\Kanna\Work\Devops\Backup\$BACKUP_FILE"  

# Create backup
& "D:\Kanna\Work\Devops\Backup\mysqldump.exe" -h $RDS_HOSTNAME -P $RDS_PORT -u $RDS_USERNAME -p$RDS_PASSWORD $DATABASE_NAME | gzip > $TEMP_BACKUP_FILE

# Upload backup to S3
aws s3 cp $TEMP_BACKUP_FILE "s3://$S3_BUCKET/$BACKUP_PATH/$BACKUP_FILE" --profile $AWS_PROFILE

# Remove local backup file
Remove-Item $TEMP_BACKUP_FILE

Write-Output "Backup and upload to S3 completed for database: $DATABASE_NAME on $(Get-Date)"
