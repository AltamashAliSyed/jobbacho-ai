🛡️ JobBacho AI
AI-Powered Job Scam Detector
JobBacho AI is a Django-based web application that helps job seekers identify potentially fraudulent job offers before they apply, make payments, or share sensitive information.

Users can paste a job offer received through platforms such as Email, WhatsApp, Telegram, SMS, or LinkedIn. The application analyzes the message using an AI model and provides a risk assessment.

🚀 Features
Analyze job offers using AI
Risk score from 0–100
Risk levels: LOW, MODERATE, HIGH, and CRITICAL
Detect common job-scam red flags
AI-generated explanation
Safety recommendation for the user
Simple beginner-friendly web interface
🛠️ Technologies Used
Python
Django
HTML
CSS
Ollama
Llama 3.2
REST API
⚙️ How It Works
User
  ↓
Paste Job Offer
  ↓
Django Application
  ↓
Ollama API
  ↓
Llama 3.2
  ↓
Risk Analysis
  ↓
Risk Score + Red Flags + Recommendation
📂 Project Structure
jobbacho-ai/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── jobbacho/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── detector/
    ├── views.py
    ├── urls.py
    ├── ollama.py
    │
    └── templates/
        └── detector/
            └── home.html
▶️ Run Locally
Install the required packages:

pip install -r requirements.txt
Make sure Ollama is installed and the required model is available:

ollama pull llama3.2
Start Ollama and then run Django:

python manage.py runserver
Open:

http://127.0.0.1:8000/
⚠️ Disclaimer
JobBacho AI provides an AI-based risk assessment and should not be treated as a definitive determination that a job offer is fraudulent. Users should independently verify companies and recruitment offers before sharing personal information or making payments.

👨‍💻 Project
Built as a practical AI + Django project focused on helping job seekers identify potential job scams.
