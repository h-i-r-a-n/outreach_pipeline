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
```
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


```
## 🧠 Detailed Architecture & Data Flow

The system operates on a synchronized, 4-stage data flow orchestrated by a central controller. Below is the detailed functional breakdown of each module within the pipeline:

### Central Controller (`main.py`)
*   **Definition:** The primary execution script that acts as the pipeline's central orchestrator.
*   **Functionality:**
    *   Initiates a **synchronous data flow** across all sub-modules.
    *   Accepts a **seed domain** (e.g., `stripe.com`) via standard terminal input.
    *   Maintains the **state** of the extracted data as it transitions through discovery, enrichment, and verification.
    *   Generates a **CLI summary view** of verified targets and requires explicit **user confirmation** before executing the final email dispatch to prevent accidental spam.

### Stage 1: Competitor Discovery (`stage1_ocean.py`)
*   **Definition:** The initial reconnaissance layer responsible for identifying market competitors based on the seed input.
*   **Functionality:**
    *   Acts as a **targeted seed-matching filter**.
    *   Evaluates the user-provided input domain to trace and extract **lookalike competitor organizations** using structural market indicators.
    *   Returns a structured list of **root domain names** representing high-value B2B targets for the next stage.

### Stage 2: Decision Maker Enrichment (`stage2_prospeo.py`)
*   **Definition:** The core data acquisition module leveraging the **Prospeo REST API** to find targeted personnel.
*   **Functionality:**
    *   Queries the `/search-person` API endpoint using the domains generated in Stage 1.
    *   Extracts specific **C-Suite/VP level profiles** and their associated professional endpoints.
    *   Implements **nested JSON parsing** to securely unpack and extract the core email string out of complex, multi-layered API response objects.
    *   Utilizes **multi-variant key extraction** to accurately identify job titles across inconsistent schema fields (checking for `title`, `job_title`, and `designation`).
    *   Applies an adaptive **2-second rate-limiting delay** between requests to prevent API threshold blocks and ensure stable server connections.

### Stage 3: Data Validation & Sanitization (`stage3_eazyreach.py`)
*   **Definition:** A strict programmatic filtering layer designed to clean, verify, and format the raw JSON data layers.
*   **Functionality:**
    *   Iterates through the enriched target profiles to catch and discard **masked entities** or **unrevealed placeholder responses** (e.g., `UNAVAILABLE`).
    *   Verifies structural compliance by ensuring the presence of mandatory characters, such as the **`@` symbol**, in the extracted email strings.
    *   Guarantees that only **fully resolved and sanitized data models** are passed into the final dispatch queue.

### Stage 4: Outreach Dispatcher (`stage4_brevo.py`)
*   **Definition:** The terminal module responsible for the programmatic delivery of targeted communications.
*   **Functionality:**
    *   Establishes a secure connection with **remote transactional mail relay servers** (utilizing Brevo / standard SMTP protocols).
    *   Authenticates session requests securely using credentials isolated in the local **`config.py`** environment variables.
    *   Parses the sanitized data models to securely format and handle the **final email dispatch** to verified target endpoints.
