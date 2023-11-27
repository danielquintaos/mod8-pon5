import openai
from langchain.llms import OpenAI

# Substitua 'your_api_key' pela sua chave API da OpenAI
api_key = 'your_api_key'

llm = OpenAI(openai_api_key=api_key)

with open('data/safety_rules.txt', 'r') as file:
    document_content = file.read()

def chatbot_response(prompt):
    system_prompt = (
        "O usuário está perguntando sobre normas de segurança em ambientes industriais. "
        "Aqui estão as normas de segurança conforme o documento: \n"
        f"{document_content}\n\n"
        "Responda de forma concisa e clara.\n\n"
    )
    full_prompt = [system_prompt + prompt]
    response = llm.generate(full_prompt)
    return response


####################################################

# Frontend

import gradio as gr

def chat_interface(prompt):
    response = chatbot_response(prompt)
    return response

interface = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(lines=2, placeholder="Faça sua pergunta aqui..."),
    outputs="text",
    title="Chatbot de Normas de Segurança Industrial",
    description="Pergunte sobre normas de segurança em ambientes industriais."
)

interface.launch()
