# Lab 08: Pre-Trained Foundation Model Deployment with SageMaker JumpStart

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 1 & Domain 3: Foundation Model Deployment & Hosting  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** Dedicated GPU endpoint usage (run for $<15$ minutes, approx $\$0.30 - \$0.50$)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Browse the open-weights and foundation model catalog in **Amazon SageMaker JumpStart**.
2. Deploy a foundation model (e.g., Falcon or Llama) to a managed real-time HTTPS endpoint.
3. Perform test inferences against the deployed model.
4. Execute proper endpoint teardown to prevent ongoing GPU hourly charges.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Browse Foundation Models in JumpStart
1. In **Amazon SageMaker Studio**, navigate to **JumpStart** in the left menu.
2. Browse the curated model hub: observe categories for Text Generation, Vision, Audio, and Tabular models.
3. Search for a lightweight open-source foundation model (e.g., **Falcon 7B Instruct** or **Hugging Face Text2Text**).

![JumpStart Model Hub](images/lab08_step01_jumpstart_model_hub.png)

### Step 2: Configure Endpoint Deployment
1. Click on the model card.
2. Review the model architecture, license, and pre-training dataset overview.
3. In the **Deploy** panel on the right side:
   * **Endpoint name:** `jumpstart-demo-endpoint`
   * **Instance type:** Select the default GPU instance (e.g., `ml.g5.2xlarge`).
   * **Initial instance count:** `1`
4. Click the orange **Deploy** button.

![JumpStart Deployment Parameters](images/lab08_step02_jumpstart_deploy_parameters.png)

### Step 3: Monitor Endpoint Status
1. Navigate to **SageMaker Console** > **Inference** > **Endpoints**.
2. Wait 5–10 minutes while SageMaker provisions the EC2 instance, downloads the model weights from S3, and starts the container.
3. Verify the status changes from `Creating` to **InService**.

![JumpStart Endpoint In Service](images/lab08_step03_jumpstart_endpoint_in_service.png)

### Step 4: Test Real-Time Inference
Invoke the endpoint via the AWS CLI:
```bash
aws sagemaker-runtime invoke-endpoint \
    --endpoint-name jumpstart-demo-endpoint \
    --content-type application/json \
    --body '{"inputs": "What are three benefits of serverless computing on AWS?"}' \
    output.json

cat output.json
```

---

## 🚨 CRITICAL CLEANUP: Immediate Endpoint Deletion

> [!WARNING]
> SageMaker hosting endpoints run on dedicated GPU instances and bill per hour until explicitly deleted. Always delete your endpoint immediately after testing.

1. In the **Amazon SageMaker Console**, navigate to **Inference** > **Endpoints**.
2. Select `jumpstart-demo-endpoint`.
3. In the **Actions** dropdown menu, click **Delete**.
4. Confirm by typing `delete` and clicking **Delete**.
5. Also delete the corresponding Endpoint Configuration and Model in the **Inference** menu.

![Endpoint Teardown Confirmation](images/lab08_step04_endpoint_teardown_dialog.png)
