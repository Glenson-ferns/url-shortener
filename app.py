import random
import string
from flask import Flask, request, redirect


app = Flask(__name__)

urls = {}

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

@app.route("/")
def home():
    return "URL shortener is running!"

@app.route("/shorten", methods=["POST"])
def shorten():
        data = request.get_json()
        long_url = data["url"]
        code = generate_code()
        urls[code] = long_url
        return {"short_url": f"http://127.0.0.1:5000/{code}"}



@app.route("/<code>")

def go(code):
    long_url = ulrs.get(code)
    if long_url is None:
        return "Not found", 404
    return redirect(long_url)

if __name__ == "__main__":
    app.run(debug=True)