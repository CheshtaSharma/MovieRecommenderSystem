# 🎬 Movie Recommender System

A content-based movie recommendation web app built using Python and Streamlit. Just enter the name of a movie and get 5 similar movies instantly!

## 🚀 Features

- Suggests 5 similar movies based on input
- Uses cosine similarity on movie feature vectors
- Clean, simple UI built with Streamlit
- Integrated with TMDB API for fetching posters (optional)

## 🛠 Tech Stack

- Python
- pandas, numpy
- scikit-learn
- Streamlit
- TMDB API (for posters)

## 🌐 Live Demo

[Click here to try it out!](https://huggingface.co/spaces/cheshtasharma/mrs) 

## 🧠 How it works

1. Vectorizes movie features (title, genre, keywords, etc.)
2. Computes cosine similarity between movies
3. Returns top 5 similar movies based on the selected one

## 📁 Setup Instructions

```bash
git clone https://github.com/CheshtaSharma/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
