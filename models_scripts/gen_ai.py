import base64
import zlib

def generate_image(prompt: str) -> str:
    """Encodes Mermaid.js code directly into a Kroki URL to render immediately in the browser."""
    # Clean up markdown formatting
    mermaid_code = prompt.replace("```mermaid", "").replace("```", "").strip()

    # Compress the code using zlib (deflate) as required by Kroki GET specification
    compressed = zlib.compress(mermaid_code.encode('utf-8'))
    
    # URL-safe Base64 encoding
    encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')

    # Return direct CDN URL for direct browser rendering
    return f"https://kroki.io/mermaid/svg/{encoded}"