import requests
import json

def analyze_job(message):
    prompt = f"""
You are JobShield AI, a job scam risk analyzer.

Analyze this job message:

{message}

Look for:
- Payment or registration fees
- Requests for deposits
- WhatsApp/Telegram-only communication
- Suspicious email addresses
- Unrealistic salary promises
- Urgent or threatening language
- Requests for OTP, password or sensitive information
- Missing company information
- Suspicious recruitment claims

Return ONLY valid JSON in this exact format:

{{
    "risk_score": 0,
    "risk_level": "LOW",
    "red_flags": [],
    "explanation": "",
    "recommendation": ""
}}

Rules:
- risk_score must be between 0 and 100.
- LOW = 0-25
- MODERATE = 26-50
- HIGH = 51-75
- CRITICAL = 76-100
- red_flags must be a list.
- Do not add Markdown.
- Do not add text outside the JSON.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
            json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
            "format": "json"
            }
    )

    result = response.json()

    return json.loads(result["response"])