def adiconar_contato(contatos, nome_contato):
  agenda = {"agenda": nome_contato, "Favorito": False}
  contatos.append(agenda)
  print(f"O contato {nome_contato} foi adicionado!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, agenda in enumerate(contatos, start=1):
    status = "★" if agenda ["Favorito"] else ""
    nome_contato = agenda["agenda"]
    print(f"{indice}. [{status}] {nome_contato}")
    return

def editar_contato(contatos, indice_contato, novo_nome_contato):
 indice_contato_ajustado = int(indice_contato) - 1
 if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
  contatos[indice_contato_ajustado] ["agenda"] = novo_nome_contato
  print(f"Contato {indice_contato} atualizada para {novo_nome_contato}")
 else:
   print("Índice de tarefa inválido.")
 return

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1 
  contatos[indice_contato_ajustado] ["Favorito"] = True
  print(f"Contato {indice_contato} marcado como favorito")
  return

def deletar_contatos(contatos):
  for agenda in contatos:
    if agenda["Favorito"]:
      contatos.remove(agenda)
  print("O contato foi deletado")
  return

contatos = []
while True:
  print("\n Agenda")
  print("1. Adicionar novo contato")
  print("2. Contatos cadastrados")
  print("3. Editar contato")
  print("4. Marcar um contato como favorito")
  print("5. Favoritos")
  print("6. Apagar contato")

  escolha = input("Digite sua escolha: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    adiconar_contato(contatos, nome_contato)

  elif escolha == "2":
    ver_contatos(contatos)
  
  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do contato: ")
    editar_contato(contatos, indice_contato, novo_nome)

  elif escolha == "4":
     ver_contatos(contatos)
     indice_contato = input("Digite o número da tarefa que deseja completar: ")
     favoritar_contato(contatos, indice_contato)

  elif escolha == "6":
    deletar_contatos(contatos)
    ver_contatos(contatos)

  elif escolha == "7":
    break

print("Programa finalizado")