# README

## install

```sh
git clone <repo_link>
cd datagen
docker build -t datagen .
docker run -d --name datagen_container -p 8000:8000 datagen
```

This will start a FastAPI server running on localhost:8000

## endpoints

- localhost/sql: generates valid SQL statements that create dummy data on SQLfiddle and similar sites

- localhost/json: generates dummy JSON data 

Both endpoints take parameters of a string header 'query_string', which is a pipe (|) separated string including names/dtypes of values.
