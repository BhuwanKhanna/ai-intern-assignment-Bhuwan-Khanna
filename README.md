# Gemini Apex AI Suite

A dual-interface AI assistant powered by Google's Gemini LLM. This project includes both a robust command-line tool and a premium web-based chat interface.

## Features
- **Terminal Interface**: Fast, efficient command-line interaction.
- **Web Interface**: A premium "Glassmorphism" styled dashboard with chat history.
- **Modern LLM**: Powered by the high-speed `gemini-flash-latest` model.
- **Secure Config**: Environment-based API key management.

## Project Structure
- `main.py`: The core terminal-based query script.
- `app.py`: The premium Streamlit web interface.
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
   GEMINI_API_KEY=your_key_here
   ```

## How to Run

### Option A: Terminal Script (main.py)
Run the classic terminal interface:
```bash
python main.py
```

### Option B: Web Interface (app.py)
Run the premium web dashboard:
```bash
python -m streamlit run app.py
```

## Why Gemini?
We chose the Gemini API for its exceptional speed, high rate limits on the free tier, and the state-of-the-art reasoning capabilities of the Flash models.
