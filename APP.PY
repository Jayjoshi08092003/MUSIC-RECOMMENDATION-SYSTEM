# app.py
import streamlit as st
import joblib

# Load the model
model = joblib.load('CONTENT.IPYNB')

def get_recommendations(artist, song):
    # Use the loaded model to make recommendations
    recommendations = model.predict(artist, song)
    return recommendations

def main():
    st.title('Music Recommender')
    
    # User input for music attributes
    artist = st.text_input('Enter artist:')
    song = st.text_input('Enter song:')
    
    # Make recommendations
    if st.button('Get Recommendations'):
        recommendations = get_recommendations(artist, song)
        st.subheader('Recommendations')
        if recommendations:
            st.write(recommendations)
        else:
            st.write('No recommendations found.')

if __name__ == '__main__':
    main()
