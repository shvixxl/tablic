# Tablic

<p>
  <a href="https://github.com/ShviXXL/tablic/actions/workflows/testing.yml">
    <img src="https://github.com/ShviXXL/tablic/actions/workflows/testing.yml/badge.svg" alt="Testing">
  </a>
  <a href="https://codecov.io/gh/ShviXXL/tablic">
    <img src="https://codecov.io/gh/ShviXXL/tablic/branch/main/graph/badge.svg"/>
  </a>
</p>

 Web Application.

- [Tablic](#tablic)
  - [Requirements](#requirements)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [Using this Project](#using-this-project)
    - [Configuration](#configuration)
      - [Additional Configuration](#additional-configuration)
        - [Logging](#logging)
    - [Development](#development)
      - [Endpoints](#endpoints)
  - [License](#license)

## Requirements

### Backend

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Frontend

## Using this Project

### Configuration

Create a copy of `.env.example` file and rename it to `.env`:

```bash
cp .env.example .env
```

Open `.env` file and set these environment variables:

- `DB_PASSWORD` - mongodb password.
- `SECRET_KEY` - backend server secret key.

#### Additional Configuration

##### Logging

For reference use the [Loguru documentation](https://loguru.readthedocs.io/en/stable/api.html#).

- [`LOGGING_LEVEL`](https://docs.python.org/3/library/logging.html#logging-levels) - The minimum severity level from which logged messages should be sent to the sink. *Default* is `20` or `INFO`.
- `LOGGING_FORMAT` - The template used to format logged messages.
- [`LOGGING_ROTATION`](https://loguru.readthedocs.io/en/stable/api/logger.html#file) - A condition indicating whenever the current logged file should be closed and a new one started. *Default* is `1 day`.
- [`LOGGING_RETENTION`](https://loguru.readthedocs.io/en/stable/api/logger.html#file) - A directive filtering old files that should be removed during rotation or end of program. *Default* is `1 month`.
- [`LOGGING_COMPRESSION`](https://loguru.readthedocs.io/en/stable/api/logger.html#file) - A compression or archive format to which log files should be converted at closure. *Default* is `tar.gz`.

### Development

Start the stack with `docker-compose`:

```bash
docker-compose up -d
```

To check the logs, run:

```bash
docker-compose logs
```

To check the logs of a specific service, add the name of the service, e.g.:

```bash
docker-compose logs backend
```

To bring the stack down, run:

```bash
docker-compose down
```

#### Endpoints

- *Client*: <http://localhost>
- *API*: <http://localhost:8000/api>
- *Interactive documentation* (Swagger UI): <http://localhost:8000/api/docs>
- *Alternative documentation* (ReDoc): <http://localhost:8000/api/redoc>

## License

[MIT](LICENSE)
