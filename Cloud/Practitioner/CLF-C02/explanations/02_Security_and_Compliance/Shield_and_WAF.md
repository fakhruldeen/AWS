# AWS WAF (Web Application Firewall)

> **Service Category:** Security, Identity & Compliance  
> **Service Role:** Web application firewall that helps protect web applications and APIs against common web exploits, bots, and vulnerabilities that may affect availability, compromise security, or consume excessive resources.  
> **Relevant Certifications:** [[01_Certifications/Cloud_Practitioner_CLF-C02/CLF-C02_Master_Blueprint|CLF-C02]], SAA-C03, SCS-C02  
> **Tags:** `#aws/services` `#aws/security` `#waf` `#firewall` `#layer7` `#clf-c02`

---

## 1. What is AWS WAF?

**AWS WAF** is a Web Application Firewall that operates at **Layer 7 (Application Layer)** of the OSI model. It inspects incoming HTTP and HTTPS requests and blocks malicious traffic before it ever reaches your application servers.

AWS WAF protects against common web vulnerabilities defined by the **OWASP Top 10**, such as **SQL Injection (SQLi)**, **Cross-Site Scripting (XSS)**, HTTP flood attacks, and automated scraper bots.

```mermaid
flowchart TD
    User["Incoming HTTP / HTTPS Traffic"] --> WAF["AWS WAF (Web ACL Evaluation)"]
    
    subgraph RuleEvaluation ["Rule Evaluation Pipeline"]
        R1["1. Rate-Based Rules (e.g. Block >2,000 reqs / 5 min per IP)"]
        R2["2. Managed Rule Sets (OWASP Top 10, Core Rule Set - CRS)"]
        R3["3. SQLi & XSS Detection Matchers"]
        R4["4. Geographic IP Whitelists / Blacklists"]
        R5["5. Custom Regex & Header Matching"]
    end

    WAF --> RuleEvaluation
    RuleEvaluation -->|Violates Rule| Blocked["DENIED: Return HTTP 403 Forbidden / Captcha"]
    RuleEvaluation -->|Passes All Rules| Allowed["ALLOWED: Forward Request to Origin"]

    Allowed --> Targets["Protected Resources:\n• Amazon CloudFront\n• Application Load Balancer (ALB)\n• Amazon API Gateway\n• AWS AppSync (GraphQL)\n• Amazon Cognito User Pools"]
```

---

## 2. Core Components of AWS WAF

1. **Web Access Control Lists (Web ACLs):**
   - The top-level resource containing a prioritized collection of rules.
   - Attached to CloudFront distributions (Global scope: `CLOUDFRONT`) or regional resources (Regional scope: `REGIONAL`).
2. **Rule Types:**
   - **AWS Managed Rules (AMR):** Pre-configured rule groups maintained by AWS security experts (e.g., Core Rule Set, Known Bad Inputs, SQL Database, Linux Operating System rules).
   - **Marketplace Managed Rules:** Rules authored and updated by third-party security vendors (Fortinet, F5, Trend Micro).
   - **Rate-Based Rules:** Automatically tracks the rate of requests from individual IP addresses and temporarily blocks or rate-limits any IP that exceeds a configured threshold (e.g., max 1,000 requests per 5 minutes) to mitigate Layer 7 HTTP floods.
   - **Custom Rules:** Custom boolean match conditions inspecting IP addresses, HTTP headers, query strings, cookies, or URI request paths.
3. **Actions:**
   - `Allow`: Request is allowed to pass to the protected application.
   - `Block`: Returns an immediate HTTP 403 Forbidden response.
   - `Count`: Logs the match without blocking (ideal for testing rules before enforcing).
   - `CAPTCHA` / `Challenge`: Presents an interactive or silent browser challenge to verify the caller is a human and not an automated bot.

---

## 3. Network ACL vs. Security Group vs. AWS WAF

| Dimension | Network ACL (NACL) | Security Group (SG) | AWS WAF |
|:---|:---:|:---:|:---:|
| **OSI Layer** | **Layer 4** (Network / Transport) | **Layer 4** (Transport / Instance) | **Layer 7 (Application)** |
| **Operation Level**| **Subnet Level** | **Instance / ENI Level** | **Application / Gateway Level** |
| **Inspection Scope**| Source/Dest IP & Port only | Source/Dest IP & Port only | **Full HTTP Body, Headers, URI, SQL strings** |
| **Rule Capabilities**| Allow & Deny (Numerical order) | Allow only (All rules evaluated) | Allow, Block, Count, CAPTCHA, Rate-limiting |
| **Attacks Prevented**| Basic IP flooding & port scans | Unauthorized network access | **SQL Injection, XSS, Scrapers, Bots** |

---

## 4. Exam Tips & Distinction Criteria

> [!IMPORTANT]
> - **SQL Injection & Cross-Site Scripting (XSS):** If an exam scenario asks how to protect an application from SQL injection or XSS, the answer is ALWAYS **AWS WAF**.
> - **Block Bad IP at Layer 7 vs Layer 4:**
>   - To block malicious web requests containing suspicious HTTP headers, use **AWS WAF**.
>   - To block a specific raw IP address at the subnet level for free, use a **Network ACL (NACL)**.
> - **Rate-Limiting Web Requests:** Use **AWS WAF Rate-Based Rules** to mitigate brute-force password guessing or web scraping.

---

## 5. Cross-Service Links
- [[AWS_Shield|AWS Shield (DDoS Protection)]]
- [[Amazon_CloudFront|Amazon CloudFront]]
- [[Amazon_VPC_and_Networking|Security Groups & Network ACLs]]
- [[AWS_Security_Services|Security Overview Hub]]
