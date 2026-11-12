# AWS Certified Cloud Practitioner (CLF-C02) - Domain 4: Billing, Pricing, and Support (12% of Exam)

This document contains 12 verified practice questions with complete answer keys and comprehensive explanations for every option, extracted from [CertSafari](https://www.certsafari.com/aws/cloud-practitioner-foundational).

## Table of Contents
- [Question 68](#question-68): An events company is planning a live-streamed product launch three months f...
- [Question 69](#question-69): Which S3 storage class is the default assigned to an object when no storage...
- [Question 70](#question-70): A backup administrator uploads a 50 KB configuration file to an S3 bucket a...
- [Question 71](#question-71): An organization has ten linked accounts under AWS Organizations, each indiv...
- [Question 72](#question-72): What is the primary purpose of AWS Cost Explorer?
- [Question 73](#question-73): A company's management account in AWS Organizations purchases a Reserved In...
- [Question 74](#question-74): A data engineering team wants the most granular billing data available, lin...
- [Question 75](#question-75): A company notices that an EC2 instance outside their own AWS account appear...
- [Question 76](#question-76): A procurement team wants a way to track which third-party software licenses...
- [Question 77](#question-77): A team's application in one AWS Region started throwing intermittent errors...
- [Question 78](#question-78): A developer hits an unusual error message while configuring a Lambda functi...
- [Question 79](#question-79): A solo developer is building a personal side project on AWS and occasionall...

---

### Question 68

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.1: Compare AWS pricing models.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> An events company is planning a live-streamed product launch three months from now and must guarantee that a specific EC2 instance type will be available in a chosen Availability Zone at that exact time, regardless of discount. Which purchasing option is designed for this guarantee?

#### Options
- **A.** On-Demand Capacity Reservations, which reserve EC2 capacity in a chosen zone for a defined window **[CORRECT]**
- **B.** Spot Instances, which draw from a shared pool of unused capacity that AWS can reclaim at any time
- **C.** Convertible Reserved Instances, which optimize long-term discount rather than guaranteed short-term capacity
- **D.** Compute Savings Plans, which discount usage but never guarantee that specific capacity will be free

**Correct Answer:** `A`
> **Summary:** On-Demand Capacity Reservations, which reserve EC2 capacity in a chosen zone for a defined window

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  On-Demand Capacity Reservations let a customer reserve EC2 capacity for a specific instance type in a specific Availability Zone for the exact time window needed, independent of any long-term billing discount.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Spot Instances draw on spare AWS capacity and can be reclaimed with short notice, which is the opposite of a guarantee that capacity will be available for a specific, time-critical event.

- **Option C:** ❌ **Why it is INCORRECT:**  
  A Convertible Reserved Instance is built to optimize price over a one- or three-year commitment and does not itself guarantee that capacity will exist at a specific future moment.

- **Option D:** ❌ **Why it is INCORRECT:**  
  A Savings Plan is a pricing commitment based on hourly spend; it lowers the rate for usage that occurs but provides no mechanism to guarantee capacity availability at a specific future time.

---

### Question 69

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.1: Compare AWS pricing models.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> Which S3 storage class is the default assigned to an object when no storage class is explicitly specified at upload time?

#### Options
- **A.** S3 Standard **[CORRECT]**
- **B.** S3 Intelligent-Tiering
- **C.** S3 Standard-IA
- **D.** S3 One Zone-IA

**Correct Answer:** `A`
> **Summary:** S3 Standard

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  S3 assigns the S3 Standard storage class by default to any object uploaded without an explicit storage class setting, matching what the question asks for.

- **Option B:** ❌ **Why it is INCORRECT:**  
  S3 Intelligent-Tiering must be selected explicitly, either at upload or through a lifecycle rule; it is not the class assigned automatically when nothing is specified.

- **Option C:** ❌ **Why it is INCORRECT:**  
  S3 Standard-IA is a class chosen deliberately for infrequently accessed data and is never applied automatically as the default for a new upload.

- **Option D:** ❌ **Why it is INCORRECT:**  
  S3 One Zone-IA must also be chosen explicitly for single-AZ infrequent-access storage and is not the automatic default class for new objects.

---

### Question 70

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.1: Compare AWS pricing models.`  
**Origin:** *Live Quiz Engine (ID: 80758)*

> **Scenario:**  
> A backup administrator uploads a 50 KB configuration file to an S3 bucket and sets its storage class to S3 Standard-IA to save on storage cost. Two days later, the administrator deletes the file to replace it with an updated version. What billing outcome should the administrator expect from this sequence?

#### Options
- **A.** The object is billed as 128 KB due to the minimum billable object size, and an early-deletion charge applies for removing it before the 30-day minimum storage duration **[CORRECT]**
- **B.** The object is billed only for its actual 50 KB size, and no early-deletion charge applies because S3 Standard-IA has no minimum storage duration
- **C.** The object is billed as 128 KB due to the minimum billable object size, but no early-deletion charge applies because Standard-IA has no minimum storage duration at all
- **D.** The object is billed only for its actual 50 KB size, but an early-deletion charge applies because it was removed before the 30-day minimum

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  S3 Standard-IA charges for a 128 KB minimum billable size for objects smaller than that threshold, and deleting an object before its 30-day minimum storage duration triggers a pro-rated early-deletion charge, both of which apply here.

- **Option B:** ❌ **Why it is INCORRECT:**  
  S3 Standard-IA does enforce both a 128 KB minimum billable size and a 30-day minimum storage duration, so billing only the actual 50 KB with no deletion charge understates both costs that apply to this class.

- **Option C:** ❌ **Why it is INCORRECT:**  
  The 128 KB minimum size is correctly applied, but S3 Standard-IA does have a 30-day minimum storage duration, so deleting the file after two days does trigger an early-deletion charge, contrary to this option.

- **Option D:** ❌ **Why it is INCORRECT:**  
  An early-deletion charge is correctly triggered by removing the file after two days, but Standard-IA bills the object at the 128 KB minimum rather than its true 50 KB size, so this option understates the storage charge.

---

### Question 71

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.2: Understand resources for billing, budget, and cost management.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> An organization has ten linked accounts under AWS Organizations, each individually storing a moderate amount of data in Amazon S3. Under consolidated billing, how does AWS calculate whether the organization reaches the lower per-GB pricing tiers for S3 storage?

#### Options
- **A.** AWS combines the S3 storage usage from every linked account into one total for the organization, so the group reaches the lower-priced volume tiers faster than any single account would alone. **[CORRECT]**
- **B.** AWS evaluates each linked account's S3 storage usage completely separately, so no account benefits from another account's usage even though they share the same management account.
- **C.** AWS applies the lower-priced volume tiers only to the management account's own S3 usage, while every linked member account is billed exclusively at the highest per-GB rate available.
- **D.** AWS requires the organization to manually request a volume-tier pricing review from AWS Support every month before any combined usage across the linked accounts can be considered for a discount.

**Correct Answer:** `A`
> **Summary:** AWS combines the S3 storage usage from every linked account into one total for the organization, so the group reaches the lower-priced volume tiers faster than any single account would alone.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Consolidated billing aggregates usage such as S3 storage across all linked accounts, so the combined total can reach volume pricing tiers that no individual account's usage would reach on its own.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Evaluating each account separately is exactly what consolidated billing avoids; the shared benefit of combining usage across linked accounts to reach lower per-GB tiers is a core reason organizations use it.

- **Option C:** ❌ **Why it is INCORRECT:**  
  The lower-priced tiers are not reserved for the management account alone; the combined usage across all linked accounts, including member accounts, is what determines the tier the whole organization reaches.

- **Option D:** ❌ **Why it is INCORRECT:**  
  No manual request to AWS Support is needed; AWS automatically aggregates linked account usage for volume pricing as part of how consolidated billing works each billing cycle.

---

### Question 72

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.2: Understand resources for billing, budget, and cost management.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> What is the primary purpose of AWS Cost Explorer?

#### Options
- **A.** It lets account owners visualize, analyze, and forecast their AWS cost and usage over time through interactive charts filtered by service, account, or tag. **[CORRECT]**
- **B.** It automatically negotiates lower per-service pricing with AWS on the customer's behalf whenever monthly spend crosses a certain threshold set by the account owner.
- **C.** It enforces spending limits by suspending resources the moment a configured budget threshold is exceeded, without requiring any manual intervention from an administrator.
- **D.** It generates the official monthly invoice PDF for an account and emails it directly to the billing contact listed in the account settings.

**Correct Answer:** `A`
> **Summary:** It lets account owners visualize, analyze, and forecast their AWS cost and usage over time through interactive charts filtered by service, account, or tag.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  This describes the core purpose of the tool: an interactive console experience for visualizing, analyzing, and forecasting cost and usage, with filtering and grouping by dimensions like service, account, or tag.

- **Option B:** ❌ **Why it is INCORRECT:**  
  No AWS billing tool negotiates custom pricing automatically based on spend thresholds; AWS pricing is published and applied according to the purchase options and usage the account already has in place.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Automatically suspending resources is not a function of this tool; enforcing hard spending limits by stopping resources is not a built-in capability of AWS's standard cost analysis and budgeting tools.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Generating and emailing the official invoice PDF is handled by the standard AWS Billing console and account settings, not by this cost analysis and forecasting tool.

---

### Question 73

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.2: Understand resources for billing, budget, and cost management.`  
**Origin:** *Live Quiz Engine (ID: 80781)*

> **Scenario:**  
> A company's management account in AWS Organizations purchases a Reserved Instance for a specific EC2 instance type, but a linked member account is the one actually running matching instances that month. What happens to the Reserved Instance discount by default?

#### Options
- **A.** By default, the Reserved Instance discount is shared across the organization and automatically applies to matching, unused instance usage in the linked member account, not only in the purchasing account. **[CORRECT]**
- **B.** The Reserved Instance discount stays locked to the management account that purchased it, and no linked member account can ever benefit from that reservation under any configuration.
- **C.** The linked member account must independently purchase and pay for its own separate Reserved Instance before receiving any discount, since reservations cannot be shared between accounts in an organization.
- **D.** AWS randomly assigns the Reserved Instance discount to whichever linked account happens to submit the most EC2 launch requests first, regardless of which account made the purchase.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Reserved Instance discount sharing is enabled by default across an AWS Organization, so unused reservation benefits automatically apply to matching instance usage anywhere in the organization, including a linked member account.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Locking the discount to the purchasing account describes RI sharing turned off, not the default behavior; by default the discount is shared across linked accounts in the organization.

- **Option C:** ❌ **Why it is INCORRECT:**  
  A separate purchase is not required for the discount to apply elsewhere in the organization; by default, reservation benefits from one account automatically extend to matching usage in other linked accounts.

- **Option D:** ❌ **Why it is INCORRECT:**  
  The discount is not assigned by a race to launch instances first; AWS applies RI benefits systematically across the organization's matching usage based on the sharing setting, not launch order.

---

### Question 74

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.2: Understand resources for billing, budget, and cost management.`  
**Origin:** *Live Quiz Engine (ID: 80784)*

> **Scenario:**  
> A data engineering team wants the most granular billing data available, line items broken down by the hour, by product, and by usage type, delivered automatically to an S3 bucket so they can query it with Amazon Athena. Which AWS billing resource should they configure?

#### Options
- **A.** AWS Cost and Usage Report **[CORRECT]**
- **B.** AWS Cost Explorer
- **C.** AWS Budgets
- **D.** AWS Pricing Calculator

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  This report provides the most comprehensive cost and usage data available, broken down to the hour, day, or month by product and usage type, delivered as CSV files to an S3 bucket that can be queried directly with Athena.

- **Option B:** ❌ **Why it is INCORRECT:**  
  This tool offers interactive charts and summaries in the console for exploring trends, but it does not deliver raw, hourly line-item CSV files to an S3 bucket for Athena queries.

- **Option C:** ❌ **Why it is INCORRECT:**  
  This service focuses on setting cost or usage thresholds and sending alerts, and it has no mechanism for exporting granular, hourly line-item data to storage for querying.

- **Option D:** ❌ **Why it is INCORRECT:**  
  This tool produces a one-time cost estimate for a proposed architecture rather than exporting ongoing, granular usage data from an active account to a storage location.

---

### Question 75

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.3: Identify AWS technical resources and AWS Support options.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> A company notices that an EC2 instance outside their own AWS account appears to be sending spam email and scanning their network for open ports, and wants to formally report this abusive activity to AWS so it can be investigated. Which AWS team handles this kind of report?

#### Options
- **A.** The AWS Support Center, because any general technical support case opened there is automatically escalated to a network abuse investigation team
- **B.** AWS Identity and Access Management, because it manages the offending account's permissions and can be used to revoke its AWS access
- **C.** The AWS Trust and Safety team, because it is responsible for investigating and responding to reports that AWS-hosted resources are being used to abuse others **[CORRECT]**
- **D.** AWS Trusted Advisor, because its security checks automatically flag resources across every AWS account that appear misconfigured or potentially malicious in nature

**Correct Answer:** `C`
> **Summary:** The AWS Trust and Safety team, because it is responsible for investigating and responding to reports that AWS-hosted resources are being used to abuse others

#### Comprehensive Verification & Explanations

- **Option A:** ❌ **Why it is INCORRECT:**  
  The Support Center is incorrect because general technical cases are not automatically routed to abuse investigation; abuse has its own dedicated reporting channel.

- **Option B:** ❌ **Why it is INCORRECT:**  
  IAM is incorrect because it manages permissions within a single account and gives a third party no mechanism to report or act on another company's abuse.

- **Option C:** ✅ **Why it is CORRECT:**  
  The Trust and Safety team is correct because it is the dedicated AWS team for receiving and investigating reports that AWS resources are being used to abuse others.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Trusted Advisor is incorrect because its checks only evaluate resources within the account it runs against, not resources belonging to other AWS customers.

---

### Question 76

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.3: Identify AWS technical resources and AWS Support options.`  
**Origin:** *Live Quiz Engine (ID: 80805)*

> **Scenario:**  
> A procurement team wants a way to track which third-party software licenses their organization has purchased through AWS, manage entitlements across multiple accounts, and keep governance over what has been deployed, from one centralized console. Which AWS offering provides this?

#### Options
- **A.** AWS Systems Manager, because it provides operational visibility and automation for managing configuration on EC2 instances across the entire account continuously
- **B.** AWS Cost Explorer, because it visualizes historical AWS service spending by account but does not track third-party software license entitlements
- **C.** AWS Marketplace, because it includes management tools that track purchased entitlements, licenses, and governance across the software an organization procures **[CORRECT]**
- **D.** AWS Organizations, because it lets the company group multiple AWS accounts together and apply consolidated billing across all of them

**Correct Answer:** `C`

#### Comprehensive Verification & Explanations

- **Option A:** ❌ **Why it is INCORRECT:**  
  Systems Manager is incorrect because it focuses on operational configuration and automation for compute resources, not license and entitlement tracking for purchased software.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Cost Explorer is incorrect because it analyzes AWS-native spending trends and has no capability to track third-party software entitlements or licenses.

- **Option C:** ✅ **Why it is CORRECT:**  
  AWS Marketplace is correct because, beyond being a purchase catalog, it includes governance and entitlement management features that track procured software across the organization.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Organizations is incorrect because it manages account structure and consolidated billing, not the entitlement and governance tracking of purchased marketplace software.

---

### Question 77

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.3: Identify AWS technical resources and AWS Support options.`  
**Origin:** *Live Quiz Engine (ID: 80796)*

> **Scenario:**  
> A team's application in one AWS Region started throwing intermittent errors, and the on-call engineer wants to quickly check whether an ongoing AWS service issue is affecting their specific account and resources, rather than a bug in their own code. Which resource should they check first?

#### Options
- **A.** AWS Trusted Advisor, because it continuously checks resource configurations against best practices for cost, security, and fault tolerance across the whole account
- **B.** The general AWS Health Dashboard (Global Service Status), because it lists the overall operating status of every AWS service across all Regions worldwide
- **C.** The AWS Health Dashboard, because its account-specific view shows operational issues and scheduled changes affecting the resources actually running in that account **[CORRECT]**
- **D.** AWS re:Post, because it is a community-driven question and answer forum where other customers may have posted about similar error messages

**Correct Answer:** `C`

#### Comprehensive Verification & Explanations

- **Option A:** ❌ **Why it is INCORRECT:**  
  Trusted Advisor is incorrect because it evaluates configuration and usage against best-practice checks rather than reporting live operational events affecting specific resources.

- **Option B:** ❌ **Why it is INCORRECT:**  
  The general AWS Health Dashboard (Service Status) is incorrect because it only shows broad, account-agnostic service status and would not confirm impact on this particular account's resources.

- **Option C:** ✅ **Why it is CORRECT:**  
  The Health Dashboard is correct because its personalized view surfaces events tied to the account's own resources, letting the engineer confirm whether an AWS-side issue is the cause.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS re:Post is incorrect because it is a peer community forum and would only surface a relevant thread by chance, not a confirmed account-specific status.

---

### Question 78

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.3: Identify AWS technical resources and AWS Support options.`  
**Origin:** *Live Quiz Engine (ID: 80798)*

> **Scenario:**  
> A developer hits an unusual error message while configuring a Lambda function and wants to search whether other AWS customers have hit the same issue and shared a workaround, without opening a paid support case. Which free AWS resource is built for this kind of peer troubleshooting?

#### Options
- **A.** The AWS Knowledge Center, because it publishes short official articles answering the most frequently asked technical questions submitted directly to AWS Support
- **B.** AWS Support Center, because it is the console where a customer opens and tracks a technical support case directly with an assigned AWS engineer
- **C.** AWS Prescriptive Guidance, because it offers structured strategies and patterns written by AWS for defined technical use cases like large migrations
- **D.** AWS re:Post, because it is a community question and answer service where customers, AWS employees, and Subject Matter Experts share solutions to common problems **[CORRECT]**

**Correct Answer:** `D`

#### Comprehensive Verification & Explanations

- **Option A:** ❌ **Why it is INCORRECT:**  
  The Knowledge Center is incorrect because its content is official short-form articles written by AWS for common questions, not a searchable peer discussion thread.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Support Center is incorrect because it is used to open and manage paid support cases directly with AWS, not to browse community-submitted answers for free.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Prescriptive Guidance is incorrect because it delivers AWS-authored strategies for defined use cases rather than a place to search other customers' shared troubleshooting posts.

- **Option D:** ✅ **Why it is CORRECT:**  
  AWS re:Post is correct because it is specifically a community Q&A platform where customers can search past questions and post new ones to crowdsource a fix.

---

### Question 79

**Classification:** `Domain 4: Billing, Pricing, and Support` | `Subdomain 4.3: Identify AWS technical resources and AWS Support options.`  
**Origin:** *Live Quiz Engine (ID: 80794)*

> **Scenario:**  
> A solo developer is building a personal side project on AWS and occasionally has general how-to questions about services, but has no production outages since nothing is live yet. Which AWS Support plan gives paid access to a support engineer for this level of need, without paying for guaranteed response times on business-critical issues?

#### Options
- **A.** AWS Basic Support, because it includes paid one-on-one engineer access for account and billing questions in addition to the free customer service channels
- **B.** AWS Enterprise On-Ramp Support, because it provides a shared pool of Technical Account Managers aimed at customers running mission-critical production workloads directly
- **C.** AWS Developer Support, because it gives business-hours access to a support engineer by email for build-and-test guidance at a lower monthly cost than production tiers **[CORRECT]**
- **D.** AWS Business Support, because it guarantees 24/7 phone, chat, and email access along with a one-hour response target for any production system impairment case

**Correct Answer:** `C`

#### Comprehensive Verification & Explanations

- **Option A:** ❌ **Why it is INCORRECT:**  
  Basic Support is incorrect because it is the free tier included with every AWS account and never includes one-on-one technical engineer access regardless of payment.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Enterprise On-Ramp Support is incorrect because it targets customers running production or mission-critical workloads that need proactive TAM guidance, not a solo learning project.

- **Option C:** ✅ **Why it is CORRECT:**  
  Developer Support is correct because it is priced for individuals and small teams who are experimenting or building, giving business-hours engineer access without production-tier 24/7 guarantees.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Business Support is incorrect because its 24/7 access and one-hour response guarantee are priced and designed for production workloads, more than a non-production project needs.

---

