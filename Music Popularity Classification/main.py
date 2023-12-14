import streamlit as st
import pandas as pd
import pickle
import sklearn




pipe = pickle.load(open('music-popularity-model.pkl', 'rb'))

st.title('Music Popularity Prediction')



artist_familiarity = st.number_input('Artist Familiarity')

artist_hotttnesss = st.number_input('Artist Hotttnesss')

duration = st.number_input('Duration')


loudness = st.number_input('Loudness')

song_hotttnesss = st.number_input('Song Hotttnesss')

start_of_fade_out = st.number_input('Start of fade out')

tempo = st.number_input('Tempo')

time_signature = st.number_input('Time Signature')

time_signature_confidence = st.number_input('Time signature confidence')

if st.button('Predict Probability'):

    input_features = [[artist_familiarity, artist_hotttnesss, duration, loudness, song_hotttnesss,
                       start_of_fade_out, tempo, time_signature, time_signature_confidence]]

    prediction = pipe.predict(input_features)[0].round(2)

    newmapper = {0: 'Song is not Popular', 1: 'Song is popular'}

    st.title(newmapper[prediction])
