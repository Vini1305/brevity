def test_index_page(client):
    # Check if the frontend loads
    response = client.get("/")
    assert response.status_code == 200
    assert b"Brevity" in response.data  # Page contains the app name

def test_summarize_with_text(client, monkeypatch):
    # Ensure dummy env so it won't crash
    import os
    os.environ["OLLAMA_MODEL"] = "dummy-model"

    # Fake Ollama response
    def fake_chat(model, messages, keep_alive=-1):
        assert model == "dummy-model"  # sanity check
        return {"message": {"content": "This is a fake summary."}}

    # Patch EXACT module used by Flask
    monkeypatch.setattr("brevity.summary.ollama.chat", fake_chat)

    payload = {"text": "Some long input text"}
    response = client.post("/summarize", json=payload)

    assert response.status_code == 200
    data = response.get_json()
    assert data["summary"] == "This is a fake summary."

def test_summarize_with_missing_input(client):
    # Should return error if no text/url provided
    response = client.post("/summarize", json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
