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

cuadrado(sudoku)