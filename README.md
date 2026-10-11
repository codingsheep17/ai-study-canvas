🎨 StudyCanvas AI
Turn messy notes and rough sketches into structured, study-ready revision packs in seconds.

StudyCanvas AI is a powerful, minimal web application built entirely in Python. It takes raw educational materials—whether that’s a dense PDF textbook chapter, a screenshot of an article, or a photo of a hand-drawn diagram—and instantly transforms them into clean visual flowcharts, high-yield notes, and interactive quizzes calibrated to your specific education level.

Built with a focus on bulletproof reliability, StudyCanvas AI features concurrent multi-file processing, intelligent OCR routing, and a multi-key cascading AI fallback system to ensure it never goes down during heavy study sessions.

✨ Features
🧠 Adaptive Smart OCR: Extracts text natively from PDFs using PyPDF2. If you upload an image or a scanned PDF, the app seamlessly offloads the task to Google's Gemini Vision AI to read the pixels.

🛡️ Bulletproof API Fallbacks: Never get locked out by a 503 High Demand error again. The pipeline automatically cycles through a pool of Gemini and Groq API keys, transferring the load gracefully if one key hits a rate limit.

⚡ Concurrent Processing: Upload up to 3 files at once. A background ThreadPoolExecutor processes them in parallel, keeping wait times at an absolute minimum.

📊 Flawless Flowcharts: Instead of relying on image diffusion models (which hallucinate gibberish text), the LLM writes pure Mermaid.js logic. This is instantly rendered into a crisp, readable PNG diagram via the open-source Kroki API.

🎯 Calibrated Learning: Select your level (School, College, or University). The AI adjusts the vocabulary of the notes and the difficulty of the multiple-choice quiz to match.

🔒 UI & Backend Locking: Fully protected against button-spamming, double-submissions, and WebSocket timeouts via asyncio threading and strict backend state locks.

🛠️ Tech Stack
This project takes a minimalist, Python-only approach to full-stack development:

Frontend & Backend: Reflex (Pure Python)

LLM Engine: Google Gemini (3.8-flash) & Groq (Llama-3.1-8b-instant)

Diagram Rendering: Kroki API (Mermaid.js)

Document Parsing: PyPDF2 & PIL (Pillow)

Concurrency: asyncio & concurrent.futures

🚀 How It Works Under the Hood
Upload & Validate: Drop up to 3 files (PNG, JPG, JFIF, PDF) into the UI. The frontend locks to prevent overlapping sessions.

Parallel Extraction: Files are dispatched concurrently. Text is ripped from standard PDFs instantly, while images are sent to Gemini Vision.

AI Pipeline: The combined text is fed to an LLM with a strict JSON schema requirement. The AI distills the text into bullet points, spots and corrects factual misconceptions, generates a quiz, and writes Mermaid.js flowchart logic.

Asynchronous Rendering: The UI streams real-time status updates back to the user without dropping the WebSocket heartbeat, while Kroki silently renders the Mermaid diagram into a clean PNG in the background.

⚙️ Local Setup & Installation
.
1. Clone the repository
git clone https://github.com/yourusername/studycanvas-ai.git
cd studycanvas-ai
.
2. Set up a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
.
3. Install dependencies
pip install -r requirements.txt
.
4. Configure Environment Variables
Create a .env file in the root directory and add your API keys. The app supports multiple keys for rate-limit protection:
.
Code snippet
# Primary & Backup Gemini Keys (For Vision OCR & General LLM)
MY_GEMINI_KEY=your_gemini_key_1
GEMINI_KEY=your_gemini_key_2
ANSA_GEMINI_KEY=your_gemini_key_3
# Primary & Backup Groq Keys (For Lightning-Fast Fallback LLM)
MY_GROQ_KEY=your_groq_key_1
GROQ_KEY=your_groq_key_2
AMINA_GROK_KEY=your_groq_key_3
.
5. Initialize and Run
reflex init
reflex run
The app will be live and running on 
.
## 👥 Team & Roles
StudyCanvas AI was brought to life by a dedicated team bridging the gap between AI backend infrastructure and beautiful frontend design:

* **Syed Haseeb Shah** – *Lead Python & AI Developer*
  Architected the core Reflex backend, engineered the multi-key cascading API fallback systems, integrated the Kroki flowchart rendering, and implemented the asynchronous OCR pipeline.
* **Amina Batool & Ansa Qayyum** – *UI & Frontend Developer*
  Designed and developed the sleek, minimalist user interface. Created the responsive components, interactive quiz layouts, and dynamic study note structures (including the custom UI lists).
* **Hammad** – *AI Integration & Infrastructure Support*
  Assisted with the LLM pipeline configuration, API key management, and prompt engineering to ensure the AI generates strictly formatted, high-quality educational content.
.
📝 License
This project is MIT licensed.