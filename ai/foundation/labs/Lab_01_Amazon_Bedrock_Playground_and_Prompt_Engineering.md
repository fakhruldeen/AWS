# Lab 01: Prompt Engineering in the Amazon Bedrock Playground

> **Course:** AWS Certified AI Practitioner (AIF-C01) Track  
> **Module:** Module 1: AI & GenAI Foundations  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** Minimal pay-per-token pricing (typically $<\$0.10$ for the entire lab)  
> **AWS Region:** `us-east-1` (N. Virginia) or `us-west-2` (Oregon)

---

## Lab Objectives

By the end of this lab, you will be able to:
1. Navigate the Amazon Bedrock console and request model access.
2. Interact with foundation models in the **Bedrock Chat and Text Playgrounds**.
3. Manipulate and evaluate the impact of **Temperature**, **Top-P**, and **Max Tokens**.
4. Construct and benchmark **Zero-Shot**, **Few-Shot**, and **Chain-of-Thought (CoT)** prompts.
5. Implement stop sequences to constrain model outputs.

---

## Prerequisites
* An active AWS Account.
* Basic understanding of generative AI terminology (tokens, prompts).

---

## Step 1: Enable Foundation Model Access in Amazon Bedrock

Foundation models in Amazon Bedrock require an initial one-time access grant per AWS account and region.

1. Sign in to the **AWS Management Console** and select Region **us-east-1 (N. Virginia)** or **us-west-2 (Oregon)**.
2. In the top search bar, type `Bedrock` and select **Amazon Bedrock**.
3. In the left navigation pane, scroll to the bottom and click **Model access**.
4. Click the orange **Enable specific models** (or **Modify model access**) button.
5. Select the checkboxes for:
   * **Amazon:** Titan Text G1 - Express, Titan Text Embeddings V2
   * **Anthropic:** Claude 3.5 Sonnet / Claude 3 Haiku (if available, complete use case confirmation)
   * **Meta:** Llama 3.1 8B Instruct
6. Click **Next**, review the selection, and click **Submit**.
7. Wait until the model status changes to **Access granted** (Amazon and Meta models are typically approved instantly).

---

## Step 2: Explore the Bedrock Chat Playground & Inference Parameters

1. In the left navigation pane, under **Playgrounds**, click **Chat**.
2. Click **Select model**. Choose **Anthropic** $\rightarrow$ **Claude 3 Haiku** (or **Amazon** $\rightarrow$ **Titan Text G1 - Express**). Click **Apply**.
3. Locate the **Configurations** panel on the right side.

### Experiment A: High Temperature vs. Low Temperature
1. Set **Temperature** to `1.0` and **Max generation length** to `300`.
2. Enter the prompt:
   ```text
   Suggest three creative, futuristic names for an autonomous drone delivery company operating in the year 2050. Include a one-sentence tagline for each.
   ```
3. Click **Run**. Observe the imaginative style and vocabulary diversity.
4. Now, set **Temperature** to `0.0`.
5. Enter the prompt:
   ```text
   Extract the customer ID, order date, and total amount from this text and output STRICTLY as valid JSON:
   "Customer CUST-9821 placed an order on 2026-11-12 for a total of $342.50 including shipping."
   ```
6. Click **Run**. Notice how Temperature `0.0` provides a clean, deterministic, deterministic JSON object without extra conversational filler.

---

## Step 3: Implement Zero-Shot vs. Few-Shot Prompting

1. In the Chat Playground, test a **Zero-Shot** classification task:
   ```text
   Classify the following customer feedback as Positive, Neutral, or Negative:
   "The package arrived two days late, but the customer support representative replaced the damaged cable immediately with no hassle."
   Classification:
   ```
2. Run the prompt and record the answer.
3. Now test a **Few-Shot** prompt enforcing a customized three-part schema:
   ```text
   Review: "Battery died after 4 hours of light use."
   Sentiment: Negative
   ActionRequired: Yes
   Department: Hardware Support
   ###
   Review: "Instructions were easy to follow and setup took 5 minutes."
   Sentiment: Positive
   ActionRequired: No
   Department: Documentation
   ###
   Review: "Color looks slightly darker than the website photo, but works fine."
   Sentiment:
   ActionRequired:
   Department:
   ```
4. Run the prompt. Notice how the model strictly mirrors the demonstration pattern without needing code or fine-tuning!

---

## Step 4: Implement Chain-of-Thought (CoT) Prompting

1. Enter the following tricky word problem directly (**Standard Prompting**):
   ```text
   A warehouse had 48 servers. On Monday, 12 servers were deployed. On Tuesday, a shipment arrived that doubled the remaining servers. On Wednesday, 5 faulty servers were retired. How many servers are now in the warehouse? Answer directly with just the number.
   ```
2. Now, apply **Chain-of-Thought (CoT)**:
   ```text
   A warehouse had 48 servers. On Monday, 12 servers were deployed. On Tuesday, a shipment arrived that doubled the remaining servers. On Wednesday, 5 faulty servers were retired.
   
   Let's solve this step by step:
   1. Calculate servers remaining after Monday deployment.
   2. Calculate servers after Tuesday shipment doubling.
   3. Calculate servers after retiring faulty units on Wednesday.
   State the final answer clearly at the end.
   ```
3. Compare the clarity and accuracy of the reasoning trail.

---

## Step 5: Test Stop Sequences

1. In the right configuration panel, click **Add stop sequence**.
2. Type `STOP_HERE` and press Enter.
3. Submit the prompt:
   ```text
   Count from 1 to 10. When you reach 5, output the word STOP_HERE and then count the rest.
   ```
4. Observe that the model terminates output immediately upon generating `STOP_HERE`, proving how stop sequences enforce hard boundaries.

---

## Clean Up
1. No active compute instances were created—Bedrock Playgrounds are billed strictly per token generated.
2. Close the browser tab.
