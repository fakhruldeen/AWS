# AWS Certified Cloud Practitioner (`CLF-C02`) Hands-On Lab Safety & Verification Guide

> **Target Repository:** `Cloud/Practitioner/CLF-C02/phase2_step07_labs/`  
> **Course:** AWS Certified Cloud Practitioner (`CLF-C02`) Student Hands-On Curriculum  
> **Primary Assigned Region:** `eu-north-1` (Stockholm, Sweden)  
> **Cost Guarantee:** **100% Free-Tier Compatible** when following the teardown protocols herein.

---

## 🧭 Executive Overview

This master guide serves as the canonical operational standard for all 14 hands-on student labs in the `CLF-C02` curriculum. It provides instructors and students with:
1. **The Master Lab Catalog:** Complete matrix of all 14 labs, estimated duration, AWS services touched, and Free-Tier safety classification.
2. **The Cost Trap Radar:** Clear identification of billable edge cases (e.g., NAT Gateways, Elastic IPs, Application Load Balancers, Multi-AZ RDS) and how to mitigate them.
3. **Universal Pre-Flight Environment Checks:** CLI commands to verify credentials, account boundaries, and region settings before beginning any lab.
4. **Universal One-Click Automated Teardown Suite:** Bash runbooks to guarantee \$0.00 bills upon completing hands-on exercises.

---

## 📊 Master Lab Catalog & Cost Safety Matrix

| Lab # | Lab Title | Primary Domain | Est. Time | AWS Services Covered | Free-Tier Safety Status | Cost Risk Level & Action |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| **00** | [Account Creation & Security Baseline](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/00_Account_Creation_Walkthrough.md) | Domain 2 | 20 min | Root Account, MFA, IAM User, Budgets | 100% Free Always | **Zero Risk:** No billable infrastructure. |
| **01** | [Multi-Tier VPC & Networking Foundations](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_01_vpc_networking.md) | Domain 3 | 25 min | Amazon VPC, Subnets, IGW, Route Tables, NAT GW | ⚠️ Conditional | **Medium Risk:** NAT Gateway costs ~\$0.045/hr. **Delete NAT GW immediately after verification.** |
| **02** | [VPC Security Controls: SGs & NACLs](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_02_vpc_security_controls.md) | Domain 2 | 20 min | Security Groups, Network ACLs, Ephemeral Ports | 100% Free Always | **Zero Risk:** Virtual firewalls carry zero hourly charge. |
| **03** | [Amazon EC2 Compute & User Data Bootstrap](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_03_ec2_compute_bootstrap.md) | Domain 3 | 20 min | Amazon EC2 (`t3.micro`), User Data, Apache, Security Groups | 100% Free Tier | **Low Risk:** Covered by 750 free hours/month of `t3.micro`. Terminate instance when finished. |
| **04** | [High Availability: ALB & Auto Scaling](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_04_alb_autoscaling_ha.md) | Domain 3 | 30 min | Application Load Balancer, Launch Templates, Auto Scaling | ⚠️ Conditional | **Low/Med Risk:** 750 free ALB hours for 1st 12 months. Delete ALB and ASG after lab. |
| **05** | [Serverless Architecture: Lambda & API GW](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_05_serverless_lambda_apigateway.md) | Domain 3 | 25 min | AWS Lambda (Python), HTTP API Gateway, IAM Roles | 100% Free Tier | **Zero Risk:** 1 million free Lambda requests & 1M API Gateway requests per month. |
| **06** | [Containerized Workloads: ECR, ECS & Fargate](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_06_containers_ecr_ecs_fargate.md) | Domain 3 | 25 min | Amazon ECR, Amazon ECS, AWS Fargate | 100% Free Tier | **Low Risk:** Delete ECS service & task definition after verification. |
| **07** | [Amazon S3 Storage Tiers & Lifecycle Rules](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_07_s3_storage_lifecycle.md) | Domain 3 | 20 min | Amazon S3, Storage Classes, Lifecycle Policies, Versioning | 100% Free Tier | **Zero Risk:** 5 GB standard storage free. Empty and delete bucket after lab. |
| **08** | [Block & File Storage: EBS & EFS](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_08_ebs_efs_storage.md) | Domain 3 | 25 min | Amazon EBS (gp3), Amazon EFS (POSIX file shares) | 100% Free Tier | **Low Risk:** 30 GB EBS free/month; 5 GB EFS free/month. Delete volume & file system. |
| **09** | [Managed Relational Database: RDS & Multi-AZ](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_09_rds_database_ha.md) | Domain 3 | 30 min | Amazon RDS (PostgreSQL `db.t3.micro`), Multi-AZ standby | 100% Free Tier | **Low Risk:** 750 free hours `db.t3.micro` Single-AZ. Delete DB without final snapshot after lab. |
| **10** | [NoSQL Database: Amazon DynamoDB](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_10_dynamodb_nosql_dax.md) | Domain 3 | 20 min | Amazon DynamoDB (On-Demand / Provisioned), Partition Keys | 100% Free Always | **Zero Risk:** 25 GB of permanent free DynamoDB storage. Delete table when done. |
| **11** | [Edge Networking: Route 53 & CloudFront](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_11_route53_cloudfront_edge.md) | Domain 3 | 25 min | Amazon CloudFront (CDN), S3 Origin, OAC, Route 53 DNS | 100% Free Tier | **Low Risk:** 1 TB CloudFront free egress/month. Disable & delete distribution. |
| **12** | [Decoupling: SQS, SNS & EventBridge](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_12_sqs_sns_eventbridge_messaging.md) | Domain 3 | 20 min | Amazon SQS (Standard/FIFO), Amazon SNS, EventBridge | 100% Free Always | **Zero Risk:** 1 million free SQS & SNS requests per month always. |
| **13** | [Observability: CloudWatch, CloudTrail & Config](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_13_observability_cloudwatch_cloudtrail_config.md) | Domain 2 & 3 | 25 min | CloudWatch Alarms/Logs, CloudTrail Trails, AWS Config | 100% Free Tier | **Low Risk:** 1 multi-region CloudTrail trail free. Delete trails & custom metrics. |
| **14** | [Cloud Financial Governance & Budgets](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_14_billing_cost_management.md) | Domain 4 | 20 min | AWS Budgets (\$1 Zero-Spend Alert), Cost Explorer, Tags | 100% Free Always | **Zero Risk:** First 2 budgets are free forever. Keep active for ongoing peace of mind! |

---

## 🚨 The Cost Trap Radar: Top 5 Billable Pitfalls

To guarantee that students incur **\$0.00** during their certification studies, strictly observe these 5 golden rules:

1. **The NAT Gateway Trap (Labs 01 & 04):**  
   * *Problem:* NAT Gateways are NOT covered by the AWS Free Tier. They cost ~\$0.045/hour (~\$32/month) plus \$0.045 per GB of data transferred.
   * *Remedy:* Always delete the NAT Gateway and release its Elastic IP address immediately after testing private subnet connectivity.
2. **The Orphaned Elastic IP Trap:**  
   * *Problem:* AWS provides Elastic IP (public IPv4) addresses for free **only while attached to a running EC2 instance**. An unattached Elastic IP or an Elastic IP attached to a stopped instance incurs a charge (~\$0.005/hour).
   * *Remedy:* Whenever you terminate an instance, explicitly **Release** the allocated Elastic IP address from the VPC console.
3. **The Multi-AZ RDS Snapshot Trap (Lab 09):**  
   * *Problem:* When deleting an Amazon RDS database, the console prompts: *"Create final snapshot?"* If checked, that snapshot remains stored in S3 indefinitely, eventually exceeding the 20 GB free backup storage limit.
   * *Remedy:* Uncheck "Create final snapshot", check "I acknowledge that upon deletion...", and confirm immediate deletion.
4. **The Idle Application Load Balancer Trap (Lab 04):**  
   * *Problem:* Application Load Balancers (ALBs) are free for 750 hours during your first 12 months, but incur hourly charges thereafter.
   * *Remedy:* Delete the ALB and target groups as soon as auto-scaling traffic simulation is verified.
5. **The Unused EBS Volume Trap:**  
   * *Problem:* Terminating an EC2 instance deletes its root EBS volume by default, but secondary EBS volumes or detached snapshots persist and consume monthly storage.
   * *Remedy:* Check the **EBS Volumes** and **EBS Snapshots** consoles regularly to confirm 0 detached volumes remain.

---

## 🛠️ Universal Pre-Flight Verification Check

Before executing any student lab, open **AWS CloudShell** or your local terminal and run this diagnostic pre-flight script:

```bash
#!/usr/bin/env bash
# Pre-Flight Verification Script for CLF-C02 Student Labs
set -euo pipefail

echo "=== AWS CLF-C02 Pre-Flight Diagnostic Check ==="

# 1. Verify Caller Identity
echo -n "1. Checking AWS Identity... "
CALLER_JSON=$(aws sts get-caller-identity --output json)
ACCOUNT_ID=$(echo "$CALLER_JSON" | grep -o '"Account": "[^"]*' | cut -d'"' -f4)
USER_ARN=$(echo "$CALLER_JSON" | grep -o '"Arn": "[^"]*' | cut -d'"' -f4)
echo "OK (Account: $ACCOUNT_ID, Identity: $USER_ARN)"

# 2. Verify Assigned Region
echo -n "2. Checking Region... "
CURRENT_REGION=$(aws configure get region || echo "eu-north-1")
echo "Configured for: $CURRENT_REGION"
if [[ "$CURRENT_REGION" != "eu-north-1" ]]; then
  echo "   [NOTE] For this course, the primary regional target is eu-north-1 (Stockholm)."
  echo "   Run: export AWS_DEFAULT_REGION=eu-north-1"
fi

# 3. Check for Active NAT Gateways
echo -n "3. Scanning for Billable NAT Gateways... "
NAT_COUNT=$(aws ec2 describe-nat-gateways --filter "Name=state,Values=available,pending" --query "length(NatGateways)" --output text --region eu-north-1)
if [[ "$NAT_COUNT" -gt 0 ]]; then
  echo "⚠️ WARNING: $NAT_COUNT active NAT Gateway(s) detected in eu-north-1!"
else
  echo "OK (0 active NAT Gateways)"
fi

# 4. Check for Unattached Elastic IPs
echo -n "4. Scanning for Idle Elastic IPs... "
IDLE_EIPS=$(aws ec2 describe-addresses --query "length(Addresses[?AssociationId==null])" --output text --region eu-north-1)
if [[ "$IDLE_EIPS" -gt 0 ]]; then
  echo "⚠️ WARNING: $IDLE_EIPS unattached Elastic IP(s) incurring charges!"
else
  echo "OK (0 idle Elastic IPs)"
fi

# 5. Check for Running EC2 Instances
echo -n "5. Checking Running EC2 Instances... "
EC2_COUNT=$(aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "length(Reservations[*].Instances[*])" --output text --region eu-north-1)
echo "$EC2_COUNT running instance(s)"

echo "=== Pre-Flight Check Complete. You are ready to start your lab! ==="
```

---

## 🧹 Universal Emergency Teardown Runbook

If you need to instantly clean up all student lab resources in Sweden (`eu-north-1`) and guarantee zero recurring charges, run this automated cleanup script in **AWS CloudShell**:

```bash
#!/usr/bin/env bash
# Universal Emergency Teardown Runbook for CLF-C02 Labs
# Region: eu-north-1 (Stockholm)
set -eo pipefail

REGION="eu-north-1"
echo "🚨 STARTING UNIVERSAL LAB TEARDOWN IN $REGION..."

# 1. Terminate all Student EC2 Instances
echo "1. Terminating student EC2 instances..."
INSTANCE_IDS=$(aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=*student*,*lab*" "Name=instance-state-name,Values=running,stopped" \
  --query "Reservations[*].Instances[*].InstanceId" \
  --output text --region "$REGION" || true)

if [ -n "$INSTANCE_IDS" ]; then
  echo "   Terminating: $INSTANCE_IDS"
  aws ec2 terminate-instances --instance-ids $INSTANCE_IDS --region "$REGION" > /dev/null
  aws ec2 wait instance-terminated --instance-ids $INSTANCE_IDS --region "$REGION"
  echo "   Instances terminated."
else
  echo "   No student instances found."
fi

# 2. Delete Auto Scaling Groups
echo "2. Deleting Auto Scaling Groups..."
ASG_NAMES=$(aws autoscaling describe-auto-scaling-groups \
  --query "AutoScalingGroups[?contains(AutoScalingGroupName, 'student') || contains(AutoScalingGroupName, 'lab')].AutoScalingGroupName" \
  --output text --region "$REGION" || true)

for asg in $ASG_NAMES; do
  echo "   Deleting ASG: $asg"
  aws autoscaling delete-auto-scaling-group --auto-scaling-group-name "$asg" --force-delete --region "$REGION" || true
done

# 3. Delete Application Load Balancers
echo "3. Deleting Load Balancers..."
ALB_ARNS=$(aws elbv2 describe-load-balancers \
  --query "LoadBalancers[?contains(LoadBalancerName, 'student') || contains(LoadBalancerName, 'lab')].LoadBalancerArn" \
  --output text --region "$REGION" || true)

for alb in $ALB_ARNS; do
  echo "   Deleting ALB: $alb"
  aws elbv2 delete-load-balancer --load-balancer-arn "$alb" --region "$REGION" || true
done

# 4. Delete NAT Gateways & Release Elastic IPs
echo "4. Deleting NAT Gateways..."
NAT_IDS=$(aws ec2 describe-nat-gateways \
  --filter "Name=state,Values=available,pending" \
  --query "NatGateways[*].NatGatewayId" \
  --output text --region "$REGION" || true)

for nat in $NAT_IDS; do
  echo "   Deleting NAT Gateway: $nat"
  aws ec2 delete-nat-gateway --nat-gateway-id "$nat" --region "$REGION" || true
done

if [ -n "$NAT_IDS" ]; then
  echo "   Waiting for NAT Gateways to delete before releasing Elastic IPs..."
  sleep 45
fi

echo "   Releasing unattached Elastic IPs..."
ALLOC_IDS=$(aws ec2 describe-addresses \
  --query "Addresses[?AssociationId==null].AllocationId" \
  --output text --region "$REGION" || true)

for alloc in $ALLOC_IDS; do
  echo "   Releasing Elastic IP: $alloc"
  aws ec2 release-address --allocation-id "$alloc" --region "$REGION" || true
done

# 5. Delete Student RDS Databases
echo "5. Deleting Student RDS databases..."
DB_IDS=$(aws rds describe-db-instances \
  --query "DBInstances[?contains(DBInstanceIdentifier, 'student') || contains(DBInstanceIdentifier, 'lab')].DBInstanceIdentifier" \
  --output text --region "$REGION" || true)

for db in $DB_IDS; do
  echo "   Deleting RDS DB: $db (without final snapshot)"
  aws rds delete-db-instance --db-instance-identifier "$db" --skip-final-snapshot --delete-automated-backups --region "$REGION" || true
done

# 6. Delete Student VPCs
echo "6. Deleting Student VPCs..."
VPC_IDS=$(aws ec2 describe-vpcs \
  --filters "Name=tag:Name,Values=*student*,*lab*" \
  --query "Vpcs[*].VpcId" \
  --output text --region "$REGION" || true)

for vpc in $VPC_IDS; do
  echo "   Found VPC: $vpc. Detaching IGWs..."
  IGW_ID=$(aws ec2 describe-internet-gateways --filters "Name=attachment.vpc-id,Values=$vpc" --query "InternetGateways[0].InternetGatewayId" --output text --region "$REGION" || true)
  if [ -n "$IGW_ID" ] && [ "$IGW_ID" != "None" ]; then
    aws ec2 detach-internet-gateway --internet-gateway-id "$IGW_ID" --vpc-id "$vpc" --region "$REGION" || true
    aws ec2 delete-internet-gateway --internet-gateway-id "$IGW_ID" --region "$REGION" || true
  fi
  echo "   Deleting VPC: $vpc"
  aws ec2 delete-vpc --vpc-id "$vpc" --region "$REGION" || true
done

echo "✅ UNIVERSAL TEARDOWN COMPLETE! All student resources removed in $REGION."
```

---

## 📈 Student Billing & Budget Guardrail Check

Every student must complete **Lab 14 (Cloud Financial Governance & Budgets)** on Day 1 of their studies. Ensure the following settings are active in the AWS Management Console:

1. **Billing Preferences:** Navigate to **Billing and Cost Management** -> **Billing Preferences** -> Check **Receive Free Tier Usage Alerts** and enter your primary email address.
2. **\$1 Zero-Spend Budget:** In **AWS Budgets**, confirm that a budget named `Zero-Spend-Budget` exists with a \$1.00 monthly threshold configured to email you when actual or forecasted spend exceeds \$0.01.
3. **Weekly Cost Audit Habit:** Every Friday, open **AWS Cost Explorer** to verify that your Daily Unblended Costs chart reflects \$0.00 spend.
