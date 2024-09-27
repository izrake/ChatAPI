# Qwen Coder API

This project provides a FastAPI-based API for the Qwen2.5-Coder-7B-Instruct model from Hugging Face. It allows users to interact with the model through a simple HTTP interface.

## Features

- FastAPI-based RESTful API
- Integration with Qwen2.5-Coder-7B-Instruct model
- Docker support for easy deployment
- Asynchronous request handling
- Customizable system prompts

## Prerequisites

- Python 3.9+
- Docker (optional, for containerized deployment)

## Setup

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/your-username/qwen-coder-api.git
   cd qwen-coder-api
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`.

### Docker Deployment

1. Build the Docker image:
   ```
   docker build -t qwen-coder-api .
   ```

2. Run the Docker container:
   ```
   docker run -p 8000:8000 qwen-coder-api
   ```

Alternatively, use Docker Compose:

```
docker-compose up --build
```

## Usage

Send a POST request to the `/chat` endpoint with a JSON payload:

```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
           "message": "Write a Python function to calculate the factorial of a number.",
           "system_prompt": "You are an expert Python programmer. Provide clear and efficient code."
         }'
```

### API Endpoints

- `POST /chat`: Send a message to the model and receive a response.

  Request body:
  ```json
  {
    "message": "Your message here",
    "system_prompt": "Optional system prompt"
  }
  ```
