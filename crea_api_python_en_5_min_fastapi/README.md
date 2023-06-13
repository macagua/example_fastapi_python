# Crea una API con Python en menos de 5 minutos (Fast API)

- Tutorial "[Crea una API con Python en menos de 5 minutos con FastAPI](https://www.youtube.com/watch?v=J0y2tjBz2Ao)"
  from [Garaje de ideas](https://www.youtube.com/@Garajedeideas).

## Install

Install System dependencies, executing the following command:

```
apt install -y curl
```

Install Python dependencies, executing the following command:

```
pip install -r requirements.txt
```

## Run it

Run the app using ``uvicorn``, executing the following command:

```
uvicorn main:app --reload
```

Then for use it,  Uvicorn running on <http://127.0.0.1:8000> (Press ``CTRL+C`` to quit).
Also you can access to the API documentation on <http://127.0.0.1:8000/docs>.

This example have two ``GET`` routes:

- ``/``
  For test this route opening the following URL <http://127.0.0.1:8000/>.

- ``/books/{id}``.
  For test this route opening the following URL <http://127.0.0.1:8000/books/1>.

This example have one ``POST`` route:

- ``/books``
  For test this route, make a request with ``curl`` tool, executing the following command:

  ```
  curl -X 'POST' \
    'http://127.0.0.1:8000/books' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "title": "Caballo de Troya 1: Jerusalen",
    "author": "J. J. Benítez",
    "pages": 736,
    "editorial": "Planeta"
  }'
  ```

  The Response body return the following message:

  ```
  {
    "message": "The 'Caballero de Troya 1' book was saved!"
  }'
  ```
