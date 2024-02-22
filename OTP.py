import smtplib
import random

class OTPVerification:
    def __init__(self):
        self.otp = None

    def generate_otp(self):
        # Generate a 6-digit random number
        self.otp = str(random.randint(100000, 999999))

    def send_email(self, to_email):
        # Your email credentials and SMTP server details
        email_address = "your_email@gmail.com"
        email_password = "your_email_password"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your email account
        server.login(email_address, email_password)

        # Compose the email message with the OTP
        subject = "OTP Verification"
        body = f"Your OTP is: {self.otp}"
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(email_address, to_email, message)

        # Close the connection to the SMTP server
        server.quit()

    def verify_otp(self, user_input):
        # Verify the entered OTP
        return user_input == self.otp

# Create an instance of OTPVerification
otp_verifier = OTPVerification()

# Step 1: Generate OTP
otp_verifier.generate_otp()

# Step 2: Send OTP via Email
user_email = input("Enter your email address: ")
otp_verifier.send_email(user_email)
print("OTP sent successfully! Check your email.")

# Step 3: Receive and Verify OTP
user_input_otp = input("Enter the OTP received in your email: ")

if otp_verifier.verify_otp(user_input_otp):
    print("OTP verification successful!")
else:
    print("OTP verification failed. Please try again.")

