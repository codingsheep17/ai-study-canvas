from datavalidator import build_llm_payload
from models_scripts.llm import process_study_material
from gen_ai import generate_image

def test_pipeline():
    # Step 1: Provide a dummy file to test. 
    # (Put a real PDF or image in your project folder and update this name)
    test_files = [
        ("img.jfif", "img.jfif") 
    ]
    
    print("--- STEP 1: Extracting Text ---")
    extracted_text = build_llm_payload(test_files)
    print(f"Extraction successful! Found {len(extracted_text)} characters.\n")
    
    print("--- STEP 2: Running LLM Analysis ---")
    report = process_study_material(extracted_text, difficulty_level="Intermediate") #difficulty level setup
    print("Found Misconceptions:", len(report.misconceptions_corrections))
    print("Generated Notes:", len(report.concise_notes))
    print("Generated Quiz Questions:", len(report.quiz_questions))
    print(f"Generated Image Prompt: {report.image_prompt}\n")
    
    print("--- STEP 3: Generating Image via Cloudflare ---")
    image_path = generate_image(report.image_prompt)
    print(f"Success! Image saved to: {image_path}")

# Run the test
if __name__ == "__main__":
    test_pipeline()