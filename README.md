# 🤖 Gen-AI & Agentic AI

## 📖 Overview

This repository contains my **hands-on work while learning and building Agentic AI systems**.
The focus is on understanding **how agents are structured, how they interact with LLMs, and how tool-based reasoning works**, rather than just prompt writing.

The repo includes:

* Mini agent projects
* Structured experiments
* Prompt and LLM fundamentals
* Notebook-based exploration

---

## 📂 Repository Structure

### `mini_projects/`

Small, focused agent implementations to understand agent behavior.

* **simple_weather_agent/**
* `agent.py`: A minimal weather agent demonstrating basic LLM interaction and response generation.


* **weather_agent/**
* `agent.py`: A more structured version of the weather agent with improved logic and flow.



### `notebooks/`

Exploratory notebooks used to test ideas, models, and prompts. These represent **experimentation and iteration**, not final production code.

* `Weather_agent.ipynb`: Notebook-based implementation of a weather agent.
* `gemini_test.ipynb`: Testing Gemini model behavior.
* `prompt_basics.ipynb`: Fundamentals of prompt design.
* `test_llm.ipynb`: Testing and comparing LLM responses.

### `src/`

Core learning modules and structured experiments.

* **check_models/**: Testing different LLM/model setups.
* **hello_world/**: Basic agent/LLM interaction examples.
* **hf_basic/**: Hugging Face fundamentals and experiments.
* **prompt_fundamentals/**: Structured work on prompt engineering concepts.

---

## 🛠 Tech Stack

* **Language:** Python 🐍
* **Environment:** Jupyter Notebook 📓
* **LLM APIs:** OpenAI / Gemini / Hugging Face (Experimental)
* **Concepts:** Prompt Engineering, Agentic Workflows

---

## 🎯 What This Project Demonstrates

* Understanding of **Agentic AI concepts**.
* Breaking problems into **small agent-based experiments**.
* Structured learning approach instead of random scripts.
* Clear separation between experiments, mini projects, and core concepts.

---

## 🚀 HOW TO RUN

Follow these steps to set up and run the project:

**1. Clone the Repository**
Clone the repo from GitHub and navigate into the folder.

**2. Create a Virtual Environment (Recommended)**
Create a Python virtual environment to keep dependencies clean.

* **Windows users:**
```bash
venv\Scripts\activate

```


* **Linux / macOS users:**
```bash
source venv/bin/activate

```



**3. Install Dependencies**
Install all required libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt

```

**4. To Run Notebooks**
Start Jupyter Notebook, navigate to the `notebooks` folder, and open/run any notebook.

**5. To Run Mini Agent Projects**
Navigate to `mini_projects`, enter any agent folder, and run the `agent.py` file.

```bash
python mini_projects/weather_agent/agent.py

```

---

## 🚧 CURRENT STATUS

> This repository represents the **learning and experimentation phase** of Agentic AI. The focus is on strengthening foundations; building a production-ready system is the next step.

---

## 📅 PLANNED IMPROVEMENTS

* [ ] Implement a planner-based agent loop.
* [ ] Create proper abstraction for tools.
* [ ] Add short-term and long-term memory.
* [ ] Convert selected agents into API-based services.
* [ ] Explore multi-agent coordination.
