tablero:list[str]=[
    ["*","*","*",],
    ["*","*","*",],
    ["*","*","*",],

]
def imprimir_tablero(tab):
    print("0","1","2")
    for i, fila in enumerate(tab):
      print(i, end = "")
      for casilla in fila:
          print(casilla, end= " ! ")
      print()
      print("\n-------")

imprimir_tablero(tablero)