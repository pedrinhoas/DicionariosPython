emails_clientes = {
    "emailPedro" : "pedro@gmail.com",
    "emailJorge" : "jorge@gmail.com",
    "emailJose" : "jose@gmail.com"

}


if "emailPedro" in emails_clientes: # Aqui ele está verificando se a chave "emailPedro" existe
    print("Tudo certo")
else :
    print("email não localizado")

if "pedro@gmail.com" in emails_clientes.values():
    print("Também está certo")

else: 
    print("esse email também não existe")
