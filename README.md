---

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

**1. Repository Clone Karein**
GitHub se repo clone karein aur us folder ke andar jaayein.

**2. Virtual Environment Banao (Recommended)**
Python ka virtual environment create karein taaki dependencies clean rahein.

* **Windows users:**
```bash
venv\Scripts\activate

```


* **Linux / macOS users:**
```bash
source venv/bin/activate

```



**3. Dependencies Install Karein**
`requirements.txt` file se saari required libraries install karein.

```bash
pip install -r requirements.txt

```

**4. Notebooks Run Karna Ho**
Jupyter Notebook start karein aur `notebooks` folder ke andar se koi bhi notebook open karke run karein.

**5. Mini Agent Projects Run Karna Ho**
`mini_projects` ke andar jaayein, kisi bhi agent folder me jaakar `agent.py` file run karein.

```bash
python mini_projects/weather_agent/agent.py

```

---

## 🚧 CURRENT STATUS

> Ye repository **Agentic AI** seekhne aur experiment karne ke phase ko represent karti hai. Isme focus foundations strong karne par hai, production-ready system banana abhi next step hai.

---

## 📅 PLANNED IMPROVEMENTS

* [ ] Planner-based agent loop implement karna.
* [ ] Tools ke liye proper abstraction banana.
* [ ] Short-term aur long-term memory add karna.
* [ ] Selected agents ko API based services me convert karna.
* [ ] Multi-agent coordination explore karna.

---
