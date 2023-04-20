FROM python:3.10.6-alpine3.16

ARG WORKING_DIRECTORY=/var/tgbot
ARG TGBOT_KEY
ARG GPT_KEY

ENV TGBOT_KEY=$TGBOT_KEY
ENV GPT_KEY=$GPT_KEY

WORKDIR ${WORKING_DIRECTORY}

COPY main.py requirements.txt ${WORKING_DIRECTORY}

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]