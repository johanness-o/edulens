# EduLens: Equity-Aware Course Feedback Analyzer

An LLM-powered web application that analyzes student course evaluations for sentiment, themes, and equity signals. EduLens ingests raw evaluation CSVs and produces an interactive dashboard surfacing insights that would be impractical to extract manually, including access barriers and inclusion patterns across instructors and semesters.

Built with the Groq API (Llama 3.3) for fast, low-cost LLM inference, paired with a companion Jupyter notebook that demonstrates the underlying traditional NLP pipeline (NLTK, TextBlob, LDA).

---

## Features

- **Sentiment analysis** — classifies open-ended feedback as positive, negative, or mixed using LLM-based analysis
- **Theme extraction** — automatically surfaces recurring topics across responses (workload, clarity, accessibility, and more)
- **Equity signal detection** — flags language indicating access barriers, inclusion concerns, and inequitable experiences
- **Instructor and term filtering** — drill into a specific professor or semester
- **Interactive dashboard** — clean, readable visualization of results
- **Works on real CSV data** — handles tab- or comma-separated files

---

## Repository Contents

```
edulens/
├── README.md                  # this file
├── feedback-analyzer.html     # the web application
├── ses_analysis_v2.ipynb      # companion NLP research notebook
└── sample_data/               # synthetic demo CSVs (no real student data)
```

---

## Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- [Python 3](https://www.python.org/downloads/) installed (used to run a simple local server)
- A free [Groq API key](https://console.groq.com/keys)

---

## Setup

### 1. Download the project

Clone the repository:

```bash
git clone https://github.com/johanness-o/edulens.git
cd edulens
```

Or download it as a ZIP from GitHub (click the green **Code** button → **Download ZIP**) and unzip it.

### 2. Add your Groq API key

Open `feedback-analyzer.html` in a text editor. Find the line containing the API key placeholder:

```javascript
"Authorization": "Bearer YOUR_GROQ_KEY_HERE"
```

Replace `YOUR_GROQ_KEY_HERE` with your actual Groq API key (it starts with `gsk_`). Save the file.

> **Note:** Never commit your real API key to GitHub. Keep it local.

### 3. Start a local server

The app makes API calls, which browsers block when opening an HTML file directly. Running a small local server solves this. From inside the project folder:

```bash
python3 -m http.server 8080
```

### 4. Open the app

In your browser, go to:

```
http://localhost:8080/feedback-analyzer.html
```

---

## How to Use

1. **Prepare your CSV.** Your file should have these columns:
   `course_number`, `term`, `instructor`, `question_id`, `question_response`
   (Both tab-separated and comma-separated files are supported. Synthetic examples are in `sample_data/`.)

2. **Upload a file.** Click the file picker and select one CSV. The app loads one file at a time.

3. **Filter (optional).** Use the dropdowns to focus on a specific instructor or term.

4. **Analyze.** Click **Analyze**. The app sends the responses to the LLM and displays a dashboard with sentiment breakdowns, extracted themes, and flagged equity signals.

---

## Sample Data

The `sample_data/` folder contains five synthetic CSVs representing different instructor profiles (strongly positive, strongly negative, mixed, and so on). All data is fabricated for demonstration — it contains no real student information and is safe to use and share.

---

## How It Works

EduLens reads your CSV, parses the responses, and sends them to the Groq API running Llama 3.3 with a structured prompt requesting sentiment, themes, and equity analysis. The response is parsed and rendered into the dashboard. The app includes safeguards for malformed or truncated LLM output so it stays reliable on larger inputs.

The companion notebook, `ses_analysis_v2.ipynb`, demonstrates the traditional NLP approach the project grew out of: ensemble sentiment analysis with NLTK and TextBlob, LDA topic modeling with bigram preprocessing, and rule-based equity detection.

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **LLM:** Groq API (Llama 3.3)
- **Data processing:** JavaScript (web app), Python with Pandas and NLTK (notebook)

---

## Author

**Joan Ojukwu**
[LinkedIn](https://linkedin.com/in/joan-ojukwu) · [GitHub](https://github.com/johanness-o)

Built from two years of NLP research at the University of Maryland's Teaching and Learning Transformation Center.
