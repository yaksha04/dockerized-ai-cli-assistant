

# 🧠 Dockerized Natural-Language Linux CLI Assistant

> A production-minded, Dockerized CLI tool that translates natural language into safe Linux, Git, and system operations — built to demonstrate real DevOps & systems engineering skills, not just scripting.

---

## 🔥 Why This Project Exists

In real engineering teams, tools fail not because of syntax —
they fail because of **poor separation of concerns, unsafe execution, and lack of portability**.

This project was built to answer one question:

> **How would I design a CLI assistant that is safe, debuggable, portable, and extensible in a real production environment?**

This is **not** an AI toy.
It is a **systems-first, DevOps-oriented CLI** with deliberate architectural choices.

---

## 🎯 What This Project Demonstrates

This project explicitly showcases:

* Clean command parsing vs execution separation
* Secure system command execution (`subprocess`, no shell abuse)
* Linux filesystem & permission handling
* Git workflow automation
* Containerized runtime (Docker)
* Defensive programming & graceful failure
* CLI UX design
* Extensibility without refactoring

These are **core expectations** at FAANG / product companies.

---

## 🧩 High-Level Architecture

```text
User Input (Natural Language)
        ↓
parser.py
  - Regex-based intent detection
  - Extracts structured action + parameters
        ↓
execution.py
  - Validates inputs
  - Executes Git / OS / system calls safely
        ↓
Linux / Git / System APIs
```

### Why this architecture?

* Parsing logic never touches the system
* Execution logic never interprets language
* Easy to audit, test, and extend
* Mirrors real production CLI design

---

## 📁 Project Structure

```text
.
├── main.py            # CLI entry point (event loop, UX)
├── parser.py          # Natural language → intent parsing
├── execution.py       # Secure execution layer
├── system_monitor.py  # CPU / memory / disk utilities
├── requirements.txt
├── Dockerfile
├── .gitignore
├── LICENSE
└── README.md
```

This structure intentionally avoids:

* God files
* Hidden side effects
* Tightly coupled logic

---

## 🚀 Supported Capabilities

### 🔹 Git Automation

```text
create a new git branch called feature-login
delete git branch feature-login
```

### 🔹 File & Directory Management

```text
create file app.log
create directory logs
delete file temp.txt
list files
where am i
```

### 🔹 Permissions (chmod)

```text
give execute permission to deploy.sh
set permission 644 on config.yaml
```

### 🔹 System Observability

```text
show disk usage
show cpu usage
show memory usage
```

---

## 🧪 Example CLI Session

```text
>>> create file app.log
📄 File 'app.log' created successfully.

>>> set permission 644 on app.log
🔐 Permissions 644 set on 'app.log'.

>>> show memory usage
🧠 Memory Usage: 41%

>>> delete file app.log
🗑️ File 'app.log' deleted successfully.

>>> exit
👋 Exiting AI CLI Assistant.
```

No debug noise.
No internal structures leaked.
Clean user-facing output.

---

## 🐳 Dockerized by Design (Not an Afterthought)

### Build

```bash
docker build -t dockerized-ai-cli-assistant .
```

### Run

```bash
docker run -it --rm dockerized-ai-cli-assistant
```

### Why Docker?

* Identical behavior across machines
* Zero dependency conflicts
* Interviewers can run it instantly
* Demonstrates production awareness

---

## 🔐 Security & Safety Considerations

This project **intentionally avoids**:

* `shell=True`
* arbitrary command execution
* silent destructive operations

Current safeguards:

* Explicit action mapping
* File existence checks
* Controlled `subprocess.run`

Planned improvements (designed, not ignored):

* Confirmation prompts for destructive actions
* Restricted paths (`/etc`, `/usr`, `/bin`)
* Dry-run mode
* Audit logging

This shows **engineering judgment**, not recklessness.

---

## 🧠 Design Decisions 

### Why regex instead of LLMs?

* Deterministic behavior
* Zero latency
* Zero cost
* Full control

LLMs are a **future extension**, not a shortcut.

---

### Why not `os.system`?

* No error handling
* Security risk
* Poor observability

`subprocess.run(check=True)` is deliberate.

---

### Why one command loop instead of shell integration?

* Predictable lifecycle
* Testability
* Clear ownership of state

---

## 📌 Tech Stack

| Technology | Reason                          |
| ---------- | ------------------------------- |
| Python 3   | Systems scripting & readability |
| Regex      | Deterministic intent parsing    |
| subprocess | Safe process execution          |
| psutil     | System observability            |
| Docker     | Runtime isolation               |
| Linux      | Target production environment   |

---

## 📈 Scalability & Extensibility

This project is intentionally built to scale:

* Add new commands without refactoring
* Replace parser with ML/LLM later
* Add plugin system
* Add role-based permissions
* Mount host volumes for real Git repos

The architecture already supports this.

---

## 👤 About the Author

I focus on **DevOps & systems engineering**, not just writing code that works once.

My priority is:

* reliability
* safety
* observability
* clean design

This project reflects that mindset.



