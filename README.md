# 🦙 LLama Blog Generator

An interactive Streamlit web application that generates custom blog content using a quantized **LLama 2 model** via `ctransformers`. Powered by **LangChain**, this app allows users to create topic-specific blogs tailored by audience type and word count, all through a simple and intuitive UI, with no GPU required.

---

## 📌 Project Overview

This project showcases how **large language models (LLMs)** can be used locally to create real-time, high-quality content based on user prompts. Instead of relying on cloud APIs, the app leverages a quantized version of Meta's LLama 2 model for **CPU-based inference**, enabling private and offline blog generation.

**Key Use Case:**  
Ideal for students, content creators, researchers, and professionals who want to generate structured blog content on specific topics with minimal setup.

---

## ✨ Features

- **LLama 2 Integration**: Uses a locally hosted LLama 2 (7B) model with `ctransformers`
- **Dynamic Prompting**: Blog generation based on user input for topic, word count, and audience
- **Prompt Engineering**: Utilizes `LangChain`'s `PromptTemplate` to format user input for the model
- **No GPU Needed**: Runs entirely on CPU using a quantized `.ggml` model
- **Streamlit Interface**: Clean, responsive web UI for easy interaction

---

## 🛠️ Technologies Used

| Tool/Library     | Purpose                                         |
|------------------|-------------------------------------------------|
| **Python**       | Core programming language                       |
| **Streamlit**    | Front-end UI and interaction                    |
| **LangChain**    | Prompt templating and language model orchestration |
| **CTransformers**| Fast, quantized LLM inference engine for CPU    |
| **LLama 2**      | Meta's open-source foundational language model  |

---
### Download the LLama model
Download a quantized LLama 2 model file such as:

llama-2-7b-chat.ggmlv3.q8_0.bin
place the file inside the Model/ directory.

---
### Run the app
streamlit run app.py

---
### How It Works
User Input: The user provides a topic, selects a target audience (e.g., Researchers, Students), and specifies the number of words.   
Prompt Generation: A dynamic prompt is built using LangChain's PromptTemplate.   
Model Inference: The prompt is passed to the LLama 2 model loaded via ctransformers, which returns a text output.   
Output Display: The generated blog is rendered in real-time on the Streamlit interface.


### User Interface
---
A multi-input form allows users to:  
Enter the blog topic   
Choose the target audience from a dropdown   
Specify desired word count   
A "Generate Blog" button triggers content generation   
Output is displayed directly in the app

---
🙌 Acknowledgements
Meta AI – for releasing LLama 2   
TheBloke – for maintaining quantized models   
LangChain   
Streamlit   
python   
