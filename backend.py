from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    entity = data['entity']
    custom_prompt = data['prompt']
    search_query = custom_prompt.replace("{entity}", entity)

    params = {
        "q": search_query,
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": 1
    }
    response = requests.get("https://serpapi.com/search", params=params)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Search API failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
