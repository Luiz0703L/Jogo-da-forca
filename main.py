palavra = 'money'

wordUser = []

chances = 5

ganhou = False

while True:
  for letra in palavra:
    if letra.lower() in wordUser:
      print(letra, end=" ")
    else:
      print("_", end=" ")

  print(f"voce tem {chances} chances.") 

  tentativa = input("Chute uma letra: ")
  wordUser.append(tentativa.lower())

  if tentativa.lower() not in palavra.lower():
    chances -= 1

  ganhou = True

  for letra in palavra:
    if letra.lower() not in wordUser:
      ganhou = False

  if tentativa == 0 or ganhou:
    break 