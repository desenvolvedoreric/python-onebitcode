class Trip():
  registers = {}
  
  def register_person(self):
    print("Bem-vindo passageiro, digite o seu nome")
    name_passenger = input("> ")
    self.registers[name_passenger] = {}
    print("Passageiro registrado!")
    return self.registers[name_passenger]
  
  def buy_ticket(self, passenger):
    print("Para onde deseja ir?")
    place = input("> ")
    print("Qual data deseja ir?") 
    date = input("> ")
    self.registers[passenger]["place"] = place
    self.registers[passenger]["date"] = date
    self.registers[passenger]["ticket_price"] = "R$ 5,00"
    print("Passagem comprada!")
    return self.registers[passenger]
  
  def show_trip(self, name_search): 
    for passenger in self.registers.keys():
      if passenger == name_search:
        return f"Nome do passageiro: {passenger}\nLocal de viagem: {self.registers[passenger]["place"]}\nData de viagem: {self.registers[passenger]["date"]}"

trip = Trip()
trip.register_person()
trip.buy_ticket("Eric")
print(trip.show_trip("Eric"))