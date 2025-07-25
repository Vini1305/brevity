from flask import Blueprint, request, jsonify, render_template
import os
import ollama
from dotenv import load_dotenv
from brevity.fetch_texts import fetch_text_from_url
import logging

logger = logging.getLogger(__name__)

load_dotenv() #Loads all the keys from .env file

bp = Blueprint('summary', __name__, url_prefix='/')

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/summarize", methods=["POST"])
def summarize():
    logger.info("Received summarize request")

    data = request.get_json()
    logger.debug(f"Request JSON: {data}")

    if not data:
        logger.warning("Missing JSON body")
        return jsonify({"error": "Missing JSON body"}), 400

    text = data.get("text") #You can send raw texts
    url = data.get("url") #Or urls

    # If URL provided, fetch article text
    if url:
        logger.info(f"Fetching text from URL: {url}")
        text = fetch_text_from_url(url)
    elif len(text) > 5000:
        logger.warning("Text too long")
        return jsonify({"error": "Text is longer than expected"}), 400

    if not text:
        logger.warning("No text or valid URL provided")
        return jsonify({"error": "No text or valid URL provided"}), 400

    # Call Ollama
    try:
        logger.info("Calling Ollama.chat...")
        context = []
        ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        client = ollama.Client(host=ollama_host)
        #the context is passed to ollama as a list of dicts (role and content)
        context.append({'role':'user', 'content':f'You have to summarize the following. Be objective and clean:\n{text}'})
        response = ollama.chat(model="gemma3:1b", messages=context, keep_alive=-1)
        summary = response['message']['content']
        logger.info("Got summary successfully")
        return jsonify({"summary": summary})

    except Exception as e:
        logger.exception("Error while calling Ollama")
        return jsonify({"error": f"API error: {e}"}), 500