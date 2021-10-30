# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:59:33 2021

@author: rodrigo vivar
"""
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
#enmarcado para que se vea mas claro 
def cuadrado(sudoku):
    for i in range(9):
        if i % 3 == 0:
            if i == 0:
                print(" ┎─────────┰─────────┰─────────┒")
            else:
                print(" ┠─────────╂─────────╂─────────┨")

        for j in range(9):
            if j % 3 == 0:
                print(" ┃ ", end=" ")

            if j == 8:
                print(sudoku[i][j], " ┃")
            else:
                print(sudoku[i][j], end=" ")

    print(" ┖─────────┸─────────┸─────────┚")
    

def celdasiguiente(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                return i, j  # row, column

    return None

def validar(sudoku, n, p):
#se definen las cajas
    cajax = p[1] // 3
    cajay = p[0] // 3
#primero verificamos fila a fila
    for i in range(9):
        if sudoku[p[0]][i] == n and p[1] != i:
            return False
#luego columna a columna
    for j in range(9):
        if sudoku[j][p[1]]==n and p[0] != j:
            return False

#se verifica cada una de las cajas
    for i in range(cajay*3, cajay*3 + 3):
        for j in range(cajax*3, cajax*3 + 3):
            if sudoku[i][j] == n and (i, j) != p:
                return False

    return True


#se resulve primero buscando primero la posicion de la celda vacia
def r(s):
    d = celdasiguiente(s)
    if d: 
        i, j = d
       
    else:
         return True
#luego se rellena con un numero del 1 al 9 
#y se valida en cada inineracion si el numero puedo o no ir 
#de no ser asi vuelve a ser 0
    for o in range(1, 10):
        if validar(s, o, (i, j)):
            s[i][j] = o

            if r(s):
                return True

            s[i][j] = 0

    return False
print('sudoku sin resolver')
cuadrado(sudoku)
r(sudoku)
print('sudoku resulto')
cuadrado(sudoku)