#!/usr/bin/env python3
"""
Script to setup credentials.yml with environment variables
Run this before starting Rasa server
"""

import os
import yaml

def setup_credentials():
    """Setup credentials.yml with environment variables"""
    
    # Get environment variables
    telegram_token = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
    telegram_verify = os.getenv('TELEGRAM_VERIFY', 'STROBO17_bot')
    
    # Railway provides RAILWAY_PUBLIC_DOMAIN or you can use custom domain
    railway_domain = os.getenv('RAILWAY_PUBLIC_DOMAIN') or os.getenv('RAILWAY_STATIC_URL')
    
    # Twilio credentials
    twilio_sid = os.getenv('TWILIO_ACCOUNT_SID', '')
    twilio_token = os.getenv('TWILIO_AUTH_TOKEN', '')
    twilio_number = os.getenv('TWILIO_NUMBER', 'whatsapp:+14155238886')
    
    # Construct webhook URLs
    if railway_domain:
        # Remove https:// if present
        domain = railway_domain.replace('https://', '').replace('http://', '')
        telegram_webhook = f"https://{domain}/webhooks/telegram/webhook"
    else:
        telegram_webhook = os.getenv('TELEGRAM_WEBHOOK_URL', 'http://localhost:5005/webhooks/telegram/webhook')
    
    # Create credentials configuration
    credentials = {
        'rest': {},
        'telegram': {
            'access_token': telegram_token,
            'verify': telegram_verify,
            'webhook_url': telegram_webhook
        },
        'twilio': {
            'account_sid': twilio_sid,
            'auth_token': twilio_token,
            'twilio_number': twilio_number
        },
        'rasa': {
            'url': os.getenv('RASA_URL', 'http://localhost:5002/api')
        }
    }
    
    # Write to credentials.yml
    with open('credentials.yml', 'w') as f:
        yaml.dump(credentials, f, default_flow_style=False)
    
    print("✅ credentials.yml configured successfully!")
    print(f"   Telegram webhook: {telegram_webhook}")
    print(f"   Railway domain: {railway_domain or 'Not detected (using localhost)'}")

if __name__ == '__main__':
    setup_credentials()