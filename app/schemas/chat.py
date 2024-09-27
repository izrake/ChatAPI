from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    system_prompt: str = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."

class ChatResponse(BaseModel):
    response: str