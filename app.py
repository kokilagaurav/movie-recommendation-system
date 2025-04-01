import streamlit as st
import nltk

import pickle

from nltk.metrics.aline import similarity_matrix


def recommend(movie):
    try:
        movie = movie.lower()
        index = movies_list[movies_list['title'].str.lower() == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

        recommended_movie = []
        for i in distances[1:6]:
            recommended_movie.append(f"- {movies_list.iloc[i[0]].title.title()}")
        return recommended_movie

    except IndexError:
        print("Movie not found in the database")



movies_list = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
print(movies_list)

st.title("Movie Recommendation system")

selected_movie_name = st.selectbox(
    'Select a movie:',  # Label
    movies_list['title'].values  # List of options
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)