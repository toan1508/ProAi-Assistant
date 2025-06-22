from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("chatai.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    reply = "👋 Xin chào! Đây là phản hồi thử nghiệm."
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
