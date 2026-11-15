# Lab 04: Autonomous AI Agents with Bedrock AgentCore, Action Groups & MCP

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 2 & Domain 3: Agentic AI & Model Context Protocol  
> **Estimated Duration:** 60 minutes  
> **Cost / Free Tier:** AWS Lambda free tier + minimal Bedrock token invocation ($<\$0.20$)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Build an autonomous agent using **Amazon Bedrock AgentCore**.
2. Create an **AWS Lambda function** to serve as an executable Action Group.
3. Define an **OpenAPI 3.0 schema** for tool parameter validation.
4. Integrate external tools via the **Model Context Protocol (MCP)**.
5. Inspect the intermediate ReAct reasoning trace in the agent test console.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Create the Backend Action Lambda Function
1. In the **AWS Management Console**, navigate to **AWS Lambda** > **Create function**.
2. **Function name:** `BedrockAgentInventoryLookup`
3. **Runtime:** Python 3.12.
4. Replace code with:
   ```python
   import json

   INVENTORY_DB = {
       "ITEM-101": {"name": "Cloud Server Rack 42U", "stock": 14, "warehouse": "Stockholm-1"},
       "ITEM-202": {"name": "100GbE Fiber Switch", "stock": 0, "warehouse": "Stockholm-2"},
       "ITEM-303": {"name": "UPS Battery Backup 3000VA", "stock": 28, "warehouse": "Stockholm-1"}
   }

   def lambda_handler(event, context):
       print("Event:", json.dumps(event))
       actionGroup = event['actionGroup']
       function = event['function']
       parameters = event.get('parameters', [])
       
       sku = None
       for param in parameters:
           if param['name'] == 'sku':
               sku = param['value']
               
       item_info = INVENTORY_DB.get(sku, {"error": "SKU not found in inventory"})
       
       response = {
           'messageVersion': '1.0',
           'response': {
               'actionGroup': actionGroup,
               'function': function,
               'functionResponse': {
                   'responseBody': {
                       'TEXT': {'body': json.dumps(item_info)}
                   }
               }
           }
       }
       return response
   ```
5. Click **Deploy**.
6. Grant Bedrock invocation permission:
   ```bash
   aws lambda add-permission \
       --function-name BedrockAgentInventoryLookup \
       --statement-id AllowBedrockAgents \
       --action lambda:InvokeFunction \
       --principal bedrock.amazonaws.com
   ```

### Step 2: Create the Amazon Bedrock Agent
1. Navigate to **Amazon Bedrock** > **Agents** > **Create agent**.
2. **Agent details:**
   * Name: `EnterpriseITOpsAgent`
   * Foundation Model: **Amazon Nova Pro** (or **Anthropic Claude 3.5 Sonnet**).
   * Instruction prompt:
     ```text
     You are an autonomous IT operations assistant. When a user asks about warehouse equipment stock or availability, call the inventory action group using the product SKU. Summarize availability and warehouse location clearly.
     ```
3. Click **Save**.

![Agent Configuration Screen](images/lab04_step01_agent_configuration_screen.png)

### Step 3: Attach the Action Group with OpenAPI Schema
1. In the Agent Builder, scroll to **Action groups** > **Add**.
2. **Action group name:** `InventoryActions`
3. **Action group type:** Select **Define with API schemas**.
4. **Action group invocation:** Choose **Select an existing Lambda function** > `BedrockAgentInventoryLookup`.
5. **Action group schema:** Select **Define with in-line schema editor** and paste:
   ```json
   {
     "openapi": "3.0.0",
     "info": {"title": "Inventory Service", "version": "1.0.0"},
     "paths": {
       "/inventory": {
         "get": {
           "summary": "Look up equipment stock by SKU",
           "operationId": "checkStock",
           "parameters": [
             {
               "name": "sku",
               "in": "query",
               "description": "The inventory SKU (e.g. ITEM-101)",
               "required": true,
               "schema": {"type": "string"}
             }
           ],
           "responses": {
             "200": {"description": "Stock details"}
           }
         }
       }
     }
   }
   ```
6. Click **Save** and then click **Prepare agent**.

![Action Group OpenAPI Schema](images/lab04_step02_action_group_openapi_schema.png)

### Step 4: Model Context Protocol (MCP) Tool Integration
1. Review how MCP servers expose external tools via JSON-RPC 2.0.
2. Observe how the Bedrock Agent runtime automatically formats tool call requests and executes responses across both Lambda and MCP interfaces.

![MCP Tool Configuration](images/lab04_step03_mcp_tool_configuration.png)

### Step 5: Test Autonomous Execution & Review Traces
1. In the **Test Agent** panel on the right, type:
   ```text
   Can you check if we have any 100GbE Fiber Switches in stock? The SKU is ITEM-202.
   ```
2. Click **Run**.
3. Click **Show trace** under the response.
4. Review the intermediate reasoning steps:
   * **Thought:** Identifies that tool `checkStock` must be called with `sku: ITEM-202`.
   * **Action:** Dispatches the payload to the Lambda function.
   * **Observation:** Receives `stock: 0`.
   * **Final Output:** Inform the user that the switch is out of stock in Stockholm-2.

![Agent Reasoning Trace](images/lab04_step04_agent_reasoning_trace.png)

---

## 🧹 Teardown & Clean-up
1. In Amazon Bedrock, delete agent `EnterpriseITOpsAgent`.
2. In AWS Lambda, delete function `BedrockAgentInventoryLookup`.
