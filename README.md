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

## Testing the password generator

1. Default test via browser:

- Go to: `http://localhost:8000/password/generate/`
- You should see a generated password returned.
- You may also add query parameters:
    - `http://localhost:8000/password/generate/?length=20`
    - `http://localhost:8000/password/generate/?symbols=true`
    - `http://localhost:8000/password/generate/?numbers=true`
    - `http://localhost:8000/password/generate/?length=15&symbols=true&numbers=true`

2. Test via CURL:

   - `curl "http://localhost:8000/password/generate/?length=20"`
   - `curl "http://localhost:8000/password/generate/?symbols=true"`
   - `curl "http://localhost:8000/password/generate/?numbers=true"`
   - `curl "http://localhost:8000/password/generate/?length=15&symbols=true&numbers=true"`
