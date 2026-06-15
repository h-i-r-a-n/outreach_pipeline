# Automated Outreach Pipeline 🚀

A modular, multi-stage backend engineering pipeline designed to automate corporate research, contact enrichment, and targeted email outreach cycles. This system automates competitive company analysis, extracts high-level decision-makers, resolves missing corporate email infrastructure, and handles programmatic delivery.

---

## 🛠️ Architecture & Core Workflow

The system is built as a synchronized, synchronous data pipeline where each stage isolates a distinct processing responsibility:

1. **Stage 1 (Discovery):** Evaluates a target seed domain to trace and extract distinct lookalike competitor organizations using structural market indicators.
2. **Stage 2 (Enrichment - Decision Makers):** Queries corporate structures of identified organizations via the Prospeo endpoint API to extract target profiles (C-Suite/VP level names and associated professional endpoints).
3. **Stage 3 (Validation - Data Sanitization):** Iterates over the raw extracted JSON data layers, unpacking nested data models and filtering out invalid, incomplete, or masked entities.
4. **Stage 4 (Outreach - Dispatcher):** Coordinates with remote transactional mail relay servers (Brevo API/SMTP protocols) to securely format and dispatch structured cold emails to verified targets.

---

## 📦 Project Structure

```text
outreach_pipeline/
├── main.py               # Central execution controller & pipeline orchestrator
├── stage1_ocean.py       # Lookalike discovery implementation
├── stage2_prospeo.py     # Prospeo REST API integration for target profile lookup
├── stage3_eazyreach.py   # Data validation, sanitization, and parsing utilities
├── stage4_brevo.py       # Transactional email relay dispatch mechanics
├── config.example.py     # API endpoint credential configuration template
└── README.md             # Systems documentation

🚀 Installation & Local Deployment
1. Prerequisites
Ensure you have Python 3.8+ installed on your machine.

2. Clone the Repository & Setup Environment
Bash
# Clone this repository
git clone [https://github.com/h-i-r-a-n/outreach_pipeline.git](https://github.com/h-i-r-a-n/outreach_pipeline.git)
cd outreach_pipeline

# Initialize and activate the virtual environment
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
3. Setup Environment Secrets
Rename config.example.py to config.py and supply your actual API tokens and SMTP mail profiles:

Python
PROSPEO_API_KEY = "your_prospeo_api_key_here"

SMTP_SERVER = "smtp.gmail.com" # Or your transactional mail handler URL
SMTP_PORT = 587
SMTP_USER = "your_email@domain.com"
SMTP_PASSWORD = "your_app_specific_password"
4. Execute the System Pipeline
Run the controller file and enter a target seed company domain (e.g., stripe.com) when prompted:

Bash
python main.py

---

### How to push this to your live GitHub repository:
Once you have created the file and pasted the code above, open your PowerShell window and run these three quick commands to update your repository live:

```powershell
git add README.md
git commit -m "Docs: Add structural README documentation"
git push
