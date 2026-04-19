from fastapi import FastAPI
import tiktoken
from enum import Enum
from pydantic import BaseModel
app = FastAPI()

class ModelName(str, Enum):
    gpt4o = "gpt-4o"
    gpt4 = "gpt-4"
    gpt3point5 = "gpt-3.5-turbo"

class EncodeRequest(BaseModel):
    text: str
    model: ModelName

class DecodeRequest(BaseModel):
    tokens: list[int]
    model: ModelName

@app.get("/healthcheck")
def health_check():
    return "OK"

@app.post("/encode")
def encode(request: EncodeRequest):
    encoder = tiktoken.encoding_for_model(request.model.value)
    tokens = encoder.encode(request.text)
    return {"tokens":tokens}

@app.post("/decode")
def decode(request: DecodeRequest):
    encoder = tiktoken.encoding_for_model(request.model.value)
    decoded_text = encoder.decode(request.tokens)
    return {"text": decoded_text}
