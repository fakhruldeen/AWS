# AWS Application Integration — Map of Content (MOC)

> **Domain:** 03_Services / Application Integration  
> **Parent MOC:** [[AWS_Brain_MOC]]  
> **Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], Developer Associate, Solutions Architect

---

## 1. Architectural Taxonomy of AWS Application Integration

Application integration services enable decoupled, asynchronous communication, choreography, and event distribution across microservices and distributed cloud architectures:

```mermaid
flowchart TD
    Integration["AWS Application Integration"]
    
    subgraph Queues["1. Message Queuing (Buffer & Decouple)"]
        SQS["Amazon SQS (Pull-based, Standard & FIFO)"]
        MQ["Amazon MQ (Managed ActiveMQ / RabbitMQ)"]
    end
    
    subgraph PubSub["2. Publish / Subscribe & Fan-Out"]
        SNS["Amazon SNS (Push-based, multi-subscriber)"]
    end
    
    subgraph EventDriven["3. Serverless Event Routing"]
        EB["Amazon EventBridge (Serverless event bus)"]
    end
    
    subgraph Orchestration["4. Workflow Orchestration"]
        Step["AWS Step Functions (Visual state machine workflow coordinator)"]
    end
    
    Integration --> Queues
    Integration --> PubSub
    Integration --> EventDriven
    Integration --> Orchestration
```

---

## 2. High-Yield Architectural Comparison

```mermaid
flowchart LR
    Producer["Producer"] --> ModeChoice{"Messaging Pattern?"}
    
    ModeChoice -->|"Buffer messages for workers to pull"| SQS["Amazon SQS (Pull)"]
    ModeChoice -->|"Broadcast simultaneously to many destinations"| SNS["Amazon SNS (Push)"]
    ModeChoice -->|"Route events from AWS/SaaS based on JSON rules"| EB["Amazon EventBridge (Router)"]
    ModeChoice -->|"Coordinate multi-step saga workflow with retries"| Step["AWS Step Functions (Choreography)"]
    ModeChoice -->|"Legacy enterprise broker protocols (JMS, AMQP)"| MQ["Amazon MQ (Broker)"]
```

| Service | Protocol / Pattern | Delivery Model | Primary Exam Trigger |
| :--- | :--- | :--- | :--- |
| **[[Amazon_SQS]]** | Queuing (point-to-point) | **Pull-based** (consumers poll queue) | *"Decouple components and absorb traffic spikes without message loss."* |
| **[[Amazon_SNS]]** | Pub/Sub Topic | **Push-based** (immediate fan-out) | *"Send a single message to multiple subscribers (email, SMS, SQS) at once."* |
| **[[Amazon_EventBridge]]** | Serverless Event Bus | **Content-based routing** | *"React to AWS service state changes or third-party SaaS events (Shopify, Zendesk)."* |
| **[[AWS_Step_Functions]]** | State Machine Workflow | **Visual coordination** | *"Coordinate multiple Lambda functions and human approvals into a multi-step workflow."* |
| **[[Amazon_MQ]]** | Open-source Broker (ActiveMQ/RabbitMQ) | Traditional broker protocols | *"Migrate existing enterprise messaging using JMS, AMQP, MQTT without rewriting code."* |

---

## 3. Atomic Notes in this Domain

| Atomic Note | Description | Key Focus / Keywords |
| :--- | :--- | :--- |
| **[[Amazon_SQS]]** | Distributed Message Queuing | Standard vs. FIFO, Visibility Timeout, Long Polling, Dead-Letter Queues (DLQ). |
| **[[Amazon_SNS]]** | Pub/Sub Notification Service | Topics, Fan-out pattern, SMS, Mobile Push, Email, Subscription filter policies. |
| **[[Amazon_EventBridge]]** | Serverless Event Bus | Default, Custom, and Partner Event Buses, declarative JSON pattern filtering. |
| **[[AWS_Step_Functions]]** | Serverless Workflow Orchestrator | State machines, Amazon States Language (ASL), error handling, sagas. |
| **[[Amazon_MQ]]** | Managed Message Broker | Apache ActiveMQ, RabbitMQ, legacy protocol migration (JMS, AMQP). |
---

## 7. Post-Topic Question Simulation & Retention Check

Test your understanding of Application Integration & DevOps with these 5 exam-style questions:

### Question 1
**Which messaging service provides a fully managed, scalable message queuing service that allows asynchronous decoupling of distributed microservices?**
- A) Amazon SNS
- B) Amazon SQS
- C) Amazon EventBridge
- D) AWS Step Functions

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) Amazon SQS**  
- **Why it's correct:** Amazon Simple Queue Service (SQS) is a pull-based message queuing service that decouples producers from consumers, buffering messages until downstream worker nodes process them.
</details>

### Question 2
**What is the primary difference between Amazon SQS and Amazon SNS?**
- A) SQS uses a publish/subscribe (push) model; SNS uses a message queue (pull) model.
- B) SQS is a message queue where consumers pull messages; SNS is a pub/sub messaging service that pushes messages simultaneously to multiple subscribers.
- C) SQS only supports email notifications; SNS supports video streaming.
- D) SQS requires physical server management; SNS is serverless.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) SQS is a message queue where consumers pull messages; SNS is a pub/sub messaging service that pushes messages simultaneously to multiple subscribers.**  
- **Why it's correct:** SQS buffers messages for individual consumers (1-to-1 asynchronous queue). SNS fans out messages to multiple subscribers (1-to-many publish/subscribe push to Lambda, SQS, email, SMS, HTTP).
</details>

### Question 3
**Which service allows developers to model, provision, and version AWS infrastructure using declarative JSON or YAML templates as Infrastructure as Code (IaC)?**
- A) AWS Elastic Beanstalk
- B) AWS CloudFormation
- C) AWS CodeDeploy
- D) AWS OpsWorks

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) AWS CloudFormation**  
- **Why it's correct:** AWS CloudFormation lets you treat your infrastructure as code, enabling repeatable, automated provisioning and updating of complete stacks of AWS resources.
</details>

### Question 4
**Which Platform as a Service (PaaS) offering allows developers to upload application code (e.g., Java, Node.js, Python) while AWS automatically handles provisioning, load balancing, scaling, and health monitoring?**
- A) Amazon EC2
- B) AWS Elastic Beanstalk
- C) AWS CodePipeline
- D) AWS Lambda

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) AWS Elastic Beanstalk**  
- **Why it's correct:** Elastic Beanstalk is AWS's PaaS solution for deploying web applications quickly without having to manually architect the underlying EC2, Auto Scaling, and ALB infrastructure.
</details>

### Question 5
**Which service coordinates distributed microservices and serverless workflows into visual state machines, handling branching logic, retries, and timeouts?**
- A) Amazon EventBridge
- B) AWS Step Functions
- C) Amazon SQS
- D) AWS CodeBuild

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) AWS Step Functions**  
- **Why it's correct:** AWS Step Functions is a low-code visual workflow orchestrator that sequences Lambda functions, ECS tasks, and AWS services into resilient state machines.
</details>
