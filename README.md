
Maritime SOF Analytics 🚢
Live Demo: https://project-sof-analysis.netlify.app/
A full-stack web application that transforms unstructured maritime Statement of Facts (SOF) documents into actionable, structured data. Upload PDF or DOCX files and instantly receive a detailed analysis, complete with an interactive events table and a dynamic Gantt chart timeline.

🚀 Key Features
Intelligent Document Parsing: Utilizes LlamaParse to accurately extract raw text content from complex PDF and DOCX documents.
Advanced AI Data Structuring: Employs a dual-pass refinement strategy with the Google Gemini Pro model. An initial extraction is critically reviewed and corrected by a second AI pass, ensuring maximum accuracy and completeness.
Robust Backend API: Built with FastAPI for high-performance, asynchronous handling of file uploads and processing. Data integrity is ensured using Pydantic schemas.
Flexible Data Export: Download the structured analysis in both CSV and JSON formats for seamless integration with other systems.

🛠️ Technology Stack
Area
Technologies
Backend
Python, FastAPI, Uvicorn, Google Generative AI (Gemini), LlamaParse, Pydantic, python-dotenv
Frontend
HTML5, CSS3 (with custom animations, flexbox, grid), Vanilla JavaScript (ES6+)
DevOps
Git, GitHub


⚙️ How It Works
File Upload: The user uploads one or more SOF documents through the web interface. The frontend provides drag-and-drop functionality and visual feedback.
Backend Processing: The FastAPI server receives the files and saves them temporarily.
Text Extraction: Each file is passed to the document_parser, which uses LlamaParse to extract clean, ordered text.
AI Structuring & Refinement:
The extracted text is sent to the processor, where the Google Gemini model performs a first pass to structure the data into a predefined JSON schema.
A second, "adjudicator" prompt is then used. The AI is given the original text and both the first and second extraction attempts, and is tasked with resolving conflicts and merging the data to produce a final, highly accurate JSON object.
Data Visualization: The final JSON is sent to the frontend. JavaScript dynamically renders the data into the dashboard on the /data page, populating the details card, events table, and the custom Gantt chart. Data is stored in localStorage to persist between pages.
Export: The user can download the complete dataset as a CSV or JSON file, generated on-the-fly by the frontend.

📂 Project Structure
The project is organized into two main directories: project-backend and project-frontend, ensuring a clean separation of concerns.
maritime-sof-analytics/
├── project-backend/
│   ├── uploads/              # Temporary storage for uploaded files (created at runtime)
│   ├── .env                  # Environment variables (API keys)
│   ├── main.py               # FastAPI application, endpoints, and static file serving
│   ├── document_parser.py    # Text extraction logic using LlamaParse
│   ├── processor.py          # Data structuring and refinement logic using Gemini
│   └── requirements.txt      # Python dependencies
└── project-frontend/
    ├── index.html            # Application homepage
    ├── upload.html           # File upload interface
    ├── data.html             # Data visualization dashboard
    ├── styles.css            # All CSS styles for the application
    └── script.js             # All JavaScript logic for the frontend



📦 Setup and Local Installation
Follow these steps to get the project running on your local machine.
Prerequisites
Python 3.8+
pip package manager
A modern web browser (e.g., Chrome, Firefox)
1. Clone the Repository
First, clone the project to your local machine.
Bash
git clone https://your-repository-url.com/maritime-sof-analytics.git
cd maritime-sof-analytics/project-backend


2. Set Up Environment Variables
This project requires API keys for LlamaParse and Google Gemini.
Inside the project-backend directory, create a file named .env.
Add your API keys to the .env file:
Code snippet
LLAMA_CLOUD_API_KEY="llx-..."
GOOGLE_API_KEY="AIz..."




3. Install Dependencies
Install the required Python packages using the
requirements.txt file2.
Bash
pip install -r requirements.txt


4. Run the Application
Start the FastAPI backend server using Uvicorn3. The
--reload flag will automatically restart the server when you make changes to the code.
Bash
uvicorn main:app --reload


5. Access the Web Interface
Once the server is running (you'll see Uvicorn running on http://127.0.0.1:8000), open your web browser and navigate to:
http://127.0.0.1:8000
The FastAPI application is configured to serve all the necessary HTML, CSS, and JavaScript files from the project-frontend directory.

🔗 Links and Resources
LlamaParse: Get your API key
Google AI Studio: Get your Gemini API key
FastAPI: Official Documentation
Pydantic: Documentation
