Research Assistant

An AI-powered Research Assistant that leverages the Gemini API along with Model Context Protocol (MCP) integration to generate structured, context-aware, and accurate research summaries on user-defined topics.

The system retrieves real-time contextual information through MCP servers and processes the data using AI-driven intelligence synthesis powered by Gemini. It also supports exporting generated research reports into .PDF and .TXT formats for documentation, sharing, and archival purposes.

Key Features
AI-Powered Research Generation
Automated multi-source research synthesis using Gemini AI.
Real-Time Context Retrieval
Live contextual data integration through MCP servers.
Export Support
Generate downloadable research reports in PDF and TXT formats.
Modern Workspace UI
High-fidelity and responsive user interface for smooth interaction.
Structured Research Output
Cleanly formatted summaries with organized sections and insights.
Tech Stack
Python
FastAPI
Gemini API
MCP (Model Context Protocol)
HTML, CSS, JavaScript
Prerequisites
Python 3.10 or higher
Google Gemini API Key
Installation
Clone the Repository
git clone https://github.com/your-username/research-assistant.git
Install Dependencies
pip install -r backend/requirements.txt
Configure Environment Variables

Create a .env file in the root directory and add:

GEMINI_API_KEY=your_actual_key_here
Running the Application
Start Backend Server
python -m uvicorn backend.main:app --reload
Launch Frontend

Open:

frontend/index.html

in any web browser.

Project Structure
backend/             # API server, AI agent logic, MCP tools
frontend/            # Frontend UI assets (HTML, CSS, JavaScript)
research_exports/    # Exported PDF and TXT research reports
Future Enhancements
Multi-agent research pipelines
Citation and reference generation
Research visualization dashboards
Cloud deployment support
User authentication and saved workspaces
