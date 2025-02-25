ChatGPT Clone
A fully functional ChatGPT clone built using React, JavaScript, Python, and API integration. This project replicates the core functionality of ChatGPT, allowing users to interact with an AI-powered chatbot.

Features
User-friendly chat interface

AI-generated responses using OpenAI API

Responsive design with Tailwind CSS

Backend powered by Python

Frontend built with React and JavaScript

Data stored in MongoDB for persistent conversations

Installation
Prerequisites
Ensure you have the following installed:

Node.js (v14 or later)

Python (v3.8 or later)

pip (Python package manager)

npm (Node package manager)

MongoDB (Installed and running)

Setup
1. Clone the Repository:
git clone https://github.com/your-username/chatgpt-clone.git
cd chatgpt-clone
2. Install Dependencies:
Backend (Python)
pip install -r requirements.txt
Frontend (React + JavaScript)
npm install
Configuration
OpenAI API Key Configuration
The OpenAI API key is stored in main.py. Update main.py with your API key as follows:

OPENAI_API_KEY = "your_openai_api_key"
Alternatively, you can use environment variables by modifying main.py:

import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
Ensure your .env file contains:

OPENAI_API_KEY=your_openai_api_key
MONGO_URI=your_mongodb_connection_string
Usage
Running the Backend (Python)
python main.py
Running the Frontend (React)
npm start
Contributing
Feel free to fork this repository and submit pull requests.

License
This project is licensed under the MIT License.

Developed by Mohammed Areeb Ali 🚀
