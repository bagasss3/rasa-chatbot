#!/usr/bin/env python3
import os
import yaml

# Read env vars
token = os.environ.get('TELEGRAM_ACCESS_TOKEN', '')
verify = os.environ.get('TELEGRAM_VERIFY', '')
domain = os.environ.get('RAILWAY_PUBLIC_DOMAIN') or os.environ.get('RAILWAY_STATIC_URL', '')

# Build webhook URL
webhook = f"https://{domain}/webhooks/telegram/webhook" if domain else ""

# Write credentials
config = {
    'rest': {},
    'telegram': {
        'access_token': token,
        'verify': verify,
        'webhook_url': webhook
    }
}

with open('/app/credentials.yml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

print(f"✅ Credentials written")
print(f"   Token set: {bool(token)}")
print(f"   Webhook: {webhook}")