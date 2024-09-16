emails_clientes = {
    "emailPedro" : "pedro@gmail.com",
    "emailJorge" : "jorge@gmail.com",
    "emailJose" : "jose@gmail.com"

}

#Esse dicionario está armazenando emails e colocando as "chaves" para identifica-los,
#como "emailPedro" ou "emailJorge"

emails_clientes["emailBruno"] = "bruno@gmail.com"

emails_clientes.pop("emailJorge") #Com o metodo .pop eu removi o email Jorge do dicionario
print(emails_clientes)