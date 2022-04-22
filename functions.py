import os
import sys
import argparse
from datetime import datetime

# Untuk menggantikan fungsi len()
def length(x):
    index = 0
    for i in x:
        index += 1
    return int(index)

# Untuk mengetahui jumlah baris dalam suatu file
def rows(folder,file):
    f = open('./'+ folder + '/' + file, 'r')
    line = f.readlines()
    row =  length(line) - 1
    return int(row)

# Untuk membuka file csv dan mengubahnya menjadi array
def opencsv(folder,file):
    if file == 'user.csv' or file == 'game.csv':
        columns = 6
    elif file == 'kepemilikan.csv':
        columns = 2
    elif file == 'riwayat.csv':
        columns = 5

    lis = []
    f = open('./'+ folder + '/' + file, 'r')
    count = 0

    for row in f:
        i = ';'
        temp = ''
        if count != 0:     
            for i in row:
                if i == ';' or i == '\n':
                    lis += [temp]
                    temp = ''
                else:
                    temp += i
            if temp:
                lis += [temp]
        count += 1

    newlis = [[0 for j in range(columns)] for i in range(rows(folder,file))]
    count = 0
    for i in range(rows(folder,file)):
        for j in range(columns):
            newlis[i][j] = lis[count]
            count += 1
        if count == length(lis):
            break
    return newlis

# Mengubah array menjadi string untuk disimpan ke file csv
def arraytocsv(x):
    temp = ''
    for i in range(length(x)):
        for j in range(length(x[0])):
            if j == length(x[0]) - 1 and i < length(x) - 1:
                temp += str(x[i][j]) + '\n'
            elif j == length(x[0]) - 1 and i == length(x) - 1:
                temp += str(x[i][j]) + ''
            elif j < length(x[0]): 
                temp += str(x[i][j]) + ';'
    return temp

# Untuk mempercantik listing game
def spaces(x,y):
    for i in range(length(x)):
            max = length(x[0][y])
            for i in range(length(x)):
                if length(x[i][y]) > max:
                    max = length(x[i][y])
    for i in range(length(x)):
        if length(x[i][y]) < max:
            temp = max - length(x[i][y])
            x[i][y] = x[i][y] + ' '*temp

def numSpaces(x):
    max = length(str(x[0]))
    for i in range(length(x)):
        if length(str(x[i])) > length(str(x[0])):
            max = length(str(x[i]))
    for i in range(length(x)):
        if length(str(x[i])) < max:
            temp = max - length(str(x[i]))
            x[i] = str(x[i]) + '.' + ' '*temp
        else:
            x[i] = str(x[i]) + '.'
