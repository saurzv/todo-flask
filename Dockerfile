FROM python:3.10

ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
CMD ["python3", "-m", "flask", "run"]