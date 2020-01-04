FROM python:3

ENV PYTHONPATH=/app:.

COPY . /app
WORKDIR /app/src
RUN pip install -r ../requirements.txt

EXPOSE 5000

CMD python ./pythonflask/flaskAppMain.py

