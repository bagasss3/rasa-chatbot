FROM rasa/rasa:3.5.0

WORKDIR /app
COPY . /app

USER root

# Install dependencies
RUN pip install --no-cache-dir rasa-sdk aiogram==2.25.2

# Make start script executable
RUN chmod +x /app/start.sh

# Train model (this happens at build time, not runtime)
RUN rasa train

# Cleanup to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER 1001

EXPOSE 5005