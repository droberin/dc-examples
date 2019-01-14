FROM python:3-slim

LABEL maintainer rsalgado@gradiant.org

COPY flask_test/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY flask_test/entrypoint.py entrypoint.py

ENTRYPOINT /usr/local/bin/python3 entrypoint.py
