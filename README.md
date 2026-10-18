<div align="center">

# 🔗 URL Shortener

**A small Flask app that turns long links into short ones and redirects them.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/status-learning%20project-blue)

</div>

---

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Limitations](#-limitations)
- [Roadmap](#-roadmap)
- [What I Learned](#-what-i-learned)
- [Author](#-author)

---

## 📌 About

This project takes a long URL and gives back a short link such as `http://127.0.0.1:5000/aB3xY9`. When someone opens the short link, they are redirected to the original page.

I built it to learn Python, Flask, SQLite and Git. It runs on your own computer and is not ready for the public internet yet.

## ✨ Features

- Generates a random 6-character code for any link
- Stores links in a SQLite database, so they survive server restarts
- Redirects short links to the original page
- Adds `https://` automatically when it is missing
- Returns a clear JSON error for bad requests instead of crashing

## 🛠 Tech Stack

| Tool | Purpose |
| --- | --- |
| [Python 3](https://www.python.org/) | Programming language |
| [Flask](https://flask.palletsprojects.com/) | Web framework for the routes |
| [SQLite](https://www.sqlite.org/) | Database stored in a single file |
| [Git](https://git-scm.com/) and [GitHub](https://github.com/) | Version control |

## 🚀 Getting Started

### Prerequisites

- Python 3
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/url-shortener.git
   cd url-shortener
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   > Using the fish shell? Run `source .venv/bin/activate.fish` instead.

3. **Install Flask**

   ```bash
   pip install flask
   ```

4. **Start the server**

   ```bash
   python app.py
   ```

   The app is now running at `http://127.0.0.1:5000`. Keep this terminal open.

## 💻 Usage

Open a second terminal and send a link to the app:

```bash
curl -X POST http://127.0.0.1:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com"}'
```

Response:

```json
{
  "short_url": "http://127.0.0.1:5000/aB3xY9"
}
```

Open the short URL in your browser and you will be redirected to the original page.

You can also leave out the `https://` and the app will add it:

```bash
curl -X POST http://127.0.0.1:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "wikipedia.org"}'
```

## 📡 API Reference

### `GET /`

Returns a message to confirm the server is running.

### `POST /shorten`

Creates a short link.

**Request body**

```json
{ "url": "https://example.com" }
```

**Responses**

| Status | Meaning | Body |
| --- | --- | --- |
| `200 OK` | Link created | `{"short_url": "http://127.0.0.1:5000/<code>"}` |
| `400 Bad Request` | Missing or invalid JSON, or no `url` key | `{"error": "Send JSON like {\"url\": \"https://example.com\"}"}` |

### `GET /<code>`

Redirects to the original URL.

| Status | Meaning |
| --- | --- |
| `302 Found` | Redirects to the original URL |
| `404 Not Found` | The code does not exist |

## 📂 Project Structure

```
url-shortener/
├── app.py          # routes, database code and validation
├── urls.db         # SQLite database (created automatically, ignored by Git)
├── .gitignore      # skips .venv, __pycache__ and urls.db
└── README.md
```

## ⚙️ How It Works

```
POST /shorten  ──►  validate URL  ──►  generate code  ──►  save in SQLite  ──►  return short link
GET  /<code>   ──►  look up code in SQLite  ──►  redirect to the original URL
```

1. A client sends a long URL to `/shorten`.
2. The app checks the input and adds `https://` if needed.
3. It creates a random code from letters and digits and saves the pair in the `urls` table.
4. When someone visits `/<code>`, the app looks the code up and redirects the browser.

The database has one table:

| Column | Type | Notes |
| --- | --- | --- |
| `code` | TEXT | Primary key, unique |
| `long_url` | TEXT | Required |

## ⚠️ Limitations

- Short links only work on your own computer, because the address is `127.0.0.1`.
- The same URL gets a new code every time it is shortened.
- If a random code already exists, saving fails (very rare).
- Flask's built-in server is meant for learning, not real traffic.

## 🗺 Roadmap

- [x] Create short codes and redirect
- [x] Store links in SQLite
- [x] Validate input and add `https://` automatically
- [ ] Simple web page with a text box and a button
- [ ] `requirements.txt`
- [ ] Retry when a generated code already exists
- [ ] Reuse the code for a repeated URL
- [ ] Click counting and link expiry
- [ ] Deploy online

## 📚 What I Learned

- Setting up a Python project with a virtual environment
- Building routes and returning JSON with Flask
- Storing data in SQLite, and why SQL needs `?` placeholders
- Testing an API from the terminal with `curl`
- Using Git and GitHub from the command line

