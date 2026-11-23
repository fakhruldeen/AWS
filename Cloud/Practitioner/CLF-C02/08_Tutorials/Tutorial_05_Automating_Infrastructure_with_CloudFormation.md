# Tutorial 05: Infrastructure as Code (IaC) with AWS CloudFormation & Change Sets

> **Vault Section:** `04_Tutorials/`  
> **Topic:** Automation & Infrastructure as Code  
> **Source Reference:** Rajesh Daswani (*Packt, 2026*), Project Tasks 15.1–15.4; Tom Taulli (*O'Reilly, 2026*), Ch 14.  
> **Associated Certifications:** [CLF-C02](../01_Syllabus/CLF-C02_Master_Blueprint.md), SAA-C03

---

## 1. Architectural Blueprint & Scenario

In this tutorial, you define and provision a reproducible, version-controlled cloud infrastructure stack using **AWS CloudFormation**. You will author a parameterized YAML template that deploys an Amazon S3 storage bucket and an Amazon EC2 web server inside an isolated security group, and safely evaluate modifications using **CloudFormation Change Sets**.

```mermaid
flowchart TD
    Template["cloudformation-webstack.yaml (Source Code)"] --> Upload["Upload to AWS CloudFormation Console / CLI"]
    
    subgraph Stacks["CloudFormation Orchestration"]
        Stack["Production-Web-Stack (Active Running Resources)"]
        ChangeSet["Change Set: Evaluate Delta (Preview Replacements)"]
    end

    Upload --> Stack
    ModifiedTemplate["Updated YAML Template (Instance Resize)"] --> ChangeSet
    ChangeSet -->|"Safe Review Passed -> Execute"| Stack

    subgraph DeployedResources["Provisioned AWS Resources"]
        S3Bucket["Amazon S3 Static Asset Bucket"]
        SecGroup["EC2 Security Group (HTTP / SSH)"]
        EC2Instance["Amazon EC2 Web Server Instance"]
        SecGroup --> EC2Instance
    end

    Stack === DeployedResources
```

---

## 2. Step-by-Step Implementation Guide

### Step 1: Author the CloudFormation Template (`webstack.yaml`)
Save the following configuration as `webstack.yaml`:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Production Infrastructure as Code: S3 Asset Bucket and EC2 Web Server'

Parameters:
  EnvironmentName:
    Description: 'Target environment prefix (e.g. dev, staging, prod)'
    Type: String
    Default: 'prod'
    AllowedValues:
      - 'dev'
      - 'staging'
      - 'prod'

  InstanceTypeParameter:
    Description: 'EC2 Instance Type'
    Type: String
    Default: 't3.micro'
    AllowedValues:
      - 't3.micro'
      - 't3.small'
      - 't3.medium'

  LatestAmiId:
    Description: 'Latest Amazon Linux 2023 AMI ID retrieved dynamically via SSM'
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64'

Resources:
  # Resource 1: Encrypted Amazon S3 Bucket
  AppAssetBucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub '${EnvironmentName}-app-assets-${AWS::AccountId}-${AWS::Region}'
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: 'AES256'
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
      VersioningConfiguration:
        Status: 'Enabled'

  # Resource 2: Dedicated EC2 Security Group
  WebServerSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: 'Allow inbound HTTP and restricted SSH access'
      SecurityGroupIngress:
        - IpProtocol: 'tcp'
          FromPort: 80
          ToPort: 80
          CidrIp: '0.0.0.0/0'
          Description: 'Allow public HTTP traffic'
      SecurityGroupEgress:
        - IpProtocol: '-1'
          CidrIp: '0.0.0.0/0'
          Description: 'Allow all outbound traffic'

  # Resource 3: Amazon EC2 Web Instance
  WebServerInstance:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: !Ref InstanceTypeParameter
      ImageId: !Ref LatestAmiId
      SecurityGroupIds:
        - !GetAtt WebServerSecurityGroup.GroupId
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          dnf update -y
          dnf install -y httpd
          systemctl start httpd
          systemctl enable httpd
          echo "<h1>Provisioned via AWS CloudFormation Stack: ${EnvironmentName}</h1>" > /var/www/html/index.html
          echo "<p>Asset Bucket: ${AppAssetBucket}</p>" >> /var/www/html/index.html
      Tags:
        - Key: 'Name'
          Value: !Sub '${EnvironmentName}-web-server'
        - Key: 'ManagedBy'
          Value: 'CloudFormation'

Outputs:
  WebServerPublicIP:
    Description: 'Public IP address of the provisioned web server'
    Value: !GetAtt WebServerInstance.PublicIp
  WebServerPublicDNS:
    Description: 'Public DNS URL to access the web server'
    Value: !Sub 'http://${WebServerInstance.PublicDnsName}'
  AssetBucketArn:
    Description: 'ARN of the provisioned S3 asset bucket'
    Value: !GetAtt AppAssetBucket.Arn
    Export:
      Name: !Sub '${EnvironmentName}-AssetBucketArn'
```

### Step 2: Deploy the Stack via AWS Management Console
1. Open the **AWS CloudFormation** Console -> **Create stack** -> **With new resources (standard)**.
2. Specify template: Select **Upload a template file** and upload `webstack.yaml`.
3. Specify stack details:
   - **Stack name:** `Production-Web-Stack`.
   - **EnvironmentName:** `prod`.
   - **InstanceTypeParameter:** `t3.micro`.
4. Configure stack options: Leave defaults and choose **Submit**.
5. Monitor Stack Events:
   - Observe the `Events` tab. CloudFormation initiates resource creation in order of mathematical dependency (Security Group first, followed by EC2 Instance and S3 Bucket).
   - Once the stack status reaches `CREATE_COMPLETE`, switch to the **Outputs** tab.
   - Click the `WebServerPublicDNS` link to verify your running web server!

### Step 3: Perform Safe Updates Using CloudFormation Change Sets
Imagine business requirements mandate upgrading the EC2 instance type from `t3.micro` to `t3.small` and adding SSH port 22 access:
1. Modify `webstack.yaml` locally:
   - Change `InstanceTypeParameter` default to `t3.small`.
2. In the CloudFormation Console, select `Production-Web-Stack` -> **Stack actions** -> **Create change set for current stack**.
3. Upload the modified template.
4. Name the Change Set: `UpgradeInstanceTypeToSmall`.
5. Under **Changes**, inspect the preview:
   - CloudFormation indicates that `WebServerInstance` will be **Modified** with `Replacement: True` or `False` depending on AWS API capability.
   - If `Replacement: True`, CloudFormation alerts you that the existing instance will be terminated and replaced with a new instance, resulting in a new IP address!
6. Once validated, choose **Execute change set** to apply updates safely.

### Step 4: Clean Up & Atomic Teardown
1. Select `Production-Web-Stack` -> **Delete**.
2. CloudFormation automatically tears down the EC2 instance, security group, and outputs in reverse dependency order, ensuring zero orphaned or lingering resources.
3. *(Note: S3 buckets containing objects will prevent stack deletion until emptied, preventing accidental data loss).*

---

## 3. Key Takeaways & Exam Distinctions
- **Intrinsic Functions:**
  - `!Ref`: References a parameter or the primary physical ID of a resource.
  - `!GetAtt`: Retrieves an attribute of a resource (such as `PublicIp`, `Arn`, or `GroupId`).
  - `!Sub`: Performs string substitution using variables (`${EnvironmentName}`).
- **Change Sets prevent unintended outages:** Always review a Change Set before executing an update on production infrastructure.
- **Drift Detection:** Identifies if an engineer made out-of-band manual changes directly in the console, violating IaC governance.


---

## 4. 🎯 Authentic Architecture Exam Practice
> Practice real-world scenarios tested on official AWS examinations that directly apply the architectural patterns built in this tutorial.

### Scenario Practice 1: CLF-C02-ET-Q052
**Question:**  
Why are AWS CloudFormation templates used?

**Options:**
- A) To reduce provisioning time by using automation.
- B) To transfer existing infrastructure to another company.
- C) To reuse on-premises infrastructure in the AWS Cloud.
- D) To deploy large infrastructure with no cost implications.

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `A`  
**Peer Consensus:** `100%` agreement.  

**Architectural Breakdown & Distractor Analysis:**
- **Option A is CORRECT:** **AWS CloudFormation** provides declarative Infrastructure as Code (IaC), allowing teams to define entire multi-tier environments in JSON or YAML templates to provision resources predictably, repeatedly, and automatically in minutes.
- **Option B is INCORRECT:** Ownership transfer between legal entities is managed through AWS Organizations and billing account migration, not template deployment.
- **Option C is INCORRECT:** CloudFormation provisions and configures native AWS cloud resources, not on-premises physical bare-metal hardware.
- **Option D is INCORRECT:** While the CloudFormation service itself incurs no additional fee, you still pay for the underlying AWS resources (EC2, RDS, VPC NAT) declared inside the template.

</details>

### Scenario Practice 2: CLF-C02-ET-Q108
**Question:**  
A developer needs to use a standardized template to create copies of a company's AWS architecture for development, test, and production environments.

Which AWS service should the developer use to meet this requirement?

**Options:**
- A) AWS Cloud Map
- B) AWS CloudFormation
- C) Amazon CloudFront
- D) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `B`  
**Peer Consensus:** `100%` agreement.  

**Architectural Breakdown & Distractor Analysis:**
- **Option A is INCORRECT:** AWS Cloud Map is a dynamic service discovery registry allowing microservices to discover one another via custom names and API queries.
- **Option B is CORRECT:** **AWS CloudFormation** allows developers to treat infrastructure as software code, creating parameterized templates that can be repeatedly deployed to instantiate identical, drift-free stacks across Development, Testing, and Production.
- **Option C is INCORRECT:** Amazon CloudFront is a globally distributed Content Delivery Network (CDN) that caches web content at edge locations.
- **Option D is INCORRECT:** AWS CloudTrail monitors and logs account governance actions and API calls for forensic auditing.

</details>

---

## 🎓 Master Architecture MCQ Blueprint: Infrastructure as Code (IaC) & CloudFormation

> Pattern recognition rules mined from the master question bank to solve CloudFormation, Elastic Beanstalk, and CDK questions in under 15 seconds.

### Layer 1: "Clue-to-Service" Linguistic Decryption Matrix

| If Scenario Text Mentions... | Target Architecture / Service | Why (The Core Mechanism) | Decoy Trap to Avoid |
| :--- | :--- | :--- | :--- |
| **"Declarative template in JSON/YAML to provision resources"** | **AWS CloudFormation** | Infrastructure as Code (IaC): models and provisions entire architectures as a single stack. | AWS Elastic Beanstalk (PaaS application framework). |
| **"Deploy identical architecture copies for Dev, Test, Prod"** | **AWS CloudFormation** | Parameterized templates instantiate identical, reproducible cloud stacks. | AWS OpsWorks (Chef/Puppet configuration management). |
| **"Deploy web app code without worrying about infrastructure provisioning"** | **AWS Elastic Beanstalk** | Platform-as-a-Service (PaaS): upload application code (Java, Node, Python); Beanstalk handles provisioning, load balancing, scaling. | AWS CloudFormation (requires writing explicit infrastructure templates). |
| **"Define cloud infrastructure using familiar programming languages (TypeScript, Python)"** | **AWS Cloud Development Kit (AWS CDK)** | Synthesizes high-level programming language constructs into CloudFormation templates. | AWS CloudTrail (captures API logs; does not provision resources). |
| **"Detect changes made to resources outside of CloudFormation"** | **CloudFormation Drift Detection** | Flags resources modified manually via console or CLI that diverge from template definition. | AWS Config alone (evaluates compliance rules rather than template parity). |

---

### Layer 2: 3-Step Rapid Elimination Heuristic

```mermaid
flowchart TD
    Q["Read Provisioning Scenario Question"] --> S1{"What is the Developer's Role?"}
    S1 -->|"Focus exclusively on application code\n(Upload ZIP, let AWS handle servers)"| EB["Lock: AWS Elastic Beanstalk\nPlatform-as-a-Service (PaaS)"]
    S1 -->|"Define entire infrastructure topology\nas reusable code / templates"| IaC{"Language / Format?"}
    
    IaC -->|"JSON or YAML Declarative Templates"| CFN["Lock: AWS CloudFormation\n(Stacks, Drift Detection)"]
    IaC -->|"TypeScript, Python, Java, C# SDK"| CDK["Lock: AWS Cloud Development Kit (CDK)"]
```

1. **Step 1: Check Abstraction Level:**
   - "Upload code and run" $\to$ **AWS Elastic Beanstalk**.
   - "Model infrastructure in declarative template" $\to$ **AWS CloudFormation**.
   - "Author infrastructure in imperative programming languages" $\to$ **AWS CDK**.
2. **Step 2: Check Cost Model:**
   - CloudFormation and Elastic Beanstalk have **no additional service fees**; you only pay for the underlying resources created.
3. **Step 3: Check Environmental Portability:**
   - Creating identical environments across multiple regions or accounts? $\to$ **CloudFormation Stacks / StackSets**.

---

### Layer 3: High-Frequency Decoy Autopsy

#### Decoy Trap: CloudFormation vs. Elastic Beanstalk
* **The Exam Trap:** A company wants a developer to deploy a PHP web application on AWS with minimal operational overhead, without manually configuring servers, networks, or load balancers.
* **The Decoy:** Option A: "Write a CloudFormation template to provision EC2, VPC, ALB, and Auto Scaling."
* **The Fatal Flaw:** CloudFormation requires the developer to design, author, and maintain explicit infrastructure definitions (subnets, route tables, security group rules, target groups).
* **The Correct Choice:** **AWS Elastic Beanstalk**. The developer simply uploads their application package, and Beanstalk automatically provisions and configures the compute, storage, load balancing, and scaling environment.

---

### Layer 4: 10-Second Visual Decision Flowchart

```mermaid
flowchart TD
    Start["Read Automation Scenario"] --> Req{"What is the Core Goal?"}
    
    Req -->|"Standardized Multi-Tier Template (JSON/YAML)"| CFN["AWS CloudFormation\n(Zero service fee; pay for provisioned resources)"]
    Req -->|"Code-Centric App Deployment (PaaS)"| Beanstalk["AWS Elastic Beanstalk\n(Upload code; AWS handles infrastructure)"]
    Req -->|"Code Infrastructure in Python/TypeScript"| CDK["AWS Cloud Development Kit (CDK)\n(Synthesizes to CloudFormation)"]
    Req -->|"Chef / Puppet Configuration Management"| OpsWorks["AWS OpsWorks"]
```
