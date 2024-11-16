import pickle
import streamlit as st
import requests
import pandas as pd


def fetch_poster(movie_id):
    # Corrected the URL format and removed hardcoded movie_id
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=42f0c33fd3c9a559b7dc87c73c66be99'
    fallback_image_url = "https://via.placeholder.com/500x750?text=No+Image"

    for attempt in range(3):  # Try up to 3 times
        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')

            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return fallback_image_url

        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching poster on attempt {attempt + 1}: {e}")
            if attempt == 2:
                return fallback_image_url

    return fallback_image_url


def recommend(movie):
    try:
        movie_data = movies[movies['title'] == movie]
        if movie_data.empty:
            st.error("The selected movie is not available in our database.")
            return [], []

        index = movie_data.index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            poster = fetch_poster(movie_id)
            if poster:
                recommended_movie_posters.append(poster)
                recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return [], []


st.header('Movie Recommender System')

# Corrected the file path by removing extra spaces
movies = pickle.load(open('_movie_dict. pkl', 'rb'))
similarity = pickle.load(open('similarities.pkl', 'rb'))

if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    if recommended_movie_names and recommended_movie_posters:
        # Create a column layout based on the number of recommendations
        cols = st.columns(len(recommended_movie_names))

        for i, col in enumerate(cols):
            with col:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
    else:
        st.warning("No recommendations found.")
