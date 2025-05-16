import streamlit as st
import uany as lch
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key = 'my_form'):
        gemini_api_key = st.text_input("Enter your Gemini API key:", type="password")
        youtube_url = st.sidebar.text_area(
            label="WHat is the youtube video url?",
            max_chars=200
        )
        query = st.sidebar.text_area(
            label="Ask me about the video",
            key =  "query"
        )
        
        submit_button=  st.form_submit_button(label="Submit")
        

if query and youtube_url:
    db = lch.create_vector_db_from_youtube_url(youtube_url, gemini_api_key)
    response, docs = lch.get_response_from_query(db, query,gemini_api_key)
    st.subheader("ANSWER:")
    st.text(textwrap.fill(response, width= 80))
