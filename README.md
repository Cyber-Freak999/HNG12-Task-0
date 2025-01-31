# HNG12 Stage 0 Backend - Public API

## Description

This is a simple public API built with FastAPI that returns:

- Registered email
- Current datetime in ISO 8601 format (UTC)
- GitHub repository URL

## Technology Stack

- **Programming Language:** Python
- **Framework:** FastAPI
- **Deployment:** Publicly accessible endpoint
- **CORS Handling:** Configured to allow cross-origin requests
- **Version Control:** Hosted on GitHub

## Installation & Setup

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Steps to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/Cyber-Freak999/HNG12-Task-0
   cd HNG12-Task-0
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
   ```
5. The API will be accessible at:
   ```
   http://127.0.0.1:8000/
   ```

## API Documentation

### Endpoint

#### **GET /**

Returns a JSON response with the following structure:

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Hire Python Developers

Looking for Python developers? Check out: [HNG Hire Python Developers](https://hng.tech/hire/python-developers)

