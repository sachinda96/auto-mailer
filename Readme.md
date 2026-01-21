# CSV Email Sender with Flask

A simple Flask web application that allows users to upload a CSV file and send personalized emails automatically using any SMTP email service (Outlook, Gmail, or custom).

---

## Features
- Upload a CSV file containing email addresses and optional names.
- Enter **email subject** and **body** directly from the web interface.
- Use `{name}` placeholder in the email body for personalization.
- Works with **any SMTP server** (Outlook, Gmail, or custom).
- Configurable via **environment variables** for security.
- Logs errors for failed emails.

---

## Project Structure
```
email_app/
│
├─ app.py             # Main Flask application
├─ config.py          # Email configuration file
├─ templates/
│   └─ index.html     # Web interface template
└─ static/
    └─ style.css      # Optional CSS
```

---

## Prerequisites
- Python 3.7+  
- Pip package manager  

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/email_app.git
cd email_app
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
# Activate the virtual environment
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
> If `requirements.txt` doesn’t exist yet:
```bash
pip install Flask Flask-Mail
pip freeze > requirements.txt
```

---

## Configuration

All email settings are in `config.py`. Sensitive data should be set as **environment variables**:

```bash
# SMTP server and port
export MAIL_SERVER=smtp.office365.com
export MAIL_PORT=587

# TLS/SSL settings
export MAIL_USE_TLS=True
export MAIL_USE_SSL=False

# Your email credentials
export MAIL_USERNAME=your_email@domain.com
export MAIL_PASSWORD=your_app_password
export MAIL_DEFAULT_SENDER=your_email@domain.com
```

> **Tip:** Use **app passwords** for Gmail or Outlook if MFA is enabled.  

---

## CSV File Format

Your CSV file should have the following format:

```
email,name
test1@example.com,John
test2@example.com,Jane
```

- The **first column** is the recipient email (required).  
- The **second column** is the recipient name (optional).  
- You can include `{name}` in the email body for personalization.

---

## Running the Application
```bash
python app.py
```

- Open your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
- Upload your CSV file.  
- Enter email **subject** and **body**.  
- Click **Send Emails**.  

---

## Usage Example

**Email Body Example (with personalization):**
```
Hello {name},

This is a test email sent from our Flask application.

Best regards,
Your Name
```

**Uploaded CSV Example:**
```
email,name
test1@example.com,John
test2@example.com,Jane
```

---

## Error Handling
- Emails that fail to send will be logged in the console.  
- Invalid rows in the CSV will be skipped.  
- For large CSV files, consider using asynchronous sending (Celery or threading).

---

## Supported Email Services
- **Outlook / Office 365**  
  ```
  MAIL_SERVER=smtp.office365.com
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USE_SSL=False
  ```
- **Gmail**  
  ```
  MAIL_SERVER=smtp.gmail.com
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USE_SSL=False
  ```
- **Any SMTP server** – just configure the correct host, port, and credentials.

---

## Security Notes
- **Do not hardcode passwords**; always use environment variables.  
- Use **app passwords** for Gmail/Outlook if MFA is enabled.  
- Limit the number of emails sent per hour to avoid throttling by your provider.

---

## Optional Improvements
- Async sending with Celery for large CSV files.  
- Dashboard to track sent/failed emails in real-time.  
- Email template editor in the web UI.  
- Multiple email account support selectable from the UI.  

---

## L