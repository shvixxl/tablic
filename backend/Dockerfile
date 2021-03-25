FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip && pip install pipenv

COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile

ARG INSTALL_DEV=false
RUN bash -c "if [[ $INSTALL_DEV == 'true' ]] ; then \
                pipenv install --system --dev --ignore-pipfile ; else \
                pipenv install --system --deploy --ignore-pipfile ; fi"

RUN pip uninstall pipenv -y && apt-get autoremove -y

COPY . .

EXPOSE 8000

ENTRYPOINT [ "/app/scripts/entrypoint.sh" ]