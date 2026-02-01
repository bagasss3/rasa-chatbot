# Dockerfile for Rasa Chatbot

FROM rasa/rasa:3.6.20-full

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
USER root
RUN pip install rasa-sdk pyyaml

# Make setup script executable
RUN chmod +x setup_credentials.py

# Expose ports
EXPOSE 5005 5055

# Switch back to rasa user
USER 1001

# Run setup script then start Rasa
# This will configure credentials.yml with environment variables
CMD python3 setup_credentials.py && \
    rasa run --enable-api --cors "*" --port 5005