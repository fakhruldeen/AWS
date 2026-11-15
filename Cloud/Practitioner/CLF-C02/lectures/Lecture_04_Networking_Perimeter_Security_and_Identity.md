# Lecture 04: Networking, Perimeter Security & Identity

## ⏱️ Timing & Delivery Strategy
- **Duration:** 120 Minutes
- **Lecture Slide Deck:** `slides/Module_03_Networking_Security_and_Identity_Slides.md`
- **Hands-On Transition:** `labs/lab_01_vpc_networking.md` & `labs/lab_02_vpc_security_controls.md`

## 🎯 Learning Objectives
1. Construct a Virtual Private Cloud (VPC) with public and private subnets across multiple AZs.
2. Master the difference between **Security Groups** (Stateful, instance level) and **Network ACLs** (Stateless, subnet level).
3. Architect perimeter defense using **Route 53**, **Amazon CloudFront**, **AWS WAF**, and **AWS Shield**.
4. Enforce Principle of Least Privilege with **AWS IAM** Users, Groups, Roles, Policies, and MFA.

## 🗣️ Instructor Talking Points & Common Traps
- **Trap 1: Security Groups vs. NACLs:**
  - *Security Groups:* Stateful! Return traffic is automatically allowed regardless of outbound rules. No explicit deny rules (everything not allowed is implicitly denied).
  - *Network ACLs:* Stateless! You MUST explicitly allow both outbound and inbound ephemeral return ports (1024-65535). Supports explicit DENY rules evaluated in numerical rule order.
- **Trap 2: IAM User vs. IAM Role:** Never issue long-term access keys to EC2 instances or Lambda functions. Always assign an **IAM Role** with temporary credentials via AWS STS!
