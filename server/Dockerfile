FROM python:3.9.7-slim


COPY api.py /home

COPY requirements.txt /home

WORKDIR /home

RUN pip install -r /home/requirements.txt


EXPOSE 8081
CMD ["python", "api.py"]

