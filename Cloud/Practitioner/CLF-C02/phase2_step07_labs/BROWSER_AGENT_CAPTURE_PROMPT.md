# Master Browser Agent Prompt: AWS Full-Course Visual Lab Capture Suite

> **Target Agent:** External Browser Automation Agent (Playwright, Puppeteer, Claude Computer Use, or Browser-Use)  
> **Mission:** Autonomously navigate the AWS Management Console (`eu-north-1`), perform the actions for each lab in sequence, and capture numbered, high-resolution screenshots for the student handbook.  
> **Output Destination:** `/home/mohamed/Desktop/Work/aws/phase2_step07_labs/assets/`  
> **Naming Standard:** `lab_<XX>_step_<YY>_<service>_<action_description>.png`

---

## 🛠️ Global Execution & Visual Capture Instructions

1. **Resolution & Scaling:**
   - Set the browser window to **1920x1080**.
   - Set browser zoom to **115%–125%** so that table columns, text inputs, radio buttons, and navigation sidebars are crisp and readable when embedded in Markdown.
2. **Redaction & Privacy Guardrails:**
   - Never expose Account IDs (12-digit numbers), Root email addresses (`aws@fakhr.me`), or secret keys.
   - Crop or blur the top-right account dropdown before finalizing screenshots.
3. **Region Anchor:**
   - Ensure the Region selector is fixed on **`eu-north-1` (Stockholm)** for all Regional services unless explicitly directed to a global service (Route 53, CloudFront, IAM).
4. **Action Timing:**
   - Wait 1.5–2.5 seconds after page transitions or dynamic modal expansions before capturing to prevent spinner or skeleton UI captures.
5. **Output File Standard:**
   - Every file must match the exact filename specified below so they link automatically into the lab markdown documents.

---

## 📸 Complete Screenshot Capture Catalog (94 Images across 14 Labs)

### 🟢 Lab 00: Account Setup & Day-1 Security Baseline
*Region: Global / eu-north-1*
1. **`lab_00_step_01_signup_portal.png`**: Registration page at `https://portal.aws.amazon.com/billing/signup` with root email and account name filled.
2. **`lab_00_step_02_payment_verification.png`**: Payment step showing card entry fields with card numbers masked/blurred.
3. **`lab_00_step_03_support_plan_selection.png`**: Support plan selection page with radio button on "Basic Support - Free".
4. **`lab_00_step_04_root_mfa_assignment.png`**: IAM console -> Security Credentials -> "Assign MFA" wizard with Authenticator App option selected.
5. **`lab_00_step_05_admin_user_creation.png`**: IAM -> Users -> "Create user" named `cloud-admin` with `AdministratorAccess` attached.
6. **`lab_00_step_06_budget_spend_alert.png`**: AWS Budgets console -> Creating a $5.00 Zero-Spend Budget with email notification alert.

---

### 🟢 Lab 01: Multi-Tier VPC & Networking Foundations
*Region: eu-north-1*
1. **`lab_01_step_01_vpc_dashboard.png`**: VPC Console home showing Region `eu-north-1` and resource summary tiles.
2. **`lab_01_step_02_vpc_and_more_wizard.png`**: "Create VPC" page with "VPC and more" selected, Name: `student-lab-vpc`, CIDR: `10.0.0.0/16`, 2 AZs, 2 Public subnets, 2 Private subnets. Focus on the interactive visual preview map.
3. **`lab_01_step_03_subnets_listing.png`**: Subnets table filtered by `student-lab-vpc` showing the 4 subnets with their CIDR blocks and AZ distributions.
4. **`lab_01_step_04_internet_gateway.png`**: Internet Gateways console showing `student-lab-vpc-igw` with "Attached" status.
5. **`lab_01_step_05_nat_gateway_allocation.png`**: NAT Gateways creation screen showing placement in Public Subnet 1 with an Elastic IP allocated.
6. **`lab_01_step_06_public_route_table.png`**: Route Tables console -> Public Route Table -> Routes tab highlighting `0.0.0.0/0 -> igw-xxxx`.
7. **`lab_01_step_07_private_route_table.png`**: Route Tables console -> Private Route Table -> Routes tab highlighting `0.0.0.0/0 -> nat-xxxx`.

---

### 🟢 Lab 02: VPC Security Controls (Security Groups vs. NACLs)
*Region: eu-north-1*
1. **`lab_02_step_01_security_group_inbound.png`**: Create Security Group screen named `web-tier-sg` showing Inbound Rules: HTTP (port 80) from `0.0.0.0/0` and SSH (port 22) from My IP.
2. **`lab_02_step_02_security_group_outbound.png`**: Outbound Rules tab showing stateful default rule allowing all traffic outbound to `0.0.0.0/0`.
3. **`lab_02_step_03_nacl_inbound_rules.png`**: Subnet Network ACLs screen showing Inbound Rules table with Rule 100 (Allow HTTP:80) and Rule 200 (Allow SSH:22).
4. **`lab_02_step_04_nacl_explicit_deny.png`**: Adding Rule 50 (DENY) for a single specific IP `198.51.100.25/32` before the allow rules.
5. **`lab_02_step_05_nacl_outbound_ephemeral.png`**: NACL Outbound Rules table showing Rule 100 allowing return ephemeral ports (`TCP 1024-65535`).
6. **`lab_02_step_06_vpc_flow_logs.png`**: VPC Flow Logs creation wizard showing aggregation of all IP traffic directed to CloudWatch Logs.

---

### 🟢 Lab 03: Compute Tier (EC2, User Data & Elastic IPs)
*Region: eu-north-1*
1. **`lab_03_step_01_ami_catalog.png`**: EC2 "Launch an instance" wizard -> Application and OS Images (Amazon Linux 2023 Free Tier eligible).
2. **`lab_03_step_02_instance_type_selection.png`**: Instance type dropdown focused on `t3.micro` or `t4g.micro` with Free Tier eligible badge visible.
3. **`lab_03_step_03_network_placement.png`**: Network settings expanded: selecting `student-lab-vpc`, `student-lab-vpc-subnet-public1`, and Auto-assign public IP: Enable.
4. **`lab_03_step_04_user_data_script.png`**: Advanced Details -> User data box filled with the bash script installing `httpd` and echoing a custom hostname HTML file.
5. **`lab_03_step_05_instance_status_checks.png`**: EC2 Instances table showing instance running with "2/2 checks passed" green indicator.
6. **`lab_03_step_06_elastic_ip_association.png`**: Elastic IPs console showing association of public IP with the instance's private IP.

---

### 🟢 Lab 04: High Availability (ALB & Auto Scaling Groups)
*Region: eu-north-1*
1. **`lab_04_step_01_target_group_creation.png`**: Target Groups creation screen -> Target type: Instances, HTTP:80, health check path `/`.
2. **`lab_04_step_02_alb_listener_routing.png`**: Create Application Load Balancer -> Scheme: Internet-facing, selecting 2 Public Subnets across 2 AZs, Listener HTTP:80 forwarding to Target Group.
3. **`lab_04_step_03_launch_template.png`**: EC2 Launch Templates -> creating template `web-launch-template` with AMI, instance type, and SG.
4. **`lab_04_step_04_asg_capacity_limits.png`**: Create Auto Scaling group wizard -> Group size settings: Min: 2, Desired: 2, Max: 4.
5. **`lab_04_step_05_asg_alb_attachment.png`**: ASG configuration step attaching the ASG to the existing ALB target group with ELB health checks enabled.
6. **`lab_04_step_06_alb_dns_browser_test.png`**: Browser tab navigating to `http://<alb-dns-name>` showing the successful web page response.
7. **`lab_04_step_07_asg_scale_out_simulation.png`**: CloudWatch alarm triggered during high CPU load showing ASG launching an additional instance.
8. **`lab_04_step_08_asg_automatic_recovery.png`**: Terminating one instance manually and showing ASG Activity History spinning up a replacement instance automatically.

---

### 🟢 Lab 05: Serverless Compute (AWS Lambda & API Gateway)
*Region: eu-north-1*
1. **`lab_05_step_01_lambda_function_create.png`**: Lambda console -> "Create function" -> Author from scratch, Name: `OrderProcessingFunction`, Runtime: Python 3.12.
2. **`lab_05_step_02_lambda_code_editor.png`**: Lambda built-in code editor showing the `lambda_handler` function returning a status 200 JSON message.
3. **`lab_05_step_03_lambda_test_event.png`**: Execution results tab showing "Execution result: succeeded" with duration and billed memory metrics.
4. **`lab_05_step_04_api_gateway_create.png`**: API Gateway console -> Choose API type -> HTTP API -> "Build".
5. **`lab_05_step_05_api_gateway_integration.png`**: API Gateway Routes and Integrations screen routing `GET /orders` to `OrderProcessingFunction`.
6. **`lab_05_step_06_api_endpoint_curl.png`**: Browser or terminal output displaying the returned JSON payload from the API Gateway invoke URL.

---

### 🟢 Lab 06: Containerized Microservices (Amazon ECR & ECS Fargate)
*Region: eu-north-1*
1. **`lab_06_step_01_ecr_repository.png`**: Amazon ECR console -> Create repository -> Private repository `student-web-service`.
2. **`lab_06_step_02_docker_push_commands.png`**: ECR "View push commands" modal dialog showing Docker auth, build, tag, and push steps.
3. **`lab_06_step_03_ecs_cluster_fargate.png`**: Amazon ECS -> Create cluster -> Infrastructure: AWS Fargate (serverless).
4. **`lab_06_step_04_ecs_task_definition.png`**: Task Definition configuration -> Task size: 0.25 vCPU, 0.5 GB memory, Container image URI pointing to ECR.
5. **`lab_06_step_05_ecs_service_alb.png`**: Create Service wizard -> Launch type: FARGATE, Desired tasks: 2, Load balancer integration.
6. **`lab_06_step_06_running_fargate_tasks.png`**: ECS Service "Tasks" tab showing 2 running tasks distributed across distinct AZs with public IPs.

---

### 🟢 Lab 07: Object Storage (Amazon S3, Versioning & Lifecycle)
*Region: Global (S3)*
1. **`lab_07_step_01_s3_create_bucket.png`**: Create bucket screen -> Name: `student-course-vault-<id>`, Region: `eu-north-1`, Block all public access: Checked.
2. **`lab_07_step_02_bucket_versioning.png`**: Bucket Properties tab showing "Bucket Versioning: Enabled".
3. **`lab_07_step_03_upload_objects.png`**: Objects tab listing uploaded assets with storage class "Standard" and file sizes.
4. **`lab_07_step_04_version_recovery.png`**: Toggling "Show versions" after deleting an object, showing the `Delete marker` and the original preserved file version.
5. **`lab_07_step_05_lifecycle_configuration.png`**: Management tab -> Create lifecycle rule: Transition to Standard-IA after 30 days, Glacier Flexible after 90 days.
6. **`lab_07_step_06_bucket_policy_editor.png`**: Permissions tab -> Bucket policy JSON editor enforcing HTTPS/TLS encryption in transit (`aws:SecureTransport: true`).
7. **`lab_07_step_07_s3_storage_lens.png`**: S3 Storage Lens dashboard displaying total storage bytes, object count, and cost efficiency metrics.

---

### 🟢 Lab 08: Block & File Storage (EBS Volumes vs. Amazon EFS)
*Region: eu-north-1*
1. **`lab_08_step_01_ebs_volume_create.png`**: EC2 -> Volumes -> "Create volume" -> Volume type: General Purpose SSD (`gp3`), Size: 20 GiB, 3000 IOPS.
2. **`lab_08_step_02_ebs_attach_volume.png`**: Actions -> "Attach volume" dialog attaching `/dev/sdf` to running EC2 web server instance.
3. **`lab_08_step_03_ebs_snapshot_creation.png`**: Snapshots console showing progress of point-in-time backup snapshot stored in S3.
4. **`lab_08_step_04_efs_filesystem_create.png`**: Amazon EFS -> "Create file system" wizard with "Regional" storage class selected.
5. **`lab_08_step_05_efs_mount_targets.png`**: Network tab of EFS file system displaying mount targets and security groups across 2 AZs.
6. **`lab_08_step_06_efs_dual_mount_test.png`**: Terminal split-screen showing two different EC2 instances mounting the same NFS EFS endpoint simultaneously.

---

### 🟢 Lab 09: Relational Databases (Amazon RDS Multi-AZ & Read Replicas)
*Region: eu-north-1*
1. **`lab_09_step_01_db_subnet_group.png`**: RDS -> Subnet groups -> "Create DB Subnet Group" associating `student-lab-vpc` with private subnets across 2 AZs.
2. **`lab_09_step_02_rds_engine_selection.png`**: "Create database" -> Standard create -> PostgreSQL -> Free Tier / Dev/Test template.
3. **`lab_09_step_03_rds_multi_az_option.png`**: Availability and durability section selecting "Multi-AZ DB instance (Creates a primary and a standby in another AZ)".
4. **`lab_09_step_04_rds_security_group.png`**: Connectivity settings -> Selecting `student-lab-vpc`, Public access: "No", and RDS Security Group allowing port 5432.
5. **`lab_09_step_05_rds_active_instance.png`**: RDS Databases listing showing instance status "Available" with its endpoint and Multi-AZ badge.
6. **`lab_09_step_06_rds_read_replica_create.png`**: Actions -> "Create read replica" dialog configuring an asynchronous read instance.
7. **`lab_09_step_07_rds_failover_reboot.png`**: Actions -> "Reboot with failover" confirmation dialog demonstrating automated standby promotion.

---

### 🟢 Lab 10: NoSQL & In-Memory Caching (DynamoDB & DAX)
*Region: eu-north-1*
1. **`lab_10_step_01_dynamodb_table_create.png`**: DynamoDB -> "Create table" -> Table name `StudentProfiles`, Partition Key `StudentID` (String).
2. **`lab_10_step_02_capacity_mode_selection.png`**: Table settings choosing "On-Demand" capacity mode for zero-management scaling.
3. **`lab_10_step_03_insert_item_json.png`**: Explore items -> "Create item" modal showing flexible JSON attributes (`Name`, `Courses`, `GradePoint`).
4. **`lab_10_step_04_table_query_vs_scan.png`**: Query interface executing targeted Partition Key lookup with sub-5ms latency indicator.
5. **`lab_10_step_05_dax_cluster_setup.png`**: Amazon DynamoDB -> DAX clusters -> Creating in-memory cache cluster inside `student-lab-vpc`.
6. **`lab_10_step_06_dynamodb_streams_enable.png`**: Exports and streams tab enabling "DynamoDB Streams: New and old images" for event triggers.

---

### 🟢 Lab 11: Edge Acceleration & Global DNS (Route 53 & CloudFront)
*Region: Global*
1. **`lab_11_step_01_route53_hosted_zone.png`**: Route 53 -> Hosted zones -> Public hosted zone showing assigned NS (Name Server) and SOA records.
2. **`lab_11_step_02_route53_alias_record.png`**: Create record wizard: Zone Apex (`example.com`), Record type: A, Toggle "Alias", Target: Application Load Balancer.
3. **`lab_11_step_03_route53_health_check.png`**: Route 53 Health Checks console configuring endpoint monitoring for failover routing.
4. **`lab_11_step_04_cloudfront_distribution.png`**: CloudFront -> "Create distribution" -> Origin domain pointing to S3 bucket origin.
5. **`lab_11_step_05_cloudfront_oac_setup.png`**: Origin access control (OAC) setup selecting "Origin access control settings (recommended)".
6. **`lab_11_step_06_cloudfront_cache_behavior.png`**: Cache key and origin requests settings showing Viewer protocol policy: "Redirect HTTP to HTTPS".
7. **`lab_11_step_07_waf_web_acl_association.png`**: AWS WAF console showing Web ACL with Common Rule Set attached to the CloudFront distribution.

---

### 🟢 Lab 12: Application Integration (SQS, SNS & EventBridge)
*Region: eu-north-1*
1. **`lab_12_step_01_sns_topic_standard.png`**: Amazon SNS -> Topics -> "Create topic" -> Type: Standard, Name: `orders-notification-topic`.
2. **`lab_12_step_02_sqs_queue_creation.png`**: Amazon SQS -> "Create queue" -> Type: Standard, Name: `orders-processing-queue`.
3. **`lab_12_step_03_sns_fanout_subscription.png`**: Subscribing the SQS queue ARN to the SNS topic for the Fan-out architecture pattern.
4. **`lab_12_step_04_sns_publish_message.png`**: Publishing a test JSON order payload into the SNS topic.
5. **`lab_12_step_05_sqs_poll_messages.png`**: SQS console -> "Send and receive messages" -> Polling messages and opening the received JSON message body.
6. **`lab_12_step_06_eventbridge_rule_creation.png`**: Amazon EventBridge -> Create rule -> Event pattern matching AWS EC2 Instance State-change Notification.

---

### 🟢 Lab 13: Observability Triad (CloudWatch, CloudTrail & AWS Config)
*Region: eu-north-1*
1. **`lab_13_step_01_cloudwatch_dashboard.png`**: CloudWatch Dashboard displaying live Line widgets for EC2 CPUUtilization and NetworkIn.
2. **`lab_13_step_02_cloudwatch_alarm_sns.png`**: Alarm creation screen: Metric `CPUUtilization > 80%`, Actions: Send notification to SNS topic.
3. **`lab_13_step_03_cloudtrail_event_history.png`**: CloudTrail Event history table showing captured API events (`RunInstances`, `AuthorizeSecurityGroupIngress`).
4. **`lab_13_step_04_cloudtrail_create_trail.png`**: "Create trail" wizard -> Multi-region trail enabled with CloudWatch Logs integration and S3 bucket storage.
5. **`lab_13_step_05_aws_config_setup.png`**: AWS Config setup wizard setting recording strategy: All resource types.
6. **`lab_13_step_06_config_managed_rules.png`**: Config Rules dashboard showing managed rule `s3-bucket-public-read-prohibited`.
7. **`lab_13_step_07_config_compliance_timeline.png`**: Resource details compliance timeline showing historical configuration change diffs.

---

### 🟢 Lab 14: Financial Governance (AWS Budgets, Cost Explorer & Rightsizing)
*Region: Global / eu-north-1*
1. **`lab_14_step_01_cost_allocation_tags.png`**: Billing console -> Cost allocation tags table with user tags `Environment` and `Project` set to "Active".
2. **`lab_14_step_02_cost_explorer_historical.png`**: AWS Cost Explorer chart showing past 6 months monthly costs grouped by Dimension: Service.
3. **`lab_14_step_03_cost_explorer_forecast.png`**: Cost Explorer forecast view projecting spending through the end of the next quarter.
4. **`lab_14_step_04_aws_budget_cost_threshold.png`**: AWS Budgets -> Create budget -> Monthly cost budget of $20 with actual and forecasted 80% thresholds.
5. **`lab_14_step_05_pricing_calculator_estimate.png`**: AWS Pricing Calculator (`calculator.aws`) displaying a full architectural cost estimate summary card.
6. **`lab_14_step_06_compute_optimizer_recommendations.png`**: AWS Compute Optimizer dashboard displaying EC2 rightsizing recommendations and estimated monthly savings.

---

## 🏁 Post-Capture Verification Checklist
Upon capturing all 94 images:
1. Verify that all images exist in `/home/mohamed/Desktop/Work/aws/phase2_step07_labs/assets/`.
2. Verify image formats are standard PNG and resolution is 1920x1080.
3. Output the manifest count confirmation: `Total Captured: 94 / 94`.
