# AWS Certified Cloud Practitioner (CLF-C02) - Domain 2: Security and Compliance (30%)

This document contains **247 verified practice questions** for Domain 2: Security and Compliance, sourced directly from the official [CloudCertPrep](https://www.cloudcertprep.io/aws/clf-c02) open-source repository.

## Table of Contents
- [Q003 - Question 1](#q003-1): You have noticed that several critical Amazon EC2 instances have been terminated...
- [Q005 - Question 2](#q005-2): Which statement is true regarding the AWS Shared Responsibility Model?...
- [Q011 - Question 3](#q011-3): An organization has a large number of technical employees who operate their AWS ...
- [Q022 - Question 4](#q022-4): What does the "Principle of Least Privilege" refer to?...
- [Q026 - Question 5](#q026-5): Hundreds of thousands of DDoS attacks are recorded every month worldwide. What s...
- [Q031 - Question 6](#q031-6): Which of the following services allows customers to manage their agreements with...
- [Q032 - Question 7](#q032-7): Which of the following are examples of AWS-managed services, where AWS is respon...
- [Q036 - Question 8](#q036-8): Which of the following must an IAM user provide to interact with AWS services us...
- [Q037 - Question 9](#q037-9): You have AWS Basic support, and you have discovered that some AWS resources are ...
- [Q038 - Question 10](#q038-10): Which of the following are examples of AWS shared controls?...
- [Q043 - Question 11](#q043-11): Under the shared responsibility model, which of the following is the responsibil...
- [Q046 - Question 12](#q046-12): Your company is developing a critical web application in AWS, and the security o...
- [Q048 - Question 13](#q048-13): In the AWS Shared responsibility Model, which of the following are the responsib...
- [Q056 - Question 14](#q056-14): Which of the following is the customer's responsibility under the AWS shared res...
- [Q057 - Question 15](#q057-15): According to the AWS shared responsibility model who is responsible for configur...
- [Q058 - Question 16](#q058-16): Which security service automatically recognizes and classifies sensitive data or...
- [Q060 - Question 17](#q060-17): Under the shared responsibility model, which of the following tasks are the resp...
- [Q064 - Question 18](#q064-18): Which AWS service allows users to identify the changes made to a resource over t...
- [Q075 - Question 19](#q075-19): Access keys in AWS Identity and Access Management (IAM) are used to:...
- [Q078 - Question 20](#q078-20): Which AWS services can be used to gather information about AWS account activity?...
- [Q090 - Question 21](#q090-21): Which AWS IAM feature allows developers to access AWS services through the AWS C...
- [Q091 - Question 22](#q091-22): The user is fully responsible for which action when running workloads on AWS?...
- [Q103 - Question 23](#q103-23): Which of the following will enhance the security of access to the AWS Management...
- [Q105 - Question 24](#q105-24): For which auditing process does AWS have sole responsibility?...
- [Q107 - Question 25](#q107-25): Which of the following common IT tasks can AWS cover to free up company IT resou...
- [Q114 - Question 26](#q114-26): If a customer needs to audit the change management of AWS resources, which of th...
- [Q117 - Question 27](#q117-27): Which of the following Identity and Access Management (IAM) entities is associat...
- [Q118 - Question 28](#q118-28): Under the shared responsibility model, which of the following is the customer re...
- [Q120 - Question 29](#q120-29): What credential components are required to gain programmatic access to an AWS ac...
- [Q121 - Question 30](#q121-30): Which of the following is a shared control between the customer and AWS?...
- [Q126 - Question 31](#q126-31): Which of the following security measures protect access to an AWS account?...
- [Q144 - Question 32](#q144-32): Which activity is a customer responsibility in the AWS Cloud according to the AW...
- [Q150 - Question 33](#q150-33): How can a customer increase security to AWS account logons?...
- [Q158 - Question 34](#q158-34): Which AWS service is used to track, record, and audit configuration changes made...
- [Q162 - Question 35](#q162-35): Which of the following services falls under the responsibility of the customer t...
- [Q163 - Question 36](#q163-36): AWS supports which of the following methods to add security to Identity and Acce...
- [Q169 - Question 37](#q169-37): A Cloud Practitioner must determine if any security groups in an AWS account hav...
- [Q170 - Question 38](#q170-38): Which of the following security-related services does AWS offer?...
- [Q171 - Question 39](#q171-39): Which of the following services have Distributed Denial of Service (DDoS) mitiga...
- [Q175 - Question 40](#q175-40): What can users access from AWS Artifact?...
- [Q179 - Question 41](#q179-41): Which of the following can limit Amazon Simple Storage Service (Amazon S3) bucke...
- [Q181 - Question 42](#q181-42): Where are AWS compliance documents, such as an SOC 1 report, located?...
- [Q182 - Question 43](#q182-43): Which of the following tasks is the responsibility of AWS?...
- [Q183 - Question 44](#q183-44): Under the shared responsibility model which of the following areas are the custo...
- [Q190 - Question 45](#q190-45): Which AWS security service protects applications from distributed denial of serv...
- [Q199 - Question 46](#q199-46): A company has moved to AWS recently. Which of the following AWS Services will he...
- [Q200 - Question 47](#q200-47): What is the AWS feature that provides an additional level of security above the ...
- [Q204 - Question 48](#q204-48): According to the AWS Acceptable Use Policy, which of the following statements is...
- [Q208 - Question 49](#q208-49): According to the AWS Shared responsibility model, which of the following are the...
- [Q211 - Question 50](#q211-50): Which of the following is equivalent to a username and password and is used to a...
- [Q213 - Question 51](#q213-51): What is the AWS service that enables you to manage all of your AWS accounts from...
- [Q219 - Question 52](#q219-52): Which of the following services can help protect your web applications from SQL ...
- [Q221 - Question 53](#q221-53): Based on the AWS Shared Responsibility Model, which of the following are the sol...
- [Q223 - Question 54](#q223-54): What are the default security credentials that are required to access the AWS ma...
- [Q226 - Question 55](#q226-55): Which of the following aspects of security are managed by AWS?...
- [Q229 - Question 56](#q229-56): What are the change management tools that helps AWS customers audit and monitor ...
- [Q231 - Question 57](#q231-57): Which of the following services will help businesses ensure compliance in AWS?...
- [Q236 - Question 58](#q236-58): Which of the following AWS security features is associated with an EC2 instance ...
- [Q238 - Question 59](#q238-59): Using Amazon RDS falls under the shared responsibility model. Which of the follo...
- [Q252 - Question 60](#q252-60): An organization runs many systems and uses many AWS products. Which of the follo...
- [Q258 - Question 61](#q258-61): What is the AWS service that performs automated network assessments of Amazon EC...
- [Q259 - Question 62](#q259-62): Under the Shared Responsibility Model, which of the following controls do custom...
- [Q269 - Question 63](#q269-63): Which of the following can help protect your EC2 instances from DDoS attacks?...
- [Q280 - Question 64](#q280-64): Which of the following is used to control network traffic in AWS?...
- [Q292 - Question 65](#q292-65): Data security is one of the top priorities of AWS. How does AWS deal with old st...
- [Q293 - Question 66](#q293-66): A developer needs to set up an SSL security certificate for a client's eCommerce...
- [Q295 - Question 67](#q295-67): A company is planning to migrate an application from Amazon EC2 to AWS Lambda to...
- [Q300 - Question 68](#q300-68): Which AWS Service is used to manage user permissions?...
- [Q302 - Question 69](#q302-69): A company needs to track resource changes using the API call history. Which AWS ...
- [Q305 - Question 70](#q305-70): What is the AWS' recommendation regarding access keys?...
- [Q306 - Question 71](#q306-71): What is the AWS IAM feature that provides an additional layer of security on top...
- [Q312 - Question 72](#q312-72): For managed services like Amazon DynamoDB, which of the below is AWS responsible...
- [Q316 - Question 73](#q316-73): A company has discovered that multiple S3 buckets were deleted, but it is unclea...
- [Q319 - Question 74](#q319-74): What are AWS shared controls?...
- [Q321 - Question 75](#q321-75): Which of the below are responsibilities of the customer when using Amazon EC2?...
- [Q323 - Question 76](#q323-76): Which of the following AWS services can help you perform security analysis and r...
- [Q332 - Question 77](#q332-77): Which of the following can be used to protect data at rest on Amazon S3?...
- [Q336 - Question 78](#q336-78): When running a workload in AWS, the customer is NOT responsible for:...
- [Q341 - Question 79](#q341-79): Which AWS service or feature is used to manage the keys used to encrypt customer...
- [Q342 - Question 80](#q342-80): Which AWS Service allows customers to download AWS SOC & PCI reports?...
- [Q345 - Question 81](#q345-81): What features does AWS offer to help protect your data in the Cloud?...
- [Q348 - Question 82](#q348-82): Which methods can be used by customers to interact with AWS Identity and Access ...
- [Q349 - Question 83](#q349-83): Which of the following are types of AWS Identity and Access Management (IAM) ide...
- [Q351 - Question 84](#q351-84): How does AWS notify customers about security and privacy events pertaining to AW...
- [Q352 - Question 85](#q352-85): Which IAM entity can best be used to grant temporary access to your AWS resource...
- [Q355 - Question 86](#q355-86): A company is seeking to better secure its AWS account from unauthorized access. ...
- [Q361 - Question 87](#q361-87): Which of the following are examples of the customer's responsibility to implemen...
- [Q362 - Question 88](#q362-88): Which of the following is a type of MFA device that customers can use to protect...
- [Q367 - Question 89](#q367-89): You have just hired a skilled sys-admin to join your team. As usual, you have cr...
- [Q368 - Question 90](#q368-90): An external auditor is requesting a log of all accesses to the AWS resources in ...
- [Q369 - Question 91](#q369-91): Which AWS service allows a company to connect their AWS resources with an on-pre...
- [Q375 - Question 92](#q375-92): Which AWS service enables you to quickly purchase and deploy SSL/TLS certificate...
- [Q380 - Question 93](#q380-93): A company wants to grant a new employee long-term access to manage Amazon Dynamo...
- [Q381 - Question 94](#q381-94): When granting permissions to applications running on Amazon EC2 instances, which...
- [Q384 - Question 95](#q384-95): Which of the following can be used to enable the Virtual Multi-Factor Authentica...
- [Q387 - Question 96](#q387-96): What should you do if you see resources, which you don't remember creating, in t...
- [Q395 - Question 97](#q395-97): A company is developing a mobile application and wants to allow users to use the...
- [Q403 - Question 98](#q403-98): There is a requirement to grant a DevOps team full administrative access to all ...
- [Q410 - Question 99](#q410-99): Which statement is true in relation to the security of Amazon EC2?...
- [Q414 - Question 100](#q414-100): Which of the following strategies helps protect your AWS root account?...
- [Q416 - Question 101](#q416-101): You have just set up your AWS environment and have created six IAM user accounts...
- [Q424 - Question 102](#q424-102): Which of the following services provide real-time auditing for compliance and vu...
- [Q428 - Question 103](#q428-103): What best describes penetration testing?...
- [Q443 - Question 104](#q443-104): Which of the following can help secure your sensitive data in Amazon S3?...
- [Q450 - Question 105](#q450-105): Which of the following services gives you access to all AWS auditor-issued repor...
- [Q455 - Question 106](#q455-106): For compliance and regulatory purposes, a government agency requires that their ...
- [Q458 - Question 107](#q458-107): What can you use to assign permissions directly to an IAM user?...
- [Q463 - Question 108](#q463-108): Which of the following would you use to manage your encryption keys in the AWS C...
- [Q466 - Question 109](#q466-109): A company has infrastructure hosted in an on-premises data center. They currentl...
- [Q468 - Question 110](#q468-110): Where can AWS account owners get a list of all users in their account, including...
- [Q469 - Question 111](#q469-111): Which of the following services enables you to easily generate and use your own ...
- [Q473 - Question 112](#q473-112): Which of the following resources can an AWS customer use to learn more about pro...
- [Q474 - Question 113](#q474-113): Which of the following security resources are available to any user for free?...
- [Q476 - Question 114](#q476-114): Which of the following is the responsibility of AWS according to the AWS Shared ...
- [Q479 - Question 115](#q479-115): Which of the following services enables you to generate and use your own encrypt...
- [Q480 - Question 116](#q480-116): Who is responsible for scaling a DynamoDB database in the AWS Shared Responsibil...
- [Q487 - Question 117](#q487-117): Which feature enables users to sign into their AWS accounts with their existing ...
- [Q488 - Question 118](#q488-118): According to the AWS shared responsibility model, what are the controls that cus...
- [Q491 - Question 119](#q491-119): Which of the following are part of the seven design principles for security in t...
- [Q493 - Question 120](#q493-120): What is the main benefit of attaching security groups to an Amazon RDS instance?...
- [Q496 - Question 121](#q496-121): You have been tasked with auditing the security of your VPC. As part of this pro...
- [Q499 - Question 122](#q499-122): Which statement is true in relation to security in AWS?...
- [Q507 - Question 123](#q507-123): What are the main differences between an IAM user and an IAM role in AWS?...
- [Q509 - Question 124](#q509-124): What does Amazon GuardDuty do to protect AWS accounts and workloads?...
- [Q516 - Question 125](#q516-125): Which of the following requires an access key ID and a secret access key to get ...
- [Q523 - Question 126](#q523-126): Which of the following AWS services integrates with AWS Shield and AWS Web Appli...
- [Q524 - Question 127](#q524-127): Which of the following services is used when encrypting EBS volumes?...
- [Q525 - Question 128](#q525-128): The AWS account administrator of your company has been fired. With the permissio...
- [Q531 - Question 129](#q531-129): A financial services company decides to migrate one of its applications to AWS. ...
- [Q535 - Question 130](#q535-130): Which of the following steps should be taken by a customer when conducting penet...
- [Q550 - Question 131](#q550-131): Which task is AWS responsible for in the shared responsibility model for securit...
- [Q553 - Question 132](#q553-132): According to the AWS shared responsibility model what is the sole responsibility...
- [Q555 - Question 133](#q555-133): Which AWS service identifies security groups that allow unrestricted access to a...
- [Q564 - Question 134](#q564-134): Under the AWS shared responsibility model, which of the following activities are...
- [Q565 - Question 135](#q565-135): Under the shared responsibility model, which of the following is a shared contro...
- [Q573 - Question 136](#q573-136): Which AWS service or feature can enhance network security by blocking requests f...
- [Q575 - Question 137](#q575-137): Which service enables risk auditing by continuously monitoring and logging accou...
- [Q576 - Question 138](#q576-138): Where can AWS compliance and certification reports be downloaded?...
- [Q581 - Question 139](#q581-139): What is the AWS customer responsible for according to the AWS shared responsibil...
- [Q587 - Question 140](#q587-140): Which AWS service would you use to obtain compliance reports and certificates?...
- [Q589 - Question 141](#q589-141): How would an AWS customer easily apply common access controls to a large set of ...
- [Q618 - Question 142](#q618-142): Which of the following is a component of the shared responsibility model managed...
- [Q628 - Question 143](#q628-143): Which of the following is entirely the responsibility of AWS, according to the A...
- [Q633 - Question 144](#q633-144): Which AWS IAM feature is used to associate a set of permissions with multiple us...
- [Q635 - Question 145](#q635-145): Which of the following can a customer use to enable single sign-on (SSO) to the ...
- [Q637 - Question 146](#q637-146): Which of the following benefits does the AWS Compliance program provide to AWS c...
- [Q638 - Question 147](#q638-147): Which of the following services provides on-demand access to AWS compliance repo...
- [Q639 - Question 148](#q639-148): As part of the AWS shared responsibility model, which of the following operation...
- [Q641 - Question 149](#q641-149): Under the shared responsibility model, which of the following tasks are the resp...
- [Q646 - Question 150](#q646-150): What function do security groups serve related Amazon Elastic Compute Cloud (Ama...
- [Q652 - Question 151](#q652-151): How is asset management on AWS easier than asset management in a physical data c...
- [Q654 - Question 152](#q654-152): Using AWS Identity and Access Management (IAM) to grant access only to the resou...
- [Q656 - Question 153](#q656-153): Under the AWS shared responsibility model, customer responsibilities include whi...
- [Q657 - Question 154](#q657-154): Which managed AWS service provides real-time guidance on AWS security best pract...
- [Q659 - Question 155](#q659-155): Under the AWS shared responsibility model, customers are responsible for which a...
- [Q661 - Question 156](#q661-156): What is a responsibility of AWS in the shared responsibility model?...
- [Q663 - Question 157](#q663-157): What does it mean to grant least privilege to AWS IAM users?...
- [Q683 - Question 158](#q683-158): Which AWS service provides a self-service portal for on-demand access to AWS com...
- [Q692 - Question 159](#q692-159): According to the AWS shared responsibility model, what is AWS responsible for?...
- [Q694 - Question 160](#q694-160): Which AWS tool will identify security groups that grant unrestricted Internet ac...
- [Q697 - Question 161](#q697-161): Which of the following is the responsibility of AWS?...
- [Q702 - Question 162](#q702-162): What tasks should a customer perform when that customer suspects an AWS account ...
- [Q705 - Question 163](#q705-163): What is an AWS Identity and Access Management (IAM) role?...
- [Q717 - Question 164](#q717-164): Which service enables customers to audit and monitor changes in AWS resources?...
- [Q722 - Question 165](#q722-165): A user is running an application on AWS and notices that one or more AWS-owned I...
- [Q727 - Question 166](#q727-166): Which AWS service offers on-demand access to AWS security and compliance reports...
- [Q730 - Question 167](#q730-167): Which AWS service provides inbound and outbound network ACLs to harden external ...
- [Q733 - Question 168](#q733-168): Under the AWS shared responsibility model, AWS is responsible for which security...
- [Q735 - Question 169](#q735-169): Under the AWS shared responsibility model, which of the following is an example ...
- [Q740 - Question 170](#q740-170): A web application running on AWS has been spammed with malicious requests from a...
- [Q746 - Question 171](#q746-171): A user needs an automated security assessment report that will identify unintend...
- [Q748 - Question 172](#q748-172): Where can users find a catalog of AWS-recognized providers of third-party securi...
- [Q755 - Question 173](#q755-173): Within the AWS shared responsibility model, who is responsible for security and ...
- [Q757 - Question 174](#q757-174): Which AWS service is used to provide encryption for Amazon EBS?...
- [Q760 - Question 175](#q760-175): What does AWS Shield Standard provide?...
- [Q766 - Question 176](#q766-176): What is one of the customer's responsibilities according to the AWS shared respo...
- [Q770 - Question 177](#q770-177): Where should users report that AWS resources are being used for malicious purpos...
- [Q771 - Question 178](#q771-178): Which AWS service needs to be enabled to track all user account changes within t...
- [Q777 - Question 179](#q777-179): Which of the following is AWS's responsibility under the AWS shared responsibili...
- [Q779 - Question 180](#q779-180): How would a system administrator add an additional layer of login security to a ...
- [Q780 - Question 181](#q780-181): Which service can identify the user that made the API call when an Amazon Elasti...
- [Q782 - Question 182](#q782-182): Where can a customer find information about prohibited actions on AWS infrastruc...
- [Q786 - Question 183](#q786-183): Which of the following are recommended practices for managing IAM users?...
- [Q793 - Question 184](#q793-184): Which situation should be reported to the AWS Abuse team?...
- [Q796 - Question 185](#q796-185): Which of the following are components of Amazon VPC?...
- [Q800 - Question 186](#q800-186): Which functions can users perform using AWS KMS?...
- [Q806 - Question 187](#q806-187): Which Amazon VPC feature enables users to capture information about the IP traff...
- [Q808 - Question 188](#q808-188): Which AWS service will provide a way to generate encryption keys that can be use...
- [Q811 - Question 189](#q811-189): Which AWS service helps users meet contractual and regulatory compliance require...
- [Q812 - Question 190](#q812-190): Under the AWS shared responsibility model, the customer manages which of the fol...
- [Q815 - Question 191](#q815-191): What is a user responsible for when running an application in the AWS Cloud?...
- [Q819 - Question 192](#q819-192): Which AWS service helps identify malicious or unauthorized activities in AWS acc...
- [Q822 - Question 193](#q822-193): A company is hosting a web application in a Docker container on Amazon EC2. AWS ...
- [Q824 - Question 194](#q824-194): Which actions represent best practices for using AWS IAM?...
- [Q825 - Question 195](#q825-195): Which AWS feature or service can be used to capture information about incoming a...
- [Q828 - Question 196](#q828-196): Which service can be used to monitor and receive alerts for AWS account root use...
- [Q839 - Question 197](#q839-197): Which tasks are the customer's responsibility in the AWS shared responsibility m...
- [Q843 - Question 198](#q843-198): A web application is hosted on AWS using an Elastic Load Balancer, multiple Amaz...
- [Q846 - Question 199](#q846-199): A company needs an Amazon S3 bucket that cannot have any public objects due to c...
- [Q849 - Question 200](#q849-200): Who is responsible for patching the guest operating system for Amazon RDS?...
- [Q855 - Question 201](#q855-201): Under the AWS shared responsibility model, which of the following is a customer ...
- [Q857 - Question 202](#q857-202): Under the AWS shared responsibility model, the security and patching of the gues...
- [Q858 - Question 203](#q858-203): Which AWS service makes it easy to create and manage AWS users and groups, and p...
- [Q859 - Question 204](#q859-204): Which AWS service provides on-demand access to AWS security and compliance docum...
- [Q862 - Question 205](#q862-205): A user needs to generate a report that outlines the status of key security check...
- [Q865 - Question 206](#q865-206): Using AWS Config to record, audit, and evaluate changes to AWS resources to enab...
- [Q873 - Question 207](#q873-207): Under the AWS shared responsibility model, which of the following are customer r...
- [Q880 - Question 208](#q880-208): Which of the following acts as a virtual firewall at the Amazon EC2 instance lev...
- [Q883 - Question 209](#q883-209): Which AWS service or feature helps restrict the AWS services, resources, and ind...
- [Q884 - Question 210](#q884-210): What is the best resource for a user to find compliance-related information and ...
- [Q889 - Question 211](#q889-211): A user would like to encrypt data that is received, stored, and managed by AWS C...
- [Q895 - Question 212](#q895-212): Which AWS service provides the ability to detect inadvertent data leaks of perso...
- [Q898 - Question 213](#q898-213): Which of the following describes a security best practice that can be implemente...
- [Q901 - Question 214](#q901-214): A company needs protection from expanded distributed denial of service (DDoS) at...
- [Q903 - Question 215](#q903-215): Under the AWS shared responsibility model, what are the customer's responsibilit...
- [Q906 - Question 216](#q906-216): Which of the following allows an application running on an Amazon EC2 instance t...
- [Q912 - Question 217](#q912-217): Which of the following tasks can only be performed after signing in with AWS acc...
- [Q917 - Question 218](#q917-218): A company is launching an e-commerce site that will store and process credit car...
- [Q919 - Question 219](#q919-219): Which AWS service can be used to track unauthorized API calls?...
- [Q920 - Question 220](#q920-220): A user needs to regularly audit and evaluate the setup of all AWS resources, ide...
- [Q924 - Question 221](#q924-221): A user needs to automatically discover, classify, and protect sensitive data sto...
- [Q928 - Question 222](#q928-222): What is the MOST effective resource for staying up to date on AWS security annou...
- [Q931 - Question 223](#q931-223): Which AWS service allows users to download security and compliance reports about...
- [Q936 - Question 224](#q936-224): During a compliance review, an auditor requests AWS compliance documentation suc...
- [Q941 - Question 225](#q941-225): A company wants to allow full access to an Amazon S3 bucket for a particular use...
- [Q945 - Question 226](#q945-226): Under the AWS shared responsibility model, which of the following is a responsib...
- [Q954 - Question 227](#q954-227): Which AWS service can be used to track resource changes and establish compliance...
- [Q959 - Question 228](#q959-228): A developer has been hired by a large company and needs AWS credentials. Which a...
- [Q962 - Question 229](#q962-229): A user is planning to migrate an application workload to the AWS Cloud. Which co...
- [Q969 - Question 230](#q969-230): A company wants to ensure that AWS Management Console users are meeting password...
- [Q970 - Question 231](#q970-231): Under the AWS shared responsibility model, which of the following is the custome...
- [Q971 - Question 232](#q971-232): Which of the following tasks is required to deploy a PCI-compliant workload on A...
- [Q977 - Question 233](#q977-233): A web developer is concerned that a DDoS attack could target an application. Whi...
- [Q978 - Question 234](#q978-234): Which AWS service gives users on-demand, self-service access to AWS compliance c...
- [Q979 - Question 235](#q979-235): A company wants to provide one of its employees with access to Amazon RDS. The c...
- [Q980 - Question 236](#q980-236): A company has a compliance requirement to record and evaluate configuration chan...
- [Q984 - Question 237](#q984-237): Which of the following is the customer's responsibility when using Amazon RDS?...
- [Q985 - Question 238](#q985-238): What is the customer's responsibility when using AWS Lambda?...
- [Q992 - Question 239](#q992-239): Which AWS service should a cloud practitioner use to identify security vulnerabi...
- [Q997 - Question 240](#q997-240): Which AWS service can be used to retrieve compliance reports on demand?...
- [Q998 - Question 241](#q998-241): A company has an AWS-hosted website located behind an Application Load Balancer....
- [Q1001 - Question 242](#q1001-242): An external auditor has requested that a company provide a list of all its IAM u...
- [Q1004 - Question 243](#q1004-243): A company wants to track AWS resource configuration changes for compliance reaso...
- [Q1006 - Question 244](#q1006-244): The AWS IAM best practice for granting least privilege is to:...
- [Q1010 - Question 245](#q1010-245): Which AWS service or feature can be used to prevent SQL injection attacks?...
- [Q1104 - Question 246](#q1104-246): A company needs to continuously assess its AWS environment against compliance fr...
- [Q1105 - Question 247](#q1105-247): Which AWS service helps simplify audit preparation by automatically collecting a...

---

<a id="q003-1"></a>
### Question 1 (`Q003`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> You have noticed that several critical Amazon EC2 instances have been terminated. Which of the following AWS services would help you determine who took this action?

#### Options
- **A.** Amazon Inspector
- **B.** AWS CloudTrail **[CORRECT]**
- **C.** AWS Trusted Advisor
- **D.** EC2 Instance Usage Report

**Correct Answer:** `B`

#### Detailed Explanation

AWS CloudTrail records all API calls and account activity across an AWS environment, capturing who performed each action, from which IP address, and at what time, making it the definitive source for identifying who terminated EC2 instances.

Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not record who performed API actions or management events. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool rather than an audit log of account activity. EC2 Instance Usage Report provides billing and usage data about EC2 instances and does not contain API call logs or identity information about who terminated instances.

---

<a id="q005-2"></a>
### Question 2 (`Q005`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which statement is true regarding the AWS Shared Responsibility Model?

#### Options
- **A.** Responsibilities vary depending on the services used **[CORRECT]**
- **B.** Security of the IaaS services is the responsibility of AWS
- **C.** Patching the guest OS is always the responsibility of AWS
- **D.** Security of the managed services is the responsibility of the customer

**Correct Answer:** `A`

#### Detailed Explanation

Under the Shared Responsibility Model, who is responsible for what shifts depending on the service type, with AWS taking on more responsibility for managed services while customers handle more of the stack for IaaS services.

Security of IaaS services is not solely AWS's responsibility, as customers using IaaS must manage the guest operating system, application stack, and data, while AWS is only responsible for the underlying infrastructure. Patching the guest OS is not always AWS's responsibility, as for IaaS services such as EC2 the customer is fully responsible for patching the operating system they run on their instances. Security of managed services is not solely the customer's responsibility, as AWS takes on significantly more of the security burden for managed services such as RDS and Lambda, covering the underlying platform and infrastructure layers.

---

<a id="q011-3"></a>
### Question 3 (`Q011`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> An organization has a large number of technical employees who operate their AWS Cloud infrastructure. What does AWS provide to help organize them into teams and then assign the appropriate permissions for each team?

#### Options
- **A.** IAM roles
- **B.** IAM users
- **C.** IAM user groups **[CORRECT]**
- **D.** AWS Organizations

**Correct Answer:** `C`

#### Detailed Explanation

IAM user groups let you organize multiple users together and assign shared permissions at the group level via IAM policies, making it easy to manage access for entire teams without configuring each user individually.

IAM roles provide temporary security credentials that can be assumed by users, services, or applications, and are not designed to organize teams or assign shared permissions to a fixed set of users in the way groups are. IAM users are individual identities each with their own credentials and permissions, and managing large numbers of users individually by attaching policies to each one is impractical compared to using groups. AWS Organizations manages multiple AWS accounts under a single structure for consolidated billing and policy enforcement, and is not the service used to organize individual IAM users into teams within a single account.

---

<a id="q022-4"></a>
### Question 4 (`Q022`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What does the "Principle of Least Privilege" refer to?

#### Options
- **A.** You should grant your users only the permissions they need when they need them and nothing more **[CORRECT]**
- **B.** All IAM users should have at least the necessary permissions to access the core AWS services
- **C.** All trusted IAM users should have access to any AWS service in the respective AWS account
- **D.** IAM users should not be granted any permissions; to keep your account safe

**Correct Answer:** `A`

#### Detailed Explanation

The Principle of Least Privilege means granting users only the exact permissions they need to perform their job and nothing beyond that, minimizing the risk of accidental or malicious misuse of AWS resources.

Granting IAM users at least the necessary permissions to access core AWS services describes a minimum baseline, which is the opposite of least privilege; least privilege means restricting permissions to only what is needed for a specific task rather than ensuring access to common services. Granting all trusted users access to any AWS service in the account contradicts least privilege by providing broad unrestricted access rather than targeted permissions. Granting no permissions to any IAM user is not a practical interpretation of least privilege, which is about granting the minimum required permissions rather than granting none at all.

---

<a id="q026-5"></a>
### Question 5 (`Q026`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Hundreds of thousands of DDoS attacks are recorded every month worldwide. What service does AWS provide to help protect AWS Customers from these attacks?

#### Options
- **A.** AWS Shield **[CORRECT]**
- **B.** AWS Config
- **C.** Amazon Cognito
- **D.** AWS WAF **[CORRECT]**
- **E.** AWS KMS

**Correct Answer:** `A, D`

#### Detailed Explanation

AWS Shield provides managed DDoS protection at the network and transport layers, and AWS WAF lets you create rules that filter malicious web traffic at the application layer. Together they defend against the full spectrum of DDoS attacks.

AWS Config continuously monitors and records AWS resource configurations to evaluate compliance, and is a configuration management and auditing service with no capability to block or mitigate DDoS traffic. Amazon Cognito is a user identity and authentication service for web and mobile applications, providing sign-up and sign-in functionality and federated identity, and has no DDoS mitigation capabilities. AWS KMS is a key management service for creating and controlling encryption keys used to protect data, and is not involved in network traffic filtering or DDoS defense.

---

<a id="q031-6"></a>
### Question 6 (`Q031`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services allows customers to manage their agreements with AWS?

#### Options
- **A.** AWS Artifact **[CORRECT]**
- **B.** AWS Certificate Manager
- **C.** AWS Systems Manager
- **D.** AWS Organizations

**Correct Answer:** `A`

#### Detailed Explanation

AWS Artifact is a self-service portal where customers can access and manage AWS compliance reports and agreements, including NDA and Business Associate Addendum (BAA) documents that govern the relationship between customers and AWS.

AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services, and is a certificate management service rather than an agreement management portal. AWS Systems Manager provides operational tools for managing AWS resources at scale including patching, parameter storage, and session management, and is not used to manage contractual agreements with AWS. AWS Organizations manages multiple AWS accounts under a master account structure for consolidated billing and service control policies, and is not a portal for managing compliance reports or agreements.

---

<a id="q032-7"></a>
### Question 7 (`Q032`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following are examples of AWS-managed services, where AWS is responsible for the operational and maintenance burdens of running the service?

#### Options
- **A.** Amazon VPC
- **B.** Amazon DynamoDB **[CORRECT]**
- **C.** Amazon EMR **[CORRECT]**
- **D.** AWS IAM
- **E.** Amazon Elastic Compute Cloud

**Correct Answer:** `B, C`

#### Detailed Explanation

Amazon DynamoDB and Amazon EMR are fully managed services where AWS handles provisioning, patching, scaling, and maintenance automatically, freeing customers from managing the underlying infrastructure.

Amazon VPC is a networking construct that customers configure and manage themselves, including subnets, route tables, internet gateways, and security groups, making it a customer-configured resource rather than a fully managed service. AWS IAM is a service customers use to manage their own users, roles, and permissions, and while AWS maintains the IAM infrastructure, customers are responsible for all identity and access configuration. Amazon Elastic Compute Cloud provides virtual servers where customers are responsible for the operating system, installed software, patches, and configuration, making it an infrastructure service where the customer manages the virtual machine layer rather than a fully managed one.

---

<a id="q036-8"></a>
### Question 8 (`Q036`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following must an IAM user provide to interact with AWS services using the AWS Command Line Interface (AWS CLI)?

#### Options
- **A.** Access keys **[CORRECT]**
- **B.** Secret token
- **C.** UserID
- **D.** User name and password

**Correct Answer:** `A`

#### Detailed Explanation

IAM access keys, consisting of an access key ID and secret access key, are the credentials used to authenticate API requests programmatically through the AWS CLI, allowing IAM users to interact with AWS services from the command line without the Management Console.

A secret token is not a standard IAM credential type for CLI access; temporary security credentials issued to IAM roles include a session token in addition to an access key ID and secret, but a standalone secret token alone is not used for CLI authentication. A UserID is an internal AWS identifier assigned to IAM users but is not a credential that can be supplied to authenticate CLI requests. A user name and password are the credentials used to log in to the AWS Management Console interactively, not to authenticate programmatic CLI requests which require access keys.

---

<a id="q037-9"></a>
### Question 9 (`Q037`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> You have AWS Basic support, and you have discovered that some AWS resources are being used maliciously, and those resources could potentially compromise your data. What should you do?

#### Options
- **A.** Contact the AWS Customer Service team
- **B.** Contact the AWS Abuse Team **[CORRECT]**
- **C.** Contact the AWS Concierge team
- **D.** Contact the AWS Security team

**Correct Answer:** `B`

#### Detailed Explanation

The AWS Abuse Team handles reports of AWS infrastructure being used for malicious activity such as hacking, spam, or unauthorised use, and this channel is available to all customers regardless of their support tier.

The AWS Customer Service team handles general account and billing enquiries, and is not the designated contact for reporting malicious use of AWS infrastructure. The AWS Concierge team is a dedicated support resource available exclusively to Enterprise support plan customers for billing and account assistance, and does not handle abuse or malicious activity reports. The AWS Security team manages AWS's own internal security posture and vulnerability disclosure program, and is not the correct channel for customers to report malicious use of AWS resources within their own accounts.

---

<a id="q038-10"></a>
### Question 10 (`Q038`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following are examples of AWS shared controls?

#### Options
- **A.** Patch Management **[CORRECT]**
- **B.** IAM Management
- **C.** VPC Management
- **D.** Configuration Management **[CORRECT]**
- **E.** Data Center operations

**Correct Answer:** `A, D`

#### Detailed Explanation

Patch Management and Configuration Management are both shared controls where AWS and the customer each manage their own layer independently, with AWS responsible for the infrastructure and customers responsible for their own operating systems and applications.

IAM Management is a customer responsibility, as customers exclusively control their own users, roles, and permissions within their AWS account. VPC Management is a customer responsibility, as customers define and configure their own virtual network settings including subnets, route tables, and security groups. Data Center operations are exclusively AWS's responsibility, covering all physical infrastructure management.

---

<a id="q043-11"></a>
### Question 11 (`Q043`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the shared responsibility model, which of the following is the responsibility of AWS?

#### Options
- **A.** Client-side encryption
- **B.** Configuring infrastructure devices **[CORRECT]**
- **C.** Server-side encryption
- **D.** Filtering traffic with Security Groups

**Correct Answer:** `B`

#### Detailed Explanation

Configuring infrastructure devices such as networking hardware and physical servers is entirely AWS's responsibility, as customers have no access to or control over the underlying physical infrastructure.

Client-side encryption is the customer's responsibility, as customers choose whether and how to encrypt data before sending it to AWS. Server-side encryption is also the customer's responsibility, as customers decide whether to enable encryption at rest for their data stored in AWS services. Filtering traffic with Security Groups is the customer's responsibility, as customers define and manage their own Security Group rules within their AWS environment.

---

<a id="q046-12"></a>
### Question 12 (`Q046`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Your company is developing a critical web application in AWS, and the security of the application is a top priority. Which of the following AWS services will provide infrastructure security optimization recommendations?

#### Options
- **A.** AWS Shield
- **B.** AWS Management Console
- **C.** AWS Secrets Manager
- **D.** AWS Trusted Advisor **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS Trusted Advisor inspects your AWS environment and provides real-time recommendations across five categories including security, cost optimization, performance, fault tolerance, and service limits, helping you follow AWS best practices.

AWS Shield is a managed DDoS protection service that defends against distributed denial of service attacks, and does not provide broad infrastructure security recommendations. AWS Management Console is the web-based interface for accessing and managing AWS services, and does not analyze or make recommendations about your environment. AWS Secrets Manager is a service for storing, rotating, and managing access to secrets such as database credentials and API keys, and does not provide infrastructure optimization recommendations.

---

<a id="q048-13"></a>
### Question 13 (`Q048`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> In the AWS Shared responsibility Model, which of the following are the responsibility of the customer?

#### Options
- **A.** Disk disposal
- **B.** Controlling physical access to compute resources
- **C.** Patching the Network infrastructure
- **D.** Setting password complexity rules **[CORRECT]**
- **E.** Configuring network access rules **[CORRECT]**

**Correct Answer:** `D, E`

#### Detailed Explanation

Setting password complexity rules and configuring network access rules such as security groups and NACLs are both customer responsibilities, as customers control their own identity policies and network configuration within their AWS environment.

Disk disposal is AWS's responsibility, as AWS manages the secure decommissioning and destruction of physical storage hardware. Controlling physical access to compute resources is AWS's responsibility, as customers have no access to the underlying physical infrastructure. Patching the network infrastructure is AWS's responsibility, covering the managed networking layer beneath the customer's virtual network.

---

<a id="q056-14"></a>
### Question 14 (`Q056`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is the customer's responsibility under the AWS shared responsibility model?

#### Options
- **A.** Patching underlying infrastructure
- **B.** Physical security
- **C.** Patching Amazon EC2 instances **[CORRECT]**
- **D.** Patching network infrastructure

**Correct Answer:** `C`

#### Detailed Explanation

Customers are responsible for patching the operating system and software on EC2 instances they launch, as the guest OS and everything running on it falls within the customer's side of the Shared Responsibility Model.

Patching underlying infrastructure is AWS's responsibility, covering the hypervisor and physical hardware beneath the customer's instances. Physical security is AWS's responsibility exclusively, as customers have no access to or control over AWS data centers. Patching network infrastructure is AWS's responsibility, covering the managed networking layer that underpins all customer virtual networks.

---

<a id="q057-15"></a>
### Question 15 (`Q057`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> According to the AWS shared responsibility model who is responsible for configuration management?

#### Options
- **A.** It is solely the responsibility of the customer
- **B.** It is solely the responsibility of AWS
- **C.** It is shared between AWS and the customer **[CORRECT]**
- **D.** It is not part of the AWS shared responsibility model

**Correct Answer:** `C`

#### Detailed Explanation

Configuration management is a shared control where AWS manages the configuration of its infrastructure, while the customer is responsible for configuring the operating systems, databases, and applications they deploy.

Configuration management is not solely the customer's responsibility, as AWS independently manages the configuration of all underlying infrastructure components including hardware, networking, and managed services. Configuration management is not solely AWS's responsibility, as customers retain full accountability for configuring the resources and workloads they deploy on top of the AWS infrastructure. Configuration management is explicitly recognized as a shared control in the AWS Shared Responsibility Model and is therefore fully accounted for within it.

---

<a id="q058-16"></a>
### Question 16 (`Q058`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which security service automatically recognizes and classifies sensitive data or intellectual property on AWS?

#### Options
- **A.** Amazon GuardDuty
- **B.** Amazon Macie **[CORRECT]**
- **C.** Amazon Inspector
- **D.** AWS Shield

**Correct Answer:** `B`

#### Detailed Explanation

Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data such as personally identifiable information and intellectual property stored in Amazon S3, making it the correct service for automatically recognizing and classifying sensitive data.

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity and anomalous behavior using machine learning and threat intelligence, and focuses on detecting security threats rather than classifying data. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not classify or discover sensitive data stored in S3. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to recognize or classify sensitive data.

---

<a id="q060-17"></a>
### Question 17 (`Q060`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the shared responsibility model, which of the following tasks are the responsibility of the AWS customer?

#### Options
- **A.** Ensuring that application data is encrypted at rest **[CORRECT]**
- **B.** Ensuring that AWS NTP servers are set to the correct time
- **C.** Ensuring that users have received security training in the use of AWS services **[CORRECT]**
- **D.** Ensuring that access to data centers is restricted
- **E.** Ensuring that hardware is disposed of properly

**Correct Answer:** `A, C`

#### Detailed Explanation

Customers are responsible for encrypting their application data at rest and for training their users on proper security practices when using AWS services, both sitting on the customer side of the model.

Ensuring that AWS NTP servers are set to the correct time is entirely AWS's responsibility, as customers have no access to or control over the underlying infrastructure components that provide time synchronisation. Ensuring that access to data centers is restricted is entirely AWS's responsibility, covering physical access controls, surveillance, and protection of the facilities that house AWS infrastructure. Ensuring that hardware is disposed of properly is entirely AWS's responsibility, as customers never take possession of physical hardware and AWS manages all end-of-life processes for its own equipment.

---

<a id="q064-18"></a>
### Question 18 (`Q064`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service allows users to identify the changes made to a resource over time?

#### Options
- **A.** Amazon Inspector
- **B.** AWS Config **[CORRECT]**
- **C.** AWS Service Catalog
- **D.** AWS IAM

**Correct Answer:** `B`

#### Detailed Explanation

AWS Config continuously tracks and records configuration changes to AWS resources over time, allowing you to review historical configurations and identify what changed and when.

Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances for security findings, not a service for tracking configuration changes over time. AWS Service Catalog allows organizations to create and manage approved portfolios of IT services for deployment, unrelated to tracking resource changes. AWS IAM manages user identities, roles, and access permissions within an AWS account and does not record or track configuration changes to resources.

---

<a id="q075-19"></a>
### Question 19 (`Q075`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Access keys in AWS Identity and Access Management (IAM) are used to:

#### Options
- **A.** Log in to the AWS Management Console
- **B.** Make programmatic calls to AWS from AWS APIs **[CORRECT]**
- **C.** Log in to Amazon EC2 instances
- **D.** Authenticate to AWS CodeCommit repositories

**Correct Answer:** `B`

#### Detailed Explanation

IAM access keys, consisting of an access key ID and a secret access key, are the credentials used to authenticate programmatic calls to AWS APIs via the CLI, SDKs, or direct HTTP requests, allowing applications and scripts to interact with AWS services without using the console.

Logging in to the AWS Management Console requires a user name and password combination, not access keys, which are reserved for programmatic and CLI access rather than browser-based console authentication. Logging in to Amazon EC2 instances uses SSH key pairs on Linux instances or a password retrieved via the console for Windows instances, and is separate from the IAM access keys used for API authentication. Authenticating to AWS CodeCommit repositories uses Git credentials or SSH keys configured separately from IAM access keys, though access keys can be used with the AWS CLI to interact with CodeCommit programmatically.

---

<a id="q078-20"></a>
### Question 20 (`Q078`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which AWS services can be used to gather information about AWS account activity?

#### Options
- **A.** Amazon CloudFront
- **B.** AWS Cloud9
- **C.** AWS CloudTrail **[CORRECT]**
- **D.** AWS CloudHSM
- **E.** Amazon CloudWatch **[CORRECT]**

**Correct Answer:** `C, E`

#### Detailed Explanation

AWS CloudTrail logs all API calls and account activity across an AWS account, providing a complete audit trail of who did what and when. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources, providing operational visibility into account activity and performance.

Amazon CloudFront is a content delivery network that caches and distributes content to users at edge locations worldwide, and does not gather information about account activity. AWS Cloud9 is a cloud-based integrated development environment for writing, running, and debugging code, and has no account monitoring or activity logging capability. AWS CloudHSM is a hardware security module service that manages and stores cryptographic keys in dedicated hardware, and is not a tool for monitoring or gathering information about account activity.

---

<a id="q090-21"></a>
### Question 21 (`Q090`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS IAM feature allows developers to access AWS services through the AWS CLI?

#### Options
- **A.** API keys
- **B.** Access keys **[CORRECT]**
- **C.** User names/Passwords
- **D.** SSH keys

**Correct Answer:** `B`

#### Detailed Explanation

IAM access keys, consisting of an access key ID and a secret access key, are the credentials used to authenticate programmatic requests to AWS services through the AWS CLI and SDKs.

API keys is an informal term not specific to AWS IAM; AWS programmatic access uses access keys consisting of an access key ID and secret access key, and this informal label does not accurately describe the credential type. User names and passwords are used to log in to the AWS Management Console interactively, and are not the credentials used for CLI or SDK programmatic access, which requires access keys. SSH keys are used to connect securely to EC2 instances via Secure Shell and are not the credentials that authenticate developers' CLI requests to AWS services.

---

<a id="q091-22"></a>
### Question 22 (`Q091`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> The user is fully responsible for which action when running workloads on AWS?

#### Options
- **A.** Patching the infrastructure components
- **B.** Maintaining the underlying infrastructure components
- **C.** Maintaining physical and environmental controls
- **D.** Implementing controls to route application traffic **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Customers are fully responsible for implementing application-level controls such as routing traffic within their own systems, as these decisions sit entirely within the customer's layer of the Shared Responsibility Model.

Patching the infrastructure components is AWS's responsibility, covering the physical servers, networking equipment, and hypervisor layer beneath the customer's workloads. Maintaining the underlying infrastructure components is AWS's responsibility, as customers have no access to or control over the physical hardware running their workloads. Maintaining physical and environmental controls is AWS's responsibility exclusively, covering data center facilities, power, cooling, and physical security.

---

<a id="q103-23"></a>
### Question 23 (`Q103`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following will enhance the security of access to the AWS Management Console?

#### Options
- **A.** AWS Secrets Manager
- **B.** AWS Certificate Manager
- **C.** AWS Multi-Factor Authentication (AWS MFA) **[CORRECT]**
- **D.** Security groups
- **E.** Password policies **[CORRECT]**

**Correct Answer:** `C, E`

#### Detailed Explanation

MFA adds a second authentication factor beyond a password to protect console logins, and password policies enforce complexity and rotation requirements. Both directly enhance the security of access to the AWS Management Console.

AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service rather than a mechanism for enhancing the authentication security of the AWS Management Console itself. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and has no role in controlling or securing console login access. Security groups act as virtual firewalls that control inbound and outbound network traffic at the EC2 instance level, and operate at the network layer rather than the console authentication layer.

---

<a id="q105-24"></a>
### Question 24 (`Q105`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> For which auditing process does AWS have sole responsibility?

#### Options
- **A.** AWS IAM policies
- **B.** Physical security **[CORRECT]**
- **C.** Amazon S3 bucket policies
- **D.** AWS CloudTrail Logs

**Correct Answer:** `B`

#### Detailed Explanation

Under the shared responsibility model, AWS has sole responsibility for physical security of its data centers, including controls such as perimeter security, surveillance, and hardware disposal, as customers never have access to AWS physical facilities.

AWS IAM policies define permissions for users, groups, and roles within an AWS account, and creating, managing, and auditing these policies is entirely the customer's responsibility as they reflect each customer's own access control decisions. Amazon S3 bucket policies control access to objects stored within S3 buckets, and configuring and auditing these policies is the customer's responsibility as they govern how the customer's own data is accessed and shared. AWS CloudTrail logs record API calls and account activity across an AWS environment, and while CloudTrail is an AWS-managed service, enabling it, configuring log retention, and auditing the logs it produces are all customer responsibilities.

---

<a id="q107-25"></a>
### Question 25 (`Q107`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following common IT tasks can AWS cover to free up company IT resources?

#### Options
- **A.** Patching database software **[CORRECT]**
- **B.** Testing application releases
- **C.** Backing up databases **[CORRECT]**
- **D.** Creating database schema
- **E.** Running penetration tests

**Correct Answer:** `A, C`

#### Detailed Explanation

Patching database software and backing up databases are maintenance tasks that AWS handles automatically for managed services such as RDS, freeing up customers' IT resources from these time-consuming operational responsibilities.

Testing application releases is the customer's responsibility as it requires knowledge of the specific application logic, acceptance criteria, and business requirements that only the customer possesses, making it a task AWS cannot cover on the customer's behalf. Creating database schema requires understanding of the customer's data model and application requirements, and is a design and development activity that the customer must perform rather than a managed service task AWS provides. Running penetration tests is a security activity that customers perform on their own applications and infrastructure, and is not an operational burden AWS covers as part of its managed service offerings.

---

<a id="q114-26"></a>
### Question 26 (`Q114`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> If a customer needs to audit the change management of AWS resources, which of the following AWS services should the customer use?

#### Options
- **A.** AWS Config **[CORRECT]**
- **B.** AWS Trusted Advisor
- **C.** Amazon CloudWatch
- **D.** Amazon Inspector

**Correct Answer:** `A`

#### Detailed Explanation

AWS Config continuously records resource configurations and changes over time, providing a detailed audit trail of what changed, when it changed, and who made the change, making it the purpose-built service for auditing change management of AWS resources.

AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, but does not record or audit configuration changes to individual resources over time. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and does not track resource configuration history or change management. Amazon Inspector is an automated security assessment service that scans for software vulnerabilities and unintended network exposure, and is a security testing tool rather than a configuration change auditing service.

---

<a id="q117-27"></a>
### Question 27 (`Q117`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following Identity and Access Management (IAM) entities is associated with an access key ID and secret access key when using AWS Command Line Interface (AWS CLI)?

#### Options
- **A.** IAM group
- **B.** IAM user **[CORRECT]**
- **C.** IAM role
- **D.** IAM policy

**Correct Answer:** `B`

#### Detailed Explanation

IAM users are the entities that have access keys consisting of an access key ID and secret access key associated with them for programmatic CLI access to AWS services.

An IAM group is a collection of IAM users used to manage shared permissions collectively, and is not an identity that can authenticate or be issued access keys of any kind. An IAM role uses temporary security credentials that are automatically issued and rotated when the role is assumed, and does not have permanent access keys associated with it. An IAM policy is a JSON document that defines permissions by specifying allowed or denied actions on resources, and is a permissions construct rather than an identity that can hold or be associated with access keys.

---

<a id="q118-28"></a>
### Question 28 (`Q118`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the shared responsibility model, which of the following is the customer responsible for?

#### Options
- **A.** Ensuring that disk drives are wiped after use
- **B.** Ensuring that firmware is updated on hardware devices
- **C.** Ensuring that data is encrypted at rest **[CORRECT]**
- **D.** Ensuring that network cables are category six or higher

**Correct Answer:** `C`

#### Detailed Explanation

Data encryption at rest is a customer responsibility. AWS provides the tools and services to enable encryption, but customers decide whether and how to encrypt their data.

Ensuring disk drives are wiped after use is AWS's responsibility. AWS handles the secure decommissioning and disposal of physical storage hardware. Ensuring firmware is updated on hardware devices is AWS's responsibility. Customers have no access to or control over physical hardware. Ensuring network cables are category six or higher is AWS's responsibility. Physical networking infrastructure is managed entirely by AWS.

---

<a id="q120-29"></a>
### Question 29 (`Q120`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> What credential components are required to gain programmatic access to an AWS account?

#### Options
- **A.** An access key ID **[CORRECT]**
- **B.** A primary key
- **C.** A secret access key **[CORRECT]**
- **D.** A user ID
- **E.** A secondary key

**Correct Answer:** `A, C`

#### Detailed Explanation

Programmatic AWS access requires an access key ID to identify the calling entity and a secret access key to sign requests, together authenticating API calls made via the CLI or SDKs.

A primary key is not a valid AWS IAM credential component; it is a database term for a unique row identifier and has no role in AWS programmatic authentication. A user ID is an internal AWS identifier assigned to IAM users for tracking purposes but cannot be supplied as a credential to authenticate programmatic API requests. A secondary key is not a recognized AWS IAM credential type, and no such concept exists in the AWS authentication model for programmatic access.

---

<a id="q121-30"></a>
### Question 30 (`Q121`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is a shared control between the customer and AWS?

#### Options
- **A.** Providing a key for Amazon S3 client-side encryption
- **B.** Configuration of an Amazon EC2 instance
- **C.** Environmental controls of physical AWS data centers
- **D.** Awareness **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Awareness and training is a shared control because both AWS and the customer must independently ensure their own staff understand their respective security responsibilities, regardless of what the other party does.

Providing a key for Amazon S3 client-side encryption is solely the customer's responsibility, as AWS has no involvement in client-side key generation or management. Configuration of an Amazon EC2 instance is solely the customer's responsibility, as customers control the guest OS and everything installed on it. Environmental controls of physical AWS data centers are solely AWS's responsibility, as customers have no access to or involvement in physical facility management.

---

<a id="q126-31"></a>
### Question 31 (`Q126`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following security measures protect access to an AWS account?

#### Options
- **A.** Enable AWS CloudTrail
- **B.** Grant least privilege access to IAM users **[CORRECT]**
- **C.** Create one IAM user and share with many developers and users
- **D.** Enable Amazon CloudFront
- **E.** Activate multi-factor authentication (MFA) for privileged users **[CORRECT]**

**Correct Answer:** `B, E`

#### Detailed Explanation

Granting least privilege access ensures IAM users only have the permissions they need, reducing the blast radius of a compromised account, and activating MFA for privileged users adds a critical second authentication factor that protects against stolen credentials. Both directly protect access to an AWS account.

Enabling AWS CloudTrail records API calls and account activity for auditing and compliance, and while it improves visibility into account actions after the fact, it does not prevent unauthorised access and is therefore not a security measure that protects access. Creating one IAM user shared across many developers is a security anti-pattern because it prevents individual accountability, makes credential rotation difficult, and means that a single compromised credential grants access to everyone sharing that account. Enabling Amazon CloudFront provides a content delivery network for distributing web content globally, and has no connection to protecting access to an AWS account.

---

<a id="q144-32"></a>
### Question 32 (`Q144`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which activity is a customer responsibility in the AWS Cloud according to the AWS shared responsibility model?

#### Options
- **A.** Ensuring network connectivity from AWS to the internet
- **B.** Patching and fixing flaws within the AWS Cloud infrastructure
- **C.** Ensuring the physical security of cloud data centers
- **D.** Ensuring Amazon EBS volumes are backed up **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Under the Shared Responsibility Model, backing up EBS volumes through snapshots is the customer's responsibility, as AWS does not automatically back up EBS volumes on the customer's behalf.

Ensuring network connectivity from AWS to the internet is entirely AWS's responsibility, as AWS manages and maintains the underlying network infrastructure that connects its services to the public internet. Patching and fixing flaws within the AWS Cloud infrastructure is entirely AWS's responsibility, as customers have no access to the underlying hardware, hypervisors, or physical networking components. Ensuring the physical security of cloud data centers is entirely AWS's responsibility, covering access controls, surveillance, and protection of the facilities that house AWS infrastructure.

---

<a id="q150-33"></a>
### Question 33 (`Q150`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> How can a customer increase security to AWS account logons?

#### Options
- **A.** Configure AWS Certificate Manager
- **B.** Enable Multi-Factor Authentication (MFA) **[CORRECT]**
- **C.** Use Amazon Cognito to manage access
- **D.** Configure a strong password policy **[CORRECT]**
- **E.** Enable AWS Organizations

**Correct Answer:** `B, D`

#### Detailed Explanation

Enabling MFA requires a second factor beyond the password to complete sign-in, and configuring a strong password policy enforces complexity, length, and rotation requirements. Both directly strengthen AWS account logon security.

AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and has no role in controlling or securing account logon processes. Amazon Cognito manages user authentication and access for customer-facing applications through user pools and identity pools, and is designed for application-level user management rather than securing AWS account logons directly. AWS Organizations is an account management service for centrally governing and consolidating multiple AWS accounts, and does not itself provide logon security features for individual account access.

---

<a id="q158-34"></a>
### Question 34 (`Q158`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service is used to track, record, and audit configuration changes made to AWS resources?

#### Options
- **A.** AWS Shield
- **B.** AWS Config **[CORRECT]**
- **C.** AWS Identity and Access Management (IAM)
- **D.** Amazon Inspector

**Correct Answer:** `B`

#### Detailed Explanation

AWS Config continuously records configuration changes to AWS resources and maintains a history of those changes, enabling audit and compliance reviews of how resources have been configured over time.

AWS Shield is a managed DDoS protection service that safeguards AWS applications against distributed denial-of-service attacks, and has no capability to track or audit resource configuration changes. AWS Identity and Access Management (IAM) is a service for controlling who can authenticate and what actions they are authorised to perform, and manages permissions and identities rather than recording configuration changes to AWS resources. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a security testing tool rather than a configuration change tracking or auditing service.

---

<a id="q162-35"></a>
### Question 35 (`Q162`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services falls under the responsibility of the customer to maintain operating system configuration, security patching, and networking?

#### Options
- **A.** Amazon RDS
- **B.** Amazon EC2 **[CORRECT]**
- **C.** Amazon ElastiCache
- **D.** AWS Fargate

**Correct Answer:** `B`

#### Detailed Explanation

With Amazon EC2, the customer is responsible for the guest operating system including configuration, security patching, and networking setup, as AWS only manages the underlying physical infrastructure.

Amazon RDS is a fully managed relational database service where AWS handles operating system patching, database engine updates, and infrastructure maintenance on the customer's behalf. Amazon ElastiCache is a fully managed in-memory caching service where AWS manages the underlying operating system and infrastructure, removing those responsibilities from the customer entirely. AWS Fargate is a serverless compute engine for containers where AWS manages the underlying infrastructure and operating system, meaning the customer only needs to manage their container images and application code.

---

<a id="q163-36"></a>
### Question 36 (`Q163`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> AWS supports which of the following methods to add security to Identity and Access Management (IAM) users?

#### Options
- **A.** Implementing Amazon Rekognition
- **B.** Using AWS Shield-protected resources
- **C.** Blocking access with Security Groups
- **D.** Using Multi-Factor Authentication (MFA) **[CORRECT]**
- **E.** Enforcing password strength and expiration **[CORRECT]**

**Correct Answer:** `D, E`

#### Detailed Explanation

MFA adds a second authentication factor beyond a password, and enforcing password strength and expiration policies reduce the risk of credential compromise. Both are supported IAM security methods that directly protect IAM user accounts.

Amazon Rekognition is a machine learning service for analyzing images and videos to detect objects, faces, and text, and has no role in adding security to IAM user authentication. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service rather than a mechanism for securing IAM user accounts. Security groups act as virtual firewalls that control inbound and outbound network traffic at the EC2 instance level, and operate at the network layer rather than the IAM authentication layer.

---

<a id="q169-37"></a>
### Question 37 (`Q169`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A Cloud Practitioner must determine if any security groups in an AWS account have been provisioned to allow unrestricted access for specific ports. What is the SIMPLEST way to do this?

#### Options
- **A.** Review the inbound rules for each security group in the Amazon EC2 management console to check for port 0.0.0.0/0
- **B.** Run AWS Trusted Advisor and review the findings **[CORRECT]**
- **C.** Open the AWS IAM console and check the inbound rule filters for open access
- **D.** In AWS Config, create a custom rule that invokes an AWS Lambda function to review firewall rules for inbound access

**Correct Answer:** `B`

#### Detailed Explanation

AWS Trusted Advisor automatically scans your account and flags security groups with unrestricted access (0.0.0.0/0) to specific ports as part of its Security category checks, making it the simplest and most direct approach without manual investigation.

Manually reviewing inbound rules for each security group in the EC2 console to look for 0.0.0.0/0 entries would work but is time-consuming and error-prone at scale, making it far less simple than using Trusted Advisor's automated check. The AWS IAM console manages identities, users, roles, and permissions, and does not contain security group configurations or inbound traffic rules, making it the wrong place to check for unrestricted port access. Creating a custom AWS Config rule that invokes a Lambda function to review firewall rules would provide automated ongoing compliance checks but requires significant setup effort, making it far more complex than running the existing Trusted Advisor check.

---

<a id="q170-38"></a>
### Question 38 (`Q170`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following security-related services does AWS offer?

#### Options
- **A.** Multi-factor authentication physical tokens
- **B.** AWS Trusted Advisor security checks **[CORRECT]**
- **C.** Data encryption **[CORRECT]**
- **D.** Automated penetration testing
- **E.** Amazon S3 copyrighted content detection

**Correct Answer:** `B, C`

#### Detailed Explanation

AWS Trusted Advisor includes security checks that flag vulnerabilities such as open security groups, and AWS provides data encryption capabilities through services like KMS and native encryption across storage and database services. Both are genuine AWS security-related offerings.

Multi-factor authentication physical tokens are hardware MFA devices that customers purchase independently rather than a service provided by AWS; customers configure them with their accounts but AWS does not supply or manufacture the hardware tokens. Automated penetration testing is not an AWS service offering; AWS permits customers to conduct their own penetration testing on permitted services, but AWS does not perform automated penetration testing on customer workloads as a service. Amazon S3 copyrighted content detection is not an AWS service; Amazon Macie detects sensitive data categories such as PII in S3, but copyright detection is not within the scope of available AWS security services.

---

<a id="q171-39"></a>
### Question 39 (`Q171`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following services have Distributed Denial of Service (DDoS) mitigation features?

#### Options
- **A.** AWS WAF **[CORRECT]**
- **B.** Amazon DynamoDB
- **C.** Amazon EC2
- **D.** Amazon CloudFront **[CORRECT]**
- **E.** Amazon Inspector

**Correct Answer:** `A, D`

#### Detailed Explanation

AWS WAF filters malicious HTTP and HTTPS traffic at the application layer by blocking requests that match defined rules, and Amazon CloudFront integrates with AWS Shield to absorb volumetric DDoS attacks at edge locations before they reach origin servers. Both directly provide DDoS mitigation features.

Amazon DynamoDB is a fully managed NoSQL database service, and while AWS protects the underlying infrastructure it runs on, DynamoDB itself is not a service that provides DDoS mitigation features. Amazon EC2 provides virtual compute instances and does not include built-in DDoS mitigation; customers can configure security groups and use additional services like Shield and WAF to protect applications running on EC2. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not provide DDoS mitigation capabilities.

---

<a id="q175-40"></a>
### Question 40 (`Q175`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What can users access from AWS Artifact?

#### Options
- **A.** AWS security and compliance documents **[CORRECT]**
- **B.** A download of configuration management details for all AWS resources
- **C.** Training materials for AWS services
- **D.** A security assessment of the applications deployed in the AWS Cloud

**Correct Answer:** `A`

#### Detailed Explanation

AWS Artifact is a self-service portal that provides on-demand access to AWS security and compliance documents such as SOC reports, ISO certifications, PCI attestations, and other auditor-issued compliance materials.

Configuration management details are not available from Artifact; AWS Config tracks resource configuration history and CloudTrail logs API activity, but neither is reached through Artifact. Training materials come from AWS Training and Certification and AWS Skill Builder, not Artifact, which holds only compliance documents. A security assessment of deployed applications is performed by Amazon Inspector, which scans EC2 instances and container images for vulnerabilities, not by Artifact.

---

<a id="q179-41"></a>
### Question 41 (`Q179`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following can limit Amazon Simple Storage Service (Amazon S3) bucket access to specific users?

#### Options
- **A.** A public and private key-pair
- **B.** Amazon Inspector
- **C.** AWS Identity and Access Management (IAM) policies **[CORRECT]**
- **D.** Security Groups

**Correct Answer:** `C`

#### Detailed Explanation

IAM policies can be applied directly to IAM users or groups to control exactly who can access an S3 bucket and what operations they can perform, providing fine-grained access control that limits access to specific users.

Signing in with AWS account credentials provides root-level access to all S3 buckets by default rather than limiting access to specific users; root credentials should never be used for day-to-day access and do not restrict bucket access to particular individuals. Enabling S3 versioning preserves multiple versions of objects to protect against accidental deletion, and is a data recovery feature rather than an access restriction mechanism that limits which users can access the bucket. Setting a bucket policy to make the bucket private removes public access, but without specifying allowed principals it does not grant access to any specific users; additional policy statements identifying particular IAM principals are required to limit access to specific users.

---

<a id="q181-42"></a>
### Question 42 (`Q181`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Where are AWS compliance documents, such as an SOC 1 report, located?

#### Options
- **A.** Amazon Inspector
- **B.** AWS CloudTrail
- **C.** AWS Artifact **[CORRECT]**
- **D.** AWS Certificate Manager

**Correct Answer:** `C`

#### Detailed Explanation

AWS Artifact is the dedicated self-service portal for accessing AWS compliance documentation, including SOC 1, SOC 2, ISO 27001, and PCI DSS reports, allowing customers to download these documents for their own audit and compliance purposes.

Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and network exposure risks, and does not provide or store AWS compliance certifications or SOC reports. AWS CloudTrail logs all API calls and management events in an AWS account for auditing purposes, and produces customer-specific activity logs rather than AWS compliance certifications or third-party audit reports. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to encrypt data in transit, and is a certificate management service rather than a repository of compliance reports.

---

<a id="q182-43"></a>
### Question 43 (`Q182`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following tasks is the responsibility of AWS?

#### Options
- **A.** Encrypting client-side data
- **B.** Configuring AWS Identity and Access Management (IAM) roles
- **C.** Securing the Amazon EC2 hypervisor **[CORRECT]**
- **D.** Setting user password policies

**Correct Answer:** `C`

#### Detailed Explanation

Under the shared responsibility model, AWS is responsible for securing the underlying hypervisor that runs EC2 virtual machines, as this forms part of the infrastructure layer that customers have no access to or control over.

Encrypting client-side data is the customer's responsibility, as AWS has no involvement in data that is encrypted before being sent to AWS services. Configuring IAM roles is the customer's responsibility, as customers define and manage the permissions that control what actions users and services can perform within their account. Setting user password policies is the customer's responsibility, as customers control the IAM password policies that govern how their users authenticate to the AWS Management Console.

---

<a id="q183-44"></a>
### Question 44 (`Q183`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the shared responsibility model which of the following areas are the customer's responsibility?

#### Options
- **A.** Firmware upgrades of network infrastructure
- **B.** Patching of operating systems **[CORRECT]**
- **C.** Patching of the underlying hypervisor
- **D.** Physical security of data centers
- **E.** Configuration of the security group **[CORRECT]**

**Correct Answer:** `B, E`

#### Detailed Explanation

Customers are responsible for patching the operating systems running on their EC2 instances and for configuring security groups to control inbound and outbound traffic within their AWS environment, both sitting on the customer side of the model.

Firmware upgrades of network infrastructure are entirely AWS's responsibility, as customers have no access to or control over the physical networking equipment that underpins the AWS Cloud. Patching the underlying hypervisor is entirely AWS's responsibility, as the virtualization layer sits below the operating system and is managed exclusively by AWS. Physical security of data centers is entirely AWS's responsibility, covering access controls, surveillance, and protection of the facilities that house AWS infrastructure.

---

<a id="q190-45"></a>
### Question 45 (`Q190`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS security service protects applications from distributed denial of service attacks with always-on detection and automatic inline mitigations?

#### Options
- **A.** Amazon Inspector
- **B.** AWS Web Application Firewall (AWS WAF)
- **C.** Elastic Load Balancing (ELB)
- **D.** AWS Shield **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS Shield provides always-on DDoS protection at no extra cost for all AWS customers, automatically detecting and mitigating the most common volumetric and protocol-based DDoS attacks without any customer configuration.

AWS WAF is a web application firewall that filters application-layer HTTP and HTTPS traffic based on configurable rules, and while it helps mitigate application-layer attacks, it is a separate service from Shield and requires customer configuration rather than providing automatic always-on protection. Amazon GuardDuty is a threat detection service that uses machine learning to identify malicious activity and anomalous behavior in AWS accounts, and is an alerting and detection service rather than a service that actively blocks DDoS traffic. AWS CloudTrail records API calls and management events for auditing and compliance purposes, and has no capability to detect or protect against distributed denial of service attacks.

---

<a id="q199-46"></a>
### Question 46 (`Q199`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> A company has moved to AWS recently. Which of the following AWS Services will help ensure that they have the proper security settings?

#### Options
- **A.** AWS Trusted Advisor **[CORRECT]**
- **B.** Amazon Inspector **[CORRECT]**
- **C.** Amazon SNS
- **D.** Amazon CloudWatch
- **E.** Concierge Support Team

**Correct Answer:** `A, B`

#### Detailed Explanation

AWS Trusted Advisor provides automated security checks identifying vulnerabilities such as unrestricted security group access and missing MFA, and Amazon Inspector performs automated security assessments of EC2 instances to identify vulnerabilities and unintended network access. Both help ensure proper security settings.

Amazon SNS is a fully managed publish/subscribe messaging service for sending notifications to subscribers, and does not evaluate or ensure AWS security settings or configurations. Amazon CloudWatch monitors operational metrics and logs for observability and alerting, and while it can trigger notifications on specific metrics or log patterns, it does not actively assess or validate AWS resource security configurations. The Concierge Support Team assists Enterprise support plan customers with billing and account management, and does not perform technical security assessments or review resource security settings.

---

<a id="q200-47"></a>
### Question 47 (`Q200`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the AWS feature that provides an additional level of security above the default authentication mechanism of usernames and passwords?

#### Options
- **A.** Encrypted keys
- **B.** Email verification
- **C.** AWS KMS
- **D.** AWS MFA **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS Multi-Factor Authentication adds a second layer of security by requiring a one-time code from a hardware or virtual device in addition to a username and password, providing an additional level of security above the default username and password mechanism.

Encrypted keys refer to cryptographic keys used for data encryption purposes such as those managed by AWS KMS, and while they protect stored data, they do not provide an additional authentication mechanism for user login security. Email verification is used to confirm ownership of an email address during account setup or password recovery flows, and is not an ongoing additional security layer applied on top of username and password for AWS console logins. AWS KMS is a key management service for creating and managing cryptographic keys used to encrypt data at rest and in transit, and does not add authentication factors to the login process.

---

<a id="q204-48"></a>
### Question 48 (`Q204`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> According to the AWS Acceptable Use Policy, which of the following statements is true regarding penetration testing of EC2 instances?

#### Options
- **A.** Penetration testing is not allowed in AWS
- **B.** Penetration testing is performed automatically by AWS to determine vulnerabilities in your AWS infrastructure
- **C.** Penetration testing can be performed by the customer on their own instances without prior authorization from AWS **[CORRECT]**
- **D.** The AWS customers are only allowed to perform penetration testing on services managed by AWS

**Correct Answer:** `C`

#### Detailed Explanation

AWS's Acceptable Use Policy allows customers to perform penetration testing on their own EC2 instances and certain other permitted services without prior authorisation from AWS, provided the testing complies with the AUP conditions.

Penetration testing is not prohibited in AWS; the Acceptable Use Policy explicitly permits customers to conduct penetration testing on their own resources within defined guidelines, making the claim that it is not allowed incorrect. AWS does not perform automated penetration testing on behalf of customers; Amazon Inspector performs automated security assessments for vulnerabilities and network exposure, but this is not the same as penetration testing, and AWS does not conduct adversarial testing of customer infrastructure. AWS customers are permitted to perform penetration testing on their own services and resources, not only on services managed by AWS; the restriction is that testing must target the customer's own resources rather than AWS shared infrastructure.

---

<a id="q208-49"></a>
### Question 49 (`Q208`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> According to the AWS Shared responsibility model, which of the following are the responsibility of the customer?

#### Options
- **A.** Managing environmental events of AWS data centers
- **B.** Protecting the confidentiality of data in transit in Amazon S3 **[CORRECT]**
- **C.** Controlling physical access to AWS Regions
- **D.** Ensuring that the underlying EC2 host is configured properly
- **E.** Patching applications installed on Amazon EC2 **[CORRECT]**

**Correct Answer:** `B, E`

#### Detailed Explanation

Customers are responsible for protecting the confidentiality of data in transit using encryption such as HTTPS/TLS on connections to Amazon S3, and for patching operating systems and applications installed on Amazon EC2 instances as part of managing their guest environment.

Managing environmental events at AWS data centers, including power, cooling, fire suppression, and natural disaster response, is entirely AWS's responsibility as part of securing the physical infrastructure that customers never interact with. Controlling physical access to AWS Regions and data center facilities is AWS's responsibility; customers have no access to physical infrastructure and rely on AWS to implement badge-based entry, biometric controls, and security staff. Ensuring that the underlying EC2 host is configured properly falls under AWS's responsibility; customers manage the guest operating system and above, while AWS is responsible for the hypervisor, host hardware, and underlying virtualization layer.

---

<a id="q211-50"></a>
### Question 50 (`Q211`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is equivalent to a username and password and is used to authenticate your programmatic access to AWS services and APIs?

#### Options
- **A.** Instance Password
- **B.** Key pairs
- **C.** Access Keys **[CORRECT]**
- **D.** MFA

**Correct Answer:** `C`

#### Detailed Explanation

AWS Access Keys, consisting of an access key ID and a secret access key, are the credentials used to authenticate programmatic API calls, functioning like a username and password for AWS SDKs and CLI.

An instance password refers to the Windows administrator password generated for EC2 Windows instances to enable RDP access, which is a server login credential rather than an API authentication mechanism equivalent to a username and password. Key pairs are RSA public/private key combinations used to authenticate SSH connections to Linux EC2 instances, and while they serve an authentication purpose, they are for instance-level SSH access rather than AWS API and service authentication. MFA is an additional authentication factor added on top of primary credentials such as a username and password, requiring a one-time code from a device, and is a supplementary mechanism rather than a standalone credential pair equivalent to a username and password.

---

<a id="q213-51"></a>
### Question 51 (`Q213`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the AWS service that enables you to manage all of your AWS accounts from a single master account?

#### Options
- **A.** AWS WAF
- **B.** AWS Trusted Advisor
- **C.** AWS Organizations **[CORRECT]**
- **D.** AWS Config

**Correct Answer:** `C`

#### Detailed Explanation

AWS Organizations enables you to create a hierarchy of AWS accounts managed from a single master account, applying policies and consolidated billing across all member accounts.

AWS WAF is a web application firewall that filters and blocks malicious web traffic using managed and custom rule sets, and has no role in managing multiple AWS accounts. AWS Trusted Advisor analyzes your AWS environment and provides recommendations across cost optimization, security, and performance, but does not provide centralized management of multiple accounts. AWS Config continuously monitors and records AWS resource configurations for compliance purposes, but operates within individual accounts rather than providing centralized multi-account management.

---

<a id="q219-52"></a>
### Question 52 (`Q219`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services can help protect your web applications from SQL injection and other vulnerabilities in your application code?

#### Options
- **A.** Amazon Cognito
- **B.** AWS IAM
- **C.** Amazon Aurora
- **D.** AWS WAF **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS WAF is a web application firewall that lets you create rules to inspect and filter HTTP and HTTPS traffic, blocking common web exploits such as SQL injection and cross-site scripting before they reach your application.

Amazon Cognito is a user identity and authentication service for web and mobile applications that handles user sign-up, sign-in, and access control for application users, and does not inspect or filter HTTP traffic for SQL injection or other web exploits. AWS IAM manages user permissions and access to AWS services and resources, and is an identity and access management service rather than a traffic inspection tool that can block malicious web requests. Amazon Aurora is a relational database service compatible with MySQL and PostgreSQL, and is a managed database offering rather than a security service for filtering web application traffic.

---

<a id="q221-53"></a>
### Question 53 (`Q221`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Based on the AWS Shared Responsibility Model, which of the following are the sole responsibility of AWS?

#### Options
- **A.** Monitoring network performance
- **B.** Installing software on EC2 instances
- **C.** Creating hypervisors **[CORRECT]**
- **D.** Configuring Access Control Lists (ACLs)
- **E.** Hardware maintenance **[CORRECT]**

**Correct Answer:** `C, E`

#### Detailed Explanation

Creating and managing hypervisors and maintaining physical hardware are solely AWS's responsibility, as customers have no access to or control over the virtualization layer or the underlying infrastructure that powers AWS services.

Monitoring network performance for their own applications and workloads is the customer's responsibility, as AWS provides the tools but customers are accountable for observing and responding to performance within their environment. Installing software on EC2 instances is the customer's responsibility, as customers manage everything above the hypervisor including the operating system, applications, and any software they choose to run. Configuring Access Control Lists is the customer's responsibility, as customers define and manage their own network access rules within their VPC environment.

---

<a id="q223-54"></a>
### Question 54 (`Q223`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What are the default security credentials that are required to access the AWS management console for an IAM user account?

#### Options
- **A.** MFA
- **B.** Security tokens
- **C.** A user name and password **[CORRECT]**
- **D.** Access keys

**Correct Answer:** `C`

#### Detailed Explanation

IAM user console access is secured with a user name and password combination as the default credentials, providing the basic authentication required to access the AWS Management Console.

MFA is an optional additional authentication factor that can be layered on top of a username and password to require a one-time code from a device, but it is not the default credential requirement and is configured separately from the primary user name and password. Security tokens are temporary credentials consisting of an access key ID, secret access key, and session token that are issued when an IAM role is assumed, and are used for programmatic and role-based access rather than as default console credentials for IAM user accounts. Access keys consisting of an access key ID and secret access key are the credentials used for programmatic API and CLI access, not for logging into the AWS Management Console, which uses user name and password.

---

<a id="q226-55"></a>
### Question 55 (`Q226`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following aspects of security are managed by AWS?

#### Options
- **A.** Encryption of EBS volumes
- **B.** VPC security
- **C.** Access permissions
- **D.** Hardware patching **[CORRECT]**
- **E.** Securing global physical infrastructure **[CORRECT]**

**Correct Answer:** `D, E`

#### Detailed Explanation

Hardware patching and maintenance of the physical servers that run AWS services, and securing the global physical infrastructure including data centers, power, cooling, and networking, are entirely AWS's responsibility under the shared responsibility model.

Encryption of EBS volumes is a customer responsibility that involves enabling EBS encryption at the volume or account level and selecting appropriate KMS keys to protect data at rest on block storage volumes. VPC security, including the configuration of security groups, network ACLs, and route tables, is the customer's responsibility as it governs how network traffic flows within and to the customer's own virtual private cloud. Access permissions, including creating IAM users, groups, roles, and attaching policies that control who can access which AWS services and resources, are entirely the customer's responsibility to define and manage.

---

<a id="q229-56"></a>
### Question 56 (`Q229`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> What are the change management tools that helps AWS customers audit and monitor all resource changes in their AWS environment?

#### Options
- **A.** AWS CloudTrail **[CORRECT]**
- **B.** Amazon Comprehend
- **C.** AWS Transit Gateway
- **D.** AWS X-Ray
- **E.** AWS Config **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

AWS CloudTrail records all API calls and resource changes for auditing, and AWS Config continuously monitors and records resource configuration changes and evaluates them against compliance rules. Together they are the primary change management and auditing tools in AWS.

Amazon Comprehend is a natural language processing service that uses machine learning to extract insights such as entities, sentiment, and key phrases from text, and is an AI analytics service with no capability to audit or monitor resource configuration changes. AWS Transit Gateway connects VPCs and on-premises networks through a central hub, providing network routing and connectivity rather than auditing or change management functionality. AWS X-Ray is an application performance tracing service that analyzes requests as they flow through distributed applications, and is a debugging and performance tool rather than an infrastructure change auditing service.

---

<a id="q231-57"></a>
### Question 57 (`Q231`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services will help businesses ensure compliance in AWS?

#### Options
- **A.** Amazon CloudFront
- **B.** AWS Migration Hub
- **C.** Amazon CloudWatch
- **D.** AWS CloudTrail **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS CloudTrail logs all API activity and account events, creating a complete audit trail that helps organizations demonstrate compliance with regulatory requirements and investigate security incidents.

Amazon CloudFront is a global content delivery network that caches and distributes web content to users at low latency through edge locations, and is a performance and distribution service with no capability to record audit logs or help with regulatory compliance. AWS Migration Hub provides a central dashboard for tracking the progress of application migrations to AWS, and is a migration management tool rather than a compliance or audit service. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, providing visibility into performance and operational health, but it does not create the comprehensive API audit trail needed for regulatory compliance.

---

<a id="q236-58"></a>
### Question 58 (`Q236`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following AWS security features is associated with an EC2 instance and functions to filter incoming traffic requests?

#### Options
- **A.** AWS X-Ray
- **B.** Network ACL
- **C.** Security Groups **[CORRECT]**
- **D.** VPC Flow logs

**Correct Answer:** `C`

#### Detailed Explanation

Security groups act as a stateful virtual firewall directly associated with EC2 instances, evaluating and filtering inbound and outbound traffic based on protocol, port, and source or destination rules defined by the customer.

AWS X-Ray is an application tracing and debugging service that analyzes requests as they flow through distributed applications to identify performance bottlenecks and errors, and has no capability to filter or control network traffic to EC2 instances. Network ACLs are stateless firewalls that operate at the subnet level rather than the EC2 instance level, applying rules to all traffic entering or leaving a subnet without tracking connection state, and are not directly associated with individual instances. VPC Flow Logs capture metadata about the IP traffic flowing to and from network interfaces within a VPC, providing visibility for analysis and troubleshooting, but they record traffic information rather than filter or block incoming requests.

---

<a id="q238-59"></a>
### Question 59 (`Q238`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Using Amazon RDS falls under the shared responsibility model. Which of the following are customer responsibilities?

#### Options
- **A.** Building the relational database schema **[CORRECT]**
- **B.** Performing backups
- **C.** Managing the database settings **[CORRECT]**
- **D.** Patching the database software
- **E.** Installing the database software

**Correct Answer:** `A, C`

#### Detailed Explanation

Under the Shared Responsibility Model for Amazon RDS, the customer is responsible for designing the database schema and managing database-level settings such as parameters and user permissions.

Performing backups is managed by AWS for RDS, which automates backup retention and point-in-time recovery without requiring the customer to manually initiate or manage backup processes. Patching the database software is entirely AWS's responsibility for RDS, as AWS handles all engine-level patching and maintenance windows as part of the managed service. Installing the database software is entirely AWS's responsibility for RDS, as AWS provisions, installs, and maintains the underlying database engine on the customer's behalf.

---

<a id="q252-60"></a>
### Question 60 (`Q252`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> An organization runs many systems and uses many AWS products. Which of the following services enables them to control how each developer interacts with these products?

#### Options
- **A.** AWS Identity and Access Management **[CORRECT]**
- **B.** Amazon RDS
- **C.** Network Access Control Lists
- **D.** Amazon EMR

**Correct Answer:** `A`

#### Detailed Explanation

AWS Identity and Access Management allows administrators to create users, groups, and roles with fine-grained permission policies that control exactly which AWS services and actions each developer or system can access across all AWS products.

Amazon RDS is a fully managed relational database service for running databases such as MySQL, PostgreSQL, and Oracle in the cloud, and is a data storage service rather than a tool for controlling developer access to AWS products. Network Access Control Lists are stateless subnet-level firewalls within a VPC that control inbound and outbound network traffic based on IP address and port rules, and are a network security mechanism rather than a service for managing developer permissions across AWS products. Amazon EMR is a managed cloud big data platform for running large-scale distributed data processing jobs using frameworks such as Apache Spark and Hadoop, and is a data processing service rather than an access management solution.

---

<a id="q258-61"></a>
### Question 61 (`Q258`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the AWS service that performs automated network assessments of Amazon EC2 instances to check for vulnerabilities?

#### Options
- **A.** Amazon Kinesis
- **B.** Security groups
- **C.** Amazon Inspector **[CORRECT]**
- **D.** AWS Network Access Control Lists

**Correct Answer:** `C`

#### Detailed Explanation

Amazon Inspector automatically assesses EC2 instances for unintended network access and known software vulnerabilities by scanning network configurations and installed packages against vulnerability databases, generating prioritized findings.

Amazon Kinesis is a real-time data streaming service for ingesting, processing, and analyzing streaming data at scale, and has no capability to perform security assessments or network vulnerability scans of EC2 instances. Security groups act as stateful virtual firewalls that control which traffic is allowed to reach EC2 instances based on defined rules, and are a traffic filtering mechanism rather than a service that performs automated vulnerability assessments. AWS Network Access Control Lists are stateless subnet-level firewalls that allow or deny traffic based on IP address and port rules, and are a network traffic control mechanism rather than an assessment service that identifies vulnerabilities.

---

<a id="q259-62"></a>
### Question 62 (`Q259`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the Shared Responsibility Model, which of the following controls do customers fully inherit from AWS?

#### Options
- **A.** Patch management controls
- **B.** Database controls
- **C.** Awareness & Training
- **D.** Environmental controls **[CORRECT]**
- **E.** Physical controls **[CORRECT]**

**Correct Answer:** `D, E`

#### Detailed Explanation

Physical controls such as data center physical security and hardware protection, and environmental controls such as power, cooling, and fire suppression, are entirely managed by AWS and fully inherited by customers who have no access to or responsibility for these areas.

Patch management is a shared control where AWS patches the underlying infrastructure and managed services, while customers retain responsibility for patching their own operating systems and applications. Database controls are a shared control where AWS manages the database engine in fully managed services, while customers remain responsible for access management, schema design, and data handling. Awareness and training is a shared control where AWS trains its own employees, while customers are independently responsible for training their own staff on security and compliance practices.

---

<a id="q269-63"></a>
### Question 63 (`Q269`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following can help protect your EC2 instances from DDoS attacks?

#### Options
- **A.** AWS CloudHSM
- **B.** Security Groups **[CORRECT]**
- **C.** AWS Batch
- **D.** AWS IAM
- **E.** Network Access Control Lists (Network ACLs) **[CORRECT]**

**Correct Answer:** `B, E`

#### Detailed Explanation

Security groups are stateful instance-level firewalls that can block unwanted traffic before it reaches EC2 instances, and Network ACLs are stateless subnet-level controls that can block volumetric attack traffic at the network perimeter. Both can help protect EC2 instances from DDoS traffic.

AWS CloudHSM provides dedicated hardware security modules for generating and managing cryptographic keys within the AWS Cloud, and is a key management service with no capability to block or mitigate DDoS traffic targeting EC2 instances. AWS Batch is a fully managed batch computing service that dynamically provisions compute resources for batch jobs, and is a job scheduling and compute service with no network traffic filtering or DDoS protection capability. AWS IAM manages user permissions and access to AWS services and resources, and is an identity and access management service rather than a network defense tool that can block DDoS traffic.

---

<a id="q280-64"></a>
### Question 64 (`Q280`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following is used to control network traffic in AWS?

#### Options
- **A.** Network Access Control Lists (NACLs) **[CORRECT]**
- **B.** Key Pairs
- **C.** Access Keys
- **D.** IAM Policies
- **E.** Security Groups **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

Network ACLs are stateless subnet-level firewalls that evaluate all inbound and outbound traffic based on numbered rules, and security groups are stateful instance-level firewalls that control traffic to and from EC2 instances. Both are used to control network traffic in AWS.

Key pairs are RSA public/private key combinations used to authenticate SSH connections to EC2 instances, and are an instance access credential rather than a network traffic control mechanism. Access keys consisting of an access key ID and secret access key are used to authenticate programmatic API calls to AWS services, and are an API authentication credential rather than a tool for controlling network traffic within a VPC. IAM policies are JSON documents that define permissions for users, groups, and roles to access AWS services and resources, and operate at the API authorisation layer rather than controlling IP-level network traffic flow.

---

<a id="q292-65"></a>
### Question 65 (`Q292`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Data security is one of the top priorities of AWS. How does AWS deal with old storage devices that have reached the end of their useful life?

#### Options
- **A.** AWS sells the old devices to other hosting providers
- **B.** AWS destroys the old devices in accordance with industry-standard practices **[CORRECT]**
- **C.** AWS sends the old devices for remanufacturing
- **D.** AWS stores the old devices in a secure place

**Correct Answer:** `B`

#### Detailed Explanation

AWS decommissions storage devices using industry-standard techniques such as DoD 5220.22-M or NIST 800-88 to ensure that data cannot be recovered from retired hardware, fulfilling their security of the cloud obligations under the shared responsibility model.

AWS does not sell old storage devices to other hosting providers, as doing so would create an unacceptable risk of data exposure; decommissioned devices are physically destroyed or securely wiped following strict protocols before disposal. AWS does not use third-party audits to verify data removal on old devices; rather, AWS performs the decommissioning itself using documented internal processes and the resulting policies and certifications are available to customers through AWS Artifact. AWS does not return old storage devices to the hardware vendors for resale, as the devices contain customer data that must be securely destroyed before any transfer outside AWS's direct control.

---

<a id="q293-66"></a>
### Question 66 (`Q293`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> A developer needs to set up an SSL security certificate for a client's eCommerce website in order to use the HTTPS protocol. Which of the following AWS services can be used to deploy the required SSL server certificates?

#### Options
- **A.** Amazon Route 53
- **B.** AWS Certificate Manager **[CORRECT]**
- **C.** AWS Directory Service
- **D.** AWS Identity and Access Management **[CORRECT]**
- **E.** AWS Config

**Correct Answer:** `B, D`

#### Detailed Explanation

AWS Certificate Manager is the primary service for provisioning, managing, and deploying SSL/TLS certificates for use with AWS services such as CloudFront and Elastic Load Balancing. AWS IAM also supports uploading and storing SSL server certificates that can be deployed to services not yet supported by ACM, making both valid options.

Amazon Route 53 is a DNS and domain registration service that manages how traffic is routed to resources, and has no capability to provision or deploy SSL certificates. AWS Directory Service is a managed Microsoft Active Directory service used for identity management, and is unrelated to SSL certificate provisioning. AWS Config is a compliance and configuration monitoring service that tracks resource configuration changes, and does not provision or deploy SSL certificates.

---

<a id="q295-67"></a>
### Question 67 (`Q295`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> A company is planning to migrate an application from Amazon EC2 to AWS Lambda to use a serverless architecture. Which of the following will be the responsibility of AWS after migration?

#### Options
- **A.** Application management
- **B.** Capacity management **[CORRECT]**
- **C.** Access control
- **D.** Operating system maintenance **[CORRECT]**
- **E.** Data management

**Correct Answer:** `B, D`

#### Detailed Explanation

After migrating to AWS Lambda, AWS takes full responsibility for capacity management by automatically scaling functions based on demand, and for operating system maintenance as Lambda runs entirely on AWS-managed infrastructure with no customer access to the underlying OS.

Application management remains the customer's responsibility after migration, as customers are always accountable for the code they write, deploy, and maintain within their Lambda functions. Access control remains the customer's responsibility, as customers must configure IAM roles, permissions, and resource policies to control who and what can invoke their Lambda functions. Data management remains the customer's responsibility, as customers control what data their functions process, where it is stored, and how it is handled throughout its lifecycle.

---

<a id="q300-68"></a>
### Question 68 (`Q300`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS Service is used to manage user permissions?

#### Options
- **A.** Security Groups
- **B.** Amazon ECS
- **C.** AWS IAM **[CORRECT]**
- **D.** AWS Support

**Correct Answer:** `C`

#### Detailed Explanation

AWS Identity and Access Management allows administrators to create users, groups, roles, and policies that control who can access which AWS services and resources, making it the primary service for managing user permissions in AWS.

AWS Key Management Service creates and manages cryptographic keys for encrypting and decrypting data, and is a data protection service rather than an access permission management tool for controlling which users can access AWS resources. AWS CloudTrail records all API calls and management events for auditing and compliance purposes, providing visibility into who did what and when, but it records activity rather than managing or enforcing user permissions. Amazon CloudWatch monitors operational metrics and events for AWS resources and applications, providing observability into performance and operational health, but has no capability to manage user access permissions to AWS services.

---

<a id="q302-69"></a>
### Question 69 (`Q302`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company needs to track resource changes using the API call history. Which AWS service can help the company achieve this goal?

#### Options
- **A.** AWS Config
- **B.** Amazon CloudWatch
- **C.** AWS CloudTrail **[CORRECT]**
- **D.** AWS CloudFormation

**Correct Answer:** `C`

#### Detailed Explanation

AWS CloudTrail records every API call made in your AWS account, including the identity of the caller, timestamp, and parameters, making it the primary service for tracking resource changes via API history.

AWS Config tracks the configuration state of AWS resources over time and evaluates them against compliance rules, but it records configuration changes rather than the underlying API calls that caused them. Amazon CloudWatch is a monitoring and observability service that collects metrics, logs, and alarms from AWS resources, and does not record API call history or track who made changes to resources. AWS CloudFormation is an infrastructure-as-code service that provisions and manages AWS resources through templates, and does not record or track API call history across an account.

---

<a id="q305-70"></a>
### Question 70 (`Q305`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the AWS' recommendation regarding access keys?

#### Options
- **A.** Delete all access keys and use passwords instead
- **B.** Only share them with trusted people
- **C.** Rotate them regularly **[CORRECT]**
- **D.** Save them within your application code

**Correct Answer:** `C`

#### Detailed Explanation

AWS recommends rotating access keys regularly to limit the window of exposure if a key is ever compromised, as shorter-lived credentials reduce the risk of unauthorised access going undetected.

Deleting all access keys and using passwords instead is not a valid approach, as passwords are used for console access while access keys are required for programmatic access through the CLI and API, and both have legitimate roles in a well-managed AWS account. Sharing access keys only with trusted people still violates the principle of least privilege, as access keys should be scoped to individual IAM users or roles rather than shared between people. Saving access keys within application code is a significant security risk as code repositories can be exposed publicly or internally, and AWS recommends using IAM roles for applications running on AWS resources instead of embedding credentials in code.

---

<a id="q306-71"></a>
### Question 71 (`Q306`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the AWS IAM feature that provides an additional layer of security on top of username and password authentication?

#### Options
- **A.** Key Pair
- **B.** Access Keys
- **C.** SDK
- **D.** MFA **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS IAM Multi-Factor Authentication adds a second verification layer requiring a one-time code from a hardware or virtual device on top of the username and password, providing an additional authentication factor that significantly increases account security.

Encryption is a data protection mechanism used to secure data at rest or in transit, and while it protects the confidentiality of stored information, it does not add an authentication layer on top of username and password for account login. AWS Access Advisor shows which AWS services IAM users and roles have accessed and when, helping administrators reduce permissions to only those actually used, but it is a permissions visibility tool rather than an authentication security mechanism. Least privilege access is a permissions management principle that involves granting users only the minimum permissions needed for their tasks, reducing the blast radius of compromised credentials, but it does not add an additional authentication factor on top of the login process.

---

<a id="q312-72"></a>
### Question 72 (`Q312`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> For managed services like Amazon DynamoDB, which of the below is AWS responsible for?

#### Options
- **A.** Protecting credentials
- **B.** Logging access activity
- **C.** Patching the database software **[CORRECT]**
- **D.** Operating system maintenance **[CORRECT]**
- **E.** Creating access policies

**Correct Answer:** `C, D`

#### Detailed Explanation

For fully managed services like Amazon DynamoDB, AWS is responsible for patching the database software and maintaining the underlying operating system, as customers have no access to the infrastructure layer beneath the service.

Protecting credentials is the customer's responsibility, as customers manage their own IAM users, access keys, and authentication mechanisms. Logging access activity is the customer's responsibility, as customers must enable and configure AWS CloudTrail and DynamoDB Streams if they want to capture access logs. Creating access policies is the customer's responsibility, as customers define and manage the IAM policies that control who can access their DynamoDB tables and what actions they can perform.

---

<a id="q316-73"></a>
### Question 73 (`Q316`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company has discovered that multiple S3 buckets were deleted, but it is unclear who performed these actions. Which AWS service can be used to identify who deleted the buckets?

#### Options
- **A.** SNS logs
- **B.** SQS logs
- **C.** CloudWatch Logs
- **D.** CloudTrail logs **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS CloudTrail records all API calls and management events in an AWS account including S3 bucket deletion events, capturing who performed the action, the source IP address, and the timestamp, making it the correct service for identifying who deleted the buckets.

SNS logs is not a recognized AWS service or log type; Amazon SNS is a messaging service for sending notifications and does not produce logs of S3 API activity or deletion events. SQS logs is not a recognized AWS service or log type; Amazon SQS is a managed message queue service for decoupling application components and does not produce logs of S3 management activity. CloudWatch Logs collects and stores log data from AWS services and applications for monitoring and analysis, but S3 bucket deletion events are management events captured by CloudTrail rather than CloudWatch, making CloudWatch Logs the wrong place to identify who deleted S3 buckets.

---

<a id="q319-74"></a>
### Question 74 (`Q319`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What are AWS shared controls?

#### Options
- **A.** Controls that are solely the responsibility of the customer based on the application they are deploying within AWS services
- **B.** Controls that a customer inherits from AWS
- **C.** Controls that apply to both the infrastructure layer and customer layers
- **D.** Controls that the customer and AWS collaborate together upon to secure the infrastructure **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Shared controls are responsibilities where both AWS and the customer independently apply controls in their own respective domains, such as AWS patching its infrastructure while the customer patches their guest operating system.

Controls solely the responsibility of the customer describes customer-specific controls, not shared controls, as these apply only to the customer's side of the model. Controls that a customer inherits from AWS describes inherited controls, where compliance certifications and physical security measures are passed down from AWS to the customer, which is a separate category from shared controls. Controls that apply to both the infrastructure and customer layers is a misleading description because shared controls do not mean the same single control applies at both layers, but rather that each party manages their own version of the same type of control independently.

---

<a id="q321-75"></a>
### Question 75 (`Q321`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the below are responsibilities of the customer when using Amazon EC2?

#### Options
- **A.** Protecting sensitive data **[CORRECT]**
- **B.** Patching of the underlying infrastructure
- **C.** Setup and operation of managed databases
- **D.** Maintaining consistent hardware components
- **E.** Installing and configuring third-party software **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

Customers using Amazon EC2 are responsible for managing user access to their EC2 instances, including configuring operating system users and SSH keys, and for protecting data at rest and in transit on those instances through encryption and access controls.

Preventing physical access to EC2 hardware is AWS's responsibility as customers have no access to or visibility into the physical data center facilities where EC2 instances run. Patching the network infrastructure is AWS's responsibility as the underlying physical and virtual networking components that connect EC2 instances are managed and maintained entirely by AWS. Managing the hypervisor is AWS's responsibility as the virtualization layer that abstracts physical hardware into EC2 instances is part of the AWS infrastructure that customers cannot access or modify.

---

<a id="q323-76"></a>
### Question 76 (`Q323`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following AWS services can help you perform security analysis and regulatory compliance auditing?

#### Options
- **A.** Amazon Inspector **[CORRECT]**
- **B.** AWS Trusted Advisor
- **C.** AWS Batch
- **D.** Amazon ECS
- **E.** AWS Config **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

Amazon Inspector automatically assesses applications for vulnerabilities and deviations from best practices, and AWS Config continuously monitors resource configurations and evaluates them against compliance rules. Both are purpose-built for security analysis and regulatory compliance auditing.

AWS Trusted Advisor provides recommendations across security, cost, performance, and fault tolerance, but offers high-level checks and guidance rather than the deep automated security assessments and compliance rule evaluation that Inspector and Config provide. AWS Batch is a managed service for running batch computing workloads at scale, and is a job scheduling and compute service with no security analysis or compliance auditing capability. Amazon ECS is a container orchestration service that manages the deployment and scaling of containerised applications, and is a compute service with no security analysis or compliance auditing capability.

---

<a id="q332-77"></a>
### Question 77 (`Q332`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following can be used to protect data at rest on Amazon S3?

#### Options
- **A.** Versioning **[CORRECT]**
- **B.** Deduplication
- **C.** Permissions **[CORRECT]**
- **D.** Decryption
- **E.** Conversion

**Correct Answer:** `A, C`

#### Detailed Explanation

Amazon S3 versioning retains multiple versions of objects, protecting against accidental deletion and allowing restoration of previous versions, and S3 permissions through IAM policies and bucket policies control who can access and modify objects. Both help protect data at rest on Amazon S3.

Deduplication is a storage optimization technique that removes duplicate copies of data to save space, and is not a data protection mechanism for Amazon S3; S3 does not expose deduplication as a security feature. Decryption is the process of converting encrypted data back to its original form, and while decryption is part of an encryption workflow, enabling decryption alone does not protect data at rest and is not a data protection mechanism for S3. Conversion refers to changing data formats or types, and has no relevance to protecting data stored in Amazon S3.

---

<a id="q336-78"></a>
### Question 78 (`Q336`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> When running a workload in AWS, the customer is NOT responsible for:

#### Options
- **A.** Running penetration tests
- **B.** Reserving capacity
- **C.** Data center operations **[CORRECT]**
- **D.** Auditing and regulatory compliance
- **E.** Infrastructure security **[CORRECT]**

**Correct Answer:** `C, E`

#### Detailed Explanation

Data center operations including physical facility management, power, cooling, and hardware decommissioning, and infrastructure security including the physical and virtual networking, hypervisor, and server hardware, are entirely AWS's responsibility and are not tasks the customer performs.

Running penetration tests is the customer's own responsibility; AWS allows customers to conduct penetration testing on their own resources following the Acceptable Use Policy, but the decision to run tests and the tests themselves are not something AWS performs for customers. Reserving capacity, such as purchasing Reserved Instances or Savings Plans for predictable workloads, is a customer decision and action taken to optimize costs rather than an AWS-managed task. Auditing and regulatory compliance is a shared responsibility; AWS provides compliance reports and certifications through AWS Artifact, but customers are responsible for applying those to their own applications and ensuring their workloads meet regulatory requirements.

---

<a id="q341-79"></a>
### Question 79 (`Q341`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service or feature is used to manage the keys used to encrypt customer data?

#### Options
- **A.** AWS KMS **[CORRECT]**
- **B.** AWS Service Control Policies (SCPs)
- **C.** Multi-Factor Authentication (MFA)
- **D.** Amazon Macie

**Correct Answer:** `A`

#### Detailed Explanation

AWS Key Management Service lets you create, manage, and control cryptographic keys used to encrypt your data across AWS services, providing centralized key management with audit logging via CloudTrail.

AWS Service Control Policies are organizational policies used within AWS Organizations to restrict the maximum permissions available to accounts in an organization, and are an access governance tool rather than a key management service for encryption keys. Multi-Factor Authentication adds a second verification factor to the login process requiring a code from a hardware or virtual device, and is an authentication security mechanism rather than a service for managing encryption keys. Amazon Macie uses machine learning to automatically discover and protect sensitive data in Amazon S3, and is a data classification and protection service rather than a key management service for creating and controlling encryption keys.

---

<a id="q342-80"></a>
### Question 80 (`Q342`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS Service allows customers to download AWS SOC & PCI reports?

#### Options
- **A.** AWS Well-Architected Tool
- **B.** AWS Artifact **[CORRECT]**
- **C.** AWS Glue
- **D.** Amazon Chime

**Correct Answer:** `B`

#### Detailed Explanation

AWS Artifact is a self-service portal for on-demand access to AWS compliance reports including SOC and PCI reports, and agreement documents such as Business Associate Addenda, making it the correct service for downloading AWS SOC and PCI compliance reports.

AWS Well-Architected Tool is a service that helps you review the state of your workloads and compare them against AWS architectural best practices across the six pillars, and is a workload review and guidance tool rather than a compliance report repository. AWS Glue is a fully managed extract, transform, and load service for preparing and transforming data for analytics, and is a data integration service with no connection to compliance documentation. Amazon Chime is a unified communications service for online meetings, video conferencing, and chat, and has no relationship to compliance reports or AWS certification documents.

---

<a id="q345-81"></a>
### Question 81 (`Q345`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> What features does AWS offer to help protect your data in the Cloud?

#### Options
- **A.** Access control **[CORRECT]**
- **B.** Physical MFA devices
- **C.** Data encryption **[CORRECT]**
- **D.** Unlimited storage
- **E.** Load balancing

**Correct Answer:** `A, C`

#### Detailed Explanation

AWS offers access control through IAM policies, security groups, and network ACLs to restrict who can reach your data, and data encryption at rest and in transit to protect data even if it is intercepted or accessed without authorisation. Both are purpose-built data protection features.

Physical MFA devices add a second layer of authentication to protect account and user access, but they secure who can log in rather than directly protecting the data itself once access is granted. Unlimited storage is a capacity characteristic of services such as Amazon S3, and is a storage scaling feature with no data protection or security capability. Load balancing distributes incoming traffic across multiple targets to improve availability and performance, and is a resilience and throughput feature with no role in protecting data from unauthorised access or exposure.

---

<a id="q348-82"></a>
### Question 82 (`Q348`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which methods can be used by customers to interact with AWS Identity and Access Management (IAM)?

#### Options
- **A.** AWS CLI **[CORRECT]**
- **B.** AWS Security Groups
- **C.** AWS SDKs **[CORRECT]**
- **D.** AWS Network Access Control Lists
- **E.** AWS CodeCommit

**Correct Answer:** `A, C`

#### Detailed Explanation

The AWS CLI provides command-line access to IAM for creating users, assigning permissions, and managing credentials, and AWS SDKs allow programmatic integration with IAM in application code to automate identity and access management operations. Both are valid methods for interacting with IAM.

AWS Security Groups are virtual firewalls that control inbound and outbound network traffic at the EC2 instance level, and are a network security component rather than a method for interacting with IAM. AWS Network Access Control Lists are stateless firewalls that control traffic at the subnet level within a VPC, and are a network traffic filtering mechanism rather than an interface for managing IAM identities or permissions. AWS CodeCommit is a fully managed source control service for hosting Git repositories, and is a code collaboration tool with no connection to interacting with IAM beyond using IAM for access control.

---

<a id="q349-83"></a>
### Question 83 (`Q349`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following are types of AWS Identity and Access Management (IAM) identities?

#### Options
- **A.** AWS Resource Groups
- **B.** IAM Policies
- **C.** IAM Roles **[CORRECT]**
- **D.** IAM Users **[CORRECT]**
- **E.** AWS Organizations

**Correct Answer:** `C, D`

#### Detailed Explanation

IAM Users represent individual people or applications with specific credentials and permissions, and IAM Roles provide temporary security credentials that can be assumed by users, services, or AWS resources. Both are types of IAM identities.

AWS Resource Groups organize AWS resources by tags or CloudFormation stacks to make it easier to manage and automate operations across groups of resources, and are not IAM identities that can be used for authentication or permission assignment. IAM Policies are JSON documents that define permissions specifying allowed or denied actions on AWS resources, and are permission documents attached to identities rather than identity types themselves. AWS Organizations is a service for managing multiple AWS accounts under a central structure for consolidated billing and governance, and is an account management service rather than an IAM identity type.

---

<a id="q351-84"></a>
### Question 84 (`Q351`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> How does AWS notify customers about security and privacy events pertaining to AWS services?

#### Options
- **A.** Using the AWS ACM service
- **B.** Using Security Bulletins **[CORRECT]**
- **C.** Using the AWS Management Console
- **D.** Using Compliance Resources

**Correct Answer:** `B`

#### Detailed Explanation

AWS publishes Security Bulletins to notify customers about security and privacy events affecting AWS services, providing details on vulnerabilities and recommended actions.

AWS Certificate Manager is a service that provisions and manages SSL/TLS certificates for use with AWS resources, and is not a channel through which AWS communicates security or privacy event notifications to customers. The AWS Management Console is a web-based interface for accessing and managing AWS services, and while customers can view some account-level alerts there, it is not the mechanism AWS uses to publish security and privacy event notifications. AWS Compliance Resources are documents and reports such as audit certifications and compliance guides that help customers understand AWS's regulatory posture, and are not used to notify customers about specific security or privacy events.

---

<a id="q352-85"></a>
### Question 85 (`Q352`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which IAM entity can best be used to grant temporary access to your AWS resources?

#### Options
- **A.** IAM Users
- **B.** Key Pair
- **C.** IAM Roles **[CORRECT]**
- **D.** IAM Groups

**Correct Answer:** `C`

#### Detailed Explanation

IAM Roles provide temporary security credentials that expire automatically, making them the best choice for granting short-term or temporary access to AWS resources without sharing long-term credentials.

IAM Users are identities with permanent, long-term credentials such as passwords and access keys, and while permissions can be granted or revoked, users themselves represent persistent identities rather than a mechanism designed specifically for temporary access. Key pairs are RSA public/private key combinations used to authenticate SSH connections to EC2 Linux instances, and are an instance access mechanism rather than an IAM feature designed for granting temporary access to AWS services and resources. IAM Groups are collections of IAM users that share the same attached policies, and are used to manage permissions for multiple users collectively rather than for granting temporary access to any single entity.

---

<a id="q355-86"></a>
### Question 86 (`Q355`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company is seeking to better secure its AWS account from unauthorized access. Which of the below options can the customer use to achieve this goal?

#### Options
- **A.** Restrict any API call made through SDKs or CLI
- **B.** Create one IAM account for each department in the company (Development, QA, Production), and share it across all staff in that department
- **C.** Require Multi-Factor Authentication (MFA) for all IAM User access **[CORRECT]**
- **D.** Set up two login passwords

**Correct Answer:** `C`

#### Detailed Explanation

Requiring MFA for all IAM users adds a second verification step beyond a password, significantly reducing the risk of unauthorised access even if a user's password is stolen or guessed, making it an effective control for securing the AWS account.

Restricting all API calls through SDKs or CLI would completely prevent programmatic and automated access to AWS services, making it operationally unworkable for development and automation workflows rather than a practical security measure. Creating a single IAM account per department shared across all staff removes individual accountability, makes it impossible to trace actions to specific users, and means a single compromised password grants access to everyone in the department, making this a security anti-pattern rather than a security improvement. Setting up two login passwords is not a feature AWS supports; AWS accounts use a single password for console access, and improved security beyond the password is achieved through MFA rather than multiple passwords.

---

<a id="q361-87"></a>
### Question 87 (`Q361`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following are examples of the customer's responsibility to implement security IN the cloud?

#### Options
- **A.** Building a schema for an application **[CORRECT]**
- **B.** Replacing physical hardware
- **C.** Creating a new hypervisor
- **D.** Patch management of the underlying infrastructure
- **E.** File system encryption **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

Building an application schema is an application development task that customers perform as part of managing their applications in the cloud, and encrypting file systems on EC2 instances to protect data at rest is a customer responsibility for security in the cloud. Both fall within the customer's side of the shared responsibility model.

Replacing physical hardware is entirely AWS's responsibility as customers have no access to or interaction with the physical servers, storage devices, and networking equipment in AWS data centers. Creating a new hypervisor is AWS's responsibility as the virtualization layer that abstracts physical hardware into virtual instances is part of the AWS-managed infrastructure that customers cannot access or modify. Patch management of the underlying infrastructure, including the host operating systems, hypervisor, and physical network equipment, is AWS's responsibility, whereas customers are responsible for patching the guest operating system on their own EC2 instances.

---

<a id="q362-88"></a>
### Question 88 (`Q362`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is a type of MFA device that customers can use to protect their AWS resources?

#### Options
- **A.** AWS CloudHSM
- **B.** U2F Security Key **[CORRECT]**
- **C.** AWS Access Keys
- **D.** AWS Key Pair

**Correct Answer:** `B`

#### Detailed Explanation

A U2F Security Key is a physical hardware device that authenticates via USB or NFC using cryptographic protocols, providing a hardware-based second factor for AWS MFA that protects accounts from phishing and credential theft.

AWS CloudHSM provides dedicated hardware security modules for generating and managing cryptographic keys for data encryption, and is a key management service rather than an MFA device used to authenticate AWS account logins. AWS Access Keys consisting of an access key ID and secret access key are credentials used for programmatic API and CLI access, and are a programmatic authentication mechanism rather than an MFA device that adds a second factor to console login. AWS Key Pairs are RSA public/private key combinations used to authenticate SSH connections to Linux EC2 instances, and are an instance-level access mechanism rather than an MFA device for AWS account authentication.

---

<a id="q367-89"></a>
### Question 89 (`Q367`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> You have just hired a skilled sys-admin to join your team. As usual, you have created a new IAM user for him to interact with AWS services. On his first day, you ask him to create snapshots of all existing Amazon EBS volumes and save them in a new Amazon S3 bucket. However, the new member reports back that he is unable to create neither EBS snapshots nor S3 buckets. What might prevent him from doing this simple task?

#### Options
- **A.** EBS and S3 are accessible only to the root account owner
- **B.** The systems administrator must contact AWS Support first to activate his new IAM account
- **C.** There is not enough space in S3 to store the snapshots
- **D.** There is a non-explicit deny to all new users **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

By default, new IAM users have no permissions attached to them, meaning all actions are implicitly denied until explicit permissions are granted through policies, which is why the new administrator cannot create EBS snapshots or S3 buckets.

EBS and S3 are not accessible only to the root account owner; they can be accessed by any IAM user, group, or role that has been granted the appropriate permissions through IAM policies, making this statement factually incorrect. A new IAM user does not need to contact AWS Support to activate their account; IAM users are created and active immediately, and the issue is the absence of permissions rather than an account activation requirement. There is no inherent storage limit in S3 that would prevent creating a new bucket for snapshots; S3 scales automatically to accommodate any amount of data, and the inability to create the bucket is due to missing permissions rather than a storage capacity issue.

---

<a id="q368-90"></a>
### Question 90 (`Q368`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> An external auditor is requesting a log of all accesses to the AWS resources in the company's account. Which of the following services will provide the auditor with the requested information?

#### Options
- **A.** AWS CloudTrail **[CORRECT]**
- **B.** Amazon CloudFront
- **C.** AWS CloudFormation
- **D.** Amazon CloudWatch

**Correct Answer:** `A`

#### Detailed Explanation

AWS CloudTrail records all API calls and management events in an AWS account including who accessed which resources, from what IP address, and at what time, providing exactly the information an auditor needs to review access logs.

Amazon CloudFront is a content delivery network that caches and distributes web content to users at low latency through edge locations, and is a performance optimization service with no capability to log all accesses to AWS account resources. AWS CloudFormation is an infrastructure as code service for provisioning and managing AWS resources through templates, and is a provisioning and automation tool rather than a service that records access logs to AWS resources. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, and while it can collect application logs and service metrics, it does not provide the comprehensive API call audit trail that records all AWS resource accesses the way CloudTrail does.

---

<a id="q369-91"></a>
### Question 91 (`Q369`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service allows a company to connect their AWS resources with an on-premises Microsoft Active Directory, enabling users to sign in with their existing corporate credentials?

#### Options
- **A.** AWS IAM Identity Center
- **B.** AWS Directory Service **[CORRECT]**
- **C.** Amazon Cognito
- **D.** AWS Secrets Manager

**Correct Answer:** `B`

#### Detailed Explanation

AWS Directory Service provides managed Microsoft Active Directory in the AWS Cloud, allowing organizations to connect their AWS resources with an existing on-premises Active Directory so users can access AWS applications using their established corporate credentials.

AWS IAM Identity Center provides single sign-on access to multiple AWS accounts and business applications, but does not provide the managed directory infrastructure needed to extend on-premises Active Directory into AWS. Amazon Cognito provides user identity and authentication for customer-facing web and mobile applications, and is not designed for corporate directory integration with AWS resources. AWS Secrets Manager stores, rotates, and retrieves credentials and secrets programmatically, but does not manage directory services or user authentication against Active Directory.

---

<a id="q375-92"></a>
### Question 92 (`Q375`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service enables you to quickly purchase and deploy SSL/TLS certificates?

#### Options
- **A.** Amazon GuardDuty
- **B.** AWS ACM **[CORRECT]**
- **C.** Amazon Detective
- **D.** AWS WAF

**Correct Answer:** `B`

#### Detailed Explanation

AWS Certificate Manager lets you provision, manage, and deploy SSL/TLS certificates for use with AWS services such as Elastic Load Balancers and CloudFront distributions, offering free public certificates that renew automatically.

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity using machine learning and threat intelligence, and has no capability to provision or manage SSL/TLS certificates. Amazon Detective helps analyze and visualise security data to investigate the root cause of suspicious activity, providing forensic investigation capabilities rather than SSL/TLS certificate provisioning. AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules to block common web exploits, and is a traffic filtering service rather than a certificate provisioning service.

---

<a id="q380-93"></a>
### Question 93 (`Q380`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company wants to grant a new employee long-term access to manage Amazon DynamoDB databases. Which of the following is a recommended best-practice when granting these permissions?

#### Options
- **A.** Create an IAM role and attach a policy with Amazon DynamoDB access permissions
- **B.** Create an IAM role and attach a policy with Administrator access permissions
- **C.** Create an IAM user and attach a policy with Amazon DynamoDB access permissions **[CORRECT]**
- **D.** Create an IAM user and attach a policy with Administrator access permissions

**Correct Answer:** `C`

#### Detailed Explanation

For a specific employee requiring long-term access, an IAM user is the appropriate identity type, and attaching a policy scoped only to Amazon DynamoDB follows the principle of least privilege by granting only the permissions needed for that role.

Creating an IAM role and attaching DynamoDB access permissions would be appropriate for applications or services that need temporary access to DynamoDB, but for a specific long-term employee, an IAM user is the correct identity type rather than a role designed for temporary credential assumption. Creating an IAM role with Administrator access permissions would grant the new employee unrestricted access to all AWS services and resources, violating the principle of least privilege and posing an unnecessary security risk. Creating an IAM user with Administrator access permissions would grant unrestricted access to all AWS services rather than scoping permissions to only Amazon DynamoDB, directly violating the principle of least privilege.

---

<a id="q381-94"></a>
### Question 94 (`Q381`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> When granting permissions to applications running on Amazon EC2 instances, which of the following is considered best practice?

#### Options
- **A.** Generate new IAM access keys every time you delegate permissions
- **B.** Store the required AWS credentials directly within the application code
- **C.** Use temporary security credentials (IAM roles) instead of long-term access keys **[CORRECT]**
- **D.** Do nothing; Applications that run on Amazon EC2 instances do not need permission to interact with other AWS services or resources

**Correct Answer:** `C`

#### Detailed Explanation

IAM Roles provide temporary security credentials that are automatically rotated when assumed, eliminating the need to embed long-term access keys in application code and reducing the risk of credential exposure if the application is compromised.

Generating new IAM access keys every time permissions are delegated would result in a large number of static, long-term credentials that must be tracked and managed, increasing the risk of credential exposure rather than reducing it, and is not a security best practice for applications on EC2. Storing required AWS credentials directly in application code is a serious security anti-pattern that risks credential exposure through code repositories, log files, or application errors, making it the opposite of a best practice. Applications running on EC2 frequently need to interact with other AWS services such as S3, DynamoDB, or SQS to function correctly, making the assumption that no permissions are needed factually incorrect for most real-world applications.

---

<a id="q384-95"></a>
### Question 95 (`Q384`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following can be used to enable the Virtual Multi-Factor Authentication?

#### Options
- **A.** Amazon Connect
- **B.** AWS CLI **[CORRECT]**
- **C.** AWS Identity and Access Management (IAM) **[CORRECT]**
- **D.** Amazon SNS
- **E.** Amazon Virtual Private Cloud

**Correct Answer:** `B, C`

#### Detailed Explanation

Virtual MFA can be enabled through AWS IAM, which provides the console interface for assigning and configuring MFA devices for users, and through the AWS CLI, which allows MFA settings to be managed programmatically.

Amazon Connect is a cloud-based contact center service for handling customer communications, entirely unrelated to authentication or MFA configuration. Amazon SNS is a notification service for sending messages to subscribers and has no role in enabling or managing MFA. Amazon VPC is a virtual private network service for isolating and configuring cloud network infrastructure, unrelated to user authentication settings.

---

<a id="q387-96"></a>
### Question 96 (`Q387`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> What should you do if you see resources, which you don't remember creating, in the AWS Management Console?

#### Options
- **A.** Stop all running services and open an investigation
- **B.** Give your root account password to AWS Support so that they can assist in troubleshooting and securing the account
- **C.** Check the AWS CloudTrail logs and delete all IAM users that have access to your resources
- **D.** Open an investigation and delete any potentially compromised IAM users **[CORRECT]**
- **E.** Change your AWS root account password and the passwords of any IAM users **[CORRECT]**

**Correct Answer:** `D, E`

#### Detailed Explanation

If unrecognized resources appear in your AWS account, this may indicate a security compromise where an attacker has gained access and is creating resources, so you should change your root account password and access keys immediately to revoke the attacker's access and protect the account.

Closing the account immediately would permanently terminate all resources and data without first investigating the extent of the compromise or recovering any workloads, making it a disproportionate response before proper incident response steps have been completed. Removing all IAM users from the account would lock out your legitimate team members and prevent any investigation or remediation work from being performed, making incident response significantly harder without actually addressing the underlying security compromise. Opening a new root account does not address the compromised account, as the original account with its resources and data would still be exposed; incident response requires securing the existing account rather than abandoning it.

---

<a id="q395-97"></a>
### Question 97 (`Q395`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company is developing a mobile application and wants to allow users to use their Amazon, Apple, Facebook, or Google identities to authenticate to the application. Which AWS service should the company use for this purpose?

#### Options
- **A.** Amazon GuardDuty
- **B.** AWS Directory Service
- **C.** Amazon Cognito **[CORRECT]**
- **D.** AWS IAM

**Correct Answer:** `C`

#### Detailed Explanation

Amazon Cognito supports federated identity authentication, allowing users to sign in with their existing Amazon, Apple, Facebook, or Google accounts and exchange those tokens for AWS credentials, making it the correct service for social identity provider integration.

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity and anomalous behavior, and is not a service for enabling user authentication with social identity providers. AWS Directory Service provides managed Microsoft Active Directory for enterprise identity management and SSO with corporate credentials, and is designed for workforce identity rather than customer-facing social identity provider authentication. AWS IAM manages user identities and permissions for accessing AWS services and resources, and while IAM can grant permissions to users authenticated through Cognito, it does not itself handle federated sign-in with Amazon, Apple, Facebook, or Google.

---

<a id="q403-98"></a>
### Question 98 (`Q403`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> There is a requirement to grant a DevOps team full administrative access to all resources in an AWS account. Who can grant them these permissions?

#### Options
- **A.** AWS account owner **[CORRECT]**
- **B.** AWS technical account manager
- **C.** AWS security team
- **D.** AWS cloud support engineers

**Correct Answer:** `A`

#### Detailed Explanation

The AWS account owner holds the root user credentials and has full administrative access to all resources in the account, making them the only entity with the authority to grant full administrative permissions to other users or teams through IAM policies.

An AWS Technical Account Manager is an AWS employee assigned to help Enterprise support plan customers with architectural guidance and support, and does not have the ability to grant permissions within a customer's AWS account. The AWS Security team manages AWS's own internal security posture and is not involved in configuring IAM permissions within individual customer accounts. AWS Cloud Support Engineers provide technical support for resolving issues and answering questions about AWS services, and do not have access to configure IAM policies or grant permissions within customer accounts.

---

<a id="q410-99"></a>
### Question 99 (`Q410`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which statement is true in relation to the security of Amazon EC2?

#### Options
- **A.** You should use instance store volumes to store login data
- **B.** You should regularly patch the operating system and applications on your EC2 instances **[CORRECT]**
- **C.** You should deploy critical components of your application in the Availability Zone that you trust
- **D.** You can track all API calls using Amazon Athena

**Correct Answer:** `B`

#### Detailed Explanation

AWS shared responsibility means the customer is responsible for securing what runs on EC2, including the operating system and applications, which requires regularly applying security patches to close vulnerabilities that could be exploited by attackers.

Instance store volumes provide temporary, high-speed local storage that is deleted when the instance stops or is terminated, making them inappropriate for storing login data that must persist across instance restarts or replacements. Deploying critical application components in a single trusted Availability Zone reduces fault tolerance and does not improve security; best practice is to distribute across multiple Availability Zones for resilience, and no AZ is inherently more trusted than another within the same region. Amazon Athena is a serverless query service for analyzing data stored in S3 using SQL, and does not track API calls; AWS CloudTrail is the correct service for recording API activity across an AWS account.

---

<a id="q414-100"></a>
### Question 100 (`Q414`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following strategies helps protect your AWS root account?

#### Options
- **A.** Delete root user access keys if you do not need them **[CORRECT]**
- **B.** Apply MFA for the root account and use it for all of your work
- **C.** Access the root account only from your personal Mobile Phone
- **D.** Only share your AWS account password or access keys with trusted persons

**Correct Answer:** `A`

#### Detailed Explanation

Deleting root user access keys removes a persistent attack vector, since the root account has unrestricted access to all AWS services and resources, and AWS best practice recommends using IAM users for daily tasks and eliminating root access keys entirely to protect the account.

Applying MFA for the root account is correct but the second part of the option is wrong; AWS recommends enabling MFA on the root account but using it as infrequently as possible and relying on IAM users for day-to-day work, not using the root account for all tasks. Accessing the root account only from a personal mobile phone does not constitute a recognized security control; MFA using an authenticator app on a mobile device is recommended, but restricting access to a specific physical device is not an AWS security best practice and introduces its own risks. Sharing your AWS account password or access keys with trusted persons violates fundamental security principles; credentials should never be shared as this removes individual accountability and increases the risk of credential exposure.

---

<a id="q416-101"></a>
### Question 101 (`Q416`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> You have just set up your AWS environment and have created six IAM user accounts for the DevOps team. What is the AWS recommendation when granting permissions to these IAM accounts?

#### Options
- **A.** Attach a separate IAM policy for each individual account
- **B.** Apply the Principle of Least Privilege **[CORRECT]**
- **C.** For security purposes, you should not grant any permission to the DevOps team
- **D.** Create six different IAM passwords

**Correct Answer:** `B`

#### Detailed Explanation

The Principle of Least Privilege means granting each IAM user only the minimum permissions necessary to perform their assigned job functions, reducing the impact of any accidental or malicious use of credentials.

Attaching a separate IAM policy to each individual account is a valid approach for highly differentiated permissions but is operationally complex; using IAM groups to assign shared policies to all DevOps team members with similar roles is the recommended approach for teams rather than managing policies per user individually. For security purposes, you should not withhold all permissions from the DevOps team; the team needs appropriate permissions to perform their infrastructure management tasks, and the goal is to define those permissions carefully rather than provide none at all. Creating six different IAM passwords involves setting distinct password requirements per user, but password variation does not address the core security concern of permission scope; applying least privilege principles to what each user is allowed to do is the AWS recommendation.

---

<a id="q424-102"></a>
### Question 102 (`Q424`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following services provide real-time auditing for compliance and vulnerabilities?

#### Options
- **A.** AWS Config **[CORRECT]**
- **B.** Amazon Redshift
- **C.** Amazon MQ
- **D.** AWS Trusted Advisor **[CORRECT]**
- **E.** Amazon Cognito

**Correct Answer:** `A, D`

#### Detailed Explanation

AWS Config continuously monitors and records resource configurations to evaluate compliance against desired rules, and AWS Trusted Advisor provides real-time checks across security, performance, cost, and fault tolerance categories. Both provide real-time auditing capabilities.

Amazon Redshift is a fully managed cloud data warehouse service for running analytical queries on large datasets, and is a data analytics service rather than a real-time auditing tool for compliance or vulnerability assessment. Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that enables application messaging and decoupling, and is a messaging infrastructure service with no auditing or compliance checking capability. Amazon Cognito is a user identity and authentication service for web and mobile applications that handles sign-up, sign-in, and access control, and is an identity service rather than a compliance auditing or vulnerability assessment tool.

---

<a id="q428-103"></a>
### Question 103 (`Q428`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What best describes penetration testing?

#### Options
- **A.** Testing your application's response time from different locations
- **B.** Testing your network to find security vulnerabilities that an attacker could exploit **[CORRECT]**
- **C.** Testing your instances to check for the unhealthy ones
- **D.** Testing your software for bugs and errors

**Correct Answer:** `B`

#### Detailed Explanation

Penetration testing is the practice of simulating cyberattacks against your own systems to discover exploitable security vulnerabilities before malicious attackers can find and use them, allowing you to remediate weaknesses proactively.

Testing application response time from different locations describes performance and latency testing, which evaluates how quickly an application responds to requests from various geographic locations rather than identifying security vulnerabilities that attackers could exploit. Testing instances to check for unhealthy ones describes health checking or monitoring, which verifies that compute instances are operational and responsive rather than assessing the security posture of the network for exploitable weaknesses. Testing software for bugs and errors describes functional or quality assurance testing, which validates that code behaves as expected rather than specifically probing for security vulnerabilities that an attacker could use to gain unauthorised access.

---

<a id="q443-104"></a>
### Question 104 (`Q443`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following can help secure your sensitive data in Amazon S3?

#### Options
- **A.** Delete the encryption keys once your data is encrypted
- **B.** With AWS you do not need to worry about encryption
- **C.** Enable S3 Encryption **[CORRECT]**
- **D.** Encrypt the data prior to uploading it **[CORRECT]**
- **E.** Delete all IAM users that have access to S3

**Correct Answer:** `C, D`

#### Detailed Explanation

Enabling S3 encryption through server-side encryption with S3-managed keys, KMS keys, or customer-provided keys protects object confidentiality at rest, and encrypting data before uploading it provides client-side encryption that ensures data is protected before it ever leaves the client. Both are valid approaches to securing sensitive data in Amazon S3.

Deleting encryption keys once data is encrypted would permanently prevent decryption of the stored data, making it impossible to read or use the data again; encryption keys must be retained and managed carefully to ensure continued access to encrypted data. AWS does not automatically handle all security concerns by default; customers are responsible for configuring appropriate encryption, access controls, and bucket policies to protect their data, as the shared responsibility model requires active customer participation in data security. Deleting all IAM users with access to S3 would prevent all legitimate users from accessing the data and disrupt normal operations; proper access control involves granting least privilege permissions to the appropriate users rather than eliminating all access.

---

<a id="q450-105"></a>
### Question 105 (`Q450`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services gives you access to all AWS auditor-issued reports and certifications?

#### Options
- **A.** AWS Artifact **[CORRECT]**
- **B.** AWS Config
- **C.** Amazon CloudWatch
- **D.** AWS CloudTrail

**Correct Answer:** `A`

#### Detailed Explanation

AWS Artifact provides on-demand, self-service access to AWS compliance reports and auditor-issued certifications such as SOC, PCI DSS, and ISO documents, directly from the AWS Management Console without needing to contact AWS support.

AWS Config continuously monitors and records resource configurations against compliance rules to help manage configuration drift and evaluate resource compliance, and is a resource configuration compliance tool rather than a repository of AWS auditor-issued certifications. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications to support observability and alerting, and has no connection to providing access to AWS compliance reports or third-party audit certifications. AWS CloudTrail records all API calls and management events across an AWS account for auditing and security analysis, and produces customer-specific activity logs rather than auditor-issued AWS compliance certifications.

---

<a id="q455-106"></a>
### Question 106 (`Q455`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> For compliance and regulatory purposes, a government agency requires that their applications must run on hardware that is dedicated to them only. How can you meet this requirement?

#### Options
- **A.** Use EC2 Dedicated Hosts **[CORRECT]**
- **B.** Use EC2 Reserved Instances
- **C.** Use EC2 Spot Instances
- **D.** Use EC2 On-demand Instances

**Correct Answer:** `A`

#### Detailed Explanation

EC2 Dedicated Hosts provide physical servers fully dedicated to your use, giving you visibility and control over instance placement on hardware that is not shared with other AWS customers, satisfying strict compliance and regulatory requirements for physical isolation.

EC2 Reserved Instances are a pricing model that provides a significant discount in exchange for a commitment to use a specific instance type for one or three years, and they do not guarantee that the underlying hardware is dedicated to a single customer; reserved instances can run on shared multi-tenant hardware. EC2 Spot Instances allow you to use spare AWS capacity at a reduced price, with the caveat that they can be interrupted when AWS needs the capacity back, and they do not provide dedicated physical hardware or compliance guarantees about hardware isolation. EC2 On-Demand Instances allow you to pay for compute capacity by the hour or second without any upfront commitments, and they run on shared multi-tenant hardware rather than dedicated servers, making them unsuitable for compliance requirements mandating physical hardware dedication.

---

<a id="q458-107"></a>
### Question 107 (`Q458`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What can you use to assign permissions directly to an IAM user?

#### Options
- **A.** IAM Identity
- **B.** IAM Group
- **C.** IAM Role
- **D.** IAM Policy **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

An IAM Policy is a JSON document that defines permissions by specifying allowed or denied actions on AWS resources, and can be attached directly to an IAM user to grant specific access rights.

IAM Identity is not a standalone IAM construct used to assign permissions; AWS IAM Identity Center is a separate service for managing workforce access across multiple accounts, and does not refer to a permission assignment mechanism within IAM itself. An IAM Group is a collection of IAM users that share the same attached policies, and while attaching a policy to a group affects all its members, the group itself is not what assigns permissions directly to an individual user. An IAM Role is an identity that defines a set of permissions and is assumed temporarily by users, services, or applications, and is not attached directly to a user the way a policy is.

---

<a id="q463-108"></a>
### Question 108 (`Q463`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following would you use to manage your encryption keys in the AWS Cloud?

#### Options
- **A.** AWS KMS **[CORRECT]**
- **B.** AWS Certificate Manager
- **C.** AWS CodeDeploy
- **D.** AWS CodeCommit
- **E.** CloudHSM **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

AWS KMS provides centralized software-based key management with AWS-managed infrastructure and integrates natively with most AWS services for encryption at rest, and AWS CloudHSM provides dedicated hardware security modules for customers requiring hardware-based key control for regulatory compliance. Both are valid services for managing encryption keys in the AWS Cloud.

AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate provisioning service rather than a key management service for creating and storing encryption keys. AWS CodeDeploy is an automated deployment service that delivers application code to EC2 instances, Lambda functions, and on-premises servers, and is a deployment automation tool with no encryption key management capability. AWS CodeCommit is a fully managed source control service for hosting Git repositories for version-controlled code storage, and is a code collaboration tool rather than an encryption key management service.

---

<a id="q466-109"></a>
### Question 109 (`Q466`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company has infrastructure hosted in an on-premises data center. They currently have an operations team that takes care of identity management. If they decide to migrate to the AWS cloud, which of the following services would help them perform the same role in AWS?

#### Options
- **A.** AWS IAM **[CORRECT]**
- **B.** AWS Outposts
- **C.** AWS Directory Service
- **D.** Amazon Redshift

**Correct Answer:** `A`

#### Detailed Explanation

AWS Identity and Access Management is the service that provides centralized control over authentication and authorisation for AWS resources, fulfilling the same identity management role in the cloud that an on-premises operations team performs in a traditional data center.

AWS Outposts extends AWS infrastructure and services to on-premises locations and is a compute and storage solution rather than an identity management service. AWS Directory Service provides managed Microsoft Active Directory integration for enterprise identity, which can complement IAM but is a specialized service for organizations needing AD integration rather than the core AWS identity management service. Amazon Redshift is a fully managed cloud data warehousing service designed for analytical queries on large datasets and has no capability to manage user identities or control access to AWS services.

---

<a id="q468-110"></a>
### Question 110 (`Q468`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Where can AWS account owners get a list of all users in their account, including the status of their AWS credentials?

#### Options
- **A.** AWS CloudTrail
- **B.** IAM Credential Report **[CORRECT]**
- **C.** AWS Artifact reports
- **D.** AWS Cost and Usage Report

**Correct Answer:** `B`

#### Detailed Explanation

The IAM credential report provides a comprehensive list of all IAM users in an AWS account along with the status of their credentials including passwords, access keys, MFA status, and last used dates, making it the correct tool for auditing user credentials.

AWS Trusted Advisor provides automated checks across security, performance, cost, and fault tolerance categories and includes some IAM-related security checks, but does not generate a downloadable report listing all users and their individual credential status details. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and has no capability to list IAM users or report on the status of their credentials such as access keys and MFA devices. AWS CloudTrail records all API calls and management events for auditing purposes, and while it logs IAM-related actions, it does not provide a consolidated report of all current users and the live status of their credentials.

---

<a id="q469-111"></a>
### Question 111 (`Q469`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services enables you to easily generate and use your own encryption keys in the AWS Cloud?

#### Options
- **A.** AWS Shield
- **B.** AWS Certificate Manager
- **C.** AWS CloudHSM **[CORRECT]**
- **D.** AWS WAF

**Correct Answer:** `C`

#### Detailed Explanation

AWS CloudHSM provides dedicated, single-tenant hardware security modules in the AWS Cloud, giving you full control over encryption key generation and management with FIPS 140-2 Level 3 validated hardware for customers requiring hardware-based key control.

AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to generate or manage encryption keys. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to encrypt data in transit, and is a certificate management service rather than a general-purpose encryption key generation service. AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules to block web exploits, and is a traffic filtering service with no capability to generate or manage customer encryption keys.

---

<a id="q473-112"></a>
### Question 112 (`Q473`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following resources can an AWS customer use to learn more about prohibited uses of the services offered by AWS?

#### Options
- **A.** AWS Service Control Policies (SCPs)
- **B.** AWS Artifact
- **C.** AWS Budgets
- **D.** AWS Acceptable Use Policy **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

The AWS Acceptable Use Policy outlines prohibited uses of AWS services, including activities such as sending spam, hosting illegal content, or launching attacks, and applies to all AWS customers and users.

AWS Service Control Policies are permission guardrails applied within AWS Organizations to restrict what actions accounts can perform, not a document describing prohibited uses of AWS services to external customers. AWS Artifact is a self-service portal for accessing AWS compliance reports and security documentation such as SOC reports and ISO certifications, not a resource for understanding usage restrictions. AWS Budgets is a cost management tool for setting spending thresholds and receiving alerts, unrelated to acceptable use or prohibited activities.

---

<a id="q474-113"></a>
### Question 113 (`Q474`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following security resources are available to any user for free?

#### Options
- **A.** AWS Bulletins **[CORRECT]**
- **B.** AWS Technical Account Manager
- **C.** AWS Support API
- **D.** AWS Security Blog **[CORRECT]**
- **E.** AWS Classroom Training

**Correct Answer:** `A, D`

#### Detailed Explanation

AWS documentation provides comprehensive technical guides and API references for all AWS services at no cost and is freely accessible to any user, and AWS discussion forums allow any user to post questions and share knowledge about AWS services at no charge. Both are free security resources.

AWS Support Center provides technical case support that requires a paid support plan to submit cases, and while some basic content is available for free, the case submission feature for getting direct engineering assistance is not a free resource available to all users without a qualifying support plan. AWS Managed Services provides ongoing management of AWS infrastructure on behalf of enterprise customers for a fee, and is a paid service rather than a free security resource available to any user. Amazon Inspector is an automated vulnerability assessment service that requires configuration and generates findings, and while there is a free trial period, it is a paid service rather than a free resource available to all users without any cost.

---

<a id="q476-114"></a>
### Question 114 (`Q476`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is the responsibility of AWS according to the AWS Shared Responsibility Model?

#### Options
- **A.** Securing regions and edge locations **[CORRECT]**
- **B.** Performing auditing tasks
- **C.** Monitoring AWS resources usage
- **D.** Securing access to AWS resources

**Correct Answer:** `A`

#### Detailed Explanation

Under the Shared Responsibility Model, AWS is responsible for securing the physical infrastructure, including Regions, Availability Zones, and edge locations that make up the AWS global network.

Performing auditing tasks is the customer's responsibility. Customers are responsible for auditing their own resource usage, access logs, and compliance activities. Monitoring AWS resources usage is the customer's responsibility. Tools like CloudWatch are available but it is the customer who configures and acts on monitoring. Securing access to AWS resources is the customer's responsibility. Managing IAM users, roles, and permissions falls under security in the cloud, not security of the cloud.

---

<a id="q479-115"></a>
### Question 115 (`Q479`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services enables you to generate and use your own encryption keys on dedicated hardware in the AWS Cloud?

#### Options
- **A.** AWS Secrets Manager
- **B.** AWS Certificate Manager
- **C.** AWS CloudHSM **[CORRECT]**
- **D.** AWS KMS

**Correct Answer:** `C`

#### Detailed Explanation

AWS CloudHSM provides dedicated, single-tenant hardware security modules within the AWS Cloud, giving customers full control over key generation and management on physical HSM hardware that only they can access, satisfying strict regulatory requirements for hardware-based key custody.

AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials, API keys, and OAuth tokens, and is a secrets management service rather than a service for generating customer-controlled encryption keys on dedicated hardware. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to encrypt data in transit, and is a certificate management service that does not provide customer-controlled encryption keys on dedicated hardware. AWS KMS is a managed service that generates and manages encryption keys using a software-based service backed by hardware that AWS manages and shares across multiple customers, and does not provide the dedicated single-tenant hardware access that CloudHSM offers.

---

<a id="q480-116"></a>
### Question 116 (`Q480`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Who is responsible for scaling a DynamoDB database in the AWS Shared Responsibility Model?

#### Options
- **A.** Your security team
- **B.** Your development team
- **C.** AWS **[CORRECT]**
- **D.** Your internal DevOps team

**Correct Answer:** `C`

#### Detailed Explanation

Amazon DynamoDB is a fully managed NoSQL database service where AWS handles all scaling automatically, including read and write capacity adjustments, so customers do not need to manage or plan for database scaling themselves.

The customer's security team focuses on security policies, access controls, and compliance rather than the operational scaling of a managed database service, and DynamoDB's autoscaling is handled by AWS infrastructure rather than any customer team. The development team builds and maintains application code, and while they configure DynamoDB table settings during development, the actual scaling of a fully managed service is performed automatically by AWS rather than manually by developers. The internal DevOps team manages infrastructure, deployments, and operational workflows, but the scaling of a fully managed service like DynamoDB is handled automatically by AWS and does not require DevOps intervention.

---

<a id="q487-117"></a>
### Question 117 (`Q487`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which feature enables users to sign into their AWS accounts with their existing corporate credentials?

#### Options
- **A.** Federation **[CORRECT]**
- **B.** Access keys
- **C.** IAM Permissions
- **D.** AWS WAF rules

**Correct Answer:** `A`

#### Detailed Explanation

Identity federation allows users to sign into AWS using credentials from an external identity provider such as Active Directory or SAML, eliminating the need to create separate IAM users for each corporate employee.

Access keys are long-term credentials consisting of an access key ID and secret used for programmatic access to AWS via the CLI or API, and are not a mechanism for signing into AWS with corporate credentials. IAM Permissions define what actions an authenticated user or role is allowed to perform on AWS resources, and are an authorisation mechanism rather than a feature that enables corporate credential sign-in. AWS WAF rules define conditions for filtering web traffic to protect applications from common exploits, and are a web security feature with no connection to identity or authentication.

---

<a id="q488-118"></a>
### Question 118 (`Q488`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> According to the AWS shared responsibility model, what are the controls that customers fully inherit from AWS?

#### Options
- **A.** Awareness and Training
- **B.** Communications controls
- **C.** Data center security controls **[CORRECT]**
- **D.** Environmental controls **[CORRECT]**
- **E.** Resource Configuration Management

**Correct Answer:** `C, D`

#### Detailed Explanation

Data center security controls and environmental controls are fully inherited from AWS because customers have no physical access to AWS facilities and take on zero responsibility for managing them.

Awareness and Training this is a shared control where both AWS and the customer independently maintain their own training programs for their respective workforces, so customers do not fully inherit it from AWS. Communications controls this is also a shared control, with each party responsible for securing and managing communications within their own environment. Resource Configuration Management customers are responsible for configuring the AWS resources they deploy, such as security groups, IAM policies, and application settings, making this a customer-managed control rather than an inherited one.

---

<a id="q491-119"></a>
### Question 119 (`Q491`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following are part of the seven design principles for security in the cloud?

#### Options
- **A.** Use manual monitoring techniques to protect your AWS resources
- **B.** Use IAM roles to grant temporary access instead of long-term credentials **[CORRECT]**
- **C.** Scale horizontally to protect from failures
- **D.** Enable real-time traceability **[CORRECT]**
- **E.** Never store sensitive data in the cloud

**Correct Answer:** `B, D`

#### Detailed Explanation

Implementing strong identity foundations through least privilege and appropriate credential management, and enabling traceability by monitoring, alerting, and auditing all actions and resource changes, are two of the seven security design principles of the Well-Architected Framework.

Using the same AWS account for all workloads in a single environment contradicts the security principle of applying security at all layers and using multiple accounts to isolate workloads, and is an anti-pattern rather than a security design principle. Replacing IAM users with API keys as the primary access mechanism would use long-term credentials for all access rather than temporary credentials through roles, which is the opposite of the principle favoring short-term credentials and role-based access. Granting root user access to all authorised users contradicts the principle of granting least privilege and protecting root account credentials, as the root user should be used minimally and its credentials never shared.

---

<a id="q493-120"></a>
### Question 120 (`Q493`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the main benefit of attaching security groups to an Amazon RDS instance?

#### Options
- **A.** Manages user access and encryption keys
- **B.** Controls what IP address ranges can connect to your database instance **[CORRECT]**
- **C.** Deploys SSL/TLS certificates for use with your database instance
- **D.** Distributes incoming traffic across multiple targets

**Correct Answer:** `B`

#### Detailed Explanation

Security groups attached to an RDS instance act as a virtual firewall controlling which IP address ranges and EC2 instances are allowed to establish connections to the database, restricting network access to only authorised sources.

Managing user access and encryption keys describes AWS IAM and AWS KMS respectively, which are separate services for identity management and key management rather than functions provided by security groups attached to an RDS instance. Deploying SSL/TLS certificates for database connections is performed by AWS Certificate Manager and the RDS parameter group configuration, not by security groups, which control network connectivity rather than certificate provisioning. Distributing incoming traffic across multiple targets describes an Elastic Load Balancer, which routes requests to multiple backend instances, and is not a function of security groups attached to a database instance.

---

<a id="q496-121"></a>
### Question 121 (`Q496`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> You have been tasked with auditing the security of your VPC. As part of this process, you need to start by analyzing what inbound and outbound traffic is allowed on your EC2 instances. What two parts of the VPC do you need to check to accomplish this task?

#### Options
- **A.** Network ACLs and Traffic Manager
- **B.** Network ACLs and Subnets
- **C.** Security Groups and Internet Gateways
- **D.** Security Groups and Network ACLs **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Security groups control inbound and outbound traffic at the EC2 instance level with stateful evaluation, and Network ACLs control traffic at the subnet level with stateless rule evaluation. Checking both gives a complete picture of what traffic is allowed to and from EC2 instances in the VPC.

Network ACLs and Traffic Manager is not a valid combination for VPC traffic analysis; AWS Traffic Manager does not exist as an AWS service name, and the correct subnet-level control is Network ACLs rather than a non-existent Traffic Manager. Network ACLs and Subnets is partially correct in that subnets are VPC components, but subnets themselves are network segments rather than traffic control mechanisms, and checking subnets does not tell you what traffic rules are applied; you need to check the ACLs attached to those subnets. Security groups and Internet Gateways is partially correct in that Internet Gateways allow internet traffic into the VPC, but they do not define granular allow/deny rules for instance-level traffic; checking security groups alone misses the subnet-level controls provided by Network ACLs.

---

<a id="q499-122"></a>
### Question 122 (`Q499`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which statement is true in relation to security in AWS?

#### Options
- **A.** AWS manages everything related to EC2 operating systems
- **B.** AWS customers are responsible for patching any database software running on Amazon EC2 **[CORRECT]**
- **C.** Server side encryption is the responsibility of AWS
- **D.** AWS is responsible for the security of your application

**Correct Answer:** `B`

#### Detailed Explanation

Under the shared responsibility model, customers are responsible for patching and maintaining any software they install on EC2 instances, including database software, operating systems, and applications.

AWS does not manage everything related to EC2 operating systems. The guest operating system, including configuration, patching, and security, is the customer's responsibility, while AWS manages only the underlying physical infrastructure. Server-side encryption is not automatically the responsibility of AWS. Customers choose whether to enable encryption and can manage their own keys through AWS KMS, making encryption a shared responsibility depending on how it is configured. AWS is not responsible for the security of customer applications. Application-level security, including code quality, access controls, and data handling, is entirely the customer's responsibility under the shared responsibility model.

---

<a id="q507-123"></a>
### Question 123 (`Q507`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> What are the main differences between an IAM user and an IAM role in AWS?

#### Options
- **A.** An IAM user is uniquely associated with only one person, however a role is intended to be assumable by anyone who needs it **[CORRECT]**
- **B.** An IAM user has permanent credentials associated with it, however a role has temporary credentials associated with it **[CORRECT]**
- **C.** IAM users are more cost effective than IAM roles
- **D.** A role is uniquely associated with only one person, however an IAM user is intended to be assumable by anyone who needs it
- **E.** An IAM user has temporary credentials associated with it, however a role has permanent credentials associated with it

**Correct Answer:** `A, B`

#### Detailed Explanation

An IAM user is a permanent identity associated with one specific person and has long-term credentials such as a password and access keys, while an IAM role provides temporary credentials and can be assumed by multiple users, services, or applications that need it.

The option stating that a role is uniquely associated with only one person and a user is assumable by anyone reverses the correct relationship; IAM users represent individual people with their own credentials, while roles are designed to be assumed by anyone or any service that requires the permissions they define. The option stating that IAM users have temporary credentials and roles have permanent credentials is the opposite of the correct relationship; IAM users have long-term permanent credentials while roles issue temporary credentials that expire automatically when the session ends. IAM users and roles are not priced differently from each other; there is no direct cost associated with creating IAM users or roles, and the claim that users are more cost effective is not a meaningful comparison.

---

<a id="q509-124"></a>
### Question 124 (`Q509`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What does Amazon GuardDuty do to protect AWS accounts and workloads?

#### Options
- **A.** Notifies AWS customers about abuse events once they are reported
- **B.** Continuously monitors AWS infrastructure and helps detect threats such as attacker reconnaissance or account compromise **[CORRECT]**
- **C.** Helps AWS customers identify the root cause of potential security issues
- **D.** Checks security groups for rules that allow unrestricted access to AWS resources

**Correct Answer:** `B`

#### Detailed Explanation

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads using machine learning and threat intelligence to identify suspicious activity such as attacker reconnaissance, compromised instances, or unusual API calls.

Notifying customers about abuse events once they are reported is the function of the AWS Abuse Team, which handles reports of AWS resources being used for malicious activity and communicates with affected account holders, rather than a capability of GuardDuty. Helping customers identify the root cause of potential security issues describes Amazon Detective, which analyzes and visualises security data from GuardDuty and CloudTrail to trace the origin and scope of suspicious activity rather than detecting threats in real time. Checking security groups for rules that allow unrestricted access to AWS resources is a function of AWS Trusted Advisor, which performs security checks including identification of overly permissive security group configurations, not GuardDuty.

---

<a id="q516-125"></a>
### Question 125 (`Q516`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following requires an access key ID and a secret access key to get long-lived programmatic access to AWS resources?

#### Options
- **A.** IAM group
- **B.** IAM user **[CORRECT]**
- **C.** IAM role
- **D.** AWS account root user **[CORRECT]**
- **E.** AWS Technical Account Manager

**Correct Answer:** `B, D`

#### Detailed Explanation

IAM users and the AWS account root user are both identities that can be issued long-lived access key IDs and secret access keys for programmatic access to AWS resources via the CLI or SDKs.

An IAM group is a collection of IAM users used to manage shared permissions collectively, and is not an identity that can authenticate or be issued access keys of any kind. An IAM role uses temporary security credentials that are automatically issued and rotated when the role is assumed, and does not support long-lived access keys. An AWS Technical Account Manager is an AWS support professional assigned to Enterprise support plan customers, and is a person rather than an IAM identity construct that can hold or be issued access keys.

---

<a id="q523-126"></a>
### Question 126 (`Q523`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following AWS services integrates with AWS Shield and AWS Web Application Firewall (AWS WAF) to protect against network and application layer DDoS attacks?

#### Options
- **A.** Amazon EFS
- **B.** AWS Secrets Manager
- **C.** AWS Systems Manager
- **D.** Amazon CloudFront **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Amazon CloudFront integrates natively with AWS Shield for DDoS protection at the network layer and with AWS WAF for application-layer traffic filtering, providing a layered defense against both network and application layer DDoS attacks at the edge.

Amazon EFS is a fully managed elastic file system for providing shared file storage to EC2 instances and other compute services, and is a storage service with no capability to integrate with Shield or WAF for DDoS protection. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service rather than a service that integrates with Shield and WAF for traffic protection. AWS Systems Manager provides operational tools for managing AWS resources at scale including patching, configuration management, and session management, and is an operations service rather than a content delivery or traffic filtering service.

---

<a id="q524-127"></a>
### Question 127 (`Q524`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services is used when encrypting EBS volumes?

#### Options
- **A.** AWS WAF
- **B.** AWS KMS **[CORRECT]**
- **C.** Amazon Macie
- **D.** Amazon GuardDuty

**Correct Answer:** `B`

#### Detailed Explanation

AWS KMS manages the encryption keys used for EBS volume encryption, handling key creation, storage, rotation, and access control, integrating transparently with EBS to encrypt data at rest.

AWS WAF is a web application firewall that filters HTTP and HTTPS traffic to block common web exploits such as SQL injection and cross-site scripting, and is a traffic filtering service with no role in managing encryption keys for EBS volumes. Amazon Macie uses machine learning to discover and classify sensitive data stored in Amazon S3, and is a data classification service for S3 rather than a key management service for EBS encryption. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity using machine learning and threat intelligence, and is a security monitoring service rather than a key management service for encrypting EBS volumes.

---

<a id="q525-128"></a>
### Question 128 (`Q525`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> The AWS account administrator of your company has been fired. With the permissions granted to him as an administrator, he was able to create multiple IAM user accounts and access keys. Additionally, you are not sure whether he has access to the AWS root account or not. What should you do immediately to protect your AWS infrastructure?

#### Options
- **A.** Download all the attached policies in a safe place
- **B.** Delete all IAM accounts and recreate them
- **C.** Use the CloudWatch service to check all API calls that have been made in your account since the administrator was fired
- **D.** Rotate all access keys **[CORRECT]**
- **E.** Change the email address and password of the root user account and enable MFA **[CORRECT]**

**Correct Answer:** `D, E`

#### Detailed Explanation

Rotating all access keys immediately invalidates any keys the former administrator may have copied or retained, and changing the root account email and password with MFA enabled prevents root-level access using any credentials the administrator may have had.

Downloading attached policies to a safe place does not address the immediate security risk; the priority is to revoke the former administrator's access rather than preserving policy documentation, and policies can be reviewed from the console at any time. Deleting all IAM accounts and recreating them would lock out the entire team immediately and disrupt operations without actually addressing whether the root account is compromised; the root account password change must take priority. Using CloudWatch to check all API calls made since the administrator was fired is a useful forensic step for understanding what actions were taken, but it is a post-incident investigation activity rather than an immediate protective measure that should come before securing credentials.

---

<a id="q531-129"></a>
### Question 129 (`Q531`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> A financial services company decides to migrate one of its applications to AWS. The application deals with sensitive data, such as credit card information, and must run on a PCI-compliant environment. Which of the following is the company's responsibility when building a PCI-compliant environment in AWS?

#### Options
- **A.** Start the migration process immediately as all AWS services are PCI compliant
- **B.** Ensure that AWS services are configured properly to meet all PCI DSS standards **[CORRECT]**
- **C.** Restrict any access to cardholder data and create a policy that addresses information security for all personnel **[CORRECT]**
- **D.** Configure the underlying infrastructure of AWS services to meet all PCI DSS requirements
- **E.** Ensure that all PCI DSS physical security requirements are met

**Correct Answer:** `B, C`

#### Detailed Explanation

Customers must properly configure AWS services to meet PCI DSS standards as AWS's compliance certifications cover the infrastructure layer but not the customer's specific service configurations, and customers must restrict cardholder data access and maintain an information security policy as these are customer responsibilities under PCI DSS.

Not all AWS services are PCI DSS compliant by default; only specific AWS services are in scope for PCI compliance, and customers must verify that the services they use are in scope and configured correctly to maintain a PCI-compliant environment. Configuring the underlying AWS infrastructure to meet PCI DSS requirements is not the customer's responsibility; AWS manages and maintains the physical infrastructure, hardware, and network to meet PCI standards, and customers are responsible only for how they configure the services built on top of that infrastructure. Ensuring that all PCI DSS physical security requirements are met is AWS's responsibility; the physical security of data centers, including access controls, surveillance, and hardware handling, is managed by AWS under the shared responsibility model.

---

<a id="q535-130"></a>
### Question 130 (`Q535`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following steps should be taken by a customer when conducting penetration testing on AWS?

#### Options
- **A.** Conduct penetration testing using Amazon Inspector, and then notify AWS support
- **B.** Request and wait for approval from the customer's internal security team, and then conduct testing **[CORRECT]**
- **C.** Notify AWS support, and then conduct testing immediately
- **D.** Request and wait for approval from AWS support, and then conduct testing

**Correct Answer:** `B`

#### Detailed Explanation

Since 2019, AWS allows customers to perform penetration testing on permitted services including EC2, RDS, CloudFront, and API Gateway without prior AWS approval, so customers should follow their own internal security review and authorisation process before conducting tests.

Amazon Inspector is an automated vulnerability assessment service that scans for known vulnerabilities and network misconfigurations, but it is not a penetration testing tool and using it does not substitute for or require notification to AWS support before conducting actual penetration testing. AWS no longer requires customers to notify AWS support before conducting penetration testing on permitted services; the policy changed to allow testing without prior approval, so notifying and then conducting testing immediately is based on an outdated requirement. Requesting and waiting for approval from AWS support before conducting penetration testing is no longer required for permitted services; AWS updated its policy to allow customers to test their own resources without prior approval, removing the requirement for a formal approval process.

---

<a id="q550-131"></a>
### Question 131 (`Q550`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which task is AWS responsible for in the shared responsibility model for security and compliance?

#### Options
- **A.** Granting access to individuals and services
- **B.** Encrypting data in transit
- **C.** Updating Amazon EC2 host firmware **[CORRECT]**
- **D.** Updating operating systems

**Correct Answer:** `C`

#### Detailed Explanation

Updating the host firmware on EC2 physical servers is AWS's responsibility, as customers have no access to or control over the underlying hardware beneath their instances.

Granting access to individuals and services is the customer's responsibility, as customers manage their own IAM users, roles, and permissions within their AWS account. Encrypting data in transit is the customer's responsibility, as customers decide whether and how to implement encryption for their own data using HTTPS, TLS, or other mechanisms. Updating operating systems is the customer's responsibility on services like EC2, where customers control the guest OS and are accountable for keeping it patched and up to date.

---

<a id="q553-132"></a>
### Question 132 (`Q553`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> According to the AWS shared responsibility model what is the sole responsibility of AWS?

#### Options
- **A.** Application security
- **B.** Edge location management **[CORRECT]**
- **C.** Patch management
- **D.** Client-side data

**Correct Answer:** `B`

#### Detailed Explanation

Managing edge locations, the physical infrastructure used by CloudFront and other services, is solely AWS's responsibility as part of its obligation to operate and maintain the global infrastructure underpinning its services.

Application security is the customer's responsibility under the Shared Responsibility Model, as customers are accountable for securing the code, configurations, and access controls within their own applications. Patch management is a shared control where AWS patches the underlying infrastructure and managed services, while customers retain responsibility for patching their own operating systems and applications. Client-side data is the customer's responsibility, as customers control how their data is classified, encrypted, and managed on the client side regardless of which AWS services they use.

---

<a id="q555-133"></a>
### Question 133 (`Q555`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service identifies security groups that allow unrestricted access to a user's AWS resources?

#### Options
- **A.** AWS Trusted Advisor **[CORRECT]**
- **B.** Amazon Inspector
- **C.** Amazon CloudWatch
- **D.** AWS CloudTrail

**Correct Answer:** `A`

#### Detailed Explanation

AWS Trusted Advisor checks your security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports such as SSH and RDP, flagging potential security risks in its Security category checks.

Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and while it identifies network reachability issues, the simplest tool for checking security groups for unrestricted access is Trusted Advisor. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability service rather than a tool that audits security group configurations for overly permissive rules. AWS CloudTrail records all API calls and management events for auditing, capturing who created or modified security group rules and when, but it records actions after the fact rather than proactively identifying groups with unrestricted access.

---

<a id="q564-134"></a>
### Question 134 (`Q564`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the AWS shared responsibility model, which of the following activities are the customer's responsibility?

#### Options
- **A.** Patching operating system components for Amazon Relational Database Server (Amazon RDS)
- **B.** Encrypting data on the client-side **[CORRECT]**
- **C.** Training the data center staff
- **D.** Configuring Network Access Control Lists (ACL) **[CORRECT]**
- **E.** Maintaining environmental controls within a data center

**Correct Answer:** `B, D`

#### Detailed Explanation

Customers are responsible for encrypting data on the client side before sending it to AWS, and for configuring Network ACLs to control inbound and outbound traffic at the subnet level in their VPC.

Patching operating system components for Amazon RDS is entirely AWS's responsibility, as RDS is a managed service where AWS handles all underlying OS and database engine patching on the customer's behalf. Training data center staff is entirely AWS's responsibility, as customers have no access to or involvement in the physical facilities and operations teams that run AWS infrastructure. Maintaining environmental controls within a data center such as power, cooling, and fire suppression is entirely AWS's responsibility and is fully inherited by customers under the model.

---

<a id="q565-135"></a>
### Question 135 (`Q565`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the shared responsibility model, which of the following is a shared control between a customer and AWS?

#### Options
- **A.** Physical controls
- **B.** Patch management **[CORRECT]**
- **C.** Zone security
- **D.** Data center auditing

**Correct Answer:** `B`

#### Detailed Explanation

Patch management is a shared control. AWS patches the underlying infrastructure and managed service platforms, while customers are responsible for patching their own guest operating systems and applications.

Physical controls are AWS's responsibility exclusively, covering physical security of data centers and hardware. Zone security is also AWS's responsibility, covering the physical and network isolation between Availability Zones. Data center auditing is AWS's responsibility, though customers can request compliance reports via AWS Artifact.

---

<a id="q573-136"></a>
### Question 136 (`Q573`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which AWS service or feature can enhance network security by blocking requests from a particular network for a web application on AWS?

#### Options
- **A.** AWS WAF **[CORRECT]**
- **B.** AWS Trusted Advisor
- **C.** AWS Direct Connect
- **D.** AWS Organizations
- **E.** Network ACLs **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

AWS WAF creates rules to block requests from specific IP addresses, networks, or matching certain patterns, filtering malicious web traffic at the application layer, and Network ACLs are stateless subnet-level firewalls that can block traffic from specific IP ranges at the network layer. Both can enhance network security by blocking requests from particular networks.

AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and while it identifies insecure configurations, it does not itself block network requests or actively enforce traffic rules. AWS Direct Connect provides a dedicated private network connection between on-premises data centers and AWS, and is a connectivity service rather than a tool for blocking or filtering web application traffic. AWS Organizations manages multiple AWS accounts under a central structure for governance and consolidated billing, and does not have the capability to block network traffic from specific IP ranges for web applications.

---

<a id="q575-137"></a>
### Question 137 (`Q575`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which service enables risk auditing by continuously monitoring and logging account activity, including user actions in the AWS Management Console and AWS SDKs?

#### Options
- **A.** Amazon CloudWatch
- **B.** AWS CloudTrail **[CORRECT]**
- **C.** AWS Config
- **D.** AWS Health

**Correct Answer:** `B`

#### Detailed Explanation

AWS CloudTrail continuously logs all account activity and API calls across AWS infrastructure, providing a complete audit trail that supports risk auditing, compliance monitoring, and security analysis.

Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational visibility into performance and health, and while it can monitor logs, it does not record API calls or user actions for risk auditing and compliance purposes. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance against desired settings, and focuses on resource configuration changes rather than logging user actions and API calls for risk auditing. AWS Health provides personalized alerts and remediation guidance when AWS is experiencing events that may affect your resources, and is a service health notification tool rather than an account activity logging or risk auditing service.

---

<a id="q576-138"></a>
### Question 138 (`Q576`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Where can AWS compliance and certification reports be downloaded?

#### Options
- **A.** AWS Artifact **[CORRECT]**
- **B.** AWS Concierge
- **C.** AWS Certificate Manager
- **D.** AWS Trusted Advisor

**Correct Answer:** `A`

#### Detailed Explanation

AWS Artifact is the self-service portal where customers can download AWS compliance and certification reports including SOC, PCI, ISO, and HIPAA eligibility documentation without needing to contact AWS directly.

AWS Concierge is a dedicated support resource for Enterprise support plan customers that assists with billing and account management, and is not a portal for downloading compliance reports or technical certification documents. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate provisioning service rather than a repository of AWS compliance and audit reports. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and while it includes security checks, it does not provide downloadable AWS compliance certification reports.

---

<a id="q581-139"></a>
### Question 139 (`Q581`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the AWS customer responsible for according to the AWS shared responsibility model?

#### Options
- **A.** Physical access controls
- **B.** Data encryption **[CORRECT]**
- **C.** Secure disposal of storage devices
- **D.** Environmental risk management

**Correct Answer:** `B`

#### Detailed Explanation

Data encryption is the customer's responsibility under the shared responsibility model. AWS provides the tools and services to enable encryption, such as AWS KMS and native encryption options across storage services, but the customer decides whether to enable encryption and manages the keys and access policies.

Physical access controls at AWS data centers are entirely AWS's responsibility; customers have no access to the physical facilities and rely on AWS to implement and enforce physical security measures. Secure disposal of storage devices is AWS's responsibility, as customers never have physical possession of AWS hardware and AWS follows industry standards for decommissioning and disposing of storage media. Environmental risk management for the AWS infrastructure, including temperature control, humidity, and fire suppression in data centers, is entirely AWS's responsibility as part of securing the underlying physical infrastructure.

---

<a id="q587-140"></a>
### Question 140 (`Q587`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service would you use to obtain compliance reports and certificates?

#### Options
- **A.** AWS Artifact **[CORRECT]**
- **B.** AWS Lambda
- **C.** Amazon Inspector
- **D.** AWS Certificate Manager

**Correct Answer:** `A`

#### Detailed Explanation

AWS Artifact provides on-demand access to AWS compliance reports and certifications including SOC, PCI DSS, ISO, and HIPAA documents, available directly from the AWS Management Console without needing to engage AWS support.

AWS Lambda is a serverless compute service that runs code in response to events without requiring server provisioning or management, and is a compute service with no connection to compliance reports or certification documentation. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and produces customer-specific vulnerability findings rather than AWS compliance certifications. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services, and is a certificate management service rather than a repository of compliance reports or regulatory certifications.

---

<a id="q589-141"></a>
### Question 141 (`Q589`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> How would an AWS customer easily apply common access controls to a large set of users?

#### Options
- **A.** Apply an IAM policy to an IAM group **[CORRECT]**
- **B.** Apply an IAM policy to an IAM role
- **C.** Apply the same IAM policy to all IAM users with access to the same workload
- **D.** Apply an IAM policy to an Amazon Cognito user pool

**Correct Answer:** `A`

#### Detailed Explanation

Attaching an IAM policy to an IAM group applies those permissions to all users in the group simultaneously, making it the most efficient way to manage common access controls for a large number of users without configuring each user individually.

Applying an IAM policy to an IAM role would affect entities that assume that role, such as applications or services, rather than applying consistent controls directly to a large set of named users who need the same permissions. Applying the same IAM policy to all IAM users individually would achieve the desired result but requires editing each user's policy separately, which is time-consuming and error-prone at scale compared to using a group. Applying an IAM policy to an Amazon Cognito user pool affects application users authenticating through Cognito rather than IAM users managing AWS resources, and is used for application-level access control rather than AWS service permission management.

---

<a id="q618-142"></a>
### Question 142 (`Q618`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is a component of the shared responsibility model managed entirely by AWS?

#### Options
- **A.** Patching operating system software
- **B.** Encrypting data
- **C.** Enforcing multi-factor authentication
- **D.** Auditing physical data center assets **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Auditing physical data center assets including hardware inventory, facility inspections, and physical access logs is entirely AWS's responsibility under the shared responsibility model, as customers never have physical access to or visibility into AWS data center infrastructure.

Patching the operating system software on EC2 instances is the customer's responsibility under the shared responsibility model, as AWS manages the underlying hypervisor and hardware but customers are responsible for maintaining the guest operating system on their virtual machines. Encrypting data at rest and in transit is the customer's responsibility; AWS provides the tools and services to enable encryption such as KMS and ACM, but customers must decide what to encrypt and configure it appropriately. Enforcing multi-factor authentication for IAM users and the root account is the customer's responsibility, as AWS provides MFA functionality but customers must enable and configure it for their account and users.

---

<a id="q628-143"></a>
### Question 143 (`Q628`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is entirely the responsibility of AWS, according to the AWS shared responsibility model?

#### Options
- **A.** Patching of the guest operating system
- **B.** Security awareness and training
- **C.** Physical and environmental controls **[CORRECT]**
- **D.** Development of an IAM password policy

**Correct Answer:** `C`

#### Detailed Explanation

Physical and environmental controls including data center security, cooling systems, fire suppression, and power management are entirely AWS's responsibility, as customers have no access to or involvement in managing AWS physical infrastructure.

Patching of the guest operating system on EC2 instances is the customer's responsibility; AWS manages the underlying hardware and hypervisor but customers are responsible for keeping the operating system and applications on their instances up to date. Security awareness and training for employees and users of the AWS environment is the customer's responsibility; AWS provides security best practice guidance and training resources, but the organization's own training program for its staff is a customer obligation. Developing an IAM password policy is the customer's responsibility; AWS provides IAM with configurable password policy settings, but defining and enforcing the specific password requirements for an organization's IAM users is a customer configuration task.

---

<a id="q633-144"></a>
### Question 144 (`Q633`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS IAM feature is used to associate a set of permissions with multiple users?

#### Options
- **A.** Multi-factor authentication
- **B.** Groups **[CORRECT]**
- **C.** Password policies
- **D.** Access keys

**Correct Answer:** `B`

#### Detailed Explanation

IAM Groups allow you to attach permission policies to the group, and all users added to that group automatically inherit those permissions, making it the IAM feature used to associate a set of permissions with multiple users at once.

Multi-factor authentication adds a second verification layer beyond passwords to secure individual user logins, and is an authentication security mechanism rather than a feature for associating a set of permissions with multiple users simultaneously. Password policies define password complexity, rotation, and reuse rules for IAM user accounts, and are an authentication credential management feature rather than a mechanism for associating permissions with multiple users. Access keys consisting of an access key ID and secret access key are programmatic credentials for CLI and API access associated with individual IAM users, and are an authentication mechanism rather than a feature for associating permissions with groups of users.

---

<a id="q635-145"></a>
### Question 145 (`Q635`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following can a customer use to enable single sign-on (SSO) to the AWS Management Console?

#### Options
- **A.** Amazon Connect
- **B.** AWS Directory Service **[CORRECT]**
- **C.** Amazon Pinpoint
- **D.** Amazon Rekognition

**Correct Answer:** `B`

#### Detailed Explanation

AWS Directory Service integrates with Microsoft Active Directory, enabling single sign-on to the AWS Management Console using existing corporate usernames and passwords without creating separate IAM users for each employee.

Amazon Connect is a cloud-based contact center service that handles customer interactions through voice and chat channels, and has no capability to enable corporate credential federation or single sign-on authentication to the AWS Management Console. Amazon Pinpoint is an outbound communications service for sending targeted messages via email, SMS, and push notifications to application users, and is a marketing and engagement service with no connection to SSO or corporate identity federation for console access. Amazon Rekognition is a machine learning service for analyzing images and videos to detect objects, faces, and scenes, and is a visual analysis service with no role in enabling corporate credential single sign-on.

---

<a id="q637-146"></a>
### Question 146 (`Q637`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following benefits does the AWS Compliance program provide to AWS customers?

#### Options
- **A.** It allows customers to inherit AWS compliance certifications and reduces the scope of their own compliance audits **[CORRECT]**
- **B.** AWS is responsible for the maintenance of common compliance framework documentation
- **C.** It assures customers that AWS is maintaining physical security and data protection **[CORRECT]**
- **D.** It ensures the use of compliance frameworks that are being used by other cloud providers
- **E.** It will adopt new compliance frameworks as they become relevant to customer workloads

**Correct Answer:** `A, C`

#### Detailed Explanation

The AWS Compliance program allows customers to inherit AWS's third-party certifications and audit results, reducing the time and cost of their own compliance efforts. It also assures customers that AWS maintains physical security and data protection standards at the infrastructure level.

AWS is not solely responsible for maintaining compliance framework documentation - compliance is a shared responsibility, and customers remain responsible for ensuring their own workloads meet applicable regulations. AWS does not guarantee alignment with frameworks simply because other cloud providers use them - its compliance programs are based on relevant industry standards and regulatory requirements. AWS does not make binding commitments to automatically adopt any new compliance framework that becomes relevant to customer workloads.

---

<a id="q638-147"></a>
### Question 147 (`Q638`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following services provides on-demand access to AWS compliance reports?

#### Options
- **A.** AWS IAM
- **B.** AWS Artifact **[CORRECT]**
- **C.** Amazon GuardDuty
- **D.** AWS KMS

**Correct Answer:** `B`

#### Detailed Explanation

AWS Artifact provides on-demand, self-service access to AWS compliance reports and certifications including SOC, PCI DSS, ISO, and HIPAA documentation, directly from the AWS Management Console.

AWS IAM manages user identities and permissions for accessing AWS services and resources, and is an access management service rather than a repository of compliance reports or certifications. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity using machine learning and threat intelligence, and is a security monitoring service rather than a compliance report portal. AWS KMS is a key management service for creating and managing encryption keys used to protect data at rest and in transit, and is an encryption infrastructure service rather than a service providing access to compliance documentation.

---

<a id="q639-148"></a>
### Question 148 (`Q639`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> As part of the AWS shared responsibility model, which of the following operational controls do users fully inherit from AWS?

#### Options
- **A.** Security management of data center **[CORRECT]**
- **B.** Patch management
- **C.** Configuration management
- **D.** User and access management

**Correct Answer:** `A`

#### Detailed Explanation

Security management of the data center is an operational control customers fully inherit from AWS, meaning AWS performs all physical security operations and customers benefit from this protection without any action required on their part.

Patch management is a shared control where AWS patches the infrastructure and managed services it operates, while customers are responsible for patching the operating systems and applications running on their own EC2 instances and other customer-managed resources. Configuration management is also a shared control where AWS maintains the configuration of its own infrastructure components while customers are responsible for configuring their own operating systems, applications, and AWS services to meet their security and operational requirements. User and access management is the customer's responsibility; customers create and manage IAM users, groups, roles, and policies, and are fully accountable for who has access to their AWS resources and what those identities are permitted to do.

---

<a id="q641-149"></a>
### Question 149 (`Q641`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the shared responsibility model, which of the following tasks are the responsibility of the customer?

#### Options
- **A.** Maintaining the underlying Amazon EC2 hardware
- **B.** Managing the VPC network access control lists **[CORRECT]**
- **C.** Encrypting data in transit and at rest **[CORRECT]**
- **D.** Replacing failed hard disk drives
- **E.** Deploying hardware in different Availability Zones

**Correct Answer:** `B, C`

#### Detailed Explanation

Customers are responsible for managing VPC network access control lists to define inbound and outbound traffic rules at the subnet level, and for encrypting their own data in transit using TLS and at rest using services such as KMS and S3 server-side encryption.

Maintaining the underlying EC2 hardware including servers, storage, and networking infrastructure is entirely AWS's responsibility, as customers have no physical access to the data center equipment that hosts EC2 instances. Replacing failed hard disk drives is AWS's responsibility as part of managing the physical infrastructure, and customers experience this transparently through AWS's hardware redundancy and replacement processes without any action required. Deploying hardware in different Availability Zones is an AWS infrastructure responsibility; AWS designs and maintains the physical separation of AZs, while customers choose which AZ to deploy their resources in but do not control the underlying hardware deployment.

---

<a id="q646-150"></a>
### Question 150 (`Q646`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What function do security groups serve related Amazon Elastic Compute Cloud (Amazon EC2) instance security?

#### Options
- **A.** Act as a virtual firewall for the Amazon EC2 instance **[CORRECT]**
- **B.** Secure AWS user accounts with AWS identity and Access Management (IAM) policies
- **C.** Provide DDoS protection with AWS Shield
- **D.** Use Amazon CloudFront to protect the Amazon EC2 instance

**Correct Answer:** `A`

#### Detailed Explanation

Security groups act as virtual firewalls for EC2 instances, controlling inbound and outbound traffic at the instance level by evaluating rules based on protocol, port, and source or destination, providing the primary network security mechanism for EC2 instance access.

Securing AWS user accounts with IAM policies is the function of AWS Identity and Access Management, which controls which users can access which AWS services and what actions they can perform, rather than a function of security groups which operate at the network traffic level. Providing DDoS protection is the function of AWS Shield, which provides managed distributed denial of service mitigation at the network and transport layers, rather than security groups which evaluate individual connection attempts based on rules. Using Amazon CloudFront to protect EC2 instances involves routing traffic through CloudFront's edge network with Shield and WAF integrations, and is a separate architectural pattern rather than a function performed by security groups directly.

---

<a id="q652-151"></a>
### Question 151 (`Q652`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> How is asset management on AWS easier than asset management in a physical data center?

#### Options
- **A.** AWS provides a Configuration Management Database that users can maintain
- **B.** AWS performs infrastructure discovery scans on the customer's behalf
- **C.** Amazon EC2 automatically generates an asset report and places it in the customer's specified Amazon S3 bucket
- **D.** Users can gather asset metadata reliably with a few API calls **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

On AWS, users can gather asset metadata reliably by making a few API calls using services such as AWS Config, Systems Manager Inventory, or the AWS CLI, providing comprehensive and up-to-date information about all resources across an account.

AWS does not provide a pre-built Configuration Management Database that customers maintain; AWS Config tracks resource configurations automatically, but maintaining a traditional CMDB requires third-party tooling or custom development rather than being a built-in AWS service offering. AWS does not perform infrastructure discovery scans on the customer's behalf; services like AWS Config and Systems Manager provide discovery capabilities, but these are tools customers use themselves rather than automated scans performed by AWS on the customer's account. Amazon EC2 does not automatically generate asset reports and place them in S3; while instances report some metadata, comprehensive asset reporting requires active use of AWS management services like Config, Systems Manager, or the CLI rather than automatic report generation.

---

<a id="q654-152"></a>
### Question 152 (`Q654`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Using AWS Identity and Access Management (IAM) to grant access only to the resources needed to perform a task is a concept known as:

#### Options
- **A.** Restricted access
- **B.** As-needed access
- **C.** Least privilege access **[CORRECT]**
- **D.** Token access

**Correct Answer:** `C`

#### Detailed Explanation

Least privilege access means granting IAM users only the minimum permissions they need to perform their specific assigned tasks, reducing the risk of accidental or intentional misuse of AWS resources through overly broad permission grants.

Restricted access is a general term that implies limiting access, but it does not specifically capture the principle of granting the minimum required permissions; least privilege is the precise IAM concept that defines permissions based on task requirements rather than broadly restricting access. As-needed access is an informal description that partially captures the idea of granting permissions when needed, but least privilege is the established AWS and security industry term for the principle of granting minimum necessary permissions. Token access refers to the use of temporary security tokens issued when IAM roles are assumed, and describes a credential mechanism rather than the principle of scoping permissions to what is required for a task.

---

<a id="q656-153"></a>
### Question 153 (`Q656`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the AWS shared responsibility model, customer responsibilities include which one of the following?

#### Options
- **A.** Securing the hardware, software, facilities, and networks that run all products and services
- **B.** Providing certificates, reports, and other documentation directly to AWS customers under NDA
- **C.** Configuring the operating system, network, and firewall **[CORRECT]**
- **D.** Obtaining industry certifications and independent third-party attestations

**Correct Answer:** `C`

#### Detailed Explanation

Configuring the operating system, network settings, and firewall rules on EC2 instances falls within the customer's responsibility under the shared responsibility model, as AWS provides the underlying infrastructure while customers are responsible for what they install and configure on top of it.

Securing the hardware, software, facilities, and networks that run all AWS products and services is AWS's responsibility under the shared responsibility model, as customers have no access to or control over the physical and virtual infrastructure that AWS manages. Providing compliance certificates, reports, and documentation to customers under NDA is a service AWS provides through AWS Artifact, not a customer responsibility; customers access these documents rather than create or provide them. Obtaining industry certifications and third-party attestations for the AWS infrastructure is AWS's responsibility, as AWS undergoes independent audits for certifications such as ISO, SOC, and PCI DSS that apply to the infrastructure layer rather than being a customer obligation.

---

<a id="q657-154"></a>
### Question 154 (`Q657`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which managed AWS service provides real-time guidance on AWS security best practices?

#### Options
- **A.** AWS X-Ray
- **B.** AWS Trusted Advisor **[CORRECT]**
- **C.** Amazon CloudWatch
- **D.** AWS Systems Manager

**Correct Answer:** `B`

#### Detailed Explanation

AWS Trusted Advisor inspects your AWS environment and provides real-time recommendations across security, cost optimization, performance, fault tolerance, and service limits, directly guiding customers toward security best practices.

Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications including CPU utilization, error rates, and custom metrics, and is an observability service rather than a service that provides security best practice guidance. AWS Config continuously monitors and records resource configurations against desired state rules, and is a compliance evaluation service rather than a service that provides proactive guidance on security best practices. AWS CloudTrail records all API calls and management events for auditing and compliance purposes, and is an activity logging service rather than a service that provides real-time guidance on improving the security posture of an AWS environment.

---

<a id="q659-155"></a>
### Question 155 (`Q659`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the AWS shared responsibility model, customers are responsible for which aspects of security in the cloud?

#### Options
- **A.** Virtualization management
- **B.** Hardware management
- **C.** Encryption management **[CORRECT]**
- **D.** Facilities management
- **E.** Firewall management **[CORRECT]**

**Correct Answer:** `C, E`

#### Detailed Explanation

Customers are responsible for managing encryption of their data at rest and in transit including configuring encryption settings and managing KMS keys, and for configuring firewall rules through security groups and Network ACLs to control traffic to their resources.

Virtualization management is not a standard shared responsibility category; the underlying virtualization infrastructure including the hypervisor is AWS's responsibility, while customers manage the virtual machines that run on top of it rather than the visualisation layer itself. Hardware management including physical servers, storage devices, and networking equipment is entirely AWS's responsibility as customers have no access to or interaction with the physical infrastructure in AWS data centers. Facilities management including data center physical security, power, and cooling is entirely AWS's responsibility as customers never have physical access to or involvement in managing the facilities that house AWS infrastructure.

---

<a id="q661-156"></a>
### Question 156 (`Q661`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is a responsibility of AWS in the shared responsibility model?

#### Options
- **A.** Updating the network ACLs to block traffic to vulnerable ports
- **B.** Patching operating systems running on Amazon EC2 instances
- **C.** Updating the firmware on the underlying EC2 hosts **[CORRECT]**
- **D.** Updating the security group rules to block traffic to the vulnerable ports

**Correct Answer:** `C`

#### Detailed Explanation

Updating the firmware on EC2 host hardware is AWS's responsibility, as customers have no access to the physical servers and AWS manages all maintenance of the hardware layer including firmware updates for security and performance improvements.

Updating network ACLs to block traffic to vulnerable ports is the customer's responsibility; customers configure their VPC network ACLs to define which traffic is allowed or denied at the subnet level as part of their security configuration. Patching operating systems running on EC2 instances is the customer's responsibility; AWS manages the underlying hypervisor and host hardware, but the guest operating system and its patches are the customer's obligation. Updating security group rules to block traffic to vulnerable ports is the customer's responsibility; customers define and maintain security group rules to control which traffic reaches their EC2 instances as part of their network security configuration.

---

<a id="q663-157"></a>
### Question 157 (`Q663`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What does it mean to grant least privilege to AWS IAM users?

#### Options
- **A.** It is granting permissions to a single user only
- **B.** It is granting permissions using AWS IAM policies only
- **C.** It is granting AdministratorAccess policy permissions to trustworthy users
- **D.** It is granting only the permissions required to perform a given task **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Least privilege means granting only the minimum permissions required to perform a specific task, ensuring that IAM users cannot access resources or perform actions beyond what their job requires, minimizing the risk of misuse.

Granting permissions to a single user only describes individual rather than shared access, but does not capture the concept of scoping permissions to the minimum required; least privilege is about the breadth of permissions granted rather than the number of users receiving them. Granting permissions using IAM policies only is a description of the mechanism for assigning permissions in AWS, but does not define the principle of least privilege, which is about minimizing the scope of those permissions rather than the method of granting them. Granting AdministratorAccess permissions to trustworthy users is the opposite of least privilege; administrator access grants unrestricted access to all AWS services and resources, which far exceeds the minimum permissions needed for most tasks regardless of how trustworthy the user is.

---

<a id="q683-158"></a>
### Question 158 (`Q683`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service provides a self-service portal for on-demand access to AWS compliance reports?

#### Options
- **A.** AWS Config
- **B.** AWS Certificate Manager
- **C.** Amazon Inspector
- **D.** AWS Artifact **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS Artifact is a self-service portal providing on-demand access to AWS compliance reports and certifications including SOC, PCI, and ISO documents, making it the purpose-built service for customers requiring on-demand access to compliance reports.

AWS Config continuously monitors and records resource configurations to evaluate compliance against desired rules, and is a resource configuration compliance tool rather than a portal for downloading AWS auditor-issued compliance reports. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to protect data in transit, and is a certificate provisioning and management service rather than a compliance documentation repository. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and produces customer-specific assessment findings rather than AWS compliance reports.

---

<a id="q692-159"></a>
### Question 159 (`Q692`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> According to the AWS shared responsibility model, what is AWS responsible for?

#### Options
- **A.** Configuring Amazon VPC
- **B.** Managing application code
- **C.** Maintaining application traffic
- **D.** Managing the network infrastructure **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS is responsible for managing the physical and virtual network infrastructure that underpins its global cloud, including the routers, switches, and physical cabling that connect data centers, Availability Zones, and Regions.

Configuring Amazon VPC is the customer's responsibility; customers define their VPC IP address ranges, subnets, route tables, internet gateways, and security settings as part of their network design within AWS. Managing application code is entirely the customer's responsibility; AWS provides the compute and runtime services, but the application logic, code quality, and updates are owned and maintained by the customer. Maintaining application traffic, including managing load balancers, CDN configurations, and DNS routing, is the customer's responsibility for their own applications, though AWS manages the underlying network infrastructure those services run on.

---

<a id="q694-160"></a>
### Question 160 (`Q694`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS tool will identify security groups that grant unrestricted Internet access to a limited list of ports?

#### Options
- **A.** AWS Organizations
- **B.** AWS Trusted Advisor **[CORRECT]**
- **C.** AWS Usage Report
- **D.** Amazon EC2 dashboard

**Correct Answer:** `B`

#### Detailed Explanation

AWS Trusted Advisor scans your security groups and flags those that grant unrestricted internet access (0.0.0.0/0) to specific ports such as SSH, RDP, and common database ports, helping identify and close potential security vulnerabilities.

AWS Organizations manages multiple AWS accounts under a central structure for consolidated billing and governance with service control policies, and does not have the capability to inspect individual security group rules or identify overly permissive internet access configurations. AWS Usage Reports provide data about AWS service usage and costs, and are billing and consumption tracking tools rather than security assessment tools that evaluate network access control configurations. The Amazon EC2 dashboard displays information about running instances, instance types, and their states, and while security groups are visible in the console, the dashboard does not automatically identify which groups grant unrestricted internet access the way Trusted Advisor's automated check does.

---

<a id="q697-161"></a>
### Question 161 (`Q697`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is the responsibility of AWS?

#### Options
- **A.** Setting up AWS Identity and Access Management (IAM) users and groups
- **B.** Physically destroying storage media at end of life **[CORRECT]**
- **C.** Patching guest operating systems
- **D.** Configuring security settings on Amazon EC2 instances

**Correct Answer:** `B`

#### Detailed Explanation

AWS is responsible for physically destroying storage media at end of life using industry-standard techniques to prevent data leakage, following secure decommissioning procedures as part of their data center operations under the shared responsibility model.

Setting up IAM users and groups is the customer's responsibility; customers define their own identity and access management structure including creating users, assigning them to groups, and attaching policies that control what each identity can access. Patching guest operating systems on EC2 instances is the customer's responsibility; AWS manages the underlying host hardware and hypervisor, but the operating system running inside the virtual machine must be patched and maintained by the customer. Configuring security settings on EC2 instances including firewall rules, operating system hardening, and application security configurations is the customer's responsibility as part of securing what they deploy and manage on AWS compute resources.

---

<a id="q702-162"></a>
### Question 162 (`Q702`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> What tasks should a customer perform when that customer suspects an AWS account has been compromised?

#### Options
- **A.** Rotate passwords and access keys **[CORRECT]**
- **B.** Remove MFA tokens
- **C.** Move resources to a different AWS Region
- **D.** Delete AWS CloudTrail Resources
- **E.** Contact AWS Support **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

When an account is suspected compromised, immediately rotating all passwords and access keys invalidates potentially stolen credentials, and contacting AWS Support provides assistance with the investigation and remediation of the compromise.

Removing MFA tokens would reduce account security at precisely the moment it is most needed, as MFA provides an additional authentication barrier that helps prevent unauthorised access even if credentials have been stolen. Moving resources to a different AWS Region does not address the underlying compromise and has no effect on the attacker's ability to access the account using stolen credentials. Deleting AWS CloudTrail resources would destroy the audit trail needed to investigate how the compromise occurred and what actions the attacker took, making remediation significantly harder.

---

<a id="q705-163"></a>
### Question 163 (`Q705`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is an AWS Identity and Access Management (IAM) role?

#### Options
- **A.** A user associated with an AWS resource
- **B.** A group associated with an AWS resource
- **C.** An entity that defines a set of permissions for use with an AWS resource **[CORRECT]**
- **D.** An authentication credential associated with a multi-factor authentication (MFA) token

**Correct Answer:** `C`

#### Detailed Explanation

An IAM role is an entity that defines a set of permissions for making AWS service requests, and unlike an IAM user it does not have permanent credentials; instead it provides temporary security credentials to whoever or whatever assumes it.

A user associated with an AWS resource describes an IAM user or service account assigned to interact with specific resources, but this does not capture the defining characteristic of an IAM role, which is that it can be assumed temporarily by multiple different entities rather than being permanently associated with a single one. A group associated with an AWS resource describes an IAM group used to manage shared permissions for multiple users, not a role, which is assumed dynamically by users, services, or applications that need its permissions temporarily. An authentication credential associated with an MFA token describes a multi-factor authentication mechanism, not an IAM role, which is an identity type that provides temporary credentials and permissions rather than being a specific authentication token.

---

<a id="q717-164"></a>
### Question 164 (`Q717`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which service enables customers to audit and monitor changes in AWS resources?

#### Options
- **A.** AWS Trusted Advisor
- **B.** Amazon GuardDuty
- **C.** Amazon Inspector
- **D.** AWS Config **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS Config continuously monitors and records AWS resource configurations, tracking changes over time and evaluating configurations against desired state compliance rules, making it the correct service for auditing and monitoring resource changes.

AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories by analyzing your AWS environment, and is an advisory tool rather than a service that specifically records and audits individual resource configuration changes over time. Amazon GuardDuty is a threat detection service that uses machine learning to identify malicious activity and anomalous behavior in AWS accounts and workloads, and is a security monitoring service rather than a resource configuration change auditing tool. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and produces security assessment findings rather than tracking and auditing resource configuration changes.

---

<a id="q722-165"></a>
### Question 165 (`Q722`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A user is running an application on AWS and notices that one or more AWS-owned IP addresses is involved in a distributed denial-of-service (DDoS) attack. Who should the user contact FIRST about this situation?

#### Options
- **A.** AWS Premium Support
- **B.** AWS Technical Account Manager
- **C.** AWS Solutions Architect
- **D.** AWS Abuse team **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

The AWS Abuse Team handles reports of AWS resources being used in malicious activities including DDoS attacks, and should be the first point of contact when AWS-owned IP addresses are identified as participating in an attack, as they can investigate and stop the misuse.

AWS Premium Support assists paying customers with technical issues and architectural guidance related to their own AWS environment, but is not the designated channel for reporting abuse originating from AWS IP addresses belonging to other accounts. The AWS Technical Account Manager is a support resource for Enterprise plan customers providing proactive guidance and operational reviews, but is not the appropriate contact for reporting external abuse incidents involving AWS infrastructure. AWS Solutions Architects help customers design architectures and optimize workloads, and are not the contact for reporting security incidents or abuse involving AWS infrastructure and IP addresses.

---

<a id="q727-166"></a>
### Question 166 (`Q727`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service offers on-demand access to AWS security and compliance reports?

#### Options
- **A.** AWS CloudTrail
- **B.** AWS Artifact **[CORRECT]**
- **C.** AWS Health
- **D.** Amazon CloudWatch

**Correct Answer:** `B`

#### Detailed Explanation

AWS Artifact provides on-demand access to AWS security and compliance reports including SOC, PCI, ISO, and other certifications, available directly from the AWS Management Console to help customers meet their own regulatory requirements.

AWS CloudTrail records all API calls and management events for auditing and compliance purposes, and produces customer-specific activity logs rather than AWS security certification reports issued by third-party auditors. AWS Health provides personalized alerts about AWS events that may affect a customer's specific resources or service availability, and is a service health and notification tool rather than a repository of compliance reports. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability and alerting service rather than a source of AWS security and compliance documentation.

---

<a id="q730-167"></a>
### Question 167 (`Q730`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service provides inbound and outbound network ACLs to harden external connectivity to Amazon EC2?

#### Options
- **A.** AWS IAM
- **B.** Amazon Connect
- **C.** Amazon VPC **[CORRECT]**
- **D.** Amazon API Gateway

**Correct Answer:** `C`

#### Detailed Explanation

Amazon VPC provides Network Access Control Lists that act as stateless firewalls at the subnet level, controlling inbound and outbound traffic to harden network connectivity for EC2 instances, as well as security groups at the instance level for additional control.

AWS IAM manages user identities and permissions for accessing AWS services and resources, and is an access control service rather than a network security component that provides inbound and outbound traffic filtering via ACLs. Amazon Connect is a cloud-based contact center service for handling customer interactions through voice and chat, and is a communications service with no connection to VPC networking or network ACL configuration. Amazon API Gateway is a fully managed service for creating, publishing, and managing APIs, and is an application integration layer rather than a VPC networking component that provides network ACLs to control connectivity.

---

<a id="q733-168"></a>
### Question 168 (`Q733`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the AWS shared responsibility model, AWS is responsible for which security-related task?

#### Options
- **A.** Lifecycle management of IAM credentials
- **B.** Physical security of global infrastructure **[CORRECT]**
- **C.** Encryption of Amazon EBS volumes
- **D.** Firewall configuration

**Correct Answer:** `B`

#### Detailed Explanation

AWS is responsible for the physical security of its global infrastructure, including the data centers, networking hardware, and facilities, as customers have no access to or control over any physical component of the AWS environment.

Lifecycle management of IAM credentials including creating, rotating, and deleting access keys and passwords for IAM users is the customer's responsibility, as customers define and manage the identities used to access their AWS resources. Encryption of Amazon EBS volumes is the customer's responsibility; while AWS provides KMS for key management and EBS supports encryption, customers must choose to enable encryption and configure the appropriate keys for their volumes. Firewall configuration through security groups and network ACLs is the customer's responsibility as part of securing network access to their own resources within their VPC.

---

<a id="q735-169"></a>
### Question 169 (`Q735`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the AWS shared responsibility model, which of the following is an example of security in the AWS Cloud?

#### Options
- **A.** Managing edge locations
- **B.** Physical security
- **C.** Firewall configuration **[CORRECT]**
- **D.** Global infrastructure

**Correct Answer:** `C`

#### Detailed Explanation

Firewall configuration through security groups and network ACLs, which customers define to control inbound and outbound traffic to their resources, is the customer's responsibility and is an example of security performed within the cloud on the customer's side of the shared responsibility model.

Managing edge locations is AWS's responsibility; AWS operates the global network of edge locations for CloudFront and other services, and customers benefit from these locations without being responsible for their management or security. Physical security of AWS data centers and hardware is entirely AWS's responsibility as customers never have physical access to the facilities where AWS infrastructure runs. Global infrastructure, including the physical data centers, Availability Zones, and Regions, is designed, built, and operated by AWS, and maintaining its security and availability is an AWS responsibility rather than a customer one.

---

<a id="q740-170"></a>
### Question 170 (`Q740`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A web application running on AWS has been spammed with malicious requests from a recurring set of IP addresses. Which AWS service can help secure the application and block the malicious traffic?

#### Options
- **A.** AWS IAM
- **B.** Amazon GuardDuty
- **C.** Amazon Simple Notification Service (Amazon SNS)
- **D.** AWS WAF **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS WAF lets you create rules to block requests from specific IP addresses or ranges, inspect request content, and filter traffic patterns, providing effective application-layer protection against repeated malicious requests from known IP addresses.

AWS IAM manages user identities and permissions for accessing AWS services and resources, and is an access control service rather than a service that can block malicious HTTP traffic targeting a web application. Amazon GuardDuty is a threat detection service that uses machine learning to identify malicious activity and anomalous behavior in AWS accounts, and while it can detect suspicious patterns, it does not actively block or filter web application traffic in real time. Amazon SNS is a fully managed publish/subscribe messaging service for sending notifications to subscribers, and is a messaging and notification service with no capability to inspect or block malicious web traffic patterns.

---

<a id="q746-171"></a>
### Question 171 (`Q746`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A user needs an automated security assessment report that will identify unintended network access to Amazon EC2 instances and vulnerabilities on those instances. Which AWS service will provide this assessment report?

#### Options
- **A.** EC2 security groups
- **B.** AWS Config
- **C.** Amazon Macie
- **D.** Amazon Inspector **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Amazon Inspector automatically assesses EC2 instances for unintended network access by analyzing network configurations and known software vulnerabilities by scanning installed packages against vulnerability databases, generating prioritized security assessment reports.

EC2 security groups are virtual firewalls that control which traffic is allowed to reach EC2 instances based on defined rules, and are a preventive network control rather than an automated assessment service that identifies vulnerabilities and generates reports. AWS Config continuously monitors and records resource configurations against desired state compliance rules, and is a configuration compliance evaluation service rather than a vulnerability assessment tool that scans for network exposure or software weaknesses. Amazon Macie uses machine learning to discover and classify sensitive data stored in Amazon S3, and is a data classification and protection service for S3 rather than a service that assesses EC2 instances for network access vulnerabilities.

---

<a id="q748-172"></a>
### Question 172 (`Q748`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Where can users find a catalog of AWS-recognized providers of third-party security solutions?

#### Options
- **A.** AWS Service Catalog
- **B.** AWS Marketplace **[CORRECT]**
- **C.** AWS Quick Start
- **D.** AWS CodeDeploy

**Correct Answer:** `B`

#### Detailed Explanation

AWS Marketplace is a digital catalog where users can find, purchase, and deploy third-party software solutions from independent software vendors that are vetted by AWS, including security tools such as firewalls, intrusion detection, and compliance products.

AWS Service Catalog allows organizations to create and manage catalogs of approved IT services for internal use within their own AWS environment, and is an internal governance tool for managing approved product portfolios rather than a public catalog of third-party security vendors. AWS Quick Start provides pre-built, automated deployments of popular technologies using AWS CloudFormation templates, and is a deployment acceleration resource rather than a catalog of third-party security solution providers. AWS CodeDeploy is an automated deployment service that delivers application code to EC2 instances, Lambda functions, and on-premises servers, and is a deployment automation tool with no connection to browsing or purchasing third-party security solutions.

---

<a id="q755-173"></a>
### Question 173 (`Q755`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Within the AWS shared responsibility model, who is responsible for security and compliance?

#### Options
- **A.** The customer is responsible
- **B.** AWS is responsible
- **C.** AWS and the customer share responsibility **[CORRECT]**
- **D.** AWS shares responsibility with the relevant governing body

**Correct Answer:** `C`

#### Detailed Explanation

Security and compliance is a shared responsibility between AWS and the customer; AWS secures the underlying cloud infrastructure while customers are responsible for securing their workloads, data, and configurations built on top of it.

The customer alone being responsible for security and compliance is incorrect; under the shared responsibility model, AWS manages security of the cloud infrastructure including physical data centers, hypervisor, and global network, which are entirely outside customer control. AWS alone being responsible for security and compliance is incorrect; customers must actively manage security in the cloud including IAM policies, encryption configuration, network security, and application security, all of which AWS cannot control or configure on the customer's behalf. AWS sharing responsibility with a relevant governing body is not how the shared responsibility model works; the model divides responsibility between AWS and the customer based on which layer of the stack each party controls, with no involvement from external regulatory bodies in the operational security responsibility.

---

<a id="q757-174"></a>
### Question 174 (`Q757`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service is used to provide encryption for Amazon EBS?

#### Options
- **A.** AWS Certificate Manager
- **B.** AWS Systems Manager
- **C.** AWS KMS **[CORRECT]**
- **D.** AWS Config

**Correct Answer:** `C`

#### Detailed Explanation

AWS Key Management Service manages the encryption keys used for EBS volume encryption, handling key creation, rotation, and access control, integrating transparently with EBS to protect data at rest.

AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and clients, and is a certificate management service rather than a key management service for EBS volume encryption at rest. AWS Systems Manager provides operational management tools for EC2 instances and other resources including patching, configuration management, and session management, and is an operations service rather than an encryption key management service for EBS volumes. AWS Config continuously monitors and records resource configurations against desired state compliance rules, and is a configuration compliance evaluation service rather than an encryption key management service.

---

<a id="q760-175"></a>
### Question 175 (`Q760`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What does AWS Shield Standard provide?

#### Options
- **A.** WAF rules
- **B.** DDoS protection **[CORRECT]**
- **C.** Identity and Access Management (IAM) permissions and access to resources
- **D.** Data encryption

**Correct Answer:** `B`

#### Detailed Explanation

AWS Shield Standard provides automatic DDoS protection at no extra cost for all AWS customers, automatically detecting and mitigating common network and transport layer attacks including UDP floods and SYN floods without any configuration required.

WAF rules are managed by AWS WAF, which is a separate service from Shield that filters application-layer HTTP and HTTPS traffic based on configurable rules, and AWS Shield Standard does not provide WAF rule functionality. IAM permissions and access to resources are managed by AWS Identity and Access Management, which controls who can access which AWS services, and have no connection to the DDoS protection that AWS Shield provides. Data encryption is provided by services such as AWS KMS, S3 server-side encryption, and EBS encryption, and has no relationship to AWS Shield, which is specifically a DDoS mitigation service.

---

<a id="q766-176"></a>
### Question 176 (`Q766`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is one of the customer's responsibilities according to the AWS shared responsibility model?

#### Options
- **A.** Virtualization infrastructure
- **B.** Network infrastructure
- **C.** Application security **[CORRECT]**
- **D.** Physical security of hardware

**Correct Answer:** `C`

#### Detailed Explanation

Application security, including securing application code, data access controls, and authentication configurations, is the customer's responsibility under the shared responsibility model as it falls within the customer's side of the stack that AWS cannot access or control.

Virtualization infrastructure including the hypervisor that abstracts physical hardware into virtual machines is managed and secured entirely by AWS as part of its security of the cloud obligations, and customers have no access to or responsibility for this layer. Network infrastructure including the global network connecting AWS Regions, Availability Zones, and edge locations is owned and maintained by AWS and is not a customer responsibility, as customers configure virtual networking within their VPC but do not manage the underlying physical network. Physical security of hardware including data center access controls, server security, and decommissioning of physical equipment is entirely AWS's responsibility as customers have no access to or interaction with AWS physical facilities.

---

<a id="q770-177"></a>
### Question 177 (`Q770`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Where should users report that AWS resources are being used for malicious purposes?

#### Options
- **A.** AWS Abuse team **[CORRECT]**
- **B.** AWS Shield
- **C.** AWS Support
- **D.** AWS Developer Forums

**Correct Answer:** `A`

#### Detailed Explanation

The AWS Abuse Team should be contacted when AWS resources or IP addresses are being used for malicious purposes such as hosting spam, conducting DDoS attacks, or distributing malware, as they are the designated channel for investigating and stopping such misuse.

AWS Shield provides managed DDoS protection that automatically detects and mitigates DDoS attacks against your own resources, and is a protective service for your own infrastructure rather than a channel for reporting AWS resources being abused by others. AWS Support assists customers with technical issues and questions about their own AWS environment, but is not the designated channel for reporting that AWS infrastructure belonging to other accounts is being used for malicious purposes. AWS Developer Forums are community discussion spaces where developers share knowledge and ask questions about AWS services, and are not an appropriate reporting channel for security incidents involving malicious use of AWS resources.

---

<a id="q771-178"></a>
### Question 178 (`Q771`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service needs to be enabled to track all user account changes within the AWS Management Console?

#### Options
- **A.** AWS CloudTrail **[CORRECT]**
- **B.** Amazon Simple Notification Service (Amazon SNS)
- **C.** VPC Flow Logs
- **D.** AWS CloudHSM

**Correct Answer:** `A`

#### Detailed Explanation

AWS CloudTrail records all API calls and user actions in the AWS Management Console, providing a complete audit trail of account changes for security analysis and compliance.

Amazon Simple Notification Service is a fully managed pub/sub messaging service that delivers notifications to subscribers such as Lambda functions, HTTP endpoints, and email addresses, and has no capability to record or track user account changes within the AWS Management Console. VPC Flow Logs capture information about IP traffic flowing to and from network interfaces within a VPC, and is a network traffic logging feature that records connection-level data rather than user actions or account changes in the console. AWS CloudHSM provides dedicated hardware security modules for generating and managing cryptographic keys, and is a key management and encryption service with no capability to track or audit user activity within the AWS Management Console.

---

<a id="q777-179"></a>
### Question 179 (`Q777`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is AWS's responsibility under the AWS shared responsibility model?

#### Options
- **A.** Configuring third-party applications
- **B.** Maintaining physical hardware **[CORRECT]**
- **C.** Securing application access and data
- **D.** Managing custom Amazon Machine Images (AMIs)

**Correct Answer:** `B`

#### Detailed Explanation

Maintaining physical hardware including servers, storage devices, and networking equipment in data centers is exclusively AWS's responsibility, as customers have no access to or interaction with the physical infrastructure that powers AWS services.

Configuring third-party applications deployed on AWS resources is the customer's responsibility; AWS provides the compute, storage, and networking infrastructure, but customers are responsible for installing, configuring, and securing any third-party software they choose to run on that infrastructure. Securing application access and data, including setting up appropriate IAM policies, encryption configurations, and access controls for applications and data stored in AWS, is the customer's responsibility as part of security in the cloud. Managing custom Amazon Machine Images including creating, maintaining, and updating AMIs used to launch EC2 instances is the customer's responsibility as part of managing their own compute environment.

---

<a id="q779-180"></a>
### Question 180 (`Q779`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> How would a system administrator add an additional layer of login security to a user's AWS Management Console?

#### Options
- **A.** Use AWS Cloud Directory
- **B.** Audit AWS Identity and Access Management (IAM) roles
- **C.** Enable Multi-Factor Authentication **[CORRECT]**
- **D.** Enable AWS CloudTrail

**Correct Answer:** `C`

#### Detailed Explanation

Enabling Multi-Factor Authentication adds a second verification layer beyond a password, requiring a time-based one-time code from a hardware or virtual device to complete login, providing an additional layer of security for AWS Management Console access.

AWS Cloud Directory is a managed directory service for building cloud-native directories that organize hierarchical data such as organizational structures and device registries, and is not a mechanism for adding a login security layer to the AWS Management Console. Auditing IAM roles reviews what permissions have been granted across an account, which is a governance activity that helps identify excessive permissions but does not add an additional authentication step to the login process itself. Enabling AWS CloudTrail records API calls and account activity for auditing and compliance, and while it improves visibility into who did what after login, it does not add any additional layer of security to the login authentication process.

---

<a id="q780-181"></a>
### Question 181 (`Q780`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which service can identify the user that made the API call when an Amazon Elastic Compute Cloud (Amazon EC2) instance is terminated?

#### Options
- **A.** Amazon CloudWatch
- **B.** AWS CloudTrail **[CORRECT]**
- **C.** AWS X-Ray
- **D.** AWS Identity and Access Management (AWS IAM)

**Correct Answer:** `B`

#### Detailed Explanation

AWS CloudTrail logs all API calls including EC2 instance terminations, recording which IAM user or role made the call, the source IP address, and the timestamp, making it the purpose-built service for identifying who performed a specific action in an AWS account.

Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and does not record API call identity or attribution information for specific actions such as instance terminations. AWS X-Ray is a distributed tracing service that analyzes and debugs the performance of applications by mapping requests as they flow through application components, and is a performance analysis tool with no API call logging or user attribution capability. AWS Identity and Access Management defines and manages permissions for users and roles, controlling what actions they are allowed to perform, but does not itself log or record which user made a specific API call or when.

---

<a id="q782-182"></a>
### Question 182 (`Q782`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Where can a customer find information about prohibited actions on AWS infrastructure?

#### Options
- **A.** AWS Trusted Advisor
- **B.** AWS Identity and Access Management (IAM)
- **C.** AWS Billing Console
- **D.** AWS Acceptable Use Policy **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

The AWS Acceptable Use Policy defines what activities are prohibited on AWS infrastructure including illegal content hosting, network attacks, and sending spam, and is the authoritative reference for customers seeking to understand what actions are not permitted.

AWS Trusted Advisor provides automated recommendations for improving the security, cost efficiency, performance, and fault tolerance of AWS environments, and is an advisory tool rather than a document defining prohibited uses of the AWS platform. AWS IAM manages user identities and permissions to control which AWS services and resources users can access, and is an access management service rather than a policy document listing prohibited infrastructure activities. The AWS Billing Console displays cost and usage data, invoices, and payment information for an AWS account, and is a financial management interface with no connection to defining or documenting prohibited uses of AWS infrastructure.

---

<a id="q786-183"></a>
### Question 183 (`Q786`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following are recommended practices for managing IAM users?

#### Options
- **A.** Require IAM users to change their passwords after a specified period of time **[CORRECT]**
- **B.** Prevent IAM users from reusing previous passwords **[CORRECT]**
- **C.** Recommend that the same password be used on AWS and other sites
- **D.** Require IAM users to store their passwords in raw text
- **E.** Disable multi-factor authentication (MFA) for IAM users

**Correct Answer:** `A, B`

#### Detailed Explanation

Requiring password rotation after a specified period limits how long any compromised password remains valid, and preventing password reuse ensures users cannot immediately revert to previously exposed credentials after a required change.

Recommending the same password across AWS and other sites creates a significant security risk through credential reuse, as a breach of any other site would then compromise the AWS account; password uniqueness for each service is a fundamental security best practice. Requiring IAM users to store passwords in raw unencrypted text would expose those passwords to anyone who gains access to wherever they are stored, creating severe security vulnerabilities; passwords should be kept confidential and never stored in plain text. Disabling MFA for IAM users removes a critical second authentication factor, leaving accounts protected only by passwords and significantly increasing the risk of unauthorised access if credentials are compromised.

---

<a id="q793-184"></a>
### Question 184 (`Q793`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which situation should be reported to the AWS Abuse team?

#### Options
- **A.** An Availability Zone has a service disruption
- **B.** An intrusion attempt is made from an AWS IP address **[CORRECT]**
- **C.** A user has trouble accessing an Amazon S3 bucket from an AWS IP address
- **D.** A user needs to change payment methods due to a compromise

**Correct Answer:** `B`

#### Detailed Explanation

Intrusion attempts originating from AWS IP addresses are abuse scenarios that should be reported to the AWS Abuse Team, which investigates misuse of AWS resources for malicious activities such as hacking, phishing, and denial of service attacks.

An Availability Zone service disruption is an infrastructure availability issue that should be monitored through the AWS Health Dashboard and reported to AWS Support if it is causing operational impact, rather than being an abuse scenario for the Abuse Team. A user having trouble accessing an S3 bucket from an AWS IP address is a technical access or permission issue that should be investigated by checking IAM policies, bucket policies, and VPC configurations, and addressed through AWS Support if needed rather than reported to the Abuse Team. A user needing to change payment methods due to a compromise is a billing and account security matter that should be handled through the AWS Management Console or by contacting AWS Customer Service for billing assistance.

---

<a id="q796-185"></a>
### Question 185 (`Q796`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following are components of Amazon VPC?

#### Options
- **A.** Objects
- **B.** Subnets **[CORRECT]**
- **C.** Buckets
- **D.** Internet gateways **[CORRECT]**
- **E.** Access key

**Correct Answer:** `B, D`

#### Detailed Explanation

Subnets divide a VPC's IP address range into segments that organize resources and define routing boundaries within the VPC, and internet gateways enable communication between resources in a VPC and the internet. Both are fundamental VPC components.

Objects is an Amazon S3 term for the data items stored within S3 buckets, and is a storage abstraction concept with no connection to Amazon VPC networking components such as subnets, route tables, or gateways. Buckets are Amazon S3 containers for storing objects and are the primary storage unit in the S3 service, and are not components of Amazon VPC, which is a virtual network service rather than an object storage service. Access keys are IAM credentials consisting of an access key ID and secret access key used for programmatic API and CLI authentication, and are identity management constructs rather than VPC networking components.

---

<a id="q800-186"></a>
### Question 186 (`Q800`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which functions can users perform using AWS KMS?

#### Options
- **A.** Create and manage AWS access keys for the AWS account root user
- **B.** Create and manage AWS access keys for an AWS account IAM user
- **C.** Create and manage keys for encryption and decryption of data **[CORRECT]**
- **D.** Create and manage keys for multi-factor authentication

**Correct Answer:** `C`

#### Detailed Explanation

AWS KMS lets users create and manage cryptographic keys for encrypting and decrypting data across AWS services, providing centralized key lifecycle management with audit logging of key usage via CloudTrail.

Creating and managing AWS access keys for the root user is done through the IAM section of the AWS Management Console, and access keys are authentication credentials rather than cryptographic keys managed by KMS. Creating and managing AWS access keys for IAM users is performed through the IAM console or CLI, and access keys are programmatic authentication credentials unrelated to the encryption key management function of AWS KMS. Creating and managing keys for multi-factor authentication involves configuring virtual or hardware MFA devices in the IAM console, and MFA tokens are authentication mechanisms rather than cryptographic keys for data encryption and decryption.

---

<a id="q806-187"></a>
### Question 187 (`Q806`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which Amazon VPC feature enables users to capture information about the IP traffic that reaches Amazon EC2 instances?

#### Options
- **A.** Security groups
- **B.** Elastic network interfaces
- **C.** Network ACLs
- **D.** VPC Flow Logs **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

VPC Flow Logs capture metadata about the IP traffic going to and from network interfaces in a VPC, providing visibility into traffic patterns for security analysis, compliance auditing, and connectivity troubleshooting.

Security groups act as stateful virtual firewalls at the EC2 instance level that control which traffic is allowed in and out based on defined rules, but they filter traffic rather than capturing or logging information about it. Elastic network interfaces are virtual network cards that attach to EC2 instances to provide network connectivity, and are a networking component rather than a feature for capturing or recording IP traffic data. Network ACLs act as stateless firewalls at the subnet level that allow or deny traffic based on IP address and port rules, but like security groups they filter traffic rather than capture or log information about it.

---

<a id="q808-188"></a>
### Question 188 (`Q808`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which AWS service will provide a way to generate encryption keys that can be used to encrypt data?

#### Options
- **A.** Amazon Macie
- **B.** AWS Certificate Manager
- **C.** AWS Key Management Service (AWS KMS) **[CORRECT]**
- **D.** AWS Secrets Manager
- **E.** AWS CloudHSM **[CORRECT]**

**Correct Answer:** `C, E`

#### Detailed Explanation

AWS KMS generates and manages encryption keys through a software-based, AWS-managed infrastructure, and AWS CloudHSM provides dedicated hardware security modules that give customers full control over key generation and management. Both services provide ways to generate encryption keys that can be used to encrypt data.

Amazon Macie uses machine learning to discover and classify sensitive data in Amazon S3, and is a data classification service rather than a key generation service that provides encryption keys for protecting data. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit, and does not generate general-purpose encryption keys for use in protecting customer data at rest. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and while it uses encryption to protect stored secrets, it is not a service that generates encryption keys for customers to use in their own data encryption workflows.

---

<a id="q811-189"></a>
### Question 189 (`Q811`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service helps users meet contractual and regulatory compliance requirements for data security by using dedicated hardware appliances within the AWS Cloud?

#### Options
- **A.** AWS Secrets Manager
- **B.** AWS CloudHSM **[CORRECT]**
- **C.** AWS Key Management Service (AWS KMS)
- **D.** AWS Directory Service

**Correct Answer:** `B`

#### Detailed Explanation

AWS CloudHSM provides dedicated, single-tenant hardware security modules within the AWS Cloud that meet FIPS 140-2 Level 3 compliance requirements, offering complete customer control over key generation and management on dedicated hardware for organizations with strict contractual or regulatory mandates.

AWS Secrets Manager stores, rotates, and manages secrets such as database credentials and API keys; it handles the secret lifecycle rather than providing dedicated hardware appliances. AWS KMS uses HSMs but shares the underlying hardware across customers, so it does not offer the dedicated single-tenant hardware that some contractual or regulatory requirements mandate. AWS Directory Service provides managed Microsoft Active Directory for identity management and single sign-on, with no connection to hardware security modules or key management.

---

<a id="q812-190"></a>
### Question 190 (`Q812`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the AWS shared responsibility model, the customer manages which of the following?

#### Options
- **A.** Decommissioning of physical storage devices
- **B.** Security group and ACL configuration **[CORRECT]**
- **C.** Patch management of an Amazon RDS instance operating system
- **D.** Controlling physical access to data centers
- **E.** Patch management of an Amazon EC2 instance operating system **[CORRECT]**

**Correct Answer:** `B, E`

#### Detailed Explanation

Customers manage security group and ACL configurations to control inbound and outbound network access to their resources as part of securing their network environment, and are responsible for patching the guest operating system on EC2 instances including applying security updates and vulnerability patches.

Decommissioning physical storage devices including secure data erasure and physical destruction is entirely AWS's responsibility as part of managing the physical infrastructure in data centers that customers never access. Controlling physical access to AWS data centers including badge readers, biometrics, and surveillance is entirely AWS's responsibility as customers have no presence in or access to the facilities where AWS hardware is located. Patch management for the Amazon RDS instance operating system is AWS's responsibility as RDS is a managed service where AWS handles the underlying database engine patching, OS patching, and maintenance; customers only need to manage patching of databases they run on EC2 themselves.

---

<a id="q815-191"></a>
### Question 191 (`Q815`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is a user responsible for when running an application in the AWS Cloud?

#### Options
- **A.** Managing physical hardware
- **B.** Updating the underlying hypervisor
- **C.** Providing a list of users approved for data center access
- **D.** Managing application software updates **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

When running applications in the AWS Cloud, users are responsible for managing application software updates, including patches, version upgrades, and security fixes for their own application code.

Managing physical hardware is entirely AWS's responsibility, as customers have no access to the underlying physical servers, networking equipment, or data center infrastructure that runs AWS services. Updating the underlying hypervisor is AWS's responsibility, as the virtualization layer that runs EC2 instances is part of the infrastructure that AWS owns and maintains on behalf of all customers. Providing a list of users approved for data center access is AWS's responsibility, as AWS manages all physical access controls to its data centers and customers have no role in determining who can enter AWS facilities.

---

<a id="q819-192"></a>
### Question 192 (`Q819`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service helps identify malicious or unauthorized activities in AWS accounts and workloads?

#### Options
- **A.** Amazon Rekognition
- **B.** AWS Trusted Advisor
- **C.** Amazon GuardDuty **[CORRECT]**
- **D.** Amazon CloudWatch

**Correct Answer:** `C`

#### Detailed Explanation

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts, CloudTrail event logs, VPC Flow Logs, and DNS logs using machine learning and threat intelligence to identify malicious activity and unauthorised behavior.

AWS CloudTrail records all API calls and management events in an AWS account for auditing and compliance purposes, and provides the raw activity data that GuardDuty analyzes, but CloudTrail itself does not identify or alert on malicious or unauthorised activities. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories including security checks for open ports and missing MFA, but does not continuously monitor for active threats or ongoing malicious behavior in accounts. Amazon Macie uses machine learning to discover and classify sensitive data stored in Amazon S3, and is a data classification and protection service rather than a real-time threat detection service monitoring account-wide activity.

---

<a id="q822-193"></a>
### Question 193 (`Q822`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company is hosting a web application in a Docker container on Amazon EC2. AWS is responsible for which of the following tasks?

#### Options
- **A.** Scaling the web application and services developed with Docker
- **B.** Provisioning or scheduling containers to run on clusters and maintain their availability
- **C.** Performing hardware maintenance in the AWS facilities that run the AWS Cloud **[CORRECT]**
- **D.** Managing the guest operating system, including updates and security patches

**Correct Answer:** `C`

#### Detailed Explanation

When a customer runs a Docker container on Amazon EC2, AWS is responsible for the physical infrastructure layer, which includes performing hardware maintenance in the AWS facilities that run the AWS Cloud.

Scaling the web application and services developed with Docker is the customer's responsibility, as EC2-based container workloads require the customer to configure scaling through services such as EC2 Auto Scaling or Amazon ECS. Provisioning or scheduling containers to run on clusters and maintaining their availability is also the customer's responsibility when running Docker directly on EC2, as the customer manages the container runtime and orchestration layer rather than AWS. Managing the guest operating system including updates and security patches is the customer's responsibility for EC2 instances, as the Shared Responsibility Model places operating system management firmly with the customer for IaaS services.

---

<a id="q824-194"></a>
### Question 194 (`Q824`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which actions represent best practices for using AWS IAM?

#### Options
- **A.** Configure a strong password policy **[CORRECT]**
- **B.** Share the security credentials among users of AWS accounts who are in the same Region
- **C.** Use access keys to log in to the AWS Management Console
- **D.** Rotate access keys on a regular basis **[CORRECT]**
- **E.** Avoid using IAM roles to delegate permissions

**Correct Answer:** `A, D`

#### Detailed Explanation

Applying least privilege permissions ensures IAM users and roles have only the access they need to perform their tasks, and using IAM roles for applications running on EC2 instances avoids embedding long-term credentials in code. Both are IAM security best practices.

Sharing credentials between users contradicts IAM best practices; each user should have their own unique credentials to maintain individual accountability and allow precise permission scoping, and sharing credentials prevents tracking who performed which actions. Storing access keys in plaintext on EC2 instances is a security anti-pattern that risks credential exposure through instance metadata, log files, or shared access to the instance; IAM roles should be used instead to provide temporary credentials automatically. Using the root user account for all administrative tasks contradicts IAM best practices; the root account should be used only for tasks that specifically require it, and IAM users with appropriate permissions should be used for all regular administrative activities.

---

<a id="q825-195"></a>
### Question 195 (`Q825`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS feature or service can be used to capture information about incoming and outgoing traffic in an AWS VPC infrastructure?

#### Options
- **A.** AWS Config
- **B.** VPC Flow Logs **[CORRECT]**
- **C.** AWS Trusted Advisor
- **D.** AWS CloudTrail

**Correct Answer:** `B`

#### Detailed Explanation

VPC Flow Logs capture metadata about IP traffic flowing to and from network interfaces in an Amazon VPC, recording information about source and destination IP addresses, ports, protocols, and whether traffic was allowed or rejected.

AWS CloudTrail records API calls and management events across an AWS account, capturing who made requests and what changes were made to AWS resources, but does not capture network-level packet flow data between instances the way VPC Flow Logs do. AWS Config continuously monitors and records AWS resource configurations and evaluates them against compliance rules, and is a configuration state tracking service rather than a network traffic capture and logging service. Amazon CloudWatch collects operational metrics, logs, and events from AWS resources and applications for monitoring and alerting purposes, and while it can collect application-level logs, it does not capture the IP traffic flow data between network interfaces that VPC Flow Logs provide.

---

<a id="q828-196"></a>
### Question 196 (`Q828`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which service can be used to monitor and receive alerts for AWS account root user AWS Management Console sign-in events?

#### Options
- **A.** Amazon CloudWatch **[CORRECT]**
- **B.** AWS Config
- **C.** AWS Trusted Advisor
- **D.** AWS IAM

**Correct Answer:** `A`

#### Detailed Explanation

Amazon CloudWatch can monitor for root user console sign-in events through CloudTrail integration, and can be configured to send alerts via SNS when the root user logs in, enabling security teams to detect and respond to unexpected root account access.

AWS CloudTrail records all API calls and management events including root user sign-ins, and is the source of the sign-in event data, but does not itself send alerts or notifications when specific events occur without integration with CloudWatch Events or EventBridge. AWS Config continuously monitors resource configurations and evaluates compliance, and while it tracks resource state changes, it is not used to send real-time alerts for specific account login events such as root user console sign-ins. AWS Artifact provides on-demand access to AWS compliance reports and certifications, and is a documentation portal with no capability to monitor or alert on AWS account activity or login events.

---

<a id="q839-197"></a>
### Question 197 (`Q839`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which tasks are the customer's responsibility in the AWS shared responsibility model?

#### Options
- **A.** Infrastructure facilities access management
- **B.** Cloud infrastructure hardware lifecycle management
- **C.** Configuration management of user's applications **[CORRECT]**
- **D.** Networking infrastructure protection
- **E.** Security groups configuration **[CORRECT]**

**Correct Answer:** `C, E`

#### Detailed Explanation

Customers are responsible for configuration management of their own applications, including how those applications are set up and maintained, and for configuring security groups that control network access to their resources. Both fall on the customer side of the shared responsibility model.

Infrastructure facilities access management refers to physical access controls for AWS data centers, which is entirely AWS's responsibility as customers have no access to or control over the physical facilities hosting their workloads. Cloud infrastructure hardware lifecycle management covers the procurement, maintenance, and decommissioning of physical servers and networking equipment, which AWS manages on behalf of all customers without any customer involvement. Networking infrastructure protection refers to securing the underlying global network that connects AWS Regions, Availability Zones, and edge locations, which is AWS's responsibility as part of its security of the cloud obligations.

---

<a id="q843-198"></a>
### Question 198 (`Q843`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> A web application is hosted on AWS using an Elastic Load Balancer, multiple Amazon EC2 instances, and Amazon RDS. Which security measures fall under the responsibility of AWS?

#### Options
- **A.** Running a virus scan on EC2 instances
- **B.** Protecting against IP spoofing and packet sniffing **[CORRECT]**
- **C.** Installing the latest security patches on the RDS instance **[CORRECT]**
- **D.** Encrypting communication between the EC2 instances and the Elastic Load Balancer
- **E.** Configuring a security group and a network access control list (NACL) for EC2

**Correct Answer:** `B, C`

#### Detailed Explanation

AWS is responsible for protecting against IP spoofing and packet sniffing at the network level as part of securing the infrastructure, and for patching the underlying operating system of managed RDS instances as RDS is a fully managed service where AWS handles database engine and OS patching.

Running a virus scan on EC2 instances is the customer's responsibility as the customer manages the guest operating system and installed software on their EC2 instances, including security tooling to detect malicious software. Encrypting communication between EC2 instances and the Elastic Load Balancer requires customer configuration of SSL/TLS settings in the application and load balancer, as the customer controls their own application architecture and must choose to enable encrypted communications. Configuring security groups and network ACLs for EC2 instances is the customer's responsibility for defining which network traffic is allowed to and from their own compute resources within the VPC.

---

<a id="q846-199"></a>
### Question 199 (`Q846`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company needs an Amazon S3 bucket that cannot have any public objects due to compliance requirements. How can this be accomplished?

#### Options
- **A.** Enable S3 Block Public Access from the AWS Management Console **[CORRECT]**
- **B.** Hold a team meeting to discuss the importance of only uploading private S3 objects
- **C.** Require all S3 objects to be manually approved before uploading
- **D.** Create a service to monitor all S3 uploads and remove any public uploads

**Correct Answer:** `A`

#### Detailed Explanation

S3 Block Public Access is an account-level or bucket-level setting that overrides any policies or ACLs that would grant public access, ensuring no objects in the bucket can be made public regardless of how they are uploaded.

Holding a team meeting relies on human awareness and voluntary compliance, which does not technically enforce the restriction and cannot guarantee that public objects will never be uploaded. Requiring manual approval before uploading is not a native S3 feature and introduces an unscalable manual process that still does not technically prevent public objects from being created. Creating a custom monitoring service to detect and remove public uploads introduces unnecessary complexity, delay between upload and remediation, and relies on reactive rather than preventive controls, making it far less reliable than the built-in Block Public Access setting.

---

<a id="q849-200"></a>
### Question 200 (`Q849`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Who is responsible for patching the guest operating system for Amazon RDS?

#### Options
- **A.** The AWS Product team **[CORRECT]**
- **B.** The customer Database Administrator
- **C.** Managed partners
- **D.** AWS Support

**Correct Answer:** `A`

#### Detailed Explanation

Patching the guest operating system for Amazon RDS is AWS's responsibility, as RDS is a fully managed database service where AWS handles all underlying infrastructure maintenance including OS patches and database engine updates.

The customer is not responsible for patching the guest OS in Amazon RDS because RDS abstracts the infrastructure layer completely; unlike EC2 where customers manage the operating system, RDS instances have their OS managed and patched by AWS as part of the managed service model. The AWS compliance team does not patch RDS operating systems; patching is performed by the RDS service engineering team as part of routine managed service maintenance, not by a compliance function within AWS. AWS Trusted Advisor provides recommendations and best practice checks across security, cost, performance, and fault tolerance, but does not perform operational tasks such as patching database instance operating systems.

---

<a id="q855-201"></a>
### Question 201 (`Q855`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the AWS shared responsibility model, which of the following is a customer responsibility?

#### Options
- **A.** Installing security patches for the Xen and KVM hypervisors
- **B.** Installing operating system patches for Amazon DynamoDB
- **C.** Installing operating system security patches for Amazon EC2 database instances **[CORRECT]**
- **D.** Installing operating system security patches for Amazon RDS database instances

**Correct Answer:** `C`

#### Detailed Explanation

Customers are responsible for installing operating system security patches on their Amazon EC2 instances, including any database software running on those instances, as the guest operating system falls within the customer responsibility boundary under the shared responsibility model.

Installing security patches for the Xen and KVM hypervisors is an AWS responsibility, as AWS owns and manages the virtualization layer that sits between the physical hardware and the customer's instances, and customers have no access to or visibility of the hypervisor. Installing operating system patches for Amazon DynamoDB is an AWS responsibility, as DynamoDB is a fully managed service where AWS handles all underlying infrastructure, operating system, and database engine maintenance on the customer's behalf. Installing operating system security patches for Amazon RDS database instances is an AWS responsibility, as RDS is a fully managed relational database service where AWS manages the operating system and database engine patching, leaving customers responsible only for their data and application-level configurations.

---

<a id="q857-202"></a>
### Question 202 (`Q857`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the AWS shared responsibility model, the security and patching of the guest operating system is the responsibility of:

#### Options
- **A.** AWS Support
- **B.** The customer **[CORRECT]**
- **C.** AWS Systems Manager
- **D.** AWS Config

**Correct Answer:** `B`

#### Detailed Explanation

Under the Shared Responsibility Model, the customer is responsible for security and patching of the guest operating system on EC2 instances, including applying security updates and configuring the OS, as AWS only manages the infrastructure beneath the hypervisor.

AWS Support provides technical assistance and guidance to customers experiencing issues with their AWS environment, but is not responsible for patching or securing operating systems on customer instances. AWS Systems Manager can assist customers in automating patch management tasks on EC2 instances, but it is a tool that helps customers fulfill their own patching responsibility rather than shifting that responsibility to AWS. AWS Config records and evaluates configuration changes to AWS resources for compliance purposes, and does not perform or take responsibility for operating system patching on EC2 instances.

---

<a id="q858-203"></a>
### Question 203 (`Q858`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service makes it easy to create and manage AWS users and groups, and provide them with secure access to AWS resources at no charge?

#### Options
- **A.** AWS Direct Connect
- **B.** Amazon Connect
- **C.** AWS Identity and Access Management (IAM) **[CORRECT]**
- **D.** AWS Firewall Manager

**Correct Answer:** `C`

#### Detailed Explanation

AWS Identity and Access Management is the service that allows you to create and manage AWS users and groups, assign permissions through policies, and control which users have access to which AWS services and resources securely.

Amazon Cognito is an identity service for web and mobile application users that enables sign-up, sign-in, and federated access with external identity providers, and is designed for application-level user management rather than managing AWS service access for administrators. AWS IAM Identity Center (formerly AWS Single Sign-On), now called AWS IAM Identity Center, provides single sign-on access to multiple AWS accounts and applications using one set of credentials, and while it builds on IAM, the foundational service for creating and managing users and groups within AWS is IAM itself. AWS Directory Service provides managed Microsoft Active Directory for enterprise identity management and integrates with IAM for AWS console access, but the primary service for creating and managing the users, groups, and access controls used within AWS itself is IAM.

---

<a id="q859-204"></a>
### Question 204 (`Q859`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service provides on-demand access to AWS security and compliance documentation?

#### Options
- **A.** AWS Directory Service
- **B.** AWS Artifact **[CORRECT]**
- **C.** AWS Trusted Advisor
- **D.** Amazon Inspector

**Correct Answer:** `B`

#### Detailed Explanation

AWS Artifact is the self-service portal that provides on-demand access to AWS security and compliance documentation including SOC reports, ISO certifications, PCI attestations, and other compliance materials available directly from the AWS console.

AWS Trusted Advisor provides automated recommendations and checks across security, cost, performance, and fault tolerance categories to help improve your AWS environment, and is an advisory service rather than a documentation and compliance report portal. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and produces customer-specific assessment findings rather than AWS security and compliance documentation. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, and is an observability and alerting service rather than a source of AWS compliance documentation.

---

<a id="q862-205"></a>
### Question 205 (`Q862`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A user needs to generate a report that outlines the status of key security checks in an AWS account. The report must include the status of Amazon S3 bucket permissions, whether multi-factor authentication is enabled for the AWS account root user, if any security groups are configured to allow unrestricted access. Where can all this information be found in one location?

#### Options
- **A.** Amazon QuickSight dashboard
- **B.** AWS CloudTrail trails
- **C.** AWS Trusted Advisor report **[CORRECT]**
- **D.** IAM credential report

**Correct Answer:** `C`

#### Detailed Explanation

AWS Trusted Advisor provides a report-style dashboard of check results across security, cost, performance, fault tolerance, and service limits, including key security checks such as MFA on root account, exposed access keys, and open security groups.

Amazon QuickSight is a business intelligence and data visualisation service for creating dashboards and reports from data sources, and while it can display data, it does not provide automated AWS security check results or account-level security status summaries. AWS CloudTrail trails record API calls and account activity for auditing purposes, and while they capture security-relevant events, they produce raw logs rather than a summarized status report of key security check findings. The IAM credential report lists all IAM users and the status of their credentials including password age, access key status, and MFA enablement, and while it is a useful security tool, it covers only IAM credential status rather than the broader set of key security checks that Trusted Advisor evaluates.

---

<a id="q865-206"></a>
### Question 206 (`Q865`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Using AWS Config to record, audit, and evaluate changes to AWS resources to enable traceability is an example of which AWS Well-Architected Framework pillar?

#### Options
- **A.** Security **[CORRECT]**
- **B.** Operational excellence
- **C.** Performance efficiency
- **D.** Cost optimization

**Correct Answer:** `A`

#### Detailed Explanation

Using AWS Config to record, audit, and evaluate changes to resources is an example of enabling traceability, which is a core design principle of the Security pillar focused on monitoring and detective controls.

Operational Excellence focuses on running and improving operations through automation and responding to events, not on detective monitoring of resource changes for traceability. Performance Efficiency focuses on using computing resources efficiently to meet workload requirements as demand changes over time. Cost Optimization focuses on eliminating unnecessary spend and selecting the right resource types to reduce overall costs.

---

<a id="q873-207"></a>
### Question 207 (`Q873`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the AWS shared responsibility model, which of the following are customer responsibilities?

#### Options
- **A.** Setting up server-side encryption on an Amazon S3 bucket **[CORRECT]**
- **B.** Amazon RDS instance patching
- **C.** Network and firewall configurations **[CORRECT]**
- **D.** Physical security of data center facilities
- **E.** Compute capacity availability

**Correct Answer:** `A, C`

#### Detailed Explanation

Customers are responsible for setting up server-side encryption on S3 buckets to protect data at rest, and for configuring network and firewall settings such as security groups and NACLs to control traffic to their resources. Both fall within the customer's side of the Shared Responsibility Model.

Amazon RDS instance patching is AWS's responsibility for managed database services, as AWS handles all engine-level patching and maintenance windows without customer involvement. Physical security of data center facilities is exclusively AWS's responsibility, covering the buildings, hardware, and environmental controls that customers have no access to. Compute capacity availability is AWS's responsibility, as AWS manages the underlying infrastructure to ensure that compute resources remain available for customers to provision and use.

---

<a id="q880-208"></a>
### Question 208 (`Q880`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following acts as a virtual firewall at the Amazon EC2 instance level to control traffic for one or more instances?

#### Options
- **A.** Access keys
- **B.** Virtual private gateways
- **C.** Security groups **[CORRECT]**
- **D.** Access Control Lists (ACL)

**Correct Answer:** `C`

#### Detailed Explanation

Security groups act as a virtual firewall at the EC2 instance level, controlling inbound and outbound traffic for one or more instances by evaluating rules based on protocol, port, and source and destination.

Access keys are long-term credentials consisting of an access key ID and secret used for programmatic access to AWS via the CLI or API, and are an authentication mechanism with no connection to network traffic control. Virtual private gateways are the AWS-side endpoint of a site-to-site VPN connection that enables encrypted communication between a VPC and an on-premises network, and are a connectivity component rather than a traffic filtering mechanism at the instance level. Access Control Lists operate as stateless firewalls at the subnet level rather than the instance level, applying inbound and outbound rules to all traffic entering or leaving a subnet without tracking connection state the way security groups do.

---

<a id="q883-209"></a>
### Question 209 (`Q883`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service or feature helps restrict the AWS services, resources, and individual API actions the users and roles in each member account can access?

#### Options
- **A.** Amazon Cognito
- **B.** AWS Organizations **[CORRECT]**
- **C.** AWS Shield
- **D.** AWS Firewall Manager

**Correct Answer:** `B`

#### Detailed Explanation

AWS Organizations Service Control Policies allow organizations to define and enforce the maximum permissions available to all accounts within an organization or specific organizational units, restricting which AWS services, resources, and API actions users in those accounts can access.

AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules to block common web exploits such as SQL injection and cross-site scripting, and operates at the application traffic layer rather than restricting access to AWS services and API actions for IAM users. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity and anomalous behavior, and is a detection and alerting service rather than a service that restricts which AWS services and API actions users can invoke. AWS Firewall Manager centrally manages AWS WAF rules, Shield protections, and security group policies across multiple accounts in an organization, and is a security management layer rather than a service that enforces IAM-level API action restrictions.

---

<a id="q884-210"></a>
### Question 210 (`Q884`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the best resource for a user to find compliance-related information and reports about AWS?

#### Options
- **A.** AWS Artifact **[CORRECT]**
- **B.** AWS Marketplace
- **C.** Amazon Inspector
- **D.** AWS Support

**Correct Answer:** `A`

#### Detailed Explanation

AWS Artifact is a self-service portal that provides on-demand access to AWS compliance reports, certifications, and agreements, making it the best resource for users seeking compliance-related information and documentation about AWS.

AWS CloudTrail records all API calls and management events in an AWS account for auditing and forensic purposes, and is an activity logging service rather than a source of compliance reports or certification documentation about AWS infrastructure. The Amazon Inspector console provides vulnerability assessment findings for EC2 instances and container images, and is a security assessment tool for customer workloads rather than a repository of AWS-level compliance information and reports. AWS Support provides technical assistance and guidance for using AWS services, and while support engineers can answer compliance-related questions, the self-service repository for compliance documentation and formal reports is AWS Artifact.

---

<a id="q889-211"></a>
### Question 211 (`Q889`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A user would like to encrypt data that is received, stored, and managed by AWS CloudTrail. Which AWS service will provide this capability?

#### Options
- **A.** AWS Secrets Manager
- **B.** AWS Systems Manager
- **C.** AWS Key Management Service (AWS KMS) **[CORRECT]**
- **D.** AWS Certificate Manager

**Correct Answer:** `C`

#### Detailed Explanation

AWS KMS manages encryption keys and integrates natively with CloudTrail to encrypt log files stored in S3, ensuring that CloudTrail log data is protected at rest using KMS-managed keys.

AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and end users, and is a certificate management service rather than a service for encrypting data received and stored by CloudTrail. Amazon Macie uses machine learning to discover and classify sensitive data stored in S3, and while it can identify sensitive content in CloudTrail logs stored in S3, it does not perform the encryption of that data. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to encrypt data stored by CloudTrail or any other AWS service.

---

<a id="q895-212"></a>
### Question 212 (`Q895`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service provides the ability to detect inadvertent data leaks of personally identifiable information (PII) and user credential data?

#### Options
- **A.** Amazon GuardDuty
- **B.** Amazon Inspector
- **C.** Amazon Macie **[CORRECT]**
- **D.** AWS Shield

**Correct Answer:** `C`

#### Detailed Explanation

Amazon Macie uses machine learning to automatically discover and classify sensitive data in Amazon S3 including personally identifiable information and user credentials, detecting potential data leaks and inadvertent exposure of sensitive data.

Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity and anomalous behavior using machine learning and threat intelligence, and focuses on detecting security threats rather than identifying specific sensitive data types stored in S3. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and does not classify or detect sensitive data such as PII stored in S3. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to discover or detect data leaks of personally identifiable information.

---

<a id="q898-213"></a>
### Question 213 (`Q898`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following describes a security best practice that can be implemented using AWS IAM?

#### Options
- **A.** Disable AWS Management Console access for all users
- **B.** Generate secret keys for every IAM user
- **C.** Grant permissions to users who are required to perform a given task only **[CORRECT]**
- **D.** Store AWS credentials within Amazon EC2 instances

**Correct Answer:** `C`

#### Detailed Explanation

Disabling and removing unnecessary IAM user credentials including inactive access keys and old passwords reduces the attack surface by eliminating credentials that could be exploited if compromised, making it an IAM security best practice.

Assigning the same permissions to all IAM users regardless of their roles violates the principle of least privilege and creates unnecessary risk by giving every user access to resources they do not need, which is an anti-pattern rather than a security best practice. Creating access keys for all IAM users by default creates unnecessary long-term credentials for users who may only need console access, increasing the risk of credential exposure without a corresponding operational benefit. Using a single shared IAM user for all team members removes individual accountability and prevents identifying which specific person performed an action, contradicting the IAM best practice of using individual accounts with unique credentials.

---

<a id="q901-214"></a>
### Question 214 (`Q901`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company needs protection from expanded distributed denial of service (DDoS) attacks on its website and assistance from AWS experts during such events. Which AWS managed service will meet these requirements?

#### Options
- **A.** AWS Shield Advanced **[CORRECT]**
- **B.** AWS Firewall Manager
- **C.** AWS WAF
- **D.** Amazon GuardDuty

**Correct Answer:** `A`

#### Detailed Explanation

AWS Shield Advanced provides expanded DDoS protection with real-time attack visibility, access to the DDoS Response Team, and cost protection for scaling costs incurred during attacks, meeting the requirements for protection against expanded DDoS attacks with dedicated response assistance.

AWS WAF filters HTTP and HTTPS traffic at the application layer based on configurable rules, and while it helps mitigate application-layer attacks and integrates with Shield Advanced, it does not on its own provide the expanded DDoS protection and dedicated response team access that the question requires. Amazon GuardDuty detects threats and malicious activity in AWS accounts using machine learning, and while it can identify DDoS-related anomalies, it is a detection service rather than an active DDoS mitigation service with a dedicated response team. AWS Trusted Advisor provides automated security, cost, performance, and fault tolerance recommendations, and is an advisory tool with no capability to protect against or respond to distributed denial of service attacks.

---

<a id="q903-215"></a>
### Question 215 (`Q903`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Under the AWS shared responsibility model, what are the customer's responsibilities?

#### Options
- **A.** Physical and environmental security
- **B.** Physical network devices including firewalls
- **C.** Storage device decommissioning
- **D.** Security of data in transit **[CORRECT]**
- **E.** Data integrity authentication **[CORRECT]**

**Correct Answer:** `D, E`

#### Detailed Explanation

Customers are responsible for securing data in transit by implementing encryption such as TLS/SSL to protect data as it moves between systems, and for data integrity authentication to verify that data has not been tampered with. Both fall within the customer's side of the Shared Responsibility Model.

Physical and environmental security of data centers is exclusively AWS's responsibility, covering the buildings, power, cooling, and physical access controls that customers have no involvement in. Physical network devices including firewalls are AWS's responsibility, as customers manage virtual networking constructs such as security groups and NACLs but have no access to the underlying physical network hardware. Storage device decommissioning is AWS's responsibility, as AWS manages the secure disposal and destruction of physical storage media when it reaches end of life.

---

<a id="q906-216"></a>
### Question 216 (`Q906`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following allows an application running on an Amazon EC2 instance to securely write data to an Amazon S3 bucket without using long-term credentials?

#### Options
- **A.** Amazon Cognito
- **B.** AWS Shield
- **C.** AWS IAM role **[CORRECT]**
- **D.** AWS IAM user access key

**Correct Answer:** `C`

#### Detailed Explanation

An IAM role attached to an EC2 instance provides temporary security credentials to applications running on that instance, allowing them to make authenticated AWS API calls to S3 without requiring hardcoded access keys in the application code.

AWS CloudTrail records API calls and management events for auditing purposes, and while it logs the S3 write operations, it does not itself grant the permissions or credentials that allow an application to authenticate and write data to S3. An S3 bucket policy can grant permissions for a specific EC2 instance to write to a bucket, but the instance still needs valid AWS credentials to authenticate those requests, and an IAM role attached to the instance is the recommended way to provide those credentials securely. An IAM user with programmatic access could provide access keys for the application to use, but storing long-term access keys in application code or on the instance is a security anti-pattern; IAM roles provide temporary credentials automatically and are the recommended approach.

---

<a id="q912-217"></a>
### Question 217 (`Q912`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> Which of the following tasks can only be performed after signing in with AWS account root user credentials?

#### Options
- **A.** Closing an AWS account **[CORRECT]**
- **B.** Creating a new IAM policy
- **C.** Changing AWS Support plans **[CORRECT]**
- **D.** Attaching a role to an Amazon EC2 instance
- **E.** Generating access keys for IAM users

**Correct Answer:** `A, C`

#### Detailed Explanation

Closing an AWS account and changing the AWS Support plan are tasks that can only be performed by the root user, as these are account-level actions that AWS reserves exclusively for the account owner to prevent unauthorised changes to fundamental account settings.

Creating a new IAM policy can be performed by any IAM user or role that has been granted the appropriate IAM permissions, and does not require root user credentials. Attaching a role to an Amazon EC2 instance can be performed by any IAM user or role with the necessary EC2 and IAM permissions, and is a routine operational task that does not require root access. Generating access keys for IAM users can be performed by IAM administrators with the appropriate permissions, and is not restricted to the root user account.

---

<a id="q917-218"></a>
### Question 218 (`Q917`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company is launching an e-commerce site that will store and process credit card data. The company requires information about AWS compliance reports and AWS agreements. Which AWS service provides on-demand access to these items?

#### Options
- **A.** AWS Certificate Manager
- **B.** AWS Config
- **C.** AWS Artifact **[CORRECT]**
- **D.** AWS CloudTrail

**Correct Answer:** `C`

#### Detailed Explanation

AWS Artifact provides on-demand access to AWS compliance reports such as PCI DSS and SOC reports, and AWS agreements such as the Business Associate Addendum, making it the purpose-built service for companies requiring compliance documentation when handling sensitive data like credit card information.

AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate management service with no capability to provide compliance reports or AWS agreements. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance against desired settings, and is a resource configuration auditing tool rather than a repository of AWS compliance documentation and agreements. AWS CloudTrail records API calls and account activity across an AWS environment for auditing and compliance purposes, and captures operational audit logs rather than providing access to AWS compliance reports or legal agreements.

---

<a id="q919-219"></a>
### Question 219 (`Q919`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service can be used to track unauthorized API calls?

#### Options
- **A.** AWS Config
- **B.** AWS CloudTrail **[CORRECT]**
- **C.** AWS Trusted Advisor
- **D.** Amazon Inspector

**Correct Answer:** `B`

#### Detailed Explanation

AWS CloudTrail records all API calls and account activity including unauthorised or unusual API calls, making it the correct service for tracking API calls that may indicate unauthorised access or activity in an AWS environment.

Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, and while CloudWatch can receive CloudTrail events and trigger alarms, it does not itself track or record API call history to identify unauthorised API actions. Amazon Detective analyzes and visualises security data from multiple sources to investigate the root cause of suspicious activity, and uses CloudTrail data as one of its inputs, but is an investigation tool that builds on top of CloudTrail rather than performing the original API call recording. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and is an advisory tool rather than a service that tracks or records API activity.

---

<a id="q920-220"></a>
### Question 220 (`Q920`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A user needs to regularly audit and evaluate the setup of all AWS resources, identify non-compliant accounts, and be notified when a resource changes. Which AWS service can be used to meet these requirements?

#### Options
- **A.** AWS Trusted Advisor
- **B.** AWS Config **[CORRECT]**
- **C.** AWS Resource Access Manager
- **D.** AWS Systems Manager

**Correct Answer:** `B`

#### Detailed Explanation

AWS Config continuously monitors resource configurations, evaluates them against compliance rules, tracks changes over time, and sends notifications when resources change or become non-compliant, making it the purpose-built service for ongoing audit, compliance evaluation, and change notification requirements.

AWS Trusted Advisor inspects your AWS environment and provides automated recommendations across security, cost, performance, and fault tolerance, but delivers periodic advisory checks rather than continuously tracking individual resource configuration changes and sending notifications when specific resources become non-compliant. AWS Resource Access Manager enables sharing of AWS resources such as subnets and Transit Gateways across AWS accounts within an organization, and is a resource sharing service with no capability to audit configurations or notify on compliance violations. AWS Systems Manager provides operational tools for managing and automating tasks across AWS resources including patching, parameter storage, and run commands, and while it can automate remediation it does not continuously evaluate resource configurations against compliance rules or send notifications when resources change.

---

<a id="q924-221"></a>
### Question 221 (`Q924`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A user needs to automatically discover, classify, and protect sensitive data stored in Amazon S3. Which AWS service can meet these requirements?

#### Options
- **A.** Amazon Inspector
- **B.** Amazon Macie **[CORRECT]**
- **C.** Amazon GuardDuty
- **D.** AWS Secrets Manager

**Correct Answer:** `B`

#### Detailed Explanation

Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data including PII stored in Amazon S3, providing visibility into data security risks and detecting potential data leaks.

Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not discover or classify sensitive data stored in Amazon S3. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity and anomalous behavior using machine learning and threat intelligence, and is a threat detection service rather than a data classification and protection service for sensitive data in S3. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a secrets lifecycle management service rather than a service for automatically discovering and classifying sensitive data stored in S3.

---

<a id="q928-222"></a>
### Question 222 (`Q928`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the MOST effective resource for staying up to date on AWS security announcements?

#### Options
- **A.** AWS Health Dashboard
- **B.** AWS Secrets Manager
- **C.** AWS Security Bulletins **[CORRECT]**
- **D.** Amazon Inspector

**Correct Answer:** `C`

#### Detailed Explanation

AWS Security Bulletins provide timely notifications about newly discovered security vulnerabilities and recommended remediation actions for AWS services, making them the most effective resource for staying up to date on AWS security announcements.

The AWS Health Dashboard provides personalized alerts about events that may affect a customer's specific AWS resources and service availability, and while it includes health events for security issues, the dedicated source for proactive AWS security announcements and vulnerability disclosures is the AWS Security Bulletins page. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service with no connection to security announcements or vulnerability notifications. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities, and generates findings about the customer's own resources rather than providing AWS-level security announcements.

---

<a id="q931-223"></a>
### Question 223 (`Q931`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service allows users to download security and compliance reports about the AWS infrastructure on demand?

#### Options
- **A.** Amazon GuardDuty
- **B.** AWS Security Hub
- **C.** AWS Artifact **[CORRECT]**
- **D.** AWS Shield

**Correct Answer:** `C`

#### Detailed Explanation

AWS Artifact provides on-demand access to AWS security and compliance reports including SOC, PCI DSS, ISO, and HIPAA documentation, available for download directly from the AWS Management Console without contacting AWS.

Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability and alerting service rather than a repository of AWS security and compliance reports. AWS CloudTrail records all API calls and management events across an AWS account for auditing purposes, and produces customer-specific activity logs rather than AWS security certification and compliance documentation. Amazon GuardDuty is a threat detection service that continuously monitors accounts and workloads for malicious activity, and is a real-time security monitoring service rather than a source of downloadable compliance reports.

---

<a id="q936-224"></a>
### Question 224 (`Q936`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> During a compliance review, an auditor requests AWS compliance documentation such as SOC 2 reports. Which AWS service provides on-demand access to these documents?

#### Options
- **A.** AWS Artifact **[CORRECT]**
- **B.** AWS Trusted Advisor
- **C.** AWS Config
- **D.** Amazon S3

**Correct Answer:** `A`

#### Detailed Explanation

AWS Artifact provides on-demand access to AWS compliance reports and certifications such as SOC 2 documents, allowing auditors and customers to download them directly from the console without requesting them through AWS Support.

AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories for improving an AWS environment, and is an advisory tool rather than a compliance documentation repository. AWS Config continuously monitors and records resource configurations against compliance rules, and is a resource configuration compliance evaluation service rather than a portal for downloading AWS-level compliance certifications. Amazon S3 is an object storage service for storing and retrieving data, and while AWS Artifact downloads documents stored in S3 on the backend, S3 itself is not the portal customers use to find and download compliance documentation.

---

<a id="q941-225"></a>
### Question 225 (`Q941`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company wants to allow full access to an Amazon S3 bucket for a particular user. Which element in the S3 bucket policy holds the user details that describe who needs access to the S3 bucket?

#### Options
- **A.** Principal **[CORRECT]**
- **B.** Action
- **C.** Resource
- **D.** Statement

**Correct Answer:** `A`

#### Detailed Explanation

The Principal element in an S3 bucket policy specifies who is allowed or denied access, and holds the user, account, role, or service details that describe the identity being granted or denied permissions.

Action specifies which S3 operations are permitted or denied, such as s3:GetObject or s3:PutObject, and defines what the principal can do rather than identifying who the principal is. Resource specifies which S3 bucket or objects the policy applies to, identifying the target of the policy rather than the identity being granted access. Statement is the top-level container element that wraps the individual policy blocks including Principal, Action, Effect, and Resource, and is the structural wrapper rather than the element that holds user details.

---

<a id="q945-226"></a>
### Question 226 (`Q945`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the AWS shared responsibility model, which of the following is a responsibility of AWS?

#### Options
- **A.** Enabling server-side encryption for objects stored in S3
- **B.** Applying AWS IAM security policies
- **C.** Patching the operating system on an Amazon EC2 instance
- **D.** Applying updates to the hypervisor **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS is responsible for the security of the underlying infrastructure including the data center physical security, hardware, and the software that runs the hypervisor and global network components, as these are outside the customer's control.

Managing application access rights for users accessing customer-built applications is the customer's responsibility, as customers control who can access their applications through application-level authentication and authorisation mechanisms. Keeping the operating system on Amazon EC2 instances up to date by applying security patches is the customer's responsibility, as the guest OS running inside EC2 virtual machines must be maintained by the customer who has administrative access to it. Configuring client-side data encryption to protect data before it is sent to AWS services is the customer's responsibility for data that requires end-to-end protection, as the customer controls the encryption process on their own systems before data leaves their environment.

---

<a id="q954-227"></a>
### Question 227 (`Q954`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service can be used to track resource changes and establish compliance?

#### Options
- **A.** Amazon CloudWatch
- **B.** AWS Config **[CORRECT]**
- **C.** AWS CloudTrail
- **D.** AWS Trusted Advisor

**Correct Answer:** `B`

#### Detailed Explanation

AWS Config continuously monitors and records configuration changes to AWS resources and evaluates those changes against compliance rules, identifying non-compliant resources and enabling auditing of the configuration history for compliance purposes.

Amazon CloudWatch monitors operational metrics, logs, and events for performance and observability, and while it can trigger alarms on unusual activity, it does not track resource configuration changes or evaluate compliance against desired configuration states. AWS CloudTrail records all API calls and management events for auditing, and while it logs who made configuration changes and when, it does not evaluate whether those configurations comply with defined rules the way Config does. Amazon Inspector is an automated vulnerability assessment service for EC2 instances and container images that identifies software vulnerabilities and unintended network access, and is not a resource configuration tracking and compliance evaluation service.

---

<a id="q959-228"></a>
### Question 228 (`Q959`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> A developer has been hired by a large company and needs AWS credentials. Which are security best practices that should be followed?

#### Options
- **A.** Grant the developer access to only the AWS resources needed to perform the job **[CORRECT]**
- **B.** Share the AWS account root user credentials with the developer
- **C.** Add the developer to the administrator's group in AWS IAM
- **D.** Configure a password policy that ensures the developer's password cannot be changed
- **E.** Ensure the account password policy requires a minimum length **[CORRECT]**

**Correct Answer:** `A, E`

#### Detailed Explanation

Granting the developer access only to the resources needed follows the principle of least privilege, and ensuring a minimum password length enforces credential security requirements. Both are IAM security best practices for onboarding new developers.

Sharing the AWS account root user credentials with any individual is a critical security violation, as the root user has unrestricted access to all AWS services and resources and should be protected and used only for tasks that specifically require it. Adding the developer to the administrator's group grants unrestricted access to all AWS services and resources, which directly violates the principle of least privilege and is not a security best practice for a new developer whose access requirements are specific to their role. Configuring a password policy that prevents the developer from changing their own password is a security anti-pattern, as the ability to change passwords is necessary for credential hygiene and periodic rotation.

---

<a id="q962-229"></a>
### Question 229 (`Q962`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A user is planning to migrate an application workload to the AWS Cloud. Which control becomes the responsibility of AWS once the migration is complete?

#### Options
- **A.** Patching the guest operating system
- **B.** Maintaining physical and environmental controls **[CORRECT]**
- **C.** Protecting communications and maintaining zone security
- **D.** Patching specific applications

**Correct Answer:** `B`

#### Detailed Explanation

Maintaining physical and environmental controls, including data center power, cooling, fire suppression, and physical security, becomes AWS's responsibility once a workload is migrated to the cloud.

Patching the guest operating system remains the customer's responsibility after migration to AWS. For services such as EC2, customers retain full control over the operating system and are responsible for applying updates and patches. Protecting communications and maintaining zone security is a shared responsibility that customers retain ownership of, including configuring network security controls such as security groups, network ACLs, and encryption in transit for their applications. Patching specific applications is always the customer's responsibility regardless of the deployment model, as AWS has no visibility into the application software customers choose to run on their infrastructure.

---

<a id="q969-230"></a>
### Question 230 (`Q969`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company wants to ensure that AWS Management Console users are meeting password complexity requirements. How can the company configure password complexity?

#### Options
- **A.** Using an AWS IAM user policy
- **B.** Using an AWS Organizations service control policy (SCP)
- **C.** Using an AWS IAM account password policy **[CORRECT]**
- **D.** Using an AWS Security Hub managed insight

**Correct Answer:** `C`

#### Detailed Explanation

IAM password policies allow administrators to enforce password complexity requirements such as minimum length, character type requirements, and expiration intervals, ensuring all IAM users must create passwords that meet the defined standards.

AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a secrets lifecycle management service rather than a tool for setting password complexity requirements for AWS Management Console users. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and has no capability to enforce password requirements for AWS console users. AWS Directory Service provides managed Microsoft Active Directory for enterprise identity management and domain joining, and while it can enforce password policies for Active Directory users, the correct service for enforcing password requirements for IAM users accessing the AWS Management Console is the IAM password policy.

---

<a id="q970-231"></a>
### Question 231 (`Q970`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Under the AWS shared responsibility model, which of the following is the customer's responsibility?

#### Options
- **A.** Patching guest OS and applications **[CORRECT]**
- **B.** Patching and fixing flaws in the infrastructure
- **C.** Physical and environmental controls
- **D.** Configuration of AWS infrastructure devices

**Correct Answer:** `A`

#### Detailed Explanation

Managing application data encryption and configuring security for their own applications are customer responsibilities under the shared responsibility model, as customers control their own data and application layer while AWS manages the underlying infrastructure.

Securing the infrastructure that runs all AWS Cloud services including physical servers, networking hardware, and data center facilities is entirely AWS's responsibility as part of the security of the cloud. Providing the physical security of global data centers including perimeter access controls, surveillance, and environmental protections is entirely AWS's responsibility as customers never have access to the physical facilities. Maintaining the hardware that provides the foundation of the global infrastructure including servers, storage devices, and networking equipment is entirely AWS's responsibility as part of owning and operating the physical cloud infrastructure.

---

<a id="q971-232"></a>
### Question 232 (`Q971`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following tasks is required to deploy a PCI-compliant workload on AWS?

#### Options
- **A.** Use any AWS service and implement PCI controls at the application layer
- **B.** Use an AWS service that is in-scope for PCI compliance and raise an AWS support ticket to enable PCI compliance at the application layer
- **C.** Use any AWS service and raise an AWS support ticket to enable PCI compliance on that service
- **D.** Use an AWS service that is in scope for PCI compliance and apply PCI controls at the application layer **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

Deploying applications on the correct services in compliance with PCI DSS requirements is the customer's responsibility, as customers must choose PCI-eligible AWS services and configure them correctly to meet the applicable PCI DSS controls on the customer's side of the shared responsibility model.

AWS does not ensure that all physical facilities and data centers meet PCI requirements on the customer's behalf; rather, AWS obtains and maintains PCI DSS certification for its infrastructure, and this certification is available to customers through AWS Artifact as evidence that the underlying platform is PCI-compliant. AWS does not patch all AWS systems used in the environment on the customer's behalf; for managed services AWS handles patching, but for services like EC2 the customer is responsible for patching the guest operating system and any installed software. Configuring network ACLs on AWS on the customer's behalf is not an AWS responsibility; customers configure their own VPC network ACLs to control traffic as part of their PCI-compliant network security architecture.

---

<a id="q977-233"></a>
### Question 233 (`Q977`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> A web developer is concerned that a DDoS attack could target an application. Which AWS services or features can help protect against such an attack?

#### Options
- **A.** AWS Shield **[CORRECT]**
- **B.** AWS CloudTrail
- **C.** Amazon CloudFront **[CORRECT]**
- **D.** AWS Support Center
- **E.** AWS Health Dashboard

**Correct Answer:** `A, C`

#### Detailed Explanation

AWS Shield provides automatic DDoS mitigation at the network and transport layers, and Amazon CloudFront absorbs and distributes traffic at edge locations, reducing the impact of volumetric attacks before they reach the application origin. Both help protect against DDoS attacks.

AWS CloudTrail records API calls and management events for auditing purposes, and while it logs account activity, it has no capability to detect or mitigate active DDoS attacks against a web application. AWS Support Center is a portal for submitting and managing support cases, and is not a technical service that provides protection against or mitigation of DDoS attacks. The AWS Health Dashboard provides real-time and historical status information about AWS services and personalized event alerts, and is a monitoring and notification tool rather than a service that actively protects applications from DDoS attacks.

---

<a id="q978-234"></a>
### Question 234 (`Q978`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service gives users on-demand, self-service access to AWS compliance control reports?

#### Options
- **A.** AWS Config
- **B.** Amazon GuardDuty
- **C.** AWS Trusted Advisor
- **D.** AWS Artifact **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS Artifact provides on-demand, self-service access to AWS compliance control reports including SOC, PCI, ISO, and HIPAA documentation directly from the AWS Management Console without requiring a request through AWS Support.

AWS Config tracks the configuration state of resources and audits how those configurations change over time, and is a resource configuration auditing service rather than a portal for downloading compliance control reports. Amazon GuardDuty is a threat detection service that uses machine learning to monitor accounts and workloads for malicious activity, and is security focused rather than a compliance documentation portal. AWS Trusted Advisor inspects an account and provides best practice recommendations across cost optimization, performance, security, fault tolerance, and service limits, and is an advisory tool rather than a source of compliance control reports.

---

<a id="q979-235"></a>
### Question 235 (`Q979`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario *(Select all that apply)*:**  
> A company wants to provide one of its employees with access to Amazon RDS. The company also wants to limit the interaction to only the AWS CLI and AWS software development kits (SDKs). Which combination of actions should the company take to meet these requirements while following the principles of least privilege?

#### Options
- **A.** Create an IAM user and provide AWS Management Console access only
- **B.** Create an IAM user and provide programmatic access only **[CORRECT]**
- **C.** Create an IAM role and provide AWS Management Console access only
- **D.** Create an IAM policy with administrator access and attach it to the IAM user
- **E.** Create an IAM policy with Amazon RDS access and attach it to the IAM user **[CORRECT]**

**Correct Answer:** `B, E`

#### Detailed Explanation

An IAM policy that grants Amazon RDS access can be attached directly to the specific IAM user, limiting that employee's AWS permissions to only the RDS actions specified in the policy and no other services.

Creating a separate AWS account for the user would be an excessive measure for granting one employee RDS access, as it introduces administrative overhead for account management and does not simplify access control compared to using an IAM policy within the existing account. Creating an IAM user with full administrator access would grant unrestricted access to all AWS services and resources, directly violating the principle of least privilege and creating unnecessary security risk for a user who only needs access to RDS. Placing all existing IAM users into a new IAM group with RDS access would grant RDS permissions to the entire user population rather than limiting access to the single employee who requires it, which contradicts the goal of providing targeted access.

---

<a id="q980-236"></a>
### Question 236 (`Q980`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company has a compliance requirement to record and evaluate configuration changes, as well as perform remediation actions on AWS resources. Which AWS service should the company use?

#### Options
- **A.** AWS Config **[CORRECT]**
- **B.** AWS Secrets Manager
- **C.** AWS CloudTrail
- **D.** AWS Trusted Advisor

**Correct Answer:** `A`

#### Detailed Explanation

AWS Config records configuration changes, evaluates them against compliance rules, and can trigger automated remediation actions when resources become non-compliant, meeting all three requirements of recording, evaluating, and remediating.

AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service with no capability to record configuration changes or trigger compliance remediation. AWS CloudTrail logs all API calls and account activity for auditing purposes, and while it records who made changes and when, it does not evaluate resources against compliance rules or trigger remediation actions. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and offers advisory guidance rather than automated compliance rule evaluation or remediation capability.

---

<a id="q984-237"></a>
### Question 237 (`Q984`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which of the following is the customer's responsibility when using Amazon RDS?

#### Options
- **A.** Patching the operating system of underlying hardware
- **B.** Controlling traffic to and from the database through security groups **[CORRECT]**
- **C.** Running backups that enable point-in-time recovery of a DB instance
- **D.** Replacing failed DB instances

**Correct Answer:** `B`

#### Detailed Explanation

Patching the database and operating system on EC2-hosted databases is the customer's responsibility when using Amazon RDS is a managed service where AWS handles patching; however the question asks about RDS specifically. Under the RDS model, configuring security groups to control network access to the RDS instance is the customer's responsibility as customers define which EC2 instances and IP addresses can connect to their database.

Installing the database software on the underlying server is not the customer's responsibility for Amazon RDS; AWS manages the database engine installation, configuration, and updates as part of the fully managed service offering. Patching the underlying operating system of the RDS instance is AWS's responsibility; RDS is a managed service where AWS performs OS and database engine patching automatically without customer involvement. Replacing failed database hardware is AWS's responsibility as part of managing the physical infrastructure; customers benefit from AWS's hardware redundancy and replacement processes transparently without any action required on their part.

---

<a id="q985-238"></a>
### Question 238 (`Q985`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> What is the customer's responsibility when using AWS Lambda?

#### Options
- **A.** Operating system configuration
- **B.** Application management **[CORRECT]**
- **C.** Platform management
- **D.** Code encryption

**Correct Answer:** `B`

#### Detailed Explanation

AWS Lambda is a serverless compute service where AWS manages the underlying infrastructure, and the customer's responsibility is limited to managing their application code, including writing, deploying, and maintaining the functions that run on the platform.

Operating system configuration is AWS's responsibility for Lambda, as the service abstracts away the underlying compute infrastructure entirely and customers have no access to or control over the operating system. Platform management is also AWS's responsibility for Lambda, as AWS handles the runtime environment, scaling, availability, and maintenance of the serverless platform on the customer's behalf. Code encryption is not a customer responsibility in the sense described, as AWS encrypts Lambda function code at rest by default, and while customers can optionally use their own KMS keys, encryption is handled automatically by AWS rather than being a customer-managed task.

---

<a id="q992-239"></a>
### Question 239 (`Q992`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service should a cloud practitioner use to identify security vulnerabilities of an AWS account?

#### Options
- **A.** AWS Secrets Manager
- **B.** Amazon Cognito
- **C.** Amazon Macie
- **D.** AWS Trusted Advisor **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

AWS Trusted Advisor identifies potential security vulnerabilities by checking for common misconfigurations such as unrestricted security group access, missing MFA on the root account, and publicly accessible S3 buckets, helping customers address security weaknesses proactively.

Amazon Detective is an investigation service that analyzes security data from GuardDuty, CloudTrail, and VPC Flow Logs to help security teams investigate the root cause of suspicious activity, and is a forensic investigation tool rather than a service for identifying security vulnerabilities in an AWS account configuration. Amazon Macie uses machine learning to discover and classify sensitive data in Amazon S3, and is a data classification service for detecting potential data exposure rather than a tool for auditing account-wide security configurations and vulnerabilities. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service rather than a security vulnerability identification tool.

---

<a id="q997-240"></a>
### Question 240 (`Q997`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service can be used to retrieve compliance reports on demand?

#### Options
- **A.** AWS Secrets Manager
- **B.** AWS Artifact **[CORRECT]**
- **C.** AWS Security Hub
- **D.** AWS Certificate Manager

**Correct Answer:** `B`

#### Detailed Explanation

AWS Artifact provides on-demand access to AWS compliance reports including SOC, PCI, ISO, and other certifications, available for download directly from the AWS Management Console.

AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service with no capability to retrieve or provide compliance documentation. AWS Security Hub provides a centralized view of security alerts and compliance status across an AWS environment by aggregating findings from multiple security services, and is a security posture management tool rather than a repository of AWS compliance reports. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate management service with no connection to compliance report retrieval.

---

<a id="q998-241"></a>
### Question 241 (`Q998`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company has an AWS-hosted website located behind an Application Load Balancer. The company wants to safeguard the website from SQL injection or cross-site scripting. Which AWS service should the company use?

#### Options
- **A.** Amazon GuardDuty
- **B.** AWS WAF **[CORRECT]**
- **C.** AWS Trusted Advisor
- **D.** Amazon Inspector

**Correct Answer:** `B`

#### Detailed Explanation

AWS WAF protects web applications behind Application Load Balancers from common exploits like SQL injection and cross-site scripting by filtering malicious HTTP requests based on custom rules.

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity and anomalous behavior, and is a detection and alerting service rather than a tool for filtering malicious web requests at the application layer. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool with no capability to intercept or block malicious web traffic. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a vulnerability scanning tool rather than a web traffic filtering service.

---

<a id="q1001-242"></a>
### Question 242 (`Q1001`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> An external auditor has requested that a company provide a list of all its IAM users, including the status of users' credentials and access keys. What is the SIMPLEST way to provide this information?

#### Options
- **A.** Create an IAM user account for the auditor, granting the auditor administrator permissions
- **B.** Take a screenshot of each user's page in the AWS Management Console, then provide the screenshots to the auditor
- **C.** Download the IAM credential report, then provide the report to the auditor **[CORRECT]**
- **D.** Download the AWS Trusted Advisor report, then provide the report to the auditor

**Correct Answer:** `C`

#### Detailed Explanation

The IAM credential report is a downloadable CSV file that lists all IAM users in the account along with the status of their credentials including passwords, access keys, MFA devices, and last-used timestamps, providing exactly what is needed for a user access audit.

AWS Config continuously monitors and records resource configuration changes and evaluates them against compliance rules, and is a resource configuration compliance tool rather than an IAM user listing service. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability service rather than a source of IAM user account information or credential status reports. AWS CloudTrail records all API calls and management events including IAM-related actions, and while it logs who created users and when, it does not provide a current consolidated list of all users and their credential status in the way the credential report does.

---

<a id="q1004-243"></a>
### Question 243 (`Q1004`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company wants to track AWS resource configuration changes for compliance reasons. Which AWS feature can be used to meet this requirement?

#### Options
- **A.** AWS Cost and Usage Report
- **B.** AWS Organizations service control policies (SCPs)
- **C.** AWS Config rules **[CORRECT]**
- **D.** VPC Flow Logs

**Correct Answer:** `C`

#### Detailed Explanation

AWS Config continuously monitors and records resource configuration changes and evaluates them against compliance rules, generating a complete history of configuration changes that auditors and compliance teams can use to demonstrate adherence to standards.

AWS CloudTrail records all API calls and account activity for auditing and forensic purposes, and while it captures who made configuration changes and when, it does not evaluate whether those configurations comply with defined rules or provide the configuration state history that Config does. Amazon Inspector is an automated vulnerability assessment service for EC2 instances and container images that identifies software vulnerabilities and network misconfigurations, and is a security scanning tool rather than a resource configuration tracking and compliance evaluation feature. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and is an advisory tool rather than a resource configuration change tracking and compliance evaluation service.

---

<a id="q1006-244"></a>
### Question 244 (`Q1006`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> The AWS IAM best practice for granting least privilege is to:

#### Options
- **A.** Apply an IAM policy to an IAM group and limit the size of the group
- **B.** Require multi-factor authentication (MFA) for all IAM users
- **C.** Require each IAM user who has different permissions to have multiple passwords
- **D.** Apply an IAM policy only to IAM users who require it **[CORRECT]**

**Correct Answer:** `D`

#### Detailed Explanation

The principle of least privilege requires granting only the permissions necessary for a user to perform their specific job function, which means applying IAM policies only to the users who actually require those permissions rather than broadly assigning permissions across all users.

Applying an IAM policy to an IAM group and limiting the size of the group addresses group management rather than least privilege, as the size of a group has no bearing on whether permissions are appropriately scoped to what users actually need. Requiring MFA for all IAM users is an authentication security best practice that protects against compromised credentials, but it does not relate to scoping permissions to the minimum required level. Requiring IAM users with different permissions to have multiple passwords conflates authentication with authorisation, and having multiple passwords does not control or limit what actions a user is permitted to perform.

---

<a id="q1010-245"></a>
### Question 245 (`Q1010`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service or feature can be used to prevent SQL injection attacks?

#### Options
- **A.** Security groups
- **B.** Network ACLs
- **C.** AWS WAF **[CORRECT]**
- **D.** IAM policy

**Correct Answer:** `C`

#### Detailed Explanation

AWS WAF is a web application firewall that inspects HTTP and HTTPS traffic and can be configured with rules to detect and block SQL injection attempts before they reach the application.

Amazon VPC provides network isolation and security controls at the infrastructure level through security groups and network ACLs, but does not inspect application-layer HTTP traffic content for SQL injection patterns the way WAF does. AWS Shield provides managed DDoS protection at the network and transport layers to defend against volumetric attacks, and is not designed to inspect or block application-layer exploits such as SQL injection. AWS CloudTrail records API calls and management events for auditing purposes, and while it logs activity in the AWS environment, it does not inspect web application traffic or block SQL injection attacks.

---

<a id="q1104-246"></a>
### Question 246 (`Q1104`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> A company needs to continuously assess its AWS environment against compliance frameworks such as PCI DSS and GDPR and automatically collect evidence for audits. Which AWS service should they use?

#### Options
- **A.** AWS Artifact
- **B.** AWS Config
- **C.** AWS Audit Manager **[CORRECT]**
- **D.** Amazon Inspector

**Correct Answer:** `C`

#### Detailed Explanation

AWS Audit Manager continuously collects evidence from AWS services, maps it to compliance framework controls such as PCI DSS and GDPR, and organizes it into audit-ready reports, automating much of the manual effort involved in compliance assessments.

AWS Artifact provides on-demand access to AWS compliance reports and certifications such as SOC and ISO documents, but it does not assess a customer's own environment or collect evidence for customer-specific compliance audits. AWS Config records and evaluates resource configurations against compliance rules, and while it contributes evidence that Audit Manager can consume, it does not itself organize findings into structured audit reports mapped to compliance frameworks. Amazon Inspector scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a vulnerability scanning tool rather than a compliance audit evidence collection service.

---

<a id="q1105-247"></a>
### Question 247 (`Q1105`)

**Classification:** `Domain 2: Security and Compliance` | `Task N/A`  
**Services:** General Cloud / AWS | **Last Verified:** `Verified`

> **Scenario:**  
> Which AWS service helps simplify audit preparation by automatically collecting and organizing evidence from AWS usage and activity into assessment reports?

#### Options
- **A.** AWS CloudTrail
- **B.** AWS Audit Manager **[CORRECT]**
- **C.** AWS Trusted Advisor
- **D.** AWS Security Hub

**Correct Answer:** `B`

#### Detailed Explanation

AWS Audit Manager automates evidence collection from multiple AWS sources including CloudTrail logs, Config evaluations, and Security Hub findings, and organizes this evidence into assessment reports that map directly to compliance framework requirements, significantly reducing audit preparation effort.

AWS CloudTrail records API calls and management events across an AWS account for auditing and forensic analysis, but it captures raw activity logs rather than organizing them into structured compliance assessment reports. AWS Trusted Advisor provides automated best-practice checks across security, cost, performance, and fault tolerance categories, but delivers advisory recommendations rather than structured audit evidence mapped to compliance frameworks. AWS Security Hub aggregates and prioritizes security findings from multiple AWS services into a centralized dashboard, but it is a security posture management tool rather than a compliance audit preparation and evidence collection service.

---

