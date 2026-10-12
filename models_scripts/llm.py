import os
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from groq import Groq

load_dotenv()

class Misconception(BaseModel):
    flawed_statement: str = Field(description="Exact quote of the flawed concept.")
    correction: str = Field(description="Factual correction and rationale.")

class QuizQuestion(BaseModel):
    question_text: str
    options: List[str] = Field(description="Multiple-choice options. Empty if none.")
    answer: str = Field(description="The correct answer and explanation.")

class AnalysisReport(BaseModel):
    misconceptions_corrections: List[Misconception] = Field(description="List of errors. Empty if none.")
    concise_notes: List[str] = Field(description="Bullet-point summary of key concepts.")
    quiz_questions: List[QuizQuestion]
    image_prompt: str = Field(
        description="Write a valid Mermaid.js flowchart (using 'graph TD') mapping out the core concepts of the text. Keep node text very short."
    )

def process_study_material(extracted_text: str, difficulty_level: str):
    yield {"status": "Sending extracted text to AI... (Hang tight!)"}
    
    SYSTEM_PROMPT = """
You are an expert educational analyst. Analyze the source text to summarize core concepts, identify factual misconceptions, and generate a difficulty-calibrated quiz.
Instructions:
1. Misconceptions: Scan for false or misleading statements. If found, quote the exact flawed statement and provide a brief, factual correction. If none exist, return an empty list.
2. Notes: Distill the material into dense, high-yield summary points. Omit conversational filler.
3. Quiz: Create 4-5 multiple-choice questions matching the requested Target Level. Provide concise explanations for the correct answers.
4. Visual Diagram: Write a valid Mermaid.js flowchart (graph TD) mapping the relationships between the core concepts. Use very short, punchy text inside the nodes. Output ONLY valid Mermaid syntax in this field.
5. Strict Formatting: Output strictly in the provided JSON schema. Do not use markdown wrappers.
"""
    
    user_payload = f"Target Level: {difficulty_level}\nSource Data:\n{extracted_text}"

    # Expanded cascade for 2026 free-tier models, plus your GROQ fix
    api_configs = [
        {"provider": "gemini", "key": os.getenv("MY_GEMINI_KEY"), "models": ["gemini-3.8-flash", "gemini-2.5-flash", "gemini-1.5-flash"]},
        {"provider": "gemini", "key": os.getenv("GEMINI_KEY"), "models": ["gemini-3.8-flash", "gemini-2.5-flash", "gemini-1.5-flash"]},
        {"provider": "gemini", "key": os.getenv("ANSA_GEMINI_KEY"), "models": ["gemini-3.8-flash", "gemini-2.5-flash", "gemini-1.5-flash"]},
        {"provider": "groq", "key": os.getenv("MY_GROQ_KEY"), "models": ["llama-3.1-8b-instant"]},
        {"provider": "groq", "key": os.getenv("GROQ_KEY"), "models": ["llama-3.1-8b-instant"]},
        {"provider": "groq", "key": os.getenv("AMINA_GROQ_KEY"), "models": ["llama-3.1-8b-instant"]},
    ]

    last_error_message = "No specific error captured."

    for config in api_configs:
        if not config["key"]:
            continue
            
        for model_name in config["models"]:
            try:
                msg = f"Connecting to {config['provider'].capitalize()} ({model_name})..."
                print(f"[STEP 2 TRYING] {msg}")
                yield {"status": msg}

                if config["provider"] == "gemini":
                    client = genai.Client(api_key=config["key"])
                    response = client.models.generate_content(
                        model=model_name,
                        contents=user_payload,
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_PROMPT,
                            temperature=0.2,
                            response_mime_type="application/json",
                            response_schema=AnalysisReport,
                        ),
                    )
                    raw_json = response.text

                elif config["provider"] == "groq":
                    groq_client = Groq(api_key=config["key"])
                    completion = groq_client.chat.completions.create(
                        model=model_name,
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": user_payload},
                        ],
                        temperature=0.2,
                        response_format={
                            "type": "json_schema",
                            "json_schema": {
                                "name": "analysis_report",
                                "strict": True,
                                "schema": AnalysisReport.model_json_schema(),
                            },
                        },
                    )
                    raw_json = completion.choices[0].message.content

                success_msg = f"Resolved via {config['provider'].capitalize()}! Generating notes..."
                print(f"[STEP 2 SUCCESS] {success_msg}")
                yield {"status": success_msg}
                yield {"result": AnalysisReport.model_validate_json(raw_json)}
                return

            except Exception as e:
                last_error_message = f"{config['provider']} ({model_name}) error: {str(e)}"
                print(f"[STEP 2 WARNING] {last_error_message}")
                continue
    
    # If it completely fails, this will now spit the exact raw error out to the red text on your UI
    raise ValueError(f"All API keys failed. Last captured error: {last_error_message}")