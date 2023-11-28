Este projeto implementa um chatbot que responde a perguntas relacionadas a normas de segurança em ambientes industriais com base naquelas utilizadas pela Universidade de Deakin. 
O chatbot utiliza a API da OpenAI, integrada através da biblioteca `langchain`, apresenta uma interface de usuário construída com `gradio`, e text-to-speech construído com `gtts`.


## Requisitos

- Python 3.x
- Acesso à API da OpenAI


## Instalação

Para configurar o ambiente do projeto, siga os seguintes passos:

1. Clone o repositório:
   ```bash
   git clone https://github.com/danielquintaos/mod8-pon5
   ```

2. Substitua 'your_api_key' pela sua chave API da OpenAI no script do chatbot.


3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script Python para iniciar a interface do chatbot:

```
python app.py
```

Isso abrirá a interface do chatbot em um navegador, onde os usuários podem interagir digitando perguntas.


## Estrutura do Projeto

- `app.py`: Arquivo principal do chatbot.
- `tts.py`: Integra a funcionalidade TTS ao projeto.
- `requirements.txt`: Lista de dependências do Python.
- `data/safety_rules.txt`: Arquivo com o texto das normas de segurança.


## Demonstração

Vídeo (sem TTS): https://youtu.be/aR2US1sYK5Y

Imagem (com TTS):
![TTS](/tts-funcionando.PNG "TTS")
