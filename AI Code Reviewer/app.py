import google.generativeai as genai
genai.configure(api_key="")
# initializing the  model
model = genai.GenerativeModel(model_name = "models/gemini-2.0-flash-exp")

from IPython.display import Markdown 
import streamlit as st

st.title("Code Reviewer AI")
st.write("Ask your coding-related queries!")



sys_prompt = """You are a helpful codereviwerer. You can resolve coding related queries.
In case if someone ask queries whicha re not relevance to data science, politely tell
them to ask queries only"""
model = genai.GenerativeModel(model_name = "models/gemini-2.0-flash-exp", system_instruction = sys_prompt)


user_prompt = st.text_area("Enter your python code")

if st.button("Generate") == True:
        st.ballons()



response = model.generate_content(user_prompt)
st.markdown(response.text)
