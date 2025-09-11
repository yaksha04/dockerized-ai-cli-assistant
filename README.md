# 🐧 Dockerized AI-Powered Linux CLI Assistant 🤖

A smart command-line assistant that understands natural language commands to automate Git operations and system monitoring tasks. Built in Python and fully containerized using Docker for cross-platform portability and ease of use.

---

## 🚀 Features

- 🔍 **Natural Language Parsing**  
  Understands input like:
  - `create a new git branch called feature-login`
  - `delete git branch login-feature`
  - `show disk usage`

- ⚙️ **Automated Command Execution**  
  Executes Git and system commands via Python safely and interactively.

- 💾 **System Monitoring with `psutil`**  
  Displays real-time disk usage statistics.

- 🐳 **Fully Dockerized**  
  Just build and run the Docker container—no setup headaches!

---

## 🧠 Tech Stack

| Technology    | Purpose                                         |
|---------------|--------------------------------------------------|
| Python 3.10    | Core programming language                       |
| `re` (regex)   | Natural language parsing                        |
| `subprocess`   | Git/system command execution                    |
| `psutil`       | Disk usage and system info                      |
| Docker         | Containerization for seamless deployment        |
| `venv`         | Local Python virtual environment (development)  |

---

## 📁 Project Structure

dockerized-ai-cli-assistant/
│
├── cli/
│ ├── main.py # CLI entry point (interactive loop)
│ └── test_parser.py # Optional parser tests
│
├── core/
│ ├── parser.py # Natural language parser
│ └── execution.py # Executes parsed actions (Git & system)
│
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image instructions
└── README.md # You're here!

yaml
Copy
Edit

---

## 🧪 How It Works

1. **User types** a natural language command.
2. `parser.py` processes it to identify intent and parameters.
3. `execution.py` runs the corresponding Git/system command.
4. Output is returned in a clear, friendly format.

---

## 🛠️ Setup (Without Docker)

### 1. Clone the repository:


git clone https://github.com/yourusername/dockerized-ai-cli-assistant.git
cd dockerized-ai-cli-assistant
2. Create and activate virtual environment:

python3 -m venv venv
source venv/bin/activate  # Linux or WSL
3. Install dependencies:

pip install -r requirements.txt
4. Run the assistant:

python cli/main.py
🐳 Run with Docker (Recommended)
1. Build the Docker image:

docker build -t dockerized-ai-cli-assistant .
2. Run the container:

docker run -it --rm dockerized-ai-cli-assistant
✨ Example Commands

>>> create a new git branch called feature-login
✅ Git branch 'feature-login' created successfully.

>>> delete git branch feature-login
✅ Git branch 'feature-login' deleted successfully.

>>> show disk usage
💾 Disk Usage:
  Total: 500 GB
  Used: 30 GB
  Free: 470 GB
📌 Limitations
Works with a limited set of natural language commands.

Only Git and disk usage features are currently supported.

Runs interactively inside the container or via CLI script.

