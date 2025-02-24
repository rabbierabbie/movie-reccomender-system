import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=71bf617720a615953b86e66a7fb9891d'.format(movie_id))
    data=response.json()
    return 'http://image.tmdb.org/t/p/w500/'+data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    L = []
    posters=[]
    for i in movies_list:
        L.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return L,posters

movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
"How would you like to be contacted?",
movies['title'].values,
)

if st.button("Recommend"):
    r,p=recommend(selected_movie_name)
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(r[0])
        st.image(p[0])

    with col2:
        st.text(r[1])
        st.image(p[1])

    with col3:
        st.text(r[2])
        st.image(p[2])

    with col4:
        st.text(r[3])
        st.image(p[3])

    with col5:
        st.text(r[4])
        st.image(p[4])