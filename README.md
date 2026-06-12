# AI-Powered Data Normalization Pipeline

A professional ETL (Extract, Transform, Load) pipeline built in Python. This system processes large customer datasets, normalizes inconsistent information using OpenAI's language models, and exports clean, production-ready data.

## Features

* **Data Extraction:** Reads and parses massive datasets efficiently using `pandas`.
* **Hybrid AI Transformation:** Integrates OpenAI's `gpt-4o-mini` API to standardize formatting (names, phone numbers, and countries) into structured JSON objects.
* **Local Fallback System:** Includes an autonomous, built-in algorithmic fallback mechanism to ensure the pipeline runs smoothly for free if no API key is provided.
* **Data Export:** Restructures the AI outputs back into a clean, standardized CSV format with English headers.

## Tech Stack

* **Language:** Python 3.x
* **Data Manipulation:** Pandas
* **AI Integration:** OpenAI API (Chat Completions)
* **Environment Management:** Virtualenv (`venv`)
* **Version Control:** Git & GitHub (Feature Branch Workflow)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JoseRamirez/DataNormalization.git](https://github.com/JoseRamirez/DataNormalization.git)
   cd DataNormalization

2. **Activate the virtual enviroment:**

# On Windows (Git Bash):
source venv/Scripts/activate

3. **Install dependencies:**
pip install pandas openai

4. **Set up your environment variable (Optional)::**
export OPENAI_API_KEY="your-api-key-here"


## To execute the full data normalization pipeline, simply run:
python main.py

The system will automatically log the process in the terminal and generate a new file named cleaned_clients.csv upon completion.