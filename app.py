import streamlit as st
import pickle
import pandas as pd
from datetime import datetime

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]  # distances will be in array form
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)  # making dataframe

# Load similarity data
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to add background using an online image URL
def add_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to add a background
add_background("https://repository-images.githubusercontent.com/561222312/74f85590-f324-4f86-895d-539fcc577289")  # Use a direct link to the image


st.markdown("""
    <style>
    .stApp h1 {
        color: white;
        text-shadow: 1px 1px 2px black;
    }
    </style>
""", unsafe_allow_html=True)


# Title
st.title("Movie Recommender System")

st.markdown("""
    <style>
    /* Make the title white */
    .stApp h1 {
        color: white;
        text-shadow: 1px 1px 2px black;
    }

    /* Make all label texts white */
    .stApp label {
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)
# Selectbox for selecting movie
selected_movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values)

# Button to get recommendations
if st.button("RECOMMEND"):
    recommendations = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")
    for i in recommendations:
        st.write(i)

# Feedback Section
st.markdown("""
    <style>
    /* Title color */
    .stApp h1 {
        color: white;
        text-shadow: 1px 1px 2px black;
    }

    /* Subheader color */
    .stApp h3 {
        color: white;
        text-shadow: 1px 1px 2px black;
    }

    /* Label color (like for selectbox) */
    .stApp label {
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)
st.subheader("Any Suggestion:")
feedback = st.text_area("Feedback", "")

# Submit button for feedback
if st.button("Submit Feedback"):
    if feedback:
        # Save feedback with timestamp
        with open('feedback.txt', 'a') as f:
            f.write(f"{datetime.now()}: {feedback}\n")
        st.success("Thank you for your feedback!")
    else:
        st.error("Please enter your feedback before submitting.")
