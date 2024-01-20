import streamlit as st
from langchain.prompts import PromptTemplate

import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SequentialChain
os.environ["OPENAI_API_KEY"] = <YOUR API GOES HERE!!>

def getllmresponse(input_text,no_words):
    first_input_prompt=PromptTemplate(
        input_variables=['blog_style' , 'input_text' ,'no_words'],
        template=f'You are an expert content writer. Write content for my linkedin post on the topic "{input_text}" within {no_words} words.'
    )

    llm=OpenAI()
    chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='theory')

    parent_chain=SequentialChain( chains=[chain],input_variables=['input_text' ,'no_words'],output_variables=['theory'],verbose=True)
    response=parent_chain({'input_text':input_text,
                      'no_words':no_words
                      })
    # print(response['theory'])
    return response['theory']



st.set_page_config(page_title="Content Generator",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Linkedin Posts 🤖")

input_text=st.text_input("Enter the Post Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')

    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getllmresponse(input_text,no_words))