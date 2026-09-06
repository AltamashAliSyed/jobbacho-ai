import requests
import json
import os


def analyze_job(message):

    prompt = f"""
You are JobBacho AI, a job scam risk analyzer.

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

    api_key = os.environ.get("OLLAMA_API_KEY")

    if not api_key:
        raise Exception("OLLAMA_API_KEY is not configured")

    response = requests.post(
        "https://ollama.com/api/generate",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-oss:120b",
            "prompt": prompt,
            "stream": False,
            "format": "json"
        },
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return json.loads(result["response"])