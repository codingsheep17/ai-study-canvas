import os
import time
import PyPDF2
from PIL import Image
from google import genai
from google.genai import types  # <-- Added types import for PDF byte handling
import concurrent.futures

allowed_extensions = {'.pdf', '.png', '.jpg', '.jpeg', '.jfif'}
maximum_files = 3

def validate_files(file_names: list) -> tuple:
    if len(file_names) > maximum_files:
        return False, "Upload limit exceeded. Maximum 3 files allowed."
    for file_name in file_names:
        extension = file_name[file_name.rfind('.'):].lower()
        if extension not in allowed_extensions:
            return False, f"Invalid format: {file_name}. Only PDF and images allowed."
    return True, "All files validated successfully."

def extract_text(file_path: str, file_name: str) -> str:
    extension = file_name[file_name.rfind('.'):].lower()
    extracted_text = ""
    print(f"[STEP 1] Extracting text from: {file_name} ({extension})")
    
    try:
        # 1. Local PDF Extraction (Text-based PDFs)
        if extension == '.pdf':
            pdf_reader = PyPDF2.PdfReader(file_path)
            if len(pdf_reader.pages) > 20:
                raise ValueError(f"Exceeds maximum limit of 20 pages: {file_name}")
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text + "\n"
                    
        # 2. Vision OCR Fallback (For Images OR Scanned/Image-based PDFs)
        if not extracted_text.strip():
            if extension == '.pdf':
                print(f"[STEP 1 INFO] PyPDF2 found no text in {file_name}. Treating as scanned PDF...")
                
            gemini_keys = [
                os.getenv("MY_GEMINI_KEY"), 
                os.getenv("GEMINI_KEY"), 
                os.getenv("ANSA_GEMINI_KEY")
            ]
            
            # Models listed in priority order: latest 3.8-flash first, then 2.5-flash fallback
            models_to_try = [
                "gemini-3.8-flash",
                "gemini-2.5-flash",
                "gemini-1.5-flash"
            ]
            
            success = False
            for key in gemini_keys:
                if not key:
                    continue
                client = genai.Client(api_key=key)
                
                # Format payload once
                if extension == '.pdf':
                    doc_bytes = open(file_path, "rb").read()
                    file_payload = types.Part.from_bytes(data=doc_bytes, mime_type='application/pdf')
                else:
                    file_payload = Image.open(file_path)

                # Try primary model, then fall back to backup model
                for model_name in models_to_try:
                    try:
                        print(f"[STEP 1 INFO] Attempting OCR with model: {model_name}")
                        response = client.models.generate_content(
                            model=model_name,
                            contents=[
                                file_payload, 
                                "Extract all readable text from this document perfectly. Output strictly the text without commentary."
                            ]
                        )
                        extracted_text += (response.text or "") + "\n"
                        success = True
                        break 
                    except Exception as model_err:
                        print(f"[STEP 1 WARNING] Model {model_name} failed on key. Error: {model_err}. Trying fallback model...")
                        time.sleep(1)
                        continue

                if success:
                    break
                    
            if not success:
                raise RuntimeError("All Gemini keys and model fallbacks failed or hit rate limits during text extraction.")

        if not extracted_text.strip():
            raise ValueError(f"No readable text found in {file_name}. Please upload clear study material.")

        print(f"[STEP 1 SUCCESS] Extracted {len(extracted_text)} characters from {file_name}.")
        return extracted_text

    except Exception as error:
        print(f"[STEP 1 ERROR] OCR/Extraction failed on {file_name}: {error}")
        raise RuntimeError(f"Text extraction failed on {file_name}: {str(error)}")

def build_llm_payload(saved_files_data: list) -> str:
    file_names = [f[1] for f in saved_files_data]
        
    is_valid, message = validate_files(file_names)
    if not is_valid:
        raise ValueError(message)  
    
    combined_text = ""
    
    # Process multiple files concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=maximum_files) as executor:
        future_to_file = {
            executor.submit(extract_text, file_path, file_name): file_name 
            for file_path, file_name in saved_files_data
        }
        
        for future in concurrent.futures.as_completed(future_to_file):
            try:
                result = future.result()
                combined_text += result + "\n\n"
            except Exception as exc:
                file_name = future_to_file[future]
                raise RuntimeError(f"Failed to process {file_name}: {exc}")
                
    return combined_text.strip()