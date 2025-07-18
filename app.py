from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
import traceback
import sys
import os
API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

app = Flask(__name__)


print("🔧 Configuring Gemini API...")
try:
    genai.configure(api_key=API_KEY)
    print("✅ API configured successfully")
except Exception as e:
    print(f"❌ API configuration failed: {e}")
    sys.exit(1)

print("🤖 Initializing model...")
try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("✅ Model initialized successfully")
except Exception as e:
    print(f"❌ Model initialization failed: {e}")
    sys.exit(1)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    
    print(f"🌐 Request method: {request.method}")
    
    if request.method == "POST":
        print("📝 Processing POST request...")
        
        # Debug form data
        print(f"📋 Form data: {dict(request.form)}")
        
        prompt = request.form.get("prompt", "").strip()
        print(f"💬 Extracted prompt: '{prompt}'")
        
        if not prompt:
            reply = "Please enter a message."
            print("⚠️ Empty prompt received")
        else:
            try:
                print(f"🚀 Sending to Gemini: '{prompt}'")
                
                # Test the API call
                response = model.generate_content(prompt)
                reply = response.text
                
                print(f"✅ Response received: '{reply[:100]}...'")
                
            except Exception as e:
                error_msg = str(e)
                print(f"🔥 DETAILED ERROR: {error_msg}")
                print("📋 FULL TRACEBACK:")
                traceback.print_exc()
                
                # Check for specific error types
                if "API_KEY_INVALID" in error_msg or "403" in error_msg:
                    reply = "❌ Invalid API key. Please check your Gemini API key."
                elif "QUOTA_EXCEEDED" in error_msg or "429" in error_msg:
                    reply = "❌ API quota exceeded. Please try again later."
                elif "BLOCKED" in error_msg:
                    reply = "❌ Content was blocked by safety filters."
                elif "PERMISSION_DENIED" in error_msg:
                    reply = "❌ Permission denied. Check your API key permissions."
                else:
                    reply = f"❌ Error: {error_msg}"
    
    return render_template("index.html", reply=reply)

# Test endpoint to verify API connectivity
@app.route("/api-test")
def api_test():
    try:
        print("🧪 Testing API connection...")
        response = model.generate_content("Say hello")
        return f"✅ API Test SUCCESS: {response.text}"
    except Exception as e:
        error_details = f"❌ API Test FAILED: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        print(error_details)
        return f"<pre>{error_details}</pre>"

# Debug endpoint to check form submission
@app.route("/debug", methods=["POST"])
def debug():
    return f"""
    <h2>Debug Info:</h2>
    <p><strong>Method:</strong> {request.method}</p>
    <p><strong>Form data:</strong> {dict(request.form)}</p>
    <p><strong>Prompt:</strong> '{request.form.get("prompt", "NOT FOUND")}'</p>
    """

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    try:
        response = model.generate_content(user_message)
        ai_reply = response.text
    except Exception as e:
        ai_reply = f"❌ Error: {str(e)}"
    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    print("🚀 Starting Flask app...")
    print("📍 Main app: http://127.0.0.1:5000/")
    print("📍 API test: http://127.0.0.1:5000/api-test")
    print("="*50)
    app.run(debug=True, host='127.0.0.1', port=5000)