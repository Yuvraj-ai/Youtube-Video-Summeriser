import streamlit as st
import uany as lch
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key = 'my_form'):
<<<<<<< HEAD
        gemini_api_key = st.text_input("Enter your Gemini API key:", type="password")
        youtube_url = st.sidebar.text_area(
            label="WHat is the youtube video url?",
            max_chars=200
=======
        youtube_url = st.sidebar.text_area(
            label="WHat is the youtube video url?",
            max_chars=100
>>>>>>> 9aaba28c3a31f9ffbe9ed90948ec154c8d6947d7
        )
        query = st.sidebar.text_area(
            label="Ask me about the video",
            key =  "query"
        )
        
        submit_button=  st.form_submit_button(label="Submit")
        

if query and youtube_url:
<<<<<<< HEAD
    db = lch.create_vector_db_from_youtube_url(youtube_url, gemini_api_key)
    response, docs = lch.get_response_from_query(db, query,gemini_api_key)
=======
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query)
>>>>>>> 9aaba28c3a31f9ffbe9ed90948ec154c8d6947d7
    st.subheader("ANSWER:")
    st.text(textwrap.fill(response, width= 80))
