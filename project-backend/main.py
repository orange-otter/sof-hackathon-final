# main.py

import os
import json
import shutil
import traceback
from typing import List
from pathlib import Path # <-- NEW: Import Path for robust path handling

from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from document_parser import extract_text_from_document
from processor import get_structured_data

# Load environment variables
load_dotenv()

# Create FastAPI app instance
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CORRECTED: Code to serve frontend files ---
# This now correctly points to your '../project-frontend' directory
# It finds the location of main.py and then navigates to the sibling folder.
BACKEND_ROOT_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BACKEND_ROOT_DIR.parent / "project-frontend"

# Mount the 'project-frontend' directory to serve CSS, JS, etc. at the '/static' path
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/")
async def read_index():
    """Serves the main index.html file."""
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/upload")
async def read_upload():
    """Serves the upload.html file."""
    return FileResponse(os.path.join(FRONTEND_DIR, "upload.html"))

@app.get("/data")
async def read_data():
    """Serves the data.html file."""
    return FileResponse(os.path.join(FRONTEND_DIR, "data.html"))
# --- END of corrected code ---


def clear_output_file(file_path: str = "output.json"):
    """
    Wipes the given file for privacy by replacing its contents with an empty JSON array.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("[]")
        print(f"--- ✅ Cleared {file_path} ---")
    except Exception as e:
        print(f"--- ❌ Could not clear {file_path}. Reason: {e} ---")


@app.post("/process")
async def process_uploaded_files(
    background_tasks: BackgroundTasks,
    files: List[UploadFile] = File(...)
):
    """
    Handles uploaded files:
    - saves them temporarily
    - extracts text
    - processes with AI
    - returns structured JSON
    - schedules cleanup in the background
    """
    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    all_detailed_data = []

    for file in files:
        file_path = os.path.join(uploads_dir, file.filename)
        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            raw_text = extract_text_from_document(file_path)
            detailed_ai_data = get_structured_data(raw_text)

            detailed_ai_data['fileName'] = file.filename
            all_detailed_data.append(detailed_ai_data)

        except Exception as e:
            print(f"--- ❌ Failed while processing {file.filename} ---")
            traceback.print_exc()
            raise HTTPException(
                status_code=500,
                detail=f"Error while processing {file.filename}: {e}"
            )
        finally:
            if not file.file.closed:
                file.file.close()
            if os.path.exists(file_path):
                os.remove(file_path)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(all_detailed_data, f, indent=2, ensure_ascii=False)

    background_tasks.add_task(clear_output_file)

    return all_detailed_data