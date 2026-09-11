🤖 AI Personal Assistant

An intelligent AI-powered personal assistant built using Python, Streamlit, Generative AI, NLP, and SQLite. The application allows users to interact with an AI assistant, manage tasks, save notes, track progress, and organize daily activities from a single dashboard.

## 🚀 Live Demo

👉 [Open AI Personal Assistant](https://ai-personal-assistant-b48q4bcrpyonm5d8pkuveh.streamlit.app)

📌 Project Overview

The AI Personal Assistant is designed to combine conversational AI with everyday productivity tools.
Instead of being limited to a simple chatbot, the application understands the user's intent and performs different actions accordingly.

For example:

"Add a high priority task to study Python tomorrow"
                ↓
          NLP Intent Detection
                ↓
              TASK
                ↓
      Extract task information
                ↓
        Save task in SQLite

Similarly:

"Save a note that I need to revise SQL"
                ↓
          Intent Detection
                ↓
              NOTE
                ↓
        Extract note content
                ↓
        Save note in SQLite

✨ Features :

🤖 AI Chat
Chat with an AI assistant using a Generative AI/LLM API.
Ask general questions and receive AI-generated responses.
Error handling for failed AI requests.

🧠 NLP & Intent Detection
The application analyzes user messages and identifies their intent.
Supported intents include:

CHAT
TASK
NOTE
LIST_TASKS
LIST_NOTES

Example:

Add a task to study Python
        ↓
TASK
Save a note that I need to revise SQL
        ↓
NOTE
✅ Task Management

Users can:

Add tasks
Set task priority
Set due dates
View tasks
Mark tasks as completed
Delete tasks
Track pending and completed tasks
📝 Notes Management

Users can:

Create notes
View saved notes
Delete notes
Save notes through natural-language commands

📅 Calendar
The application provides a calendar-based interface for organizing and viewing scheduled activities.

📊 Dashboard
The dashboard provides an overview of productivity, including:

Total tasks
Pending tasks
Completed tasks
Total notes
Task completion progress
Recent tasks
🗄️ SQLite Database

The application uses SQLite to persist application data.
Database functionality includes:

Task storage
Note storage
Task status
Priority
Due dates
Creation timestamps

🎨 Streamlit Interface
The project uses Streamlit to provide a clean and interactive web interface without requiring a separate frontend framework.

🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
Generative AI / Gemini API	AI-powered conversations
NLP	Intent detection and information extraction
SQLite	Database management
JSON	Data/configuration handling
python-dotenv	Environment variable management
Git	Version control
GitHub	Source code hosting
🏗️ Project Architecture
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Streamlit UI    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    NLP / Intent     │
                    │     Detection       │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
          ┌──────┐          ┌──────┐          ┌──────┐
          │ Chat │          │Tasks │          │Notes │
          └──┬───┘          └──┬───┘          └──┬───┘
             │                 │                 │
             ▼                 ▼                 ▼
        ┌─────────┐       ┌──────────┐      ┌──────────┐
        │ Gemini  │       │ SQLite   │      │ SQLite   │
        │   AI    │       │ Database │      │ Database │
        └─────────┘       └──────────┘      └──────────┘
                               │
                               ▼
                       ┌────────────────┐
                       │   Dashboard    │
                       └────────────────┘
📂 Project Structure
AI-Personal-Assistant/
│
├── app.py
│
├── database/
│   ├── database.py
│   └── assistant.db
│
├── modules/
│   ├── ai.py
│   ├── nlp.py
│   ├── tasks.py
│   └── notes.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md


⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project directory:

cd AI-Personal-Assistant
2. Create a virtual environment
python -m venv venv
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
📦 Install Dependencies

Install the required Python packages:
pip install -r requirements.txt
If you haven't created requirements.txt yet, you can generate it using:
pip freeze > requirements.txt

🔑 API Key Configuration
The AI functionality requires an API key.
Create a .env file in the project root:
GEMINI_API_KEY=your_api_key_here
The application loads the API key through environment variables.

⚠️ Security
Never upload your .env file or API key to GitHub.
Your .gitignore should include:

.env
venv/
__pycache__/
*.pyc

▶️ Running the Application
Activate your virtual environment and run:
streamlit run app.py
The application will open in your browser.
Usually the local address is:
http://localhost:8501

💬 Example Commands
Chat
What is Python?

The assistant detects:

CHAT
Add a task
Add a high priority task to study Python tomorrow

The assistant extracts:

Task: Study Python
Priority: High
Due Date: Tomorrow

🧠 How the AI Assistant Works

The application follows a simple processing pipeline:

User Input
    ↓
Streamlit
    ↓
NLP Processing
    ↓
Intent Detection
    ↓
┌───────────────┬───────────────┬───────────────┐
│     CHAT      │     TASK      │     NOTE      │
└───────┬───────┴───────┬───────┴───────┬───────┘
        ↓               ↓               ↓
     Gemini          Extract          Extract
       AI             Task             Note
        ↓               ↓               ↓
    Response        SQLite DB        SQLite DB

This allows the application to combine conversational AI with productivity automation.

🗃️ Database

The project uses SQLite as its local database.
The task system stores information such as:

Task ID
Title
Description
Priority
Due Date
Status
Created At

The notes system stores note information such as:

Note ID
Title
Content
Created At

SQLite was selected because it is lightweight, easy to configure, and suitable for a beginner-to-intermediate Python project.

🔐 Security Considerations

The project follows basic security practices:
API keys are stored in environment variables.
.env is excluded from Git.
Sensitive credentials should never be committed.
Database operations use parameterized SQL queries.

🚀 Future Improvements
Possible future enhancements include:

🔐 User authentication
👤 Multiple user accounts
🌐 Cloud database
📱 Mobile-friendly interface
🎙️ Voice input
🔊 Voice responses
📧 Email reminders
🔔 Task notifications
📆 Google Calendar integration
🤖 More advanced AI agent capabilities
📊 Advanced productivity analytics
☁️ Cloud deployment
🔄 Task synchronization across devices
🎓 Learning Outcomes

Through this project, the following concepts were practiced:

Python programming
Streamlit application development
Generative AI integration
LLM API usage
Natural Language Processing
Intent classification
Information extraction
SQLite database operations
CRUD operations
Environment variables
Git and GitHub
Application architecture
Error handling
UI development
🎯 Project Objective

The main objective of this project is to develop an AI-powered productivity assistant capable of understanding natural-language commands and helping users manage their daily tasks and notes.
The project demonstrates how Artificial Intelligence, Natural Language Processing, Python, databases, and web application development can be integrated into a single practical application.

👩‍💻 Author
BCA Student — AI & Python Project

Developed as part of a Summer Internship Project.

📜 License
This project is created for educational and internship purposes.
