# Lab 00: AWS Free Tier Account Creation Walkthrough

This guide provides a comprehensive, step-by-step walkthrough of creating a new **AWS Free Tier Account** using best practices for security and account management.

---

## 📌 Prerequisites & Information Needed
Before starting the registration process, ensure you have the following ready:
1. **Email Address:** `aws@fakhr.me` (or your chosen root email).
2. **Account Name:** A clear identifier (e.g., `fakhr-cloud-admin`).
3. **Credit/Debit Card:** Required for identity verification (a temporary \$1 USD hold may be placed and refunded).
4. **Phone Number:** Capable of receiving an SMS or automated voice call for 2-factor verification.
5. **Government ID / Tax Information:** Depending on your country of residence.

---

## Step 1: Navigating to the Registration Portal
1. Open your browser in **Incognito/Private** mode to avoid session collisions.
2. Navigate to: [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup)
3. Select **Create a new AWS account**.

```
+-------------------------------------------------------------+
|                     AWS Sign-Up Portal                      |
|                                                             |
|  Root user email address:                                   |
|  [ aws@fakhr.me                                           ] |
|                                                             |
|  AWS account name:                                          |
|  [ fakhr-cloud-admin                                      ] |
|                                                             |
|  [ Verify email address ]  <--- (Click to receive OTP code) |
+-------------------------------------------------------------+
```

---

## Step 2: Email Verification (OTP)
1. Check the inbox for `aws@fakhr.me`.
2. Locate the email from **Amazon Web Services (AWS)** with the subject: *AWS Email Verification*.
3. Copy the 6-digit verification code.
4. Paste the code into the verification field and click **Verify**.

> [!NOTE]
> The verification code expires in 10 minutes. If delayed, click **Resend code**.

---

## Step 3: Setting the Root Password
Create a strong, complex password for the **Root User**:
- At least 8 characters (16+ recommended).
- Include uppercase letters, lowercase letters, numbers, and symbols (`!@#$%^&*`).

> [!CAUTION]
> **Root Account Safety:** The Root user has absolute, unrestricted access to all resources and billing in your account. **Never** share this password or create access keys for the Root user.

---

## Step 4: Contact Information & Plan Selection
1. Select **Personal** (for learning/training/individual projects) or **Business** (for organizations).
2. Fill out your full legal name, phone number, country, and residential address.
3. Check the box agreeing to the **AWS Customer Agreement**.
4. Click **Continue (Step 2 of 5)**.

---

## Step 5: Billing & Payment Information
1. Enter your credit or debit card details:
   - Card Number
   - Expiration Date
   - Cardholder's Name
   - CVV / Security Code
2. Confirm the billing address matches the card statement.
3. Click **Verify and Continue (Step 3 of 5)**.

> [!TIP]
> **Free Tier Safeguards:** You are not charged during the Free Tier period unless your usage exceeds Free Tier limits. AWS places a temporary \$1 USD authorization hold to verify card validity.

---

## Step 6: Identity Verification (SMS/Voice Call)
1. Choose verification method: **Text message (SMS)** or **Voice call**.
2. Select your country code and enter your active mobile phone number.
3. Solve the visual CAPTCHA security check.
4. Click **Send SMS (Step 4 of 5)**.
5. Enter the 4-digit code received on your phone and click **Continue**.

---

## Step 7: Selecting a Support Plan
Select the **Basic Support - Free** plan:
- **Basic Support (Free):** 24/7 customer service and documentation access. Ideal for labs and Cloud Practitioner preparation.
- **Developer Support:** Starts at \$29/month (not needed for basic training).
- **Business Support:** Starts at \$100/month (for production workloads).

Click **Complete sign-up**.

---

## Step 8: Welcome Screen & Initial Console Login
1. You will be greeted with: *"Congratulations! Thank you for signing up for AWS."*
2. Click **Go to the AWS Management Console**.
3. Select **Root user**, enter `aws@fakhr.me`, and supply your root password.

---

## 🔒 Mandatory Post-Creation Security Checklist (Day 1 Best Practices)

Immediately after logging into your new account:

### 1. Enable Root Multi-Factor Authentication (MFA)
- Go to the **IAM Console** (`https://console.aws.amazon.com/iam/`).
- Click **Add MFA** under *Security recommendations* for the Root user.
- Register a Virtual Authenticator App (e.g., Google Authenticator, 1Password, or Authy).

### 2. Create an Admin IAM User or Identity Center User
- Never use the Root account for daily administration.
- Create a dedicated admin group and user with `AdministratorAccess`.
- Log out of Root and log in with your administrative identity.

### 3. Configure Billing Alerts & Free Tier Notifications
- Open **AWS Billing & Cost Management**.
- Navigate to **Billing Preferences**.
- Check **Receive Free Tier Usage Alerts** and **Receive Billing Alerts**.
- Enter your notification email: `aws@fakhr.me`.

---

## 💻 CLI Verification
To verify your AWS CLI connection to your newly configured profile:

```bash
# Check caller identity
aws sts get-caller-identity --profile aws-notes

# Verify region configuration
aws configure get region --profile aws-notes
```
