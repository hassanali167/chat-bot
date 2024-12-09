## README for AI Chatbot 

# AI Chatbot 

Welcome to the **AI Chatbot** repository! This project implements an intelligent AI chatbot using [Chainlit](https://www.chainlit.io/), [Groq API](https://www.groq.com/), and open-source Meta AI models. The chatbot provides seamless conversational capabilities, offering a wide range of applications such as customer support, educational tools, and real-time Q&A systems.

---

## Features
- **Chainlit Framework:** Simplifies chatbot development and offers a clean user interface.
- **Groq API:** Provides high-performance computations and efficient model inference.
- **Meta AI Models:** Utilizes state-of-the-art open-source models for natural language processing.
- Fully customizable and scalable.

---

## Requirements
- Python 3.8 or higher
- pip (Python package installer)

---

## Setup Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/hassanali167/chat-bot.git
cd chat-bot
```

### Step 2: Create a Virtual Environment
Create an isolated environment to manage dependencies.

#### On Windows:
```bash
python -m venv chatbot-env
chatbot-env\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv chatbot-env
source chatbot-env/bin/activate
```

### Step 3: Install Dependencies
After activating the virtual environment, install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Get Your Groq API Key
1. Visit [Groq Console](https://console.groq.com/) and create an account.
2. Once registered and logged in, generate an API key from your account dashboard.
3. Copy the generated API key.

### Step 5: Configure Environment Variables
Create a `.env` file in the root directory of the project and paste your API key:
```
GROQ_API_KEY=your_groq_api_key

```

Replace `your_groq_api_key` with the Groq API key in .env file

---

## Running the Chatbot

1. **Start the Chatbot Server:**
   Run the following command:
   ```bash
   chainlit run main.py
   ```

2. **Access the Chatbot Interface:**
   Open your web browser and navigate to `http://localhost:8000` (or the port configured in your project).

---

## Commands 
Here’s a quick list of all the commands you’ll need:

1. Clone the repository:
   ```bash
   git clone https://github.com/hassanali167/chat-bot.git
   cd chat-bot
   ```

2. Create and activate a virtual environment:
   - **Windows:**
     ```bash
     python -m venv chatbot-env
     chatbot-env\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv chatbot-env
     source chatbot-env/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Get and set the Groq API key:
   - Visit [console.groq.com](https://console.groq.com/), create an account, and generate an API key.
   - Paste the API key into the `.env` file.

5. Run the application:
   ```bash
   chainlit run main.py
   ```

---

## License
This project is licensed under the [MIT License](LICENSE).

---

If you have any issues or suggestions, feel free to open an issue or contribute to improve the project. Happy coding! 🎉
