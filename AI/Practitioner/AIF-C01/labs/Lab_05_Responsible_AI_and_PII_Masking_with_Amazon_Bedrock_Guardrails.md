# Lab 05: Responsible AI & PII Masking with Amazon Bedrock Guardrails

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 4: Guidelines for Responsible AI  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** Minimal Bedrock token usage ($<\$0.05$)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Create a production **Amazon Bedrock Guardrail**.
2. Configure **Denied Topics** to enforce organizational boundaries.
3. Establish **Content Filters** across Hate, Insults, Sexual, and Violence categories.
4. Enforce **Sensitive Information Filters** to mask emails/names and block credit cards.
5. Benchmark Guardrail interventions against adversarial and toxic prompts.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Create a Guardrail in Amazon Bedrock
1. In the **AWS Management Console**, navigate to **Amazon Bedrock** > **Guardrails**.
2. Click **Create guardrail**:
   * **Name:** `CustomerSupportSafetyGuardrail`
   * **Description:** Protects customer support chat from toxic content and PII leaks.
3. Click **Next**.

![Guardrail Builder Overview](images/lab05_step01_guardrail_builder_overview.png)

### Step 2: Configure Denied Topics
1. Under **Topic policy**, click **Add topic**:
   * **Name:** `TaxAndInvestmentAdvice`
   * **Definition:** Providing formal financial advice, tax planning strategies, or stock picking suggestions.
   * **Sample phrases:**
     * "Should I purchase government bonds or stocks?"
     * "How do I evade capital gains taxes?"
2. Click **Confirm**.

![Denied Topics Configuration](images/lab05_step02_denied_topics_configuration.png)

### Step 3: Configure Content Filters
1. In **Content policy**:
   * **Hate:** Set input and output strength to **High**.
   * **Insults:** Set input to **Medium**, output to **High**.
   * **Sexual:** Set input and output strength to **High**.
   * **Violence:** Set input and output strength to **High**.
2. Click **Next**.

### Step 4: Configure Sensitive Information & PII Filters
1. Under **Sensitive information policy**, scroll to **PII entities**:
   * Add **Email**: Action = `Anonymize`
   * Add **Name**: Action = `Anonymize`
   * Add **Credit/Debit Card Number**: Action = `Block`
   * Add **US Social Security Number**: Action = `Block`
2. Scroll to **Contextual grounding policy** (v1.2 feature):
   * Set Grounding threshold to `0.70`
   * Set Relevance threshold to `0.70`
3. In **Blocked messaging**:
   * Input message: `"I am sorry, but your prompt contains content that violates our corporate safety guidelines."`
   * Output message: `"The response was withheld due to enterprise compliance policies."`
4. Click **Next**, review summary, and click **Create guardrail**.

![PII Masking Policy](images/lab05_step03_pii_masking_policy.png)

### Step 5: Test the Guardrail Interventions
1. On the Guardrail details page, locate the **Test guardrail** pane on the right side.
2. Select model: **Amazon Nova Pro** (or **Anthropic Claude 3.5 Sonnet**).
3. **Test 1 (Denied Topic):**
   ```text
   Can you recommend three high-yield index funds for my retirement portfolio?
   ```
   *Result:* Triggers the `TaxAndInvestmentAdvice` policy and returns the custom canned rejection message.
4. **Test 2 (PII Masking):**
   ```text
   Hi, my name is Alice Smith and my email is alice.smith@example.com. Can you summarize our company refund policy?
   ```
   *Result:* The prompt passes, but in the trace logs, the name is replaced with `[NAME]` and the email with `[EMAIL]`.

![Guardrail Blocking Test](images/lab05_step04_guardrail_blocking_test.png)

---

## 💻 AWS CLI v2 Runbook

Apply the guardrail programmatically to any text:
```bash
aws bedrock-runtime apply-guardrail \
    --guardrail-identifier YOUR_GUARDRAIL_ID \
    --guardrail-version "1" \
    --source "INPUT" \
    --content '[{"text": {"text": "My credit card is 4111-2222-3333-4444."}}]'
```

---

## 🧹 Teardown & Clean-up
* In the Amazon Bedrock Console, select **Guardrails** > select `CustomerSupportSafetyGuardrail` > click **Delete**.
