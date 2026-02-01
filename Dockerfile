FROM rasa/rasa:3.6.20-full
WORKDIR /app
COPY . /app

USER root
RUN pip install rasa-sdk supervisor

RUN rasa train
USER 1001

# Copy supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 5005
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]