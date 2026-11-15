# 02. Networking & The OSI Model Prerequisite

## 1. The OSI 7-Layer Model in Cloud Computing
Understanding where AWS networking components operate is vital for Cloud Practitioner:

| Layer # | Layer Name | Protocol / Unit | Key AWS Component |
| :---: | :--- | :--- | :--- |
| **Layer 7** | Application | HTTP, HTTPS, DNS, SSH | **AWS WAF**, **Application Load Balancer (ALB)**, **Route 53**, **API Gateway** |
| **Layer 4** | Transport | TCP, UDP, Ports (80, 443, 22) | **Network Load Balancer (NLB)**, **Security Groups**, **NACLs** |
| **Layer 3** | Network | IP Addresses, Packets, Routing | **VPC Routers**, **Route Tables**, **Internet Gateway (IGW)**, **NAT Gateway** |
| **Layer 2** | Data Link | MAC Addresses, Frames | Managed by AWS hypervisor (Nitro) |
| **Layer 1** | Physical | Fiber, Ethernet, Copper | Managed by AWS physical infrastructure |

## 2. IP Addressing & CIDR Block Subnetting
IPv4 addresses consist of 32 bits divided into 4 octets (`X.X.X.X` from `0.0.0.0` to `255.255.255.255`).
**Classless Inter-Domain Routing (CIDR)** notation indicates the prefix network mask:

$$\text{Available IP Addresses} = 2^{(32 - \text{Prefix})}$$

* `10.0.0.0/16`: $32 - 16 = 16$ bits $\implies 2^{16} = 65,536$ addresses (Standard VPC size).
* `10.0.1.0/24`: $32 - 24 = 8$ bits $\implies 2^8 = 256$ addresses (Standard Subnet size).

> [!IMPORTANT]
> **AWS Reserved IPs in Every Subnet:** AWS always reserves **5 IP addresses** in every subnet (Network address, VPC Router, DNS server, Future use, Broadcast). Therefore, a `/24` subnet yields $256 - 5 = 251$ usable addresses for your instances.

## 3. Public vs. Private IP Addresses & NAT
- **RFC 1918 Private Ranges:** `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`. Not routable over the public internet.
- **Public IP Addresses:** Globally routable on the internet.
- **Network Address Translation (NAT):** Translates private IP addresses to a single public IP address, allowing instances in private subnets to download patches from the internet while blocking unsolicited inbound connections. In AWS, this is provided as a managed service: **AWS NAT Gateway**.
