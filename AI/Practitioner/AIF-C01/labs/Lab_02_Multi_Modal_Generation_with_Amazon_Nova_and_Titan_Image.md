# Lab 02: Multi-Modal Generation with Amazon Nova & Titan Image Generator

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 2: Fundamentals of Generative AI  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** Pay-per-image and pay-per-token ($<\$0.15$)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Synthesize high-resolution marketing imagery using **Amazon Titan Image Generator G1/v2**.
2. Perform visual **Inpainting** and **Outpainting** directly in the Bedrock Image Playground.
3. Verify tamper-resistant invisible **digital watermarking** generated on synthetic images.
4. Process multimodal inputs (text + chart image) using **Amazon Nova Lite / Pro**.
5. Invoke multimodal inference using the AWS CLI v2.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Generate Synthetic Images with Titan Image Generator
1. In the **Amazon Bedrock Console**, navigate to **Playgrounds** > **Image**.
2. Click **Select model** > **Amazon** > **Titan Image Generator G1/v2**. Click **Apply**.
3. In the configuration panel:
   * Mode: **Generate**
   * Aspect ratio: `1:1 (Square - 1024x1024)`
   * Number of images: `1`
   * Quality: `Standard`
4. Enter the prompt:
   ```text
   A modern, clean enterprise cloud data center with glowing server racks, subtle blue and violet neon ambient lighting, cinematic photography, 8k resolution.
   ```
5. Click **Generate**.

![Titan Image Playground](images/lab02_step01_image_playground_canvas.png)

### Step 2: Inpainting and Object Replacement
1. Select the generated image in the gallery.
2. Click **Inpaint / Outpaint**.
3. Select the **Brush tool** and paint a mask over a portion of the floor or background.
4. Enter the modification prompt:
   ```text
   Add a sleek autonomous robotic inspection rover on the floor.
   ```
5. Click **Generate**. Review how the diffusion model seamlessly blends the object into the scene while maintaining lighting consistency.

![Inpainting Mask Selection](images/lab02_step02_inpainting_mask_selection.png)

### Step 3: Multimodal Vision Analysis with Amazon Nova
1. Navigate to **Playgrounds** > **Chat**.
2. Select model **Amazon Nova Pro** (or **Amazon Nova Lite**).
3. Click the **Paperclip / Upload image** icon and upload a screenshot of an architectural diagram or sales line chart.
4. Add the prompt:
   ```text
   Analyze the uploaded image. Identify the key trends shown in the graph and summarize three strategic takeaways for business leadership.
   ```
5. Click **Run**. Observe how Nova processes both pixel data and textual directives simultaneously.

![Multimodal Nova Analysis](images/lab02_step03_multimodal_nova_analysis.png)

---

## 💻 AWS CLI v2 Runbook

Generate an image using the Titan Image Generator via the AWS CLI:
```bash
aws bedrock-runtime invoke-model \
    --model-id amazon.titan-image-generator-v2:0 \
    --body '{
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {
            "text": "Enterprise cloud operations dashboard displayed on a modern holographic interface"
        },
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "quality": "standard",
            "height": 1024,
            "width": 1024,
            "cfgScale": 8.0
        }
    }' \
    --cli-binary-format raw-in-base64-out \
    response.json
```

---

## 🧹 Teardown & Clean-up
* Generated images in the playground session are stored ephemerally. Download any images you wish to retain.
* Delete local output files (`response.json`) to keep your workspace tidy.
