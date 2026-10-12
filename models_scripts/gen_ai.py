import os
import requests
import time
import reflex as rx

def generate_image(prompt: str, file_name: str = None) -> str:
    """Takes Mermaid.js diagram code and renders it as a perfect PNG flowchart using Kroki."""

    mermaid_code = prompt.replace("```mermaid", "").replace("```", "").strip()
    url = "https://kroki.io/mermaid/png"

    response = requests.post(
        url,
        data=mermaid_code.encode('utf-8'),
        headers={"Content-Type": "text/plain"},
        timeout=30,
    )
    response.raise_for_status()
    image_bytes = response.content

    # Generate the unique dynamic filename
    if not file_name or file_name == "study_visual.png":
        file_name = f"study_visual_{int(time.time())}.png"

    # CRITICAL FIX: Save to Reflex's dynamic runtime folder, NOT .web/public
    save_directory = rx.get_upload_dir()
    
    output_path = os.path.join(save_directory, file_name)
    with open(output_path, "wb") as image_file:
        image_file.write(image_bytes)

    return file_name