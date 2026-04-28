from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.core.config import settings


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_TLS=True,
    MAIL_SSL=False,
)


async def send_reset_email(email: str, token: str):

    reset_link = f"http://localhost:8000/reset-password?token={token}"

    message = MessageSchema(
        subject="Password Reset",
        recipients=[email],
        body=f"Click the link to reset your password:\n{reset_link}",
        subtype="plain",
    )

    fm = FastMail(conf)
    await fm.send_message(message)