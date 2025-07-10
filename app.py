from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)
model = joblib.load("fake_review_detector.pkl")

# Temporary fake extractor
def extract_review_text_from_link(link):
    # In real case, scrape review from the link using BeautifulSoup
    return "This is an example extracted review from the URL."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        link = request.form["link"]

        # Extract review from the link (fake logic for now)
        review_text = extract_review_text_from_link(link)

        prediction = model.predict([review_text])[0]
        result = "Fake Review ❌" if prediction == 1 else "Genuine Review ✅"
        return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)

