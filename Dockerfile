FROM rasa/rasa:3.5.0-full
WORKDIR /app
COPY . /app

USER root
RUN pip install rasa-sdk supervisor
RUN pip install aiogram==2.25.2 --force-reinstall  # Now compatible

RUN rasa train
USER 1001

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 5005