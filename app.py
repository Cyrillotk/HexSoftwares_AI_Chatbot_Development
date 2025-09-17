from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# app = Flask(__name__)

# # Replace with your OpenAI API key
# client = OpenAI(api_key="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")
import os

openai_api_key = os.getenv("OPENAI_API_KEY")

print(openai_api_key)  # optional: just to check it loaded


# Serve HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Handle chat messages
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    
    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": user_input}
        ]
    )
    
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
