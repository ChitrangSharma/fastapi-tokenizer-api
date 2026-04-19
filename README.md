# Tokenizer API (FastAPI + tiktoken)

This is a simple API built using FastAPI that allows users to:

* Encode text into tokens
* Decode tokens back into text
* Select different OpenAI models

## Tech Stack

* Python
* FastAPI
* tiktoken

## Endpoints

### POST /encode

Request:
{
"text": "hello world",
"model": "gpt-4o"
}

Response:
{
"tokens": [15339, 1917]
}

### POST /decode

Request:
{
"tokens": [15339, 1917],
"model": "gpt-4o"
}

Response:
{
"text": "hello world"
}

## Run Locally

pip install -r requirements.txt
uvicorn app:app --reload

## Future Improvements

* Add caching for encoders
