from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("data/colleges.csv")


# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# FILTER COLLEGES
# -------------------------
@app.route("/filter", methods=["POST"])
def filter_colleges():
    data = request.json

    rank = int(data.get("rank", 0))
    branch = data.get("branch", "")

    filtered = df[
        (df["cutoff_rank"] >= rank) &
        (df["branch"] == branch)
    ]

    return jsonify(filtered.to_dict(orient="records"))


# -------------------------
# CHATBOT ROUTE
# -------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()

    # SIMPLE CHATBOT LOGIC (can later connect ai/chatbot.py)
    if "cse" in message:
        result = df[df["branch"] == "CSE"].head(5)
        reply = result.to_dict(orient="records")

    elif "ece" in message:
        result = df[df["branch"] == "ECE"].head(5)
        reply = result.to_dict(orient="records")

    elif "eee" in message:
        result = df[df["branch"] == "EEE"].head(5)
        reply = result.to_dict(orient="records")

    elif "it" in message:
        result = df[df["branch"] == "IT"].head(5)
        reply = result.to_dict(orient="records")

    elif "top" in message:
        result = df.sort_values(by="cutoff_rank").head(5)
        reply = result.to_dict(orient="records")

    else:
        reply = "I can help you find colleges by branch (CSE, ECE, EEE, IT) or rank."

    return jsonify({"reply": reply})


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)