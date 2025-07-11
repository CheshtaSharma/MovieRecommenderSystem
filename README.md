# 🎬 Movie Recommender System

A content-based movie recommendation web app powered by machine learning. Just enter the name of a movie, and the app will suggest 5 similar movies using cosine similarity on feature vectors.

## 🚀 Features

- Recommends 5 similar movies based on input title
- Machine Learning–powered content-based filtering
- Vectorization of movie metadata using [CountVectorizer / TF-IDF]
- Streamlit-based web UI for real-time interaction
- Optionally integrates with TMDB API for posters

## 🧠 ML Approach

- Preprocessed metadata (title, genre, keywords, etc.)
- Combined textual features into a single string
- Applied [CountVectorizer / TF-IDF] to generate feature vectors
- Computed cosine similarity between all movies
- Returned top 5 most similar movies to the user input

## 🛠 Tech Stack

- **Python**
- **scikit-learn** – for vectorization and cosine similarity
- **pandas, numpy** – for data handling
- **Streamlit** – for web app
- **TMDB API** (optional) – for poster images


## 🌐 Live Demo

[🔗 Try the live version](https://huggingface.co/spaces/cheshtasharma/mrs) 

## 📁 Setup Instructions

```bash
git clone https://github.com/CheshtaSharma/MovieRecommenderSystem.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py

