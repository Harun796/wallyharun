import string
import random
simbols = []
#https://docs.python.org/2/library/string.html
simbols=list(string.printable)
def initLandscape(landscape):
  for i in range(100):
      landscape.append("")
  return landscape
def populateLandscape(landscape,personatges):
  wally = False
  for posicio in range(100):
      personatge = random.choice(simbols)
      if (personatge == personatges):
          if (personatges not in landscape):
              wally = True
              landscape[posicio] = personatge
      else:  
          landscape[posicio] = personatge
   if (not wally):
    if (personatge == personatges):
      landscape[random.randrange(100)] =personatges  
  return landscape
def whereIsCharacter(landscape,toFind):
  posicio = -1
  for f in landscape:
    posicio = posicio + 1
    if(f == toFind):
      return posicio
  return -1
 
personatges= input("Quin personatge vols trobar")
paisatge=populateLandscape(initLandscape([]),personatges)
print(paisatge)
print("El personatge  està en la posició "+str(whereIsCharacter(paisatge,personatges)))