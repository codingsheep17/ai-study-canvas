import os
import time
import requests

def generate_image(prompt: str, file_name: str = None) -> str:
    """Takes Mermaid.js diagram code and renders it as a PNG flowchart using Kroki."""

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

    # Generate unique timestamped filename to prevent browser caching
    if not file_name or file_name == "study_visual.png":
        file_name = f"study_visual_{int(time.time())}.png"

    # Save directly to the static assets directory
    save_directory = "assets"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    output_path = os.path.join(save_directory, file_name)
    with open(output_path, "wb") as image_file:
        image_file.write(image_bytes)

    return file_name