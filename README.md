```markdown
# Maritime SOF Analytics 🚢

**Live Demo:** 👉 [**https://project-sof-analysis.netlify.app/**](https://project-sof-analysis.netlify.app/)

A **full-stack web application** that transforms unstructured maritime **Statement of Facts (SOF)** documents into actionable, structured data.  

Upload **PDF/DOCX** files and instantly receive a detailed analysis, including:  
- An **interactive events table**  
- A **dynamic Gantt chart timeline**  

---

## 🚀 Key Features

- **📄 Intelligent Document Parsing**  
  Extracts raw text from complex PDF/DOCX files using **LlamaParse**.

- **🤖 Advanced AI Structuring**  
  Dual-pass refinement with **Google Gemini Pro**:
  1. First AI pass → structures extracted data.  
  2. Second AI pass → validates, corrects, and merges inconsistencies for maximum accuracy.

- **⚡ Robust Backend API**  
  Built with **FastAPI**, ensuring fast, asynchronous file handling.  
  Uses **Pydantic** schemas for strong data validation.

- **🎨 Framework-Free Frontend**  
  Responsive, modern UI built with **vanilla HTML, CSS, and JavaScript** (no heavy frameworks).

- **📊 Rich Data Visualization**  
  - **Detailed Events Table** → color-coded, sortable.  
  - **Custom Gantt Chart** → interactive timeline built from scratch.

- **💾 Flexible Data Export**  
  Download structured data in **CSV** and **JSON** formats.

---

## 🛠️ Technology Stack

| Area        | Technologies                                                                 |
|-------------|------------------------------------------------------------------------------|
| **Backend** | Python, FastAPI, Uvicorn, Google Gemini, LlamaParse, Pydantic, python-dotenv |
| **Frontend**| HTML5, CSS3 (grid, flexbox, animations), Vanilla JS (ES6+)                   |
| **DevOps**  | Git, GitHub                                                                  |

---

## ⚙️ How It Works

1. **File Upload** → Upload SOF documents (drag & drop supported).  
2. **Backend Processing** → Files saved temporarily by FastAPI.  
3. **Text Extraction** → `document_parser` extracts ordered text with **LlamaParse**.  
4. **AI Structuring & Refinement**:  
   - First pass → Gemini structures data.  
   - Second pass (adjudicator) → Compares original text + both extractions → resolves conflicts.  
   - Output → **final, high-accuracy JSON object**.  
5. **Data Visualization** → Frontend renders data into:  
   - Details card  
   - Events table  
   - Custom Gantt chart  
   *(stored in localStorage for persistence)*  
6. **Export** → Data downloadable as **CSV/JSON**.

---

## 📂 Project Structure

```

maritime-sof-analytics/
├── project-backend/
│   ├── uploads/             # Temp storage for uploaded files (runtime only)
│   ├── .env                 # API keys
│   ├── main.py              # FastAPI app, routes, static file serving
│   ├── document\_parser.py   # Text extraction logic (LlamaParse)
│   ├── processor.py         # AI structuring & refinement logic (Gemini)
│   └── requirements.txt     # Python dependencies
│
└── project-frontend/
├── index.html           # Homepage
├── upload.html          # File upload page
├── data.html            # Visualization dashboard
├── styles.css           # CSS styles
└── script.js            # Frontend logic

````

---

## 📦 Setup & Local Installation

### 🔑 Prerequisites
- Python **3.8+**
- `pip` package manager
- A modern web browser (Chrome/Firefox)

### 1️⃣ Clone the Repository
```bash
git clone https://your-repository-url.com/maritime-sof-analytics.git
cd maritime-sof-analytics/project-backend
````

### 2️⃣ Set Environment Variables

Create a `.env` file in `project-backend/` and add:

```env
LLAMA_CLOUD_API_KEY="llx-..."
GOOGLE_API_KEY="AIz-..."
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Backend

```bash
uvicorn main:app --reload
```

### 5️⃣ Access the App

Open: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
The FastAPI server serves all frontend files.

---

## 🔗 Resources

* [🌐 LlamaParse – Get API Key](https://cloud.llamaindex.ai/)
* [🌐 Google AI Studio – Get Gemini Key](https://aistudio.google.com/app/apikey)
* [📘 FastAPI Documentation](https://fastapi.tiangolo.com/)
* [📘 Pydantic Documentation](https://docs.pydantic.dev/latest/)

---

✨ Built with passion for smarter maritime analytics 🚢

```
```
