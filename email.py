import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password):
    # Create a MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS for security
        server.login(sender_email, sender_password)  # Log in to the server

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

    print("Email sent successfully.")

# Replace these variables with your own values
subject = "Test Email"
body = "This is the second test email sent from Python."
to_email = "auto.update.consultancycomissie@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "auto.update.consultancycomissie@gmail.com"
sender_password = "Vbnimplementatie"

# Call the function to send the email
send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password)