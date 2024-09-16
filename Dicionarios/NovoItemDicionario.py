emails_clientes = {
    "emailPedro" : "pedro@gmail.com",
    "emailJorge" : "jorge@gmail.com",
    "emailJose" : "jose@gmail.com"

}

#Esse dicionario está armazenando emails e colocando as "chaves" para identifica-los,
#como "emailPedro" ou "emailJorge"

emails_clientes["emailBruno"] = "bruno@gmail.com" # Nesse trecho eu adicionei mais um elemento ao dicionario
                                                  # Sem precisar voltar nele manualmente

exibir = emails_clientes["emailBruno"]
print(exibir)