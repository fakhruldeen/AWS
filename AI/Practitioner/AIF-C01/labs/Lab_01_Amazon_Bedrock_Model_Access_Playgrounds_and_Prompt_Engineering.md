# Lab 01: Amazon Bedrock Model Access, Playgrounds & Prompt Engineering

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 2 & Domain 3: Generative AI & Foundation Models  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** Minimal pay-per-token usage ($<\$0.10$ for the entire lab)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Navigate the Amazon Bedrock console and request model access for Amazon Nova, Titan, and Claude.
2. Experiment with inference parameters: **Temperature**, **Top-P**, and **Max Tokens**.
3. Benchmark **Zero-Shot**, **Few-Shot**, and **Chain-of-Thought (CoT)** prompt strategies.
4. Configure **Amazon Bedrock Prompt Management** and enable **Prompt Caching**.
5. Invoke models programmatically via the AWS CLI v2 `converse` API.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Enable Foundation Model Access in Amazon Bedrock
1. Sign in to the **AWS Management Console** and select your active region (`eu-north-1` or `us-east-1`).
2. Navigate to **Amazon Bedrock**.
3. In the left navigation pane, scroll to the bottom and select **Model access**.
4. Click **Modify model access** (or **Enable specific models**).
5. Select the checkboxes for:
   * **Amazon:** Nova Micro, Nova Lite, Nova Pro, Titan Text Express v1.
   * **Anthropic:** Claude 3.5 Sonnet / Claude 3 Haiku.
6. Click **Next**, review the selection, and click **Submit**.
7. Wait until the model status changes to **Access granted**.

![Model Access Overview](images/lab01_step01_model_access_catalog.png)

### Step 2: Explore the Chat Playground & Inference Parameters
1. In the left navigation bar under **Playgrounds**, select **Chat**.
2. Click **Select model**, choose **Amazon Nova Pro** (or **Claude 3.5 Sonnet**), and click **Apply**.
3. Locate the **Configurations** panel on the right.

![Chat Playground Setup](images/lab01_step02_chat_playground_setup.png)

#### Experiment A: Temperature Impact
* Set **Temperature** to `1.0` and enter:
  ```text
  Suggest three futuristic brand names for an autonomous drone logistics startup in 2050. Include a one-sentence tagline for each.
  ```
  *Observe the creative lexical diversity.*
* Now set **Temperature** to `0.0` and run the prompt again twice.
  *Notice how the output becomes completely deterministic and repeatable.*

![Temperature Output Comparison](images/lab01_step03_temperature_comparison.png)

#### Experiment B: Top-P Nucleus Sampling
* Keep Temperature at `0.7` and reduce **Top-P** to `0.2`.
* Observe how the model restricts itself to only the highest probability tokens, eliminating unexpected vocabulary.

### Step 3: Prompt Engineering Paradigms (Few-Shot & Chain-of-Thought)
1. **Few-Shot Prompting:** In the prompt box, paste:
   ```text
   Classify customer support feedback into: [Billing, Technical, Shipping].
   
   Feedback: "The package arrived with a torn box and broken screen."
   Category: Shipping
   
   Feedback: "I was charged twice on my credit card statement."
   Category: Billing
   
   Feedback: "The API keeps returning HTTP 504 Gateway Timeout."
   Category:
   ```
   *The model accurately predicts "Technical" following the established pattern.*

2. **Chain-of-Thought (CoT) Prompting:**
   ```text
   Solve the following problem by thinking step-by-step before stating the final answer:
   A warehouse receives 15 pallets of server racks. Each pallet holds 8 racks. 
   Each rack requires 4 cooling fans. The technician has 420 cooling fans in stock. 
   How many more cooling fans are needed to equip all racks?
   ```
   *Observe how step-by-step reasoning eliminates arithmetic errors.*

### Step 4: Prompt Management and Prompt Caching
1. In the left navigation menu under **Foundation models**, select **Prompt management**.
2. Click **Create prompt**:
   * Name: `CustomerSupportTriage`
   * Add template text with variable: `"You are a support bot. Triage this query: {{customer_query}}"`
3. Enable **Prompt Caching** for the static preamble.

![Prompt Caching Setup](images/lab01_step04_prompt_caching_panel.png)

---

## 💻 AWS CLI v2 Runbook

Invoke Amazon Nova Micro via the Bedrock Converse API:
```bash
aws bedrock-runtime converse \
    --model-id amazon.nova-micro-v1:0 \
    --messages '[
        {
            "role": "user",
            "content": [{"text": "Explain the difference between supervised and unsupervised learning in two sentences."}]
        }
    ]' \
    --inference-config '{"temperature": 0.2, "maxTokens": 150}'
```

---

## 🧹 Teardown & Clean-up
* In Bedrock, on-demand playground usage incurs zero ongoing idle charges.
* If you saved test prompts in Prompt Management, delete them if they are no longer needed.
