# Lab 2: Hosting a Resilient Global Static Website using Amazon S3 & CloudFront

> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Domain Focus:** Domain 3 (Cloud Technology & Services)  
> **Estimated Duration:** 45 minutes  
> **Level:** Foundational (Student Hands-On)  
> **Cost to Student:** **\$0.00 (Free Tier Compliant)**

---

## 🎯 Lab Objectives

In this hands-on lab, students will build a secure, global, and highly available web architecture:
1. Create a secure private **Amazon S3** bucket.
2. Upload a sample responsive HTML5 static website.
3. Deploy an **Amazon CloudFront** Content Delivery Network (CDN) distribution.
4. Configure **Origin Access Control (OAC)** to ensure the S3 bucket is completely private and only accessible via CloudFront.
5. Verify HTTPS security and edge caching across global Points of Presence.

---

## 🏗️ Architecture Diagram

```mermaid
flowchart LR
    Client[Global Browser Client]
    
    subgraph EdgeLayer ["Amazon CloudFront (Global CDN)"]
        Edge["CloudFront Distribution\n- HTTPS Enforced\n- Global Edge Caching\n- Origin Access Control (OAC)"]
    end
    
    subgraph StorageLayer ["Amazon S3 (Private Origin)"]
        S3["Amazon S3 Bucket\n- Block Public Access = ON\n- Bucket Policy: Allow OAC Only"]
        HTML["index.html\nstyles.css"]
    end
    
    Client -->|HTTPS Request (Edge Latency)| Edge
    Edge -->|Cache Hit| Client
    Edge -.->|Cache Miss (Private OAC)| S3
    Client x--|Direct Public HTTP Access Blocked| S3
```

---

## 📋 Prerequisites
* An active AWS Account.
* Basic text editor to create `index.html`.

---

## 🛠️ Step-by-Step Instructions

### Step 1: Create a Sample `index.html` File
Create a simple `index.html` file on your local machine:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First CloudFront S3 Webpage</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin-top: 100px; background-color: #f7f9fa; }
        .card { background: white; max-width: 600px; margin: 0 auto; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        h1 { color: #232f3e; }
        p { color: #545b64; font-size: 1.1em; }
        .badge { background: #ff9900; color: white; padding: 6px 12px; border-radius: 6px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">AWS Cloud Practitioner</span>
        <h1>Global CloudFront + S3 Website</h1>
        <p>This static webpage is hosted privately in an Amazon S3 bucket and distributed globally across 600+ Edge Locations via Amazon CloudFront.</p>
    </div>
</body>
</html>
```

---

### Step 2: Create a Private Amazon S3 Bucket
1. Open the **Amazon S3 Console**.
2. Click **Create bucket**.
3. Enter a globally unique bucket name (e.g., `clf-student-web-<your-name>-2026`).
4. Select your preferred AWS Region (e.g., `us-east-1`).
5. Ensure **Block *all* public access** is **CHECKED (Enabled)**.
6. Leave other defaults as-is and click **Create bucket**.
7. Click on your newly created bucket, click **Upload**, select your local `index.html` file, and click **Upload**.

---

### Step 3: Create an Amazon CloudFront Distribution with Origin Access Control (OAC)
1. Open the **CloudFront Console**.
2. Click **Create distribution**.
3. Under **Origin domain**, select your S3 bucket from the dropdown.
4. Under **Origin access**, select **Origin access control settings (recommended)**.
5. Click **Create control setting** (accept default name) and click **Create**.
6. Under **Default cache behavior**:
   * Viewer protocol policy: Select **Redirect HTTP to HTTPS**.
   * Allowed HTTP methods: Select **GET, HEAD**.
7. Under **Settings**:
   * Default root object: Type `index.html`.
8. Click **Create distribution**.
9. In the blue banner that appears at the top, click **Copy policy**. (This is the S3 bucket policy required to allow CloudFront to read your bucket).

---

### Step 4: Attach the OAC Policy to the S3 Bucket
1. Return to the **Amazon S3 Console** and click on your bucket.
2. Select the **Permissions** tab.
3. Scroll down to **Bucket policy** and click **Edit**.
4. Paste the copied policy from CloudFront into the editor.
5. Click **Save changes**.

---

### Step 5: Test Global Web Access
1. Return to the **CloudFront Console**.
2. Wait until the **Last modified** status changes from *Deploying* to a timestamp.
3. Copy the **Distribution domain name** (e.g., `https://d111111abcdef8.cloudfront.net`).
4. Paste the URL into your web browser.
> *Verification:* Your webpage should load instantly over a secure HTTPS connection with a valid Amazon SSL certificate!

---

## 🧹 Clean-Up (To Avoid Any Unintended Charges)
1. In the CloudFront console, select your distribution, click **Disable**, wait for it to disable, then click **Delete**.
2. In the Amazon S3 console, open your bucket, click **Empty** to delete `index.html`, and then click **Delete bucket**.
