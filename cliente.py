from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8000/tradutor")
texto = chain_remota.invoke({"língua": "japones", "texto": "Já deu um like hoje?"})
print(texto)