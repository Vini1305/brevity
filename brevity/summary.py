from flask import Blueprint, request, jsonify, render_template
import os
import ollama
from dotenv import load_dotenv
from brevity.fetch_texts import fetch_text_from_url

load_dotenv() #Loads all the keys from .env file

bp = Blueprint('summary', __name__, url_prefix='/')

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    text = data.get("text") #You can send raw texts
    url = data.get("url") #Or 

    # If URL provided, fetch article text
    if url:
        text = fetch_text_from_url(url)

    if not text:
        return jsonify({"error": "No text or valid URL provided"}), 400

    # Call Ollama
    try:
        context = []
        #the context is passed to ollama as a list of dicts (role and content)
        context.append({'role':'user', 'content':f'You have to summarize the following. Be objective and clean:\n{text}'})
        response = ollama.chat(model=os.getenv("OLLAMA_MODEL"), messages=context, keep_alive=-1)
        summary = response['message']['content']

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": f"OpenAI API error: {e}"}), 500