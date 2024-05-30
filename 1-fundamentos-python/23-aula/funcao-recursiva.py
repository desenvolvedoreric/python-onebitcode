def countToTen(acumulator):
  if acumulator == 10:
    return acumulator
  
  return countToTen(acumulator + 1)

print(countToTen(1))