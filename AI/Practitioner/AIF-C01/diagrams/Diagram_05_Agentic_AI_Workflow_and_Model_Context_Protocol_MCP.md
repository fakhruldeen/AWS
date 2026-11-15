# Diagram 05: Agentic AI Workflow and Model Context Protocol (MCP)

> **Architecture Blueprint:** `Diagram_05_Agentic_AI_Workflow_and_Model_Context_Protocol_MCP.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Domain Alignment:** Domain 2 & Domain 3 (Agentic AI & MCP additions - v1.2)

---

## 🏛️ Architectural Blueprint

```mermaid
flowchart TD
    User["User Goal:\n'Check stock for SKU-901 and create return label'"] --> BedrockAgent["Amazon Bedrock Agent\n(AgentCore Orchestrator)"]

    subgraph AgentLoop["Autonomous ReAct Execution Loop"]
        BedrockAgent <--> PromptManager["Prompt Management & Caching"]
        BedrockAgent --> FMReasoning["Foundation Model (Nova Pro / Claude)\nFormulates Reasoning: 'Thought: Need to call inventory tool'"]
        FMReasoning --> ActionDecision["Tool Selection & Argument Formulation"]
    end

    subgraph ActionExecution["Action Groups & Protocols"]
        ActionDecision --> Protocol{"Tool Protocol Type"}
        
        Protocol -- "OpenAPI / Lambda" --> Lambda["AWS Lambda Action Group"]
        Protocol -- "Model Context Protocol" --> MCPClient["MCP Host / Client Layer"]
        
        Lambda --> DynDB["Amazon DynamoDB (Inventory Table)"]
        
        MCPClient --> MCPServer["MCP Server (JSON-RPC 2.0)"]
        MCPServer --> ExternalAPI["External Shipping / Carrier API"]
    end

    DynDB --> Lambda --> BedrockAgent
    ExternalAPI --> MCPServer --> MCPClient --> BedrockAgent

    BedrockAgent --> Reflection["Agent Reflection:\n'Observation: Stock confirmed, label generated'"]
    Reflection --> FinalResponse["Synthesized Confirmation to User"]
```

---

## 🔍 Core Architectural Highlights

1. **Autonomous Planning:** Bedrock Agents use ReAct (Reason + Act) prompting to break complex natural language goals into executable sub-actions.
2. **Standardized Tool Integration:** Interoperates seamlessly with native AWS Lambda action groups and industry-standard Model Context Protocol (MCP) servers.
3. **Auditability:** Internal execution traces (thoughts, tool inputs, execution results) are logged to Amazon CloudWatch for debugging and security auditing.
