import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to generate a response using the LLama model

def getLLamaResponse(input_text, no_words, blog_style):
    ## Load the LLama model
    llm =  CTransformers(model="Model/llama-2-7b-chat.ggmlv3.q8_0.bin", 
                                  model_type="llama", 
                                  config = {"temperature": 0.01,
                                            "max_new_tokens": 1000})
    
    #Promt template for generating the blog
    template = """ Write a blog for {blog_style} job prfile for a topic {input_text} with {no_words} words. """
    
    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"], 
        template = template)
    
    #Generate the response from LLama model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words = no_words))
    print(response)
    return response
 
st.set_page_config(page_title="Generate Blogs",
                   page_icon=":robot_face:",
                   
                   layout = "centered",
                   initial_sidebar_state = "collapsed")

st.header("Generate Blogs with LLama")

input_text = st.text_area("Enter your blog topic here:", height=200)

##creating two more column for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Enter the number of words you want in your blog:")
with col2:
    blog_style = st.selectbox("Select the style of the blog:", 
                              ('Researchers', 'Data Scientists', 'Students', 'General Public'), index = 0)
    
submit_button = st.button("Generate Blog")

#Final Response
if submit_button:
    st.write(getLLamaResponse(input_text, no_words, blog_style))
    
    