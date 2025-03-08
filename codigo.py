# Vídeo: https://www.youtube.com/watch?v=7L0MnVu1KEo
# Install pip install langchain
# https://python.langchain.com/docs/introduction/
# pip install -qU "langchain[openai]"

from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("Se inscrevam no canal para aprender Python")
]

# Grátis
modelo = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()
chain = modelo | parser

# resposta = modelo.invoke(mensagens)
# texto = parser.invoke(resposta)

texto = chain.invoke(mensagens)

print(texto)