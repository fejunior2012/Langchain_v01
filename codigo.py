# Vídeo: https://www.youtube.com/watch?v=7L0MnVu1KEo#
# https://python.langchain.com/docs/introduction/
# pip install -qU "langchain[openai]"
# pip install langchain

from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
# SystemMessage = Orientação de como a IA deve responder
# HumanMessage = Mensagem do usuário

from langchain_core.output_parsers import StrOutputParser
#  StrOutputParser é a função que enxuga a saída

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# Necessário criar sua chave no arquivo .env. Exemplo de conteúdo do arquivo .env: OPENAI_API_KEY = "minha chave API criada no site "
load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")

# Lista de mensagens que será enviada para IA 
mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("Se inscrevam no canal Hastag para aprender Python")
]

# Grátis é o gpt-3.5-turbo, mas você pode usar outro modelo pago.
modelo = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

chain = modelo | parser

# Função invoke é utilizada para enviar para IA
# resposta = modelo.invoke(mensagens)
# texto = parser.invoke(resposta)

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}"),
])

template_mensagem.invoke({"idioma": "inglês", "texto" : "Dê um like no vídeo e comente o que você achou."})
chain = template_mensagem | modelo | parser

texto = chain.invoke({"idioma": "inglês", "texto" : "Dê um like no vídeo e comente o que você achou."})

print(texto)