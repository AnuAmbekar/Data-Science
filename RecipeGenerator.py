import streamlit as st
from langchain_community.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_google_genai import GoogleGenerativeAI


import streamlit as st

api_key = '-----' #I will not reveal API key here, but I have tested this app and it works with the API key.

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key, temperature=0.7)

cuisine = st.selectbox(
    'Which cusisine is your favourite?',
    ('Indian', 'Mexican', 'Italian', 'Korean')
)

dietary_preference = st.selectbox(
    'Which diet preference is your favourite?',
    ('Vegan', 'Gluten-free', 'Vegetarian', 'Ketogenic')
)

def LLM_Function(cuisine, dietary_preference):
    prompt1 = PromptTemplate(
        input_variables = ['cuisine'],
        template = 'Give me a {cuisine} that I can cook with.'
    )

    chain1 = LLMChain(llm=llm, prompt=prompt1, output_key='output1')

    prompt2 = PromptTemplate(
        input_variables = ['output1', 'dietary_preference'],
        template = 'With {output1} cuisine, my dietary preferences are {dietary_preference}. Give me some recipe ideas.'
    )

    chain2 = LLMChain(llm=llm, prompt=prompt2, output_key='output2')

    chain = SequentialChain(
        chains = [chain1, chain2],
        input_variables = ['cuisine', 'dietary_preference'],
        output_variables = ['output1', 'output2']
    )

    output = chain({'cuisine': cuisine, 'dietary_preference': dietary_preference})

    return output


if cuisine:
    output = LLM_Function(cuisine, dietary_preference)
    st.title(output['cuisine'])
    st.write(output['output2'])


