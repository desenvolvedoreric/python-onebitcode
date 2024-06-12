class Movie:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.evaluators = 0
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme: {self.name}"
    
    def get_infos(self):
      message = f"""
      ----- Dados do Filme -----
      
      Nome Filme: {self.name}
      Ano Lançamento: {self.yearLaunch}
      Está no plano? {self.includedPlan}
      Avaliação Filme: {self.get_note()}
      Duração Filme: {self.durationMinutes}
      
      -----
      """
      
      return message
    
    def give_evaluation(self, note):
      self.totalEvaluation += note
      self.evaluators += 1
    
    def get_note(self): 
      return self.totalEvaluation / self.evaluators

movie = Movie("Velozes e Furiosos", 2003, False, 145)
movie.give_evaluation(4.5)
movie.give_evaluation(5)
print(movie.get_infos())