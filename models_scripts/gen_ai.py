import os
import requests
import time

def generate_image(prompt: str, file_name: str = None) -> str:
    """Takes Mermaid.js diagram code and renders it as a perfect PNG flowchart using Kroki."""

    # Clean up the code in case the LLM wrapped it in markdown backticks
    mermaid_code = prompt.replace("```mermaid", "").replace("```", "").strip()

    # Use the free Kroki API to render the flowchart
    url = "https://kroki.io/mermaid/png"

    # Kroki accepts the raw diagram code directly
    response = requests.post(
        url,
        data=mermaid_code.encode('utf-8'),
        headers={"Content-Type": "text/plain"},
        timeout=30,
    )
    response.raise_for_status()

    # Kroki directly returns the raw image bytes
    image_bytes = response.content

    save_directory = ".web/public"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # If no custom file_name was passed, generate a dynamic timestamp filename
    if not file_name or file_name == "study_visual.png":
        file_name = f"study_visual_{int(time.time())}.png"

    output_path = os.path.join(save_directory, file_name)
    with open(output_path, "wb") as image_file:
        image_file.write(image_bytes)

    # Return the dynamic filename so the state/UI updates to the exact new image path
    return file_name