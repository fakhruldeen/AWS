# Lecture 02: Compute Virtualization & Containers

## ⏱️ Timing & Delivery Strategy
- **Duration:** 120 Minutes
- **Lecture Slide Deck:** `slides/Module_02_Compute_Storage_and_Databases_Slides.md` (Part 1)
- **Hands-On Transition:** `labs/lab_03_ec2_compute_bootstrap.md` & `labs/lab_04_alb_autoscaling_ha.md`

## 🎯 Learning Objectives
1. Understand the spectrum of compute: Virtual Machines (EC2), Containers (ECS/EKS/Fargate), and Serverless (Lambda).
2. Master EC2 instance purchasing options: On-Demand, Savings Plans, Reserved Instances, Spot Instances, and Dedicated Hosts.
3. Understand Auto Scaling Group elasticity (Horizontal vs. Vertical scaling).
4. Identify when to choose AWS Lambda vs. running a persistent Docker container on ECS Fargate.

## 🗣️ Instructor Talking Points & Common Traps
- **Trap 1: Spot Instances for Mission-Critical Production:** Students often pick Spot instances because they are cheap (up to 90% discount). Emphasize: *Spot instances can be reclaimed by AWS with a 2-minute notice! Only use them for batch processing, image transcoding, CI/CD runners, or fault-tolerant workloads.*
- **Trap 2: Vertical vs. Horizontal Scaling:** Vertical = scaling UP (bigger instance type, e.g. `t3.micro` to `m5.large`, requires downtime). Horizontal = scaling OUT (adding more identical instances behind an ALB). Cloud architecture prioritizes horizontal elasticity.
