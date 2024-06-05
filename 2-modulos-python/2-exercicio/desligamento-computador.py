# Crie um script que faça o desligamento do computador em 30 minutos e 1 hora

import os

timeInSecondsForShutdown = "1800"

def shutdownPc(time): 
  os.system(f"shutdown -s -t {time}")

shutdownPc(timeInSecondsForShutdown)