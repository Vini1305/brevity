````markdown
# Brevity 📰✨

Brevity is a simple **AI-powered article summarizer**.  
Paste a URL or some text, and it instantly gives you a **clear, concise summary**.  

---

## 🚀 Features

✅ Summarizes long articles into a few sentences  
✅ Works with **URLs or plain text**  
✅ Clean and minimal UI  
✅ Powered by **OpenAI GPT models**  
✅ Mobile-friendly  

---

## 🖼️ Preview

<!-- Add a screenshot or GIF of the app -->
![Brevity Screenshot](./assets/preview.png)

---

## 🛠️ Tech Stack

- **Frontend:** Jinja2 + Bootstrap  
- **Backend:** Flask
- **AI:** OpenAI GPT API  
- **Deployment:** Vercel
- **Self-hosting:** Docker

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/Vini1305/brevity.git
cd brevity
python -m venv venv
source venv/bin/activate   # On Linux/Mac
# OR
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
````

Create a `.env` file with your API key:

```env
OPENAI_API_KEY=your-key-here
FLASK_ENV=development
```

Run the development server:

```bash
flask --app brevity run
```

Then open http://localhost:5000 in your browser.

---

## 💡 How It Works

1. User enters a URL or text
2. The app fetches the article content (if a URL is given)
3. Sends the text to the **OpenAI API** with a summarization prompt
4. Displays a **concise summary**

<!-- Add a small diagram or flow image here -->

![How It Works](./assets/flow.png)

---

## 🔑 Environment Variables

| Variable         | Description         |
| ---------------- | ------------------- |
| `OPENAI_API_KEY` | Your OpenAI API key |
| `FLASK_ENV`      | Your Flask Env here |

---

## 🤝 Contributing

Pull requests are welcome!
If you’d like to suggest features, open an issue.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vinícius de Paula**

* [LinkedIn](www.linkedin.com/in/vinícius-de-paula-5076991b0)
* [Medium](https://medium.com/@vinicius.13052002)
