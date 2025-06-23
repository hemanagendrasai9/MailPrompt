# CloudPilot

[Demo](#) | ![MIT](https://img.shields.io/badge/License-MIT-green.svg) | Tech: GPT-4 | LangChain | Streamlit | AWS (Mock)

---

## Overview

**CloudPilot** is an AI-powered DevOps assistant that enables users to manage and simulate cloud infrastructure via natural language. By interpreting commands like “Deploy a web server in Mumbai with Python and Nginx,” CloudPilot generates safe execution plans, evaluates potential risks, and simulates cloud actions.

Built using **LangChain**, **GPT-4**, and mocked **AWS SDK**, CloudPilot showcases how AI agents can replace traditional IaC (Infrastructure as Code) with conversational workflows.

---

## Features

- 💬 Natural language to infrastructure translation
- 🔐 Risk evaluation for sensitive/destructive ops
- ⚙️ Agent routing and tool execution via LangChain
- 🧪 boto3-mocked simulation (no real billing)
- 🌐 Streamlit frontend for easy testing

---

## Tech Stack

- GPT-4 via LangChain
- Python + Streamlit
- Simulated AWS SDK via boto3/moto
- JSON output for infrastructure plans and logs

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/CloudPilot.git
cd CloudPilot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run streamlit_app.py
```

> ⚠️ No real AWS access is needed. All API calls are mocked using `moto`.

---

## 🧠 Architecture

```
User Prompt → LangChain Agent → Tool: Simulated AWS Action → JSON Plan + Logs → UI
```

📦 Tools: LangChain Agent | Simulated AWS Tool (boto3-mock)  
🎯 Output: Infra Plan, Execution Result, Cost Estimate (Mocked)


---

## 💡 Use Cases

- Quickly prototype cloud infra using English
- Train junior DevOps engineers on safe infra practices
- Demo LLM-based agent tool chaining

---

## 🛣️ Roadmap

- [ ] Real AWS support via access keys
- [ ] Cost estimator using AWS Pricing API
- [ ] Chat interface with memory (LangGraph)
- [ ] Terraform plan generation

---

## 🧪 Sample Prompts

- “Create an EC2 instance in us-east-1 with Python and nginx”
- “Destroy the server in ap-south-1” ⚠️
- “List all storage buckets and show usage stats”

---

## 🙏 Acknowledgements

Inspired by:
- LangChain Agents + Tools Architecture
- AWS Boto3 SDK
- Streamlit for rapid prototyping
