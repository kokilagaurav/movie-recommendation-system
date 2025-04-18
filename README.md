# Movie Recommendation System

This project is a **Movie Recommendation System** built with Python and [Streamlit](https://streamlit.io/). It provides personalized movie recommendations based on a selected movie from a list.

## Overview

The system uses a precomputed similarity matrix to suggest movies that are similar to the one chosen by the user. The recommendations are displayed in a simple and interactive web interface powered by Streamlit.

## Features

- **Interactive UI:** Users can select a movie from a dropdown list.
- **Personalized Recommendations:** The system suggests the top 5 movies similar to the selected one.
- **Easy to Use:** No prior setup required for the user, just run the app and start exploring recommendations.

## How It Works

1. **Data Loading:** The app loads a list of movies and a similarity matrix from pickled files (`movie_list.pkl` and `similarity.pkl`).
2. **User Selection:** The user selects a movie from the dropdown menu.
3. **Recommendation Engine:** The app finds the most similar movies using the similarity matrix and displays them.
4. **Display:** Recommendations are shown directly in the Streamlit web interface.

## Requirements

- Python 3.x
- Streamlit
- NLTK
- Pandas (for DataFrame operations)
- Pickle (for loading data)

## How to Run

1. Install the required packages:
    ```bash
    pip install streamlit nltk pandas
    ```
2. Make sure `movie_list.pkl` and `similarity.pkl` are present in the project directory.
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## File Structure

- `app.py` : Main application file containing the Streamlit UI and recommendation logic.
- `movie_list.pkl` : Pickled DataFrame containing movie titles.
- `similarity.pkl` : Pickled similarity matrix for movie recommendations.

---

Feel free to explore and enhance the recommendation logic or the user interface!
