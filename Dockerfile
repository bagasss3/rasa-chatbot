FROM rasa/rasa:3.6.20-full
WORKDIR /app
COPY . /app

USER root
RUN pip install rasa-sdk supervisor

# Copy supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

USER 1001
EXPOSE 5005 5055

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]