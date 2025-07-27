# This file is part of the Inventory Management System project.
# It is responsible for sending email alerts when stock levels are low.
# It uses environment variables for SMTP configuration and sends alerts
# when the reorder quantity exceeds a specified threshold.

import logging
import os
import smtplib
from email.message import EmailMessage

logger = logging.getLogger(__name__)


def send_alerts(df, threshold=0):
    low = df[df["ReorderQty"] > threshold]
    if low.empty:
        logger.info("No low-stock items to alert")
        return

    logger.info(f"Found {len(low)} items needing restock")
    smtp = os.getenv("SMTP_SERVER")
    port = int(os.getenv("SMTP_PORT", 25))
    sender = os.getenv("EMAIL_FROM")
    recipient = os.getenv("EMAIL_TO")

    if not smtp or not sender or not recipient:
        logger.error("SMTP configuration is incomplete")
        return

    msg = EmailMessage()
    msg["Subject"] = "⚠️ Low Stock Alert"
    msg["From"] = sender
    msg["To"] = recipient
    body = low.to_json(orient="records", indent=2)
    msg.set_content(f"Items needing restock:\n\n{body}")

    with smtplib.SMTP(smtp, port) as s:
        s.send_message(msg)
    logger.info(f"Sent low-stock alert for {len(low)} items")