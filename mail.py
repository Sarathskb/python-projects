import qrcode
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Get user input for name, phone, and email
name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")

# Combine the input data into a single string (or format it as needed)
data = f"Name: {name}\nPhone: {phone}\nEmail: {email}"

# Generate a QR code with the user's data
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
qr_image.save("user_info_qr.png")

# Email configuration
sender_email = '21sarathkumar2000@gmail.com'
sender_password = 'sptx samj gqee vywv'
receiver_email = email  # Use the provided email as the recipient
subject = 'QR Code Email'

# Create a MIMEText object for the email content
email_message = MIMEMultipart()
email_message['From'] = sender_email
email_message['To'] = receiver_email
email_message['Subject'] = subject

# Attach the email body
message = MIMEText("Please find the attached QR code.")
email_message.attach(message)

# Attach the QR code image
with open("user_info_qr.png", "rb") as qr_file:
    qr_image_data = MIMEImage(qr_file.read(), name="user_info_qr.png")
email_message.attach(qr_image_data)

# Establish an SMTP connection and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, email_message.as_string())

    print(f"Email with QR code sent successfully to {receiver_email}!")

except Exception as e:
    print("Error sending email:", str(e))

finally:
    # Close the SMTP server connection
    server.quit()
