# BookLens — ML-Powered Book Recommendation System

A Flask web application that recommends books using collaborative filtering on a dataset of 270,000+ books.

## Features

- **Top 50 Books** — most popular books ranked by real user ratings and vote counts
- **Book Recommendations** — enter a title and get similar books based on reader behavior patterns

## How It Works

Uses **Collaborative Filtering** with cosine similarity — no external API or LLM involved.

1. A user-book ratings matrix (pivot table) is built from the Book-Crossing dataset
2. Cosine similarity scores are pre-computed between all books in the model
3. When a title is entered, the top N most similar books are returned based on shared readership patterns

All model data is stored in pre-computed `.pkl` files, so the app runs fully offline.

## Tech Stack

- **Backend** — Python, Flask
- **ML** — scikit-learn (cosine similarity), NumPy, Pandas
- **Frontend** — HTML, CSS, Bootstrap 3, Inter (Google Fonts)
- **Dataset** — Book-Crossing dataset (270,000+ books, real user ratings)

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
git clone https://github.com/eknoorsingh007/BookLens.git
cd BookLens
pip install -r requirements.txt
```

### Run

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Project Structure

```
BookLens/
├── app.py                   # Flask application and routes
├── templates/
│   ├── index.html           # Home page — Top 50 books
│   └── recommend.html       # Recommendation page
├── books.pkl                # Full books dataset
├── popular.pkl              # Pre-computed top 50 popular books
├── pt.pkl                   # User-book ratings pivot table
├── similarity_scores.pkl    # Pre-computed cosine similarity matrix
├── requirements.txt
└── .gitignore
```

## Contributors

- **Eknoor Singh**
- **Vipul**
- **Tarun Gupta**
