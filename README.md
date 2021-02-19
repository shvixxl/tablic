# Tablic

 Web Application.

- [Requirements](#requirements)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Using this Project](#using-this-project)
  - [Configuration](#configuration)
  - [Development](#development)
- [License](#license)

## Requirements

### Backend

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

### Frontend

## Using this Project

### Configuration

Create a copy of `.env.example` file and rename it to `.env`:

```bash
cp .env.example .env
```

Open `.env` file and set these enviroment variables:

* `DB_PASSWORD` - mongodb password.
* `SECRET_KEY` - backend server secret key.

### Development

Start the stack with `docker-compose`:

```bash
docker-compose up -d
```

**Available urls**:

* *API*: http://localhost:8000/api/

* *Interactive documentation* (Swagger UI): http://localhost:8000/docs

* *Alternative documentation* (ReDoc): http://localhost:8000/redoc

To check the logs, run:

```bash
docker-compose logs
```

To check the logs of a specific service, add the name of the service, e.g.:

```bash
docker-compose logs backend
```

## License
[MIT](https://github.com/ShviXXL/tablic/blob/main/LICENSE)