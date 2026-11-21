# Tutorial 02: Multi-Agent Autonomous System with Bedrock AgentCore and MCP

> **Architecture Build Tutorial:** `Tutorial_02_Multi_Agent_Autonomous_System_with_Bedrock_AgentCore_and_MCP.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Services Integrated:** Amazon Bedrock Agents, AgentCore, AWS Lambda, Amazon DynamoDB, Model Context Protocol (MCP), AWS IAM  
> **Level:** Advanced Multi-Service Autonomous System

---

## 🏛️ Architecture Overview

Modern enterprise AI systems decompose complex workflows into specialized autonomous agents. This tutorial implements an autonomous multi-agent customer service and fulfillment system using **Amazon Bedrock AgentCore**, **AWS Lambda Action Groups**, and the **Model Context Protocol (MCP)**.

```mermaid
flowchart TD
    User["Customer Goal:\n'Check order #8912 and reschedule delivery'"] --> Supervisor["Supervisor Bedrock Agent\n(Bedrock AgentCore Router)"]

    subgraph AgentMesh["Specialized Collaborator Agents"]
        OrderAgent["Order Status Agent\n(Tools: DynamoDB Query)"]
        FulfillmentAgent["Fulfillment Agent\n(Tools: Carrier Reschedule API via MCP)"]
    end

    Supervisor -->|"Delegates Order Lookup"| OrderAgent
    Supervisor -->|"Delegates Reschedule"| FulfillmentAgent

    subgraph BackendExecution["Action Execution Plane"]
        LambdaOrder["AWS Lambda: GetOrderDetails"]
        DynDB["DynamoDB Orders Table"]
        MCPServer["Shipping Carrier MCP Server\n(JSON-RPC 2.0 / SSE Transport)"]
        CarrierAPI["Carrier Logistics REST API"]
    end

    OrderAgent --> LambdaOrder --> DynDB
    FulfillmentAgent --> MCPServer --> CarrierAPI
```

---

## 🛠️ Step-by-Step Implementation Guide

### Step 1: Create the DynamoDB Orders Table
```bash
aws dynamodb create-table \
    --table-name CustomerOrders \
    --attribute-definitions AttributeName=OrderId,AttributeType=S \
    --key-schema AttributeName=OrderId,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --region eu-north-1

# Seed test order record
aws dynamodb put-item \
    --table-name CustomerOrders \
    --item '{
        "OrderId": {"S": "8912"},
        "CustomerName": {"S": "Jane Doe"},
        "Status": {"S": "In-Transit"},
        "DeliveryDate": {"S": "2026-11-20"},
        "Address": {"S": "123 Cloud Way, Stockholm"}
    }' \
    --region eu-north-1
```

### Step 2: Create the Lambda Function for Action Groups
Author `order_lookup_lambda.py`:
```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CustomerOrders')

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])
    
    order_id = None
    for param in parameters:
        if param['name'] == 'orderId':
            order_id = param['value']
            
    if not order_id:
        response_body = {"error": "Missing orderId parameter"}
    else:
        res = table.get_item(Key={'OrderId': order_id})
        response_body = res.get('Item', {"error": "Order not found"})
        
    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': {
                'TEXT': {
                    'body': json.dumps(response_body)
                }
            }
        }
    }
    
    return {'response': action_response, 'messageVersion': '1.0'}
```

Deploy the Lambda function and grant permission to Amazon Bedrock:
```bash
aws lambda add-permission \
    --function-name GetOrderDetails \
    --statement-id AllowBedrockInvocation \
    --action lambda:InvokeFunction \
    --principal bedrock.amazonaws.com \
    --source-arn "arn:aws:bedrock:eu-north-1:*:agent/*"
```

### Step 3: Define the OpenAPI Schema for the Action Group
Save as `order_actions_schema.json`:
```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Customer Orders Service",
    "version": "1.0.0",
    "description": "APIs to query order tracking and status."
  },
  "paths": {
    "/order": {
      "get": {
        "summary": "Get Order By ID",
        "description": "Retrieves the shipping status, customer name, and scheduled delivery date.",
        "operationId": "getOrderById",
        "parameters": [
          {
            "name": "orderId",
            "in": "query",
            "description": "The unique 4-digit order identifier",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Order details payload",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Step 4: Configure the Model Context Protocol (MCP) Server for Fulfillment
Create a lightweight MCP server implementing the carrier rescheduling tool:
```json
{
  "name": "carrier_rescheduler",
  "description": "Reschedules parcel delivery window with external logistics carrier",
  "inputSchema": {
    "type": "object",
    "properties": {
      "orderId": {"type": "string"},
      "newDate": {"type": "string", "format": "date"}
    },
    "required": ["orderId", "newDate"]
  }
}
```

### Step 5: Build and Test the Bedrock Agent
1. In the Amazon Bedrock Console, navigate to **Agents** > **Create agent**.
2. **Name:** `CustomerCareOrchestrator`.
3. **Foundation model:** `Amazon Nova Pro` or `Anthropic Claude 3.5 Sonnet`.
4. **Instruction prompt:**
   > "You are an autonomous customer care supervisor. Analyze the user request. If they ask about order status, invoke the Order Action Group. If they want to change the delivery date, invoke the Fulfillment tool via the MCP connection. Always confirm actions to the user."
5. Attach the Action Group pointing to the Lambda ARN and S3 OpenAPI schema.
6. Click **Prepare agent** and test in the interactive testing console.

---

## 🔒 Security & Governance Safeguards
* **AgentCore Least Privilege:** Ensure the Agent IAM role only has permissions to invoke specific Lambda ARNs.
* **Bedrock Guardrail Attachment:** Attach an active Guardrail to redact PII (phone numbers, addresses) from the conversational agent transcript.
* **Audit Traces:** Inspect the Amazon CloudWatch log groups created for the agent to review intermediate reasoning thoughts and tool invocations.
