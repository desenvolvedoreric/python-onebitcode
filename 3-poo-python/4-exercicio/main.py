from contact import Contact
from contactBook import ContactBook

contact_book = ContactBook()

print("=== AGENDA DE CONTATOS ===")
print("> Selecione uma opção abaixo")
print("""
1 - Adicionar contato      
2 - Remover contato
3 - Listar contatos
4 - Buscar contato
5 - Sair      
""")

choise = None
finish = False

while not finish:
  print("""
1 - Adicionar contato      
2 - Remover contato
3 - Listar contatos
4 - Buscar contato
5 - Sair      
""")
  
  choise = input("> ")
  
  match(choise):
    case '1':
      print("Qual o nome do seu contato")
      name = input("> ")

      print("Qual o número?")
      phone = input("> ")
      
      print("Qual o email do contato?")
      email = input("> ")
      
      contact = Contact(name, phone, email)
      contact_book.add(contact.__dict__)
    case '2':
      print("Qual o nome do contato que deseja remover?")
      name = input("> ")
      contact_book.remove(name)
    case '3':
      contact_book.list()
    case '4':
      print("Qual o nome do contato que deseja Procurar?")
      name = input("> ")
      print(contact_book.search(name))
    case _:
      print("Agenda de contatos fechada!")
      finish = True