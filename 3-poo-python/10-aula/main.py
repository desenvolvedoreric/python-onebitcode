class Animal: 
  name = ""
  size = ""
  color = ""
  
  def eat(self): 
    print("Animal comendo")

class Horse(Animal):
  race = ""
  
  def escape(self):
    print("Cavalo escapando...")

class Lion(Animal):
  mane = True
  
  def hunt(self): 
    print("Leão caçando...")

horse = Horse()
horse.name = "Pé de pano"
horse.color = "Branco"
horse.size = "140cm"
horse.eat()
horse.escape()

lion = Lion()
lion.name = "Mico"
lion.color = "Castanho claro"
lion.size = "165cm"
lion.eat()
lion.hunt()