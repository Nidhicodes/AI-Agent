import requests
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def fetch_web_results(entity, prompt):
    """Fetch web results for a given entity and prompt."""
    response = requests.post("http://localhost:5000/search", json={"entity": entity, "prompt": prompt})
    return response.json() if response.status_code == 200 else None

def parse_results_with_llm(results, entity, custom_prompt):
    full_prompt = custom_prompt.replace("{entity}", entity).replace("{results}", results)
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": full_prompt}],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Error with Groq API call: {e}")
        return None
