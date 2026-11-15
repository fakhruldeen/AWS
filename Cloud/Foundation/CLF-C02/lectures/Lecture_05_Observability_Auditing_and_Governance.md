# Lecture 05: Observability, Auditing & Enterprise Governance

## ⏱️ Timing & Delivery Strategy
- **Duration:** 90 Minutes
- **Lecture Slide Deck:** `slides/Module_04_Monitoring_Governance_and_DevOps_Slides.md`
- **Hands-On Transition:** `labs/lab_13_observability_cloudwatch_cloudtrail_config.md`

## 🎯 Learning Objectives
1. Dissect the Observability Triad: **Amazon CloudWatch** (Performance/Metrics), **AWS CloudTrail** (Auditing/API Calls), and **AWS Config** (Compliance/Configuration History).
2. Understand multi-account architecture with **AWS Organizations** and **Service Control Policies (SCPs)**.
3. Deploy centralized compliance governance using **AWS Control Tower**.

## 🗣️ Instructor Talking Points & Common Traps
- **Trap 1: CloudWatch vs. CloudTrail vs. Config:**
  - *CloudWatch:* "How are my instances performing right now? CPU is 92%, sound an alarm!"
  - *CloudTrail:* "Who terminated that instance at 3:14 AM yesterday from what IP address?"
  - *Config:* "Has anyone attached an unencrypted EBS volume or opened port 22 to `0.0.0.0/0` over time?"
- **Trap 2: SCPs Granting Permissions:** SCPs specify the *maximum permissions* an account or OU can have. An SCP **never grants permissions** by itself; users still require an IAM policy.
