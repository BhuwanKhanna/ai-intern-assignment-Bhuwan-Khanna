# Research Assistant

An AI-Powered Research Assistant that uses the Gemini API and MCP integration to generate structured and accurate research summaries on user-provided topics. The system fetches real-time contextual information through MCP servers and processes it  using AI. The assistant also supports exporting research reports into .PDF and .TXT formats for documentation and sharing.

## Key Features
*   **AI-Powered Research Generation**: Automated multi-source research synthesis using Gemini AI.
*   **Real Time Context Retrieval**: Live contextual data integration through MCP servers.
*   **Export Support**: Generate downloadable research reports in PDF and TXT formats.
*   **Modern Workspace UI**: High-fidelity and responsive user interface for smooth interaction.
*   **Structured Research Output** : Cleanly formatted summaries with organized sections and insights.

## Tech Stack
Python
FastAPI
Gemini API
MCP (Model Context Protocol)
HTML, CSS, JavaScript

## Prerequisites
*   Python 3.10 or higher
*   Google Gemini API Key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/research-assistant.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. Configure environment variables:
   *   Create a `.env` file in the root directory.
   *   Add your API key: `GEMINI_API_KEY=your_actual_key_here`

## Running the Application

1. Start the backend server:
   ```bash
   python -m uvicorn backend.main:app --reload
   ```

2. Launch the interface:
   *   Open `frontend/index.html` in any modern web browser.

## Project Structure
*   `backend/`: API server, research agent logic, and MCP tools.
*   `frontend/`: Institutional user interface assets (HTML, CSS, JS).
*   `research_exports/`: Local directory for saved research reports.
