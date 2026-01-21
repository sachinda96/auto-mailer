import os

# Default email configuration
EMAIL_CONFIG = {
    "MAIL_SERVER": os.environ.get("MAIL_SERVER", "smtp.office365.com"),
    "MAIL_PORT": int(os.environ.get("MAIL_PORT", 587)),
    "MAIL_USE_TLS": os.environ.get("MAIL_USE_TLS", "True") == "True",
    "MAIL_USE_SSL": os.environ.get("MAIL_USE_SSL", "False") == "True",
    "MAIL_USERNAME": os.environ.get("MAIL_USERNAME", "your_email@example.com"),
    "MAIL_PASSWORD": os.environ.get("MAIL_PASSWORD", "your_email_password"),
    "MAIL_DEFAULT_SENDER": os.environ.get("MAIL_DEFAULT_SENDER", "your_email@example.com")
}
