document.getElementById("summarize-btn").addEventListener("click", async () => {
    const input = document.getElementById("input-text").value.trim();
    const resultBox = document.getElementById("result");
    resultBox.classList.remove("d-none");
    resultBox.innerHTML = `
        <div class="d-flex align-items-center justify-content-center">
            <div class="spinner-border text-light me-2" role="status"></div>
            <span>Summarizing...</span>
        </div>
        `;

    if (!input) {
    resultBox.innerHTML = "⚠️ Please enter some text or a URL.";
    return;
    }

    // Detect if it's a URL (basic check)
    const isUrl = input.startsWith("http://") || input.startsWith("https://");

    const payload = isUrl ? { url: input } : { text: input };

    try {
    const response = await fetch("/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (data.summary) {
        resultBox.innerHTML = `<strong>Summary:</strong><br>${data.summary}`;
    } else {
        resultBox.innerHTML = `⚠️ Error: ${data.error || "Unknown error"}`;
    }
    } catch (err) {
    resultBox.innerHTML = `❌ Request failed: ${err}`;
    }
});
