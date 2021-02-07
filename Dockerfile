FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile* ./
RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r ./requirements.txt

COPY . .

RUN pip install --no-cache .

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]