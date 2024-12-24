from flask import Flask, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

app = Flask(__name__)

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "khrushil08@gmail.com"  # Replace with your Gmail address
EMAIL_PASSWORD = "notq cndd alhu yigt"  # Replace with your App Password
TO_EMAIL = "tech@themedius.ai"
CC_EMAIL = "hr@themedius.ai"
SUBJECT = "Python (Selenium) Assignment - Rushil Khanna"

# File paths (replace with your actual file paths)
files_to_send = [
    r"C:\Users\wihh\Desktop\selenium project\form_submission_confirmation.png",  # Screenshot of the form
    r"C:\Users\wihh\Desktop\selenium project\selenium project.rar",  # Source code GitHub repo link as a file or zip
    r"C:\Users\wihh\Desktop\selenium project\Documentation.docx",  # Documentation of your approach
    r"C:\Users\wihh\Desktop\CV\Rushil_Khanna_CV.pdf",  # Your resume file
    r"C:\Users\wihh\Desktop\selenium project\links.txt",  # Links to past projects/work samples
    r"C:\Users\wihh\Desktop\selenium project\availbility.txt"  # Confirmation of availability
]

@app.route('/')
def home():
    return "Flask app is working!"

@app.route('/send-email', methods=['GET'])
def send_email():
    try:
        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = TO_EMAIL
        msg['Cc'] = CC_EMAIL
        msg['Subject'] = SUBJECT

        # Email body
        body = """Dear Team,

        Please find the following attached as part of my Python Selenium assignment submission:

        1. Screenshot of the form filled via code.
        2. Source code (GitHub repository link).
        3. Brief documentation of my approach.
        4. My resume.
        5. Links to past projects/work samples.
        6. Confirmation of availability to work full time (10 am to 7 pm) for the next 3-6 months.

        Regards,
        Rushil Khanna
        """
        msg.attach(MIMEText(body, 'plain'))

        # Attach files
        for file_path in files_to_send:
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(file_path)}")
                msg.attach(part)

        # SMTP server connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Start TLS encryption
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        # Send email
        recipients = [TO_EMAIL] + [CC_EMAIL]
        server.sendmail(EMAIL_USER, recipients, msg.as_string())
        server.quit()

        return jsonify({"message": "Email sent successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
