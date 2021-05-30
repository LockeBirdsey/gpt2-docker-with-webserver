FROM tensorflow/tensorflow:1.15.2-gpu-py3
ENV LANG=C.UTF-8
ARG GPT2_MODEL_NAME=124M
ENV GPT2_MODEL_NAME=$GPT2_MODEL_NAME
ARG UPLOAD_FOLDER=upload
ENV UPLOAD_FOLDER=$UPLOAD_FOLDER

RUN apt-get update
ADD "https://api.github.com/repos/LockeBirdsey/gpt2-docker-with-webserver/commits?per_page=1" latest_commit
RUN curl -sLO "https://github.com/LockeBirdsey/gpt2-docker-with-webserver/archive/refs/heads/master.zip" && unzip master.zip

WORKDIR gpt2-docker-with-webserver-master
RUN chmod +x entrypoint.sh
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
#TODO: Should we download basic 124M model on build?
RUN python startup.py

#Get the things running
ENTRYPOINT ["/gpt2-docker-with-webserver-master/entrypoint.sh"]
CMD ["run"]
#CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "server:app"]