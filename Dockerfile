FROM rasa/rasa:3.6.20-full
WORKDIR /app
COPY . /app

USER root
RUN pip install rasa-sdk supervisor
RUN pip install aiogram==2.25.2 aiohttp==3.9.5 --force-reinstall

RUN rasa train
USER 1001

# Copy supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 5005
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]