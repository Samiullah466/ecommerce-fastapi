# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
# from pydantic import EmailStr

# conf = ConnectionConfig(
#     MAIL_USERNAME="samiullah6890@gmail.com",
#     MAIL_PASSWORD="irqs yowd sbxd rwiw",   # Gmail App Password 
#     MAIL_FROM="samiullah6890@gmail.com",
#     MAIL_PORT=587,
#     MAIL_SERVER="smtp.gmail.com",
#     MAIL_STARTTLS=True,
#     MAIL_SSL_TLS=False,
#     USE_CREDENTIALS=True
# )

# async def send_reset_email(email_to: EmailStr, reset_link: str):
#     subject = "Password Reset - Ecommerce App"
#     body = f"""
#     <h3>Reset Your Password</h3>
#     <p>Click the link below to reset your password:</p>
#     <a href="{reset_link}">{reset_link}</a>
#     <p>This link expires in 15 minutes.</p>
#     """

#     message = MessageSchema(
#         subject=subject,
#         recipients=[email_to],
#         body=body,
#         subtype="html"
#     )

#     fm = FastMail(conf)
#     await fm.send_message(message)
