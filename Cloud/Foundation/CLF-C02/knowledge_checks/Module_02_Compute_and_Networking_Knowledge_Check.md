# Module 02 Knowledge Check: Compute & Networking

### Questions
1. **Which EC2 instance type family is optimized for workloads that process high volumes of data in memory, such as in-memory caches and distributed databases?**
   - A) Compute Optimized (`C` family)
   - B) Memory Optimized (`R` family)
   - C) Storage Optimized (`I` family)
   - D) Accelerated Computing (`P`/`G` family)
2. **Which component within an Amazon VPC allows resources in a public subnet to communicate directly with the internet?**
   - A) NAT Gateway
   - B) Internet Gateway (IGW)
   - C) VPC Peering Connection
   - D) Direct Connect Gateway
3. **What is the stateful network firewall that controls inbound and outbound traffic at the individual EC2 instance level?**
   - A) Network Access Control List (NACL)
   - B) Security Group
   - C) AWS WAF
   - D) Route Table
4. **How many IP addresses are reserved by AWS in every VPC subnet?**
   - A) 1
   - B) 3
   - C) 5
   - D) 0
5. **Which service automatically launches or terminates EC2 instances to maintain a constant number of healthy instances and handle traffic spikes?**
   - A) AWS Elastic Beanstalk
   - B) EC2 Auto Scaling
   - C) AWS CloudFormation
   - D) AWS Systems Manager
6. **Which load balancer operates at Layer 7 of the OSI model and supports URL path-based routing?**
   - A) Application Load Balancer (ALB)
   - B) Network Load Balancer (NLB)
   - C) Gateway Load Balancer (GWLB)
   - D) Classic Load Balancer
7. **Which compute service allows you to run containerized workloads without managing the underlying EC2 instances?**
   - A) Amazon ECS on EC2
   - B) AWS Fargate
   - C) AWS Batch
   - D) Amazon Lightsail
8. **What enables EC2 instances in a private subnet to securely initiate outbound connections to the internet while preventing inbound internet connections?**
   - A) Internet Gateway
   - B) NAT Gateway
   - C) Virtual Private Gateway
   - D) Elastic IP Address
9. **What is an Amazon Machine Image (AMI)?**
   - A) A real-time CPU metric graph in CloudWatch
   - B) A pre-configured template containing OS, software packages, and boot volume permissions for EC2
   - C) An automated database backup snapshot in RDS
   - D) An IAM user credential file
10. **Which service enables serverless code execution in response to HTTP requests without provisioning any server infrastructure?**
    - A) AWS Lambda + Amazon API Gateway
    - B) Amazon EC2 + Application Load Balancer
    - C) Amazon EFS + AWS Direct Connect
    - D) AWS CloudTrail + Amazon SNS

---

### Answer Key & Explanations
| Q# | Answer | Key Concept Reference |
| :---: | :---: | :--- |
| **1** | **B** | Memory Optimized (`R` family) provides highest RAM-to-vCPU ratios for in-memory workloads. |
| **2** | **B** | An Internet Gateway (IGW) provides bidirectional public internet communication for public subnets. |
| **3** | **B** | Security Groups are stateful firewalls operating at the virtual network interface (ENI) level. |
| **4** | **C** | AWS always reserves 5 IP addresses per subnet (.0, .1, .2, .3, and .255). |
| **5** | **B** | EC2 Auto Scaling maintains desired instance counts and scales horizontally based on CloudWatch metrics. |
| **6** | **A** | ALB operates at Layer 7 (HTTP/HTTPS) and routes traffic based on URL paths, hosts, and HTTP headers. |
| **7** | **B** | AWS Fargate is the serverless container execution engine for Amazon ECS and Amazon EKS. |
| **8** | **B** | A NAT Gateway deployed in a public subnet allows outbound internet access for private instances. |
| **9** | **B** | An AMI is a master image template providing the OS and software needed to launch EC2 instances. |
| **10** | **A** | API Gateway receives HTTP requests and triggers AWS Lambda serverless function execution. |
