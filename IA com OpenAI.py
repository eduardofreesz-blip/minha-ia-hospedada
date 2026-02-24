import openai
from flask import Flask, request, jsonify

openai.api_key = "SUA_CHAVE_OPENAI"

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content": msg}]
    )
    response = completion.choices[0].message.content
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
