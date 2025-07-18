# Gemini AI Assistant

Your intelligent AI companion for insightful conversations, file uploads, and more—powered by Google Gemini.

---

## 🚀 Overview

**Gemini AI Assistant** is a modern, full-stack chatbot web application built with Flask and Google Gemini (Generative AI). It features:
- Natural language chat with Gemini AI
- Persistent chat history (per user, in sidebar)
- Multiple conversations (switch, delete, start new)
- File and image upload (see and download in chat)
- Responsive, beautiful UI with sidebar slider

---

## ✨ Features
- **Conversational AI:** Chat with Gemini for answers, explanations, and more
- **Chat History:** Sidebar menu with all your previous chats, easy switching
- **Clear Chat:** Clear messages in the current chat only
- **File Upload:** Upload images, PDFs, and documents; view/download in chat
- **Modern UI:** Responsive, sidebar slider, upload icon, and more
- **API Test:** Built-in endpoint to test Gemini API connectivity

---

## 🛠️ Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/TahaSaadat680/gemini-ai-assistant.git
   cd gemini-ai-assistant
   ```

2. **Create a virtual environment (recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Create a `.env` file and add your Gemini API key:
     ```env
     GEMINI_API_KEY=your-gemini-api-key-here
     ```
   - Or edit `app.py` to use your API key directly (not recommended for production).

5. **Run the app:**
   ```sh
   python app.py
   ```
   Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## ⚙️ Deployment

- **Production:**
  - Use [Render](https://render.com/), [Railway](https://railway.app/), [PythonAnywhere](https://www.pythonanywhere.com/), or [Heroku](https://heroku.com/).
  - Use `gunicorn` for production serving:
    ```sh
    gunicorn app:app
    ```
  - Set environment variables for your API key and secret key.

- **Expose Locally:**
  - Use [ngrok](https://ngrok.com/) for a public URL:
    ```sh
    ngrok http 5000
    ```

---

## 🔑 Environment Variables
- `GEMINI_API_KEY` — Your Google Gemini API key
- `SECRET_KEY` — Flask secret key (for sessions)

---

## 📁 File Uploads
- Uploaded files are stored in the `uploads/` directory.
- Images and documents are shown in chat and can be downloaded.
- (For production, use cloud storage for uploads.)

---

## 📝 Usage
- Start a new chat or select a previous chat from the sidebar.
- Type your message and press send.
- Upload files/images using the paperclip icon.
- Clear the current chat with the trash icon.
- Delete or switch chats from the sidebar.

---

## 🧑‍💻 Credits
- **Developed by:** Taha Saadat
- **AI Model:** Google Gemini (Generative AI)
- **UI:** Custom, inspired by modern chat apps

---

## 📜 License
This project is licensed under the MIT License.
