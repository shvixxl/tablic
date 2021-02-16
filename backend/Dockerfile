# Build

FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "/usr/src/app/scripts/entrypoint.sh" ]