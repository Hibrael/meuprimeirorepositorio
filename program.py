def substituir_caractere(frase, antigo, novo):
  
    vetor = list(frase)

    for i in range(len(vetor)):
        if vetor[i] == antigo:
            vetor[i] = novo

    return "".join(vetor)


frase = input("Digite uma frase: ")
antigo = input("Qual caractere deseja substituir? ")
novo = input("Por qual caractere deseja trocar? ")

nova_frase = substituir_caractere(frase, antigo, novo)

print("Frase original :", frase)
print("Frase alterada :", nova_frase)