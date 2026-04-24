# AI-INTERN-ASSIGNMENT-BHUWAN-KHANNA

This project is a Python-based AI assistant that takes a user’s question as input, sends it to the Google Gemini API, and prints the response in the console.
In addition to the required terminal script, a simple Streamlit web interface is also included as an optional extension.

## Features
- Command-line interface for quick interaction
- Integration with Google Gemini (gemini-1.5-flash)
- Optional Streamlit-based web interface
- Environment-based API key configuration

## Project Structure
- `main.py`: The core terminal-based query script.
- `app.py`: Optional Streamlit UI.
- `requirements.txt`: Project dependencies.
- `env_example.txt`: Template for API configuration.

## Setup Instructions

### 1. Prerequisites
- Python 3.9+
- A Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Configuration
1. Create a `.env` file in the root directory.
2. Copy the contents of `env_example.txt` into `.env`.
3. Add your API key:
   ```env
   Create a .env file in the root directory and add:

GOOGLE_API_KEY=your_api_key_here
   ```

## How to Run

### Option A: Terminal Script (main.py)
Run the classic terminal interface:
```bash
python main.py
```

### Option B: Web Interface (app.py)
Run the  web dashboard:
```bash
python -m streamlit run app.py
```

## Why Gemini?
The Gemini API was chosen because it offers a generous free tier, fast response times with the Flash model, and an easy-to-use Python SDK, making it well-suited for lightweight AI applications.
