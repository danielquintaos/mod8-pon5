Este projeto implementa um chatbot que responde a perguntas relacionadas a normas de segurança em ambientes industriais com base naquelas utilizadas pela Universidade de Deakin. 
O chatbot utiliza a API da OpenAI, integrada através da biblioteca `langchain`, e apresenta uma interface de usuário construída com `gradio`.


## Requisitos

- Python 3.x

- Acesso à API da OpenAI


## Instalação

Para configurar o ambiente do projeto, siga os seguintes passos:

1. Clone o repositório:
   ```bash
   git clone [URL do Repositório]
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd [Nome do Diretório]
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```


## Configuração

1. **Chave API da OpenAI:** Defina a chave API da OpenAI como uma variável de ambiente (`OPENAI_API_KEY`) ou modifique o arquivo `app.py` para incluir a chave API diretamente no código (não recomendado por questões de segurança).

2. **Conteúdo do Documento:** Certifique-se de que o arquivo `data/safety_rules.txt` contém o texto atualizado das normas de segurança que deseja que o chatbot utilize como contexto.


## Uso

Para iniciar o chatbot, execute:

```bash
python app.py
```

Isso abrirá a interface do chatbot em um navegador web, onde os usuários podem interagir digitando perguntas.


## Estrutura do Projeto

- `app.py`: Arquivo principal do chatbot.
- `requirements.txt`: Lista de dependências do Python.
- `data/safety_rules.txt`: Arquivo com o texto das normas de segurança.


## Demonstração

Vídeo: https://youtu.be/aR2US1sYK5Y