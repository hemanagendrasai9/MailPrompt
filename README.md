
# MailPrompt

[Demo](#) | ![MIT](https://img.shields.io/badge/License-MIT-green.svg) | Tech: GPT-4 | LangChain | Python | JSON

---

## Overview

**MailPrompt** is a local-first AI inbox agent that reads, classifies, and responds to emails using natural language reasoning. It autonomously manages email flow by assigning priority, generating smart replies, and simulating executive assistant-like behavior.

Built using **LangChain**, **GPT-4**, and **Python**, MailPrompt helps busy professionals handle inbox overload with AI.

---

## Features

- ✉️ Classifies emails by priority (High/Medium/Low)
- 🧠 Suggests intelligent replies using LLM context
- 🔄 Maintains thread memory via simulated context
- 🗂️ Outputs reply plans and metadata to `replies.json`
- 📁 Ready for IMAP/SMTP integration or LangGraph upgrade

---

## Tech Stack

- LangChain + OpenAI (GPT-4 or compatible)
- Python
- JSON inbox simulation (via `inbox.json`)
- CLI-based response generation

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/MailPrompt.git
cd MailPrompt
```

### 2. Install dependencies
```bash
pip install langchain openai
```

### 3. Run the agent
```bash
python mail_agent.py
```

> ✅ AI-generated replies will be saved in `replies.json`

---

## 🧠 Architecture

```
Inbox JSON → LangChain LLM Agent → Priority + Suggested Reply → replies.json
```

📨 Input: Email Subject + Body  
🧠 Process: Classification + Intent Recognition + Reply Generation  
📤 Output: Action Plan + Reply Text

---

## 💡 Use Cases

- Auto-manage job application emails
- Prioritize client or vendor conversations
- Generate polite rejections, acceptances, or reschedules

---

## 🛣️ Roadmap

- [ ] Integrate live Gmail inbox (via IMAP)
- [ ] Add calendar sync for scheduling replies
- [ ] Support summarizing entire threads
- [ ] LangGraph autonomous agent upgrade

---

## 🧪 Sample Emails

```json
{
  "subject": "Interview Invitation",
  "body": "We’d love to schedule an interview with you this week. Are you available?"
}
```

---

## 🙏 Acknowledgements

Inspired by:
- LangChain + Agent Tools
- InboxZero workflow models
- GPT-native productivity tooling
