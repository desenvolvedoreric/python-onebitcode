class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.initialPrice = price
  
  def __str__(self): 
    return f'Produto > {self.name}'

  def getProduct(self):
    return print(f"Nome: {self.name}\nValor: {self.price}")
  
  def percentageDiscount(self, percertage):
    discount = (percertage / 100) * self.price
    self.price -= discount
    return self.price
  
  def clearDiscount(self): 
    self.price = self.initialPrice
    return self.price

ballon = Product("Grande Balão Mágico", 100)
ballon.percentageDiscount(10);
ballon.getProduct();
ballon.clearDiscount();
ballon.getProduct();
print(ballon)