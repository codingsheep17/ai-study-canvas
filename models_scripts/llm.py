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

    api_configs = [
        {"provider": "gemini", "key": os.getenv("MY_GEMINI_KEY"), "model": "gemini-3.8-flash"},
        {"provider": "gemini", "key": os.getenv("GEMINI_KEY"), "model": "gemini-3.8-flash"},
        {"provider": "gemini", "key": os.getenv("ANSA_GEMINI_KEY"), "model": "gemini-3.8-flash"},
        {"provider": "groq", "key": os.getenv("MY_GROQ_KEY"), "model": "llama-3.1-8b-instant"},
        {"provider": "groq", "key": os.getenv("GROQ_KEY"), "model": "llama-3.1-8b-instant"},
        {"provider": "groq", "key": os.getenv("AMINA_GROK_KEY"), "model": "llama-3.1-8b-instant"},
    ]

    for config in api_configs:
        if not config["key"]:
            continue
            
        try:
            msg = f"Connecting to {config['provider'].capitalize()}... (This will take a little bit)"
            print(f"[STEP 2 TRYING] {msg}")
            yield {"status": msg}

            if config["provider"] == "gemini":
                client = genai.Client(api_key=config["key"])
                response = client.models.generate_content(
                    model=config["model"],
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
                    model=config["model"],
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

            # API Success
            success_msg = f"Resolved via {config['provider'].capitalize()}! Generating notes..."
            print(f"[STEP 2 SUCCESS] {success_msg}")
            yield {"status": success_msg}
            
            yield {"result": AnalysisReport.model_validate_json(raw_json)}
            return

        except Exception as e:
            print(f"[STEP 2 WARNING] {config['provider']} ({config['model']}) failed: {e}")
            continue
    
    raise ValueError("All API keys and fallback pipelines failed to generate a response.")