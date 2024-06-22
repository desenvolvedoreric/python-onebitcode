class ContactBook():
  def __init__(self):
    self.contacts = []
  
  def add(self, contact):
    self.contacts.append(contact)
    return 'Contato adicionado!'

  def remove(self, name):
    for contact in self.contacts:
      if contact["name"] == name:
        self.contacts.remove(contact) 
  
    return 'Contato Removido!'

  def search(self, name):
    for contact in self.contacts:
      if contact["name"] == name:
        print(f"Nome: {contact["name"]}")
        print(f"Número: {contact["phone"]}")
        print(f"E-mail: {contact["email"]}")
        return contact

  def list(self):
    for contact in self.contacts:
      print(f"Nome: {contact["name"]}")
      print(f"Número: {contact["phone"]}")
      print(f"E-mail: {contact["email"]}")
      print("-----")
    
    print(f"Total de contatos listados: {len(self.contacts)}")