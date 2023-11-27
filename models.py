from pydantic import BaseModel

class SubmitRequest(BaseModel):
    url: str

class SubmitResponse(BaseModel):
    title: str
    thumbnail_url: str
    author: str
    text: str

