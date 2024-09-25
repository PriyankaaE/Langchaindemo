import streamlit as st
import langchain_helper

st.title("Making my jobsearch easy")

question = st.text_input("Question: ")

if question:
	response = langchain_helper.query_question(question)
	st.header("Answer")
	st.write(response)



