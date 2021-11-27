import os, random

def menu() -> int:
  printCabecalho("*** Avaliação Algoritmo e lógica ***")
  print("\nSelecione a Opção\n")
  print("1 - Percorrer palavra")
  print("2 - Jogo da Quina\n")
  print("9 - Finalizar o programa")
  opcao = int(input("\nInforme a opção desejada: ") or 0)

  return opcao

def printCabecalho(text):
  print(36*"=")
  print(text)
  print(36*"=","\n")
  print("UTILIZE LETRAS MAIÚSCULAS\n")

def percorrePalavra():
  # Limpando a tela
  os.system("cls" if os.name == 'nt' else "clear")
  # exibindo cabeçalho
  printCabecalho("Percorrer Palavra - Obter a Posição")

  # Recebendo a palava e a assegurando que vai ser maiuscula caso o usuário digite minuscula
  palavra = input("Digite uma única palavra: ").upper()
  print("\n")

  alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  print(alfabeto)
  print("12345678901234567890123456\n")

  # Contador de posição da palavra
  posCount = 1
  for letra in palavra:
    # busca a posição da palavra no alfabeto
    indexAlfabeto = (alfabeto.find(letra)+1)
    print(f"Letra da Palavra: {letra} - Posição: {posCount}")
    print(f"Letra Alfabeto na posição: {indexAlfabeto}")    
    print(40*"*")

    posCount += 1
  
  input("\nPressione ENTER para Prosseguir...")

def jogoQuina():
  # Limpando a tela
  os.system("cls" if os.name == 'nt' else "clear")
  # exibindo cabeçalho
  printCabecalho("Quina - Concurso 2711 - 27/11/2021")

  # Gerando numeros
  aposta = geraNumeros()
  resultado = geraNumeros()

  print(f"Aposta...: {' - '.join(str(n) for n in aposta)}",)
  print(f"Resultado: {' - '.join(str(n) for n in resultado)}\n")

  countAcertos = 0
  for n in aposta:    
    print(f"Número Apostado: {n}")
    # Valida se o numero foi sorteado
    if n in resultado:
      print(f"ACERTOU!!!!!! {n} - {n}")    
      countAcertos += 1
  
  print(f"Acertos: {countAcertos}\n")

  input("Pressione ENTER para Prosseguir...")

def geraNumeros() -> list:
  nSorteado = []
  # gera numero até o list possuir 5 numeros distintos
  while len(nSorteado) <= 4:
    numero = random.randint(1,80) 
    
    if numero not in nSorteado:
      nSorteado.append(numero)
  
  return nSorteado
  

def run():
  opcao = 0
  while opcao != 9:
    os.system("cls" if os.name == 'nt' else "clear")
    opcao = menu()
    if(opcao == 1):
      percorrePalavra()
    elif(opcao == 2):
      jogoQuina()
    elif(opcao == 9):
      print("\nFinalizando programa.....")
    else:
      print(".......")

run()      