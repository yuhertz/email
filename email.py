import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        # Create a secure connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to your email account
        server.login(sender_email, sender_password)

        # Compose the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

        # Close the connection to the SMTP server
        server.quit()
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

# Set your email credentials and the email details
sender_email = input("Enter your email: ")
sender_password = input("Enter your password: ")
recipient_email = input("Enter target email: ")
subject = input("Enter title name of email: ")
message = input("Enter your message: ")

# Call the function to send the email
send_email(sender_email, sender_password, recipient_email, subject, message)
