from langchain.llms import OpenAI
llm = OpenAI()

def classify_email(email):
    prompt = f"""Classify and reply:

Subject: \{email['subject']\}
Body: \{email['body']\}

Give:
1. Priority (High/Medium/Low)
2. Action (Reply/Delete/Ignore)
3. Suggested Reply
"""
    return llm(prompt)
}
