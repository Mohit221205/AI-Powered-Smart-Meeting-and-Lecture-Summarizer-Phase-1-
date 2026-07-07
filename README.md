# 🎙️ AI-Powered Lecture & Meeting Summarizer

An ultra-low latency, production-prototype workspace designed to convert raw academic lectures and business meeting recordings into highly structured, actionable Markdown notes. Powered by **Groq's LPU Inference Engine**, this application orchestrates advanced Speech-to-Text (ASR) pipelines and high-intelligence LLM reasoning models.

---

## ✨ Features

* **Multi-Format Audio Upload:** Supports `mp3`, `wav`, `m4a`, `ogg`, and `flac` files with native in-app audio playback previews.


* **Ultra-Low Latency Transcription:** Uses the lightning-fast `whisper-large-v3-turbo` model via Groq to execute near-instantaneous Speech-to-Text pipeline transformations.


* **Elite Academic Formatting:** Integrates an advanced `llama-3.3-70b-versatile` reasoning prompt layer that transforms raw verbal text into:


* 📋 Comprehensive 3-paragraph executive summaries.


* 🔑 Deeply structured technical concept breakdowns.


* 📝 Actionable task checklists and tracking deadlines.




* **Dual-Workspace Interface:** View results instantly inside a clean, modern tabbed interface separating **Structured AI Notes** from the **Verbatim Raw Transcript**.



---

## 🛠️ Architecture & Tech Stack

* **Frontend Interface:** Streamlit (Responsive Python Web Framework)


* **Inference Compute:** Groq Cloud SDK


* **Audio Transcription (ASR):** `whisper-large-v3-turbo`

* **Text Synthesis & Structure:** `llama-3.3-70b-versatile`


---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher installed.
* A **Groq API Key** (Get yours from the Groq Console).

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

```


2. **Create and activate a virtual environment (Optional but Recommended):**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```


3. **Install the required dependencies:**
```bash
pip install streamlit groq python-dotenv

```


4. **Configure your Environment Variables:**
Create a `.env` file in the root directory of your project and add your API key:


```env
GROQ_API_KEY=your_actual_groq_api_key_here

```


Note: If you do not create a `.env` file, the application allows you to securely paste your key directly into the application sidebar at runtime.



### Running the Application

Launch the Streamlit workspace local server by running:

```bash
streamlit run app.py

```

Open your browser and navigate to `http://localhost:8501` to start summarizing!

---

## 📖 How It Works

1. **Upload & Preview:** Drag and drop an audio file into the sidebar uploader. Play it directly inside the browser using the built-in media preview element.


2. **ASR Execution:** Clicking the **"Generate Academic Summary"** button streams the raw file buffer directly to the Groq Whisper endpoint without bloating your local disk.


3. **Structured Prompt Synthesis:** The raw output transcript is instantly processed through an elite engineering system instructions layout using Llama 3.3.


4. **Workspace Review:** Interact with your compiled notes inside the clean workspace layout tabs.



---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
