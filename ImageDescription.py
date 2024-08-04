import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from PIL import Image
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
# API key configuration

api_key = "AIzaSyAYBo-4MHpCX52dHjJv0rU_q1NIp0r0b_g"

genai.configure(api_key=api_key)


def generate_response(input, image):

    model = genai.GenerativeModel('gemini-1.5-flash')
    if input:
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)

    return response.text



text = st.text_input('Enter a question about the image you have entered')

uploaded_image = st.file_uploader('Enter an image', type=['jpeg', 'jpg', 'png'])
image = False

if uploaded_image is not False:
    image = Image.open(uploaded_image)
    st.image(image)


submit = st.button("Submit")

if submit:
    if text:
        response = generate_response(text, image)
        st.header('Response:')
        st.write(response)