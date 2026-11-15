# Lecture 01: Introduction to Cloud & Global Infrastructure

## ⏱️ Timing & Delivery Strategy
- **Duration:** 90 Minutes
- **Lecture Slide Deck:** `slides/Module_01_Cloud_Concepts_and_Architecture_Slides.md`
- **Hands-On Transition:** `labs/00_Account_Creation_Walkthrough.md`

## 🎯 Learning Objectives
1. Articulate the 6 Core Advantages of Cloud Computing over legacy on-premises datacenters.
2. Differentiate between Cloud deployment models (Public, Private, Hybrid) and service models (IaaS, PaaS, SaaS).
3. Explain the relationship between AWS Regions, Availability Zones (AZs), Local Zones, and Edge Locations.
4. Distinguish the 6 Perspectives of the AWS Cloud Adoption Framework (CAF 3.0).

## 🗣️ Instructor Talking Points & Common Traps
- **Trap 1: Region vs. Availability Zone:** Students frequently confuse a single data center with an AZ. Emphasize: *An Availability Zone consists of one or more discrete data centers with redundant power and networking, and an AWS Region consists of at least 3 physical Availability Zones.*
- **Trap 2: High Availability vs. Fault Tolerance:** HA ensures minimal disruption and fast recovery; fault tolerance guarantees zero downtime (often requiring redundant active systems).
- **Interactive Check:** Ask students: *"If a company operates in Germany and must legally keep patient data inside German borders, which AWS construct solves this compliance requirement?"* (Answer: AWS Region selection — Frankfurt `eu-central-1`).
