# Password Generator

## Prerequisites

- Docker

## Quickstart

1. Build the docker image:
```
docker build -t passgen:latest .
```

2. Run the docker image:
```
docker run -p 8000:8000 passgen:latest
```

3. In your browser enter the page: `http://localhost:8000/` and make sure that it directs you to the default Django page