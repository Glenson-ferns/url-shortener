import random
import string
import sqlite3
from flask import Flask, request, redirect


app = Flask(__name__)


#urls = {} # in memory storage office , if the server stops everything will be lost as of now.  

DB_FILE = "urls.db"


def init_db():
#connect opens the file, and creates it if it doesn't exit yet
    conn = sqlite3.connect(DB_FILE)

    conn.execute(
        "CREATE TABLE IF NOT EXISTS URLs ("
        "code Text Primary KEY, " # primary key = each code must be unique 
        "long_url TEXT NOT NULL)" # not null = a url is required
    )

    conn.commit() # commit () makes the changes permanent on disk
    conn.close()



def save_url(code, long_url):
    conn = sqlite3.connect(DB_FILE)
    conn.execute("INSERT INTO urls (code, long_url) VALUES (?,?)",(code, long_url))
    conn.commit()
    conn.close()


def find_url(code):
    conn = sqlite3.connect(DB_FILE)
    row = conn.execute("SELECT long_url FROM urls WHERE code = ?",(code,)).fetchone()
    conn.close()
    #fetchone() returns one row element(a tuple) or None if nothing matched
    return row[0] if row else None


def generate_code(length=6):
    # allowed characters {a-z,A-Z,0-9}
    chars = string.ascii_letters + string.digits
    # joining characters/ numbers
    return "".join(random.choice(chars) for _ in range(length))

@app.route("/")
def home():
    # check to confirm the server is up
    return "URL shortener is running!"

@app.route("/shorten", methods=["POST"])
def shorten():
    # read the JSON body sent by the client e.g {"url" : "https://google.com"}
        data = request.get_json(silent=True)

        # reject request iwth no body or url key
        if not data or "url" not in data:
            return {"error": 'Send JSON like {"url": "https://example.com"}'},400
        long_url = data["url"].strip() # strip() removes spaces around the text

        # if it doens't start with http:// or https://, add https://
        if not long_url.startswith(("http://", "https://")):
            long_url = "https://" + long_url


        # make a random code and remember which URL it belongs to
        code = generate_code()
        save_url(code, long_url)

        #send back to short link as JSON
        return {"short_url": f"http://127.0.0.1:5000/{code}"}



@app.route("/<code>")

def go(code):
    long_url = find_url(code)
    if long_url is None:
        return "Not found", 404
        # goes back to original URL
    return redirect(long_url)

init_db() # runs onces whenever the app starts, before any request

if __name__ == "__main__":
    # only runs when you start this file directly
    app.run(debug=True)