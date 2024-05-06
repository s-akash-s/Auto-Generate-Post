import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def LLamaresponse(input_text, number_words, blog_styles, post_type):
    if not number_words.isdigit():
        number_words = '300'
    llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q8_0.bin",
                      model_type="llama",
                      config={'max_new_tokens':int(number_words),
                              'temperature':0.01 #less becasue to get new reponses everytime 
                              })


    template="""
       Generate a {post_type} social media post for the topic {input_text}, which should be within {number_words} words for {blog_styles} social media platform with the hashtags.
"""
    prompt=PromptTemplate(input_variables=['input_text','number_words','blog_styles'],
                         template=template)

    
    response= llm(prompt.format(blog_styles=blog_styles,post_type=post_type, input_text=input_text,number_words=number_words))
    print(response)
    return response

st.set_page_config(page_title = "Generate Post",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Posts 🤖")

input_text=st.text_input("Enter the topic")
post_type=st.selectbox("Post Type", ('Informative', 'Promotional', 'Inspirational'), index=0)
col1, col2, col3 = st.columns([3,3,3])
with col1:
    number_words=st.text_input("Number of words")
with col2:
        blog_styles=st.selectbox("Social Media", 
                                 ('LinkedId', 'BlogPost', "Instagram", "YouTube", "FaceBook"), index=0)

submit=st.button("Generate")

if submit:
      st.write(LLamaresponse(input_text, number_words, blog_styles, post_type))