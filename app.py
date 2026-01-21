from flask import Flask, render_template, request
from flask_mail import Mail, Message
import csv
from config import EMAIL_CONFIG

app = Flask(__name__)

# Load configuration from config.py
app.config.update(EMAIL_CONFIG)

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form.get('subject')
        body_template = request.form.get('body')
        file = request.files.get('csv_file')

        if not file:
            return "No file uploaded", 400

        csv_file = csv.reader(file.stream)
        next(csv_file, None)  # Skip header

        sent_count = 0
        for row in csv_file:
            if len(row) < 1:
                continue
            email = row[0]
            name = row[1] if len(row) > 1 else ""
            body = body_template.replace("{name}", name)

            try:
                msg = Message(subject=subject, recipients=[email], body=body)
                mail.send(msg)
                sent_count += 1
            except Exception as e:
                print(f"Error sending to {email}: {e}")

        return f"Emails sent successfully: {sent_count}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
