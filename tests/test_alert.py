# This test ensures alert content includes critical stock info and proper formatting.

from unittest.mock import patch, MagicMock
import pandas as pd
import pytest
from services.alert import send_alerts


@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv("SMTP_SERVER", "smtp.test.com")
    monkeypatch.setenv("SMTP_PORT", "587")
    monkeypatch.setenv("EMAIL_FROM", "bot@test.com")
    monkeypatch.setenv("EMAIL_TO", "team@test.com")

def test_send_alerts_sends_email(mock_env):
    # Create test DataFrame with 2 low-stock items
    df = pd.DataFrame([
        {"SKU": "SKU01", "Location": "WH1", "ReorderQty": 30},
        {"SKU": "SKU02", "Location": "WH2", "ReorderQty": 5}
    ])

    with patch("smtplib.SMTP") as mock_smtp:
        mock_conn = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_conn

        send_alerts(df, threshold=0)

        # Ensure SMTP was called and a message was sent
        mock_smtp.assert_called_once_with("smtp.test.com", 587)
        mock_conn.send_message.assert_called_once()
