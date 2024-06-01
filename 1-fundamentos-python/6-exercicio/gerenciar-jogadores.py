## Gerenciamento de Jogadores e Times

# Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

# - Adicionar um time - OK
# - Remover um time - OK
# - Listar times -  OK
# - Adicionar jogador em um time
# - Remover jogador de um time
# - Listar jogadores de um time

# [x] A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
# [x] A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
# [x] A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
# [x] A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
# [x] A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
# [x] A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

# Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.

indexCount = 0
teams = []

def interface(): 
  print("Gerenciamento de jogadores: ")
  
  options = """
  1 - Adicionar um time
  2 - Remover um time
  3 - Listar times
  4 - Adicionar jogador em um time
  5 - Remover jogador de um time
  6 - Listar jogadores de um time
  """
  
  print(options)
  
  optionSelected = input("Escolha uma opção: ")
  
  match optionSelected: 
    case "1": 
      addTeam()
      
    case "2": 
      removeTeam()

    case "3": 
      getTeams()

    case "4": 
      addPlayer()

    case "5": 
      removePlayer()

    case "6": 
      getPlayers()
      
def addTeam():
  nameSelected = input("Qual o nome do TIME para ser adicionado?\nR: ")
  teamsLengthPrevius = len(teams)
  global indexCount
  
  if(hasTeam(nameSelected)): 
    print("Esse time já existe")
  else: 
    teams.append({
      "id": indexCount,
      "team": {
        "name": nameSelected,
        "players": []
      }
    })
    
    print(">>> Time Adicionado <<<")
  
  
  if teamsLengthPrevius != len(teams): 
    indexCount += 1
  
  interface()

def addPlayer(): 
  idSelected = int(input("Insira o ID do time que deseja ADICIONAR um jogador: "))
  playerSelected = input("Insira o NOME do jogador que deseja ADICIONAR: ")
  
  for teamIndex in teams: 
    if teamIndex["id"] == idSelected: 
      teamIndex["team"]["players"].append(playerSelected)

  interface()
  
def removeTeam(): 
  idSelected = int(input("Selecione o ID do time que deseja REMOVER: "))
  
  for teamsIndex in teams: 
    if teamsIndex["id"] == idSelected:
      print(f"Time removido {teamsIndex["team"]["name"]}")
      teams.remove(teamsIndex)

  interface()

def removePlayer(): 
  idSelected = int(input("Insira o ID do time que deseja REMOVER um jogador: "))
  playerSelected = input("Insira o NOME do jogador que deseja REMOVER: ")
  
  for teamIndex in teams: 
    if teamIndex["id"] == idSelected: 
      teamIndex["team"]["players"].remove(playerSelected)

  interface()

def getTeams(): 
  if len(teams) == 0 :
    print("Não há times para mostrar.")
  else: 
    for teamIndex in teams: 
      print(f"""
      Indice: {teamIndex["id"]}
      Time: {teamIndex["team"]["name"]}
      Número de jogadores: {len(teamIndex["team"]["players"])}
      """)
  
  interface()

def getPlayers(): 
  idSelected = int(input("Insira o ID do time que deseja REMOVER um jogador: "))
  stringPlayers = ''
  
  for teamIndex in teams: 
    if teamIndex["id"] == idSelected: 
      stringPlayers += ', '.join(teamIndex["team"]["players"])

  print(f"Jogadores: {stringPlayers}")
  
  interface()

def hasTeam(teamNme): 
  for teamIndex in teams: 
    return teamIndex["team"]["name"] == teamNme

interface()