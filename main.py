from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai
import os

# Set your OpenAI API key
openai.api_key = "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"

app = Flask(__name__)

# Configure MongoDB connection
app.config["MONGO_URI"] = "mongodb+srv://aribali1804:R7YX60qx4JlvtdbR@yt.twdwa.mongodb.net/chatgpt"
mongo = PyMongo(app)

@app.route("/")
def home():
    """Render the home page with chat history."""
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats=myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    """Handle API requests for Q&A."""
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        if not question:
            return jsonify({"error": "Question not provided"}), 400
        
        # Check if the question already exists in the database
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            return jsonify({"question": question, "answer": chat["answer"]})

        # Define conversation context for the OpenAI API
        messages = [
            {"role": "system", "content": "You are an AI that provides creative and helpful responses."},
            {"role": "user", "content": question},
        ]

        # Make the API call to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with "gpt-4" if needed
            messages=messages,
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # Extract the assistant's response
        answer = response["choices"][0]["message"]["content"]

        # Save the question and answer to the database
        mongo.db.chats.insert_one({"question": question, "answer": answer})

        return jsonify({"question": question, "answer": answer})

    # Default response for GET requests
    return jsonify({"result": "Welcome to the ChatGPT API! Use POST to ask questions."})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
